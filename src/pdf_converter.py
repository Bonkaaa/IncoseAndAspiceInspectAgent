import os
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

import pymupdf
import pymupdf4llm
import yaml


class IncoseParser:
    """
    Parser chuyển đổi tài liệu INCOSE Guide to Writing Requirements (v3.1)
    thành các file Markdown theo từng tiêu chí (14 Characteristics và 41 Rules).
    """

    def clean_text(self, md_text: str) -> str:
        """
        Làm sạch nội dung Markdown:
        - Xóa running headers, footers, số trang rác.
        - Xóa các thẻ HTML <mark>, </mark>.
        - Chuẩn hóa các đề mục (Definition, Rationale, Guidance, Elaboration, Examples).
        """
        text = md_text

        # 1. Xóa running headers và footers bản quyền
        text = re.sub(r'_Guide to Writing Requirements_', '', text, flags=re.IGNORECASE)
        text = re.sub(
            r'INCOSE-TP-2010-006-04\|\s*VERS/REV:\s*3\.1\s*\|\s*May 2022',
            '',
            text,
            flags=re.IGNORECASE
        )
        text = re.sub(
            r'INCOSE-TP-2010-006-[^\n]+',
            '',
            text,
            flags=re.IGNORECASE
        )

        # 2. Xóa các số trang rác đứng riêng dòng
        text = re.sub(r'(?:^|\n)\s*\d{1,3}\s*(?:\n|$)', '\n', text)

        # 3. Xóa các thẻ HTML rác <mark>, </mark>
        text = re.sub(r'</?mark>', '', text)

        # 4. Chuẩn hóa các đề mục con
        # Thường pymupdf4llm render thành ## _Definition:_ hoặc ## Definition:
        section_headers = [
            'Definition',
            'Rationale',
            'Guidance',
            'Elaboration',
            'Examples',
            'Exceptions and relationships',
            'Rules that help establish this characteristic',
            'Characteristics that are established by this rule',
            'Attributes that help establish this characteristic',
            'Activities and concepts associated with this characteristic',
        ]
        for header in section_headers:
            # Pattern bắt các dạng ## _Header:_ hoặc ## **Header:** hoặc Header: [nội dung cùng dòng]
            pattern = rf'(?m)^#{{0,4}}\s*[_*]*\s*({re.escape(header)})[ \t:_\\*]*(.*)$'
            def replace_header(match, h=header):
                rest = match.group(2).strip(' _*')
                if rest:
                    return f"### {h}\n\n{rest}"
                return f"### {h}"
            text = re.sub(pattern, replace_header, text, flags=re.IGNORECASE)

        # 5. Làm sạch và chuẩn hóa các thẻ gạch chân <u> trong mục Examples
        # 5a. Xóa các biến thể dấu hai chấm kỳ lạ của pymupdf4llm: _<u>:</u>_ hoặc <u>:</u>
        text = re.sub(r'[_*]*\s*<u>\s*:\s*</u>\s*[_*]*', ':', text)

        # 5b. Chuyển các đề mục ví dụ con như <u>Subject examples</u> thành header cấp 4: #### Subject examples
        text = re.sub(
            r'(?m)^[ \t]*_?<u>\s*([A-Za-z0-9\s-]+examples?)\s*</u>\s*:?[ \t]*$',
            r'#### \1',
            text,
            flags=re.IGNORECASE
        )

        # 5c. Chuẩn hóa các nhãn Unacceptable / Acceptable / Poor / Better / Good thành **Label:**
        def format_example_label(m):
            raw = m.group(1).strip()
            lbl_match = re.match(
                r'^(Unacceptable[^\n:]*|Acceptable[^\n:]*|Poor|Better|Good|Correct|Incorrect)[:\s]*(.*)$',
                raw,
                flags=re.IGNORECASE
            )
            if lbl_match:
                lbl = lbl_match.group(1).strip()
                rest = lbl_match.group(2).strip().rstrip('[').strip()
                if rest:
                    return f"**{lbl}:** {rest}"
                return f"**{lbl}:**"
            return raw

        text = re.sub(
            r'<u>\s*((?:Unacceptable|Acceptable|Poor|Better|Good|Correct|Incorrect)[^<]*)</u>',
            format_example_label,
            text,
            flags=re.IGNORECASE
        )

        # 5d. Loại bỏ toàn bộ các thẻ <u> và </u> còn sót lại
        text = re.sub(r'</?u>', '', text)

        # 5e. Dọn dẹp các lỗi dấu hai chấm lặp lại
        text = re.sub(r':\*\*\s*:\s*', ':** ', text)
        text = re.sub(r':\s*:\s*', ': ', text)

        # 6. In đậm câu phát biểu quy tắc cốt lõi (Core rule statement)
        def bold_rule_stmt(match):
            title = match.group(1).strip()
            stmt = match.group(2).strip()
            stmt_clean = stmt.strip('*_ ')
            next_header = match.group(3)
            return f"{title}\n\n**{stmt_clean}**\n\n{next_header}"

        text = re.sub(
            r'(?m)(^##\s*\**4\.\d+\.\d+\s+R\d+[^\n]+)\n+(.*?)\n+(###\s+[^\n]+)',
            bold_rule_stmt,
            text,
            count=1,
            flags=re.DOTALL
        )

        # 7. Loại bỏ tiêu đề nhóm mục bị rò rỉ ở cuối file (ví dụ: ## **4.3 Non-ambiguity**)
        text = re.sub(r'(?m)\n+##\s*\**\d+\.\d+\s+[A-Za-z].*$', '', text)

        # 8. Chuyển danh sách Characteristics và Rules thành gạch đầu dòng (bullet points)
        def format_char_bullets(m):
            header = m.group(1).strip()
            block = m.group(2).strip()
            items = re.findall(
                r'[_*]*(C\d+)[_*]*\s*[-–—]\s*([A-Za-z\s]+?)[_*]*(?=(?:\s+[_*]*C\d+\b|\n|\Z))',
                block
            )
            if items:
                bullets = "\n".join([f"- {c[0]} - {c[1].strip()}" for c in items])
                return f"{header}\n\n{bullets}\n\n"
            return m.group(0)

        text = re.sub(
            r'(### Characteristics that are established by this rule)\s*\n+(.*?)(?=\n+#{1,4}\s|\Z)',
            format_char_bullets,
            text,
            flags=re.DOTALL
        )

        def format_rule_bullets(m):
            header = m.group(1).strip()
            block = m.group(2).strip()
            items = re.findall(
                r'[_*]*(R\d+)[_*]*\s*[-–—]\s*([^\n\r]+?)[_*]*(?=(?:\s+[_*]*R\d+\b|\n|\Z))',
                block
            )
            if items:
                bullets = "\n".join([f"- {r[0]} - {r[1].strip()}" for r in items])
                return f"{header}\n\n{bullets}\n\n"
            return m.group(0)

        text = re.sub(
            r'(### Rules that help establish this characteristic)\s*\n+(.*?)(?=\n+#{1,4}\s|\Z)',
            format_rule_bullets,
            text,
            flags=re.DOTALL
        )

        # 9. Làm sạch khoảng trắng thừa
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def extract_rule_metadata(
        self,
        raw_text: str,
        rule_id: str,
        rule_name: str,
        page_num: int
    ) -> Dict[str, Any]:
        """
        Trích xuất metadata cho Rule:
        - id: R1..R41
        - name: Tên rule
        - type: 'rule'
        - page: Số trang in PDF
        - target_scope: 'individual_statement' hoặc 'set_of_statements'
        - established_characteristics: Danh sách C...
        - related_rules: Danh sách R...
        """
        rule_num = int(rule_id[1:]) if rule_id[1:].isdigit() else 1
        target_scope = "set_of_statements" if rule_num in [40, 41] else "individual_statement"

        # Trích xuất established_characteristics
        est_chars = []
        char_block_match = re.search(
            r'Characteristics that are established by this rule:?(.*?)(?:\n#{1,3}|\Z)',
            raw_text,
            flags=re.DOTALL | re.IGNORECASE
        )
        if char_block_match:
            block = char_block_match.group(1)
            found = re.findall(r'\bC\d+\b', block)
            # Giữ thứ tự số tăng dần
            seen = set()
            for c in sorted(found, key=lambda x: int(x[1:])):
                if c not in seen:
                    seen.add(c)
                    est_chars.append(c)

        # Trích xuất related_rules từ cụm 'See also' hoặc 'Refer to'
        rel_rules = []
        for match in re.finditer(r'\b(?:See also|Refer to)\s+([^\n]+)', raw_text, flags=re.IGNORECASE):
            line = match.group(1)
            found = re.findall(r'\bR\d+\b', line)
            for r in found:
                if r != rule_id and r not in rel_rules:
                    rel_rules.append(r)
        rel_rules.sort(key=lambda x: int(x[1:]))

        return {
            "id": rule_id,
            "name": rule_name,
            "type": "rule",
            "page": page_num,
            "target_scope": target_scope,
            "established_characteristics": est_chars,
            "related_rules": rel_rules
        }

    def extract_characteristic_metadata(
        self,
        raw_text: str,
        char_id: str,
        char_name: str,
        page_num: int
    ) -> Dict[str, Any]:
        """
        Trích xuất metadata cho Characteristic:
        - id: C1..C14
        - name: Tên characteristic
        - type: 'characteristic'
        - target_scope: 'individual_statement' (C1-C9) hoặc 'set_of_statements' (C10-C14)
        - supporting_rules: Danh sách R...
        - page: Số trang in PDF
        """
        char_num = int(char_id[1:]) if char_id[1:].isdigit() else 1
        target_scope = "set_of_statements" if char_num >= 10 else "individual_statement"

        # Trích xuất supporting_rules
        supp_rules = []
        rule_block_match = re.search(
            r'Rules that help establish this characteristic:?(.*?)(?:Attributes that help|\n#{1,3}|\Z)',
            raw_text,
            flags=re.DOTALL | re.IGNORECASE
        )
        if rule_block_match:
            block = rule_block_match.group(1)
            found = re.findall(r'\bR\d+\b', block)
            seen = set()
            for r in sorted(found, key=lambda x: int(x[1:])):
                if r not in seen:
                    seen.add(r)
                    supp_rules.append(r)

        return {
            "id": char_id,
            "name": char_name,
            "type": "characteristic",
            "target_scope": target_scope,
            "supporting_rules": supp_rules,
            "page": page_num
        }

    def generate_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """
        Tạo khối YAML Frontmatter theo chuẩn:
        ---
        key: value
        ---
        """
        yaml_str = yaml.dump(metadata, sort_keys=False, allow_unicode=True)
        return f"---\n{yaml_str}---\n\n"

    def locate_criteria_pages(self, doc: pymupdf.Document) -> List[Dict[str, Any]]:
        """
        Quét qua tài liệu PDF để định vị số trang bắt đầu của từng tiêu chí.
        """
        criteria = []

        # Lấy bản đồ tên chuẩn PascalCase từ Mục lục TOC (trang 4 và 5)
        toc_text = ""
        if len(doc) > 5:
            toc_text = doc[4].get_text() + "\n" + doc[5].get_text()
        toc_rule_names = dict(re.findall(r'(R\d+)\s*[-–—]\s*/[^/]+/([^\n\.\s]+)', toc_text))

        for page_idx in range(25, 102):
            text = doc[page_idx].get_text()

            # Quét Characteristics: e.g. 2.1 C1 - Necessary hoặc 3.1 C10 - Complete
            c_matches = re.finditer(
                r'(?:^|\n)(?:##\s*\**)?(?:(2|3)\.\d+)\s+(C\d+)\s*[-–—]\s*([^\n\*\r]+)',
                text
            )
            for m in c_matches:
                cid = m.group(2)
                raw_name = m.group(3).strip()
                cname = re.sub(r'[^a-zA-Z0-9]', '', raw_name.title())
                criteria.append({
                    'id': cid,
                    'name': cname,
                    'display_name': raw_name,
                    'type': 'characteristic',
                    'page_idx': page_idx,
                    'page_num': page_idx  # trang in trùng chỉ số trang ở dải này
                })

            # Quét Rules: e.g. 4.1.1 R1 - /ACCURACY/SENTENCESTRUCTURE
            r_matches = re.finditer(
                r'(?:^|\n)(?:##\s*\**)?(?:4\.\d+\.\d+)\s+(R\d+)\s*[-–—]\s*(?:/([^/\n]+)/)?([^\n\*\r]+)',
                text
            )
            for m in r_matches:
                rid = m.group(1)
                raw_name = m.group(3).strip()
                rname = toc_rule_names.get(rid) or re.sub(r'[^a-zA-Z0-9]', '', raw_name.title())
                criteria.append({
                    'id': rid,
                    'name': rname,
                    'display_name': raw_name,
                    'type': 'rule',
                    'page_idx': page_idx,
                    'page_num': page_idx
                })

        # Sắp xếp theo trang xuất hiện
        criteria.sort(key=lambda x: (x['page_idx'], int(x['id'][1:])))
        return criteria

    def parse_pdf(
        self,
        pdf_path: str,
        output_dir: str = "data/processed"
    ) -> Dict[str, List[Path]]:
        """
        Điều phối toàn bộ quá trình parse:
        1. Định vị trang.
        2. Chuyển đổi Markdown bằng pymupdf4llm.
        3. Tách chunk, làm sạch, trích xuất metadata và lưu file.
        """
        doc = pymupdf.open(pdf_path)
        criteria_list = self.locate_criteria_pages(doc)

        out_path = Path(output_dir)
        chars_dir = out_path / "characteristics"
        rules_dir = out_path / "rules"
        chars_dir.mkdir(parents=True, exist_ok=True)
        rules_dir.mkdir(parents=True, exist_ok=True)

        # 1. Render Markdown cho Section 2 & 3 (Characteristics: trang 26-56)
        print("Rendering Markdown for Characteristics (pages 26-56)...")
        md_chars = pymupdf4llm.to_markdown(pdf_path, pages=list(range(26, 57)))

        # 2. Render Markdown cho Section 4 (Rules: trang 57-101)
        print("Rendering Markdown for Rules (pages 57-101)...")
        md_rules = pymupdf4llm.to_markdown(pdf_path, pages=list(range(57, 102)))

        saved_files: Dict[str, List[Path]] = {"characteristics": [], "rules": []}

        # Tách Characteristics
        char_pattern = r'(?=(?:^|\n)##\s*\**(?:\d+\.\d+)\s+C\d+\s*[-–—])'
        char_chunks = re.split(char_pattern, md_chars)
        # Bỏ chunk mở đầu trước C1
        char_chunks = [ch for ch in char_chunks if re.search(r'##\s*\**(?:\d+\.\d+)\s+C\d+\s*[-–—]', ch)]

        # Tách Rules
        rule_pattern = r'(?=(?:^|\n)##\s*\**(?:\d+\.\d+\.\d+)\s+R\d+\s*[-–—])'
        rule_chunks = re.split(rule_pattern, md_rules)
        # Bỏ chunk mở đầu trước R1
        rule_chunks = [ch for ch in rule_chunks if re.search(r'##\s*\**(?:\d+\.\d+\.\d+)\s+R\d+\s*[-–—]', ch)]

        # Ghép cặp metadata và nội dung cho Characteristics
        char_meta_list = [c for c in criteria_list if c['type'] == 'characteristic']
        for i, meta_item in enumerate(char_meta_list):
            chunk = char_chunks[i] if i < len(char_chunks) else ""
            
            # Cắt bỏ phần mở đầu Section 3 nếu bị dính vào cuối C9
            if meta_item['id'] == 'C9':
                chunk = re.split(r'#\s*\**Section 3:', chunk)[0]

            meta = self.extract_characteristic_metadata(
                raw_text=chunk,
                char_id=meta_item['id'],
                char_name=meta_item['name'],
                page_num=meta_item['page_num']
            )
            cleaned_content = self.clean_text(chunk)
            frontmatter = self.generate_frontmatter(meta)

            file_num = int(meta_item['id'][1:])
            filename = f"C{file_num:02d}_{meta_item['name']}.md"
            target_file = chars_dir / filename

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter + cleaned_content + "\n")
            saved_files["characteristics"].append(target_file)

        # Ghép cặp metadata và nội dung cho Rules
        rule_meta_list = [r for r in criteria_list if r['type'] == 'rule']
        for i, meta_item in enumerate(rule_meta_list):
            chunk = rule_chunks[i] if i < len(rule_chunks) else ""

            # Cắt bỏ phần Appendix A nếu bị dính vào cuối R41
            if meta_item['id'] == 'R41':
                chunk = re.split(r'#\s*\**Appendix A:', chunk, flags=re.IGNORECASE)[0]

            meta = self.extract_rule_metadata(
                raw_text=chunk,
                rule_id=meta_item['id'],
                rule_name=meta_item['name'],
                page_num=meta_item['page_num']
            )
            cleaned_content = self.clean_text(chunk)
            frontmatter = self.generate_frontmatter(meta)

            file_num = int(meta_item['id'][1:])
            filename = f"R{file_num:02d}_{meta_item['name']}.md"
            target_file = rules_dir / filename

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(frontmatter + cleaned_content + "\n")
            saved_files["rules"].append(target_file)

        return saved_files


def main():
    pdf_path = "data/raw/INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf"
    output_dir = "data/processed"

    print(f"Bắt đầu chuyển đổi: {pdf_path}")
    parser = IncoseParser()
    results = parser.parse_pdf(pdf_path, output_dir)

    print("\n--- KẾT QUẢ CHUYỂN ĐỔI ---")
    print(f"Characteristics: {len(results['characteristics'])} files tạo thành công tại {output_dir}/characteristics")
    print(f"Rules: {len(results['rules'])} files tạo thành công tại {output_dir}/rules")
    print("Hoàn tất!")


if __name__ == '__main__':
    main()
