import pytest
import yaml
from src.pdf_converter import IncoseParser, AspiceParser


def test_clean_text():
    parser = IncoseParser()
    sample_text = (
        "_Guide to Writing Requirements_\n\n"
        "58\n\n"
        "## **4.1.1 R1 - /ACCURACY/SENTENCESTRUCTURE**\n\n"
        "Use a structured, complete sentence.\n\n"
        "## _<mark>Elaboration:</mark>_\n\n"
        "The structure of needs and requirements...\n\n"
        "INCOSE-TP-2010-006-04| VERS/REV: 3.1  |  May 2022\n\n"
        "## _Exceptions and relationships:_\n\n"
        "While this rule states..."
    )
    cleaned = parser.clean_text(sample_text)
    
    # Running headers/footers removed
    assert "_Guide to Writing Requirements_" not in cleaned
    assert "INCOSE-TP-2010-006-04" not in cleaned
    assert "\n58\n" not in cleaned
    
    # HTML mark tags removed
    assert "<mark>" not in cleaned
    assert "</mark>" not in cleaned
    
    # Standardized heading
    assert "### Elaboration" in cleaned
    assert "### Exceptions and relationships" in cleaned

    # Core rule statement is bolded
    assert "**Use a structured, complete sentence.**" in cleaned


def test_clean_examples_and_u_tags():
    parser = IncoseParser()
    sample = (
        "### Examples\n\n"
        "<u>Subject examples</u> _<u>:</u>_\n\n"
        "<u>Unacceptable system requirement: “The User shall ……….” [</u>\n\n"
        "- [This is unacceptable...]\n\n"
        "<u>Acceptable</u> _<u>:</u>_ “The <system> shall …….”\n"
    )
    cleaned = parser.clean_text(sample)
    assert "<u>" not in cleaned
    assert "</u>" not in cleaned
    assert "#### Subject examples" in cleaned
    assert "**Unacceptable system requirement:** “The User shall ……….”" in cleaned
    assert "**Acceptable:** “The <system> shall …….”" in cleaned


def test_clean_inline_headers_and_leaked_category():
    parser = IncoseParser()
    sample = (
        "## **4.2.2 R11 - /CONCISION/SEPARATECLAUSES**\n\n"
        "Place each distinct idea in its own sentence.\n\n"
        "### Elaboration\n\n"
        "Content of elaboration...\n\n"
        "_Characteristics that are established by this rule:_ C3 - Unambiguous C4 - Complete C7 - Verifiable C8 - Correct\n\n"
        "## **4.3 Non-ambiguity**\n"
    )
    cleaned = parser.clean_text(sample)
    assert "### Characteristics that are established by this rule" in cleaned
    assert "- C3 - Unambiguous\n- C4 - Complete" in cleaned
    assert "## **4.3 Non-ambiguity**" not in cleaned


def test_extract_rule_metadata():
    parser = IncoseParser()
    sample_r1 = (
        "## **4.1.1 R1 - /ACCURACY/SENTENCESTRUCTURE**\n\n"
        "Use a structured, complete sentence.\n\n"
        "See also R2, R3, R11, R18, R27, and Appendix C.\n\n"
        "### Characteristics that are established by this rule:\n"
        "C3 - Unambiguous C4 - Complete C7 - Verifiable C8 - Correct C9 - Conforming\n"
    )
    meta = parser.extract_rule_metadata(
        raw_text=sample_r1,
        rule_id="R1",
        rule_name="SentenceStructure",
        page_num=57
    )
    
    assert meta["id"] == "R1"
    assert meta["name"] == "SentenceStructure"
    assert meta["type"] == "rule"
    assert meta["page"] == 57
    assert meta["target_scope"] == "individual_statement"
    assert meta["established_characteristics"] == ["C3", "C4", "C7", "C8", "C9"]
    assert meta["related_rules"] == ["R2", "R3", "R11", "R18", "R27"]


def test_extract_characteristic_metadata():
    parser = IncoseParser()
    sample_c1 = (
        "## **2.1 C1 - Necessary**\n\n"
        "### Definition:\n"
        "The need or requirement statement defines an essential capability...\n\n"
        "### Rules that help establish this characteristic:\n"
        "R20 - /Singularity/AvoidPurpose\n"
        "R30 - /Uniqueness/ExpressOnce\n"
    )
    meta = parser.extract_characteristic_metadata(
        raw_text=sample_c1,
        char_id="C1",
        char_name="Necessary",
        page_num=26
    )
    
    assert meta["id"] == "C1"
    assert meta["name"] == "Necessary"
    assert meta["type"] == "characteristic"
    assert meta["page"] == 26
    assert meta["target_scope"] == "individual_statement"
    assert meta["supporting_rules"] == ["R20", "R30"]


def test_target_scope_distinction():
    parser = IncoseParser()
    
    # C1..C9 vs C10..C14
    meta_c5 = parser.extract_characteristic_metadata("", "C5", "Singular", 35)
    assert meta_c5["target_scope"] == "individual_statement"
    
    meta_c12 = parser.extract_characteristic_metadata("", "C12", "Feasible", 51)
    assert meta_c12["target_scope"] == "set_of_statements"
    
    # R1..R39 vs R40..R41
    meta_r15 = parser.extract_rule_metadata("", "R15", "LogicalCondition", 72)
    assert meta_r15["target_scope"] == "individual_statement"
    
    meta_r40 = parser.extract_rule_metadata("", "R40", "RelatedRequirements", 99)
    assert meta_r40["target_scope"] == "set_of_statements"


def test_generate_frontmatter():
    parser = IncoseParser()
    meta = {
        "id": "R1",
        "name": "SentenceStructure",
        "type": "rule",
        "page": 57,
        "target_scope": "individual_statement",
        "established_characteristics": ["C3", "C4"],
        "related_rules": ["R2", "R3"]
    }
    fm_str = parser.generate_frontmatter(meta)
    
    assert fm_str.startswith("---\n")
    assert fm_str.endswith("---\n\n")
    
    # Parse back with yaml to ensure validity
    yaml_content = fm_str.strip("- \n")
    parsed_yaml = yaml.safe_load(yaml_content)
    assert parsed_yaml["id"] == "R1"
    assert parsed_yaml["established_characteristics"] == ["C3", "C4"]


def test_integration_generated_dataset():
    """
    Kiểm tra toàn vẹn bộ dữ liệu đã được xuất ra trong data/processed:
    - Đủ 14 Characteristics và 41 Rules.
    - 100% file có YAML Frontmatter chuẩn và nội dung thân không rỗng.
    - Headers chủ đạo (Definition, Rationale, Elaboration, Examples) tồn tại.
    """
    from pathlib import Path
    
    chars = sorted(list(Path("data/processed/characteristics").glob("*.md")))
    rules = sorted(list(Path("data/processed/rules").glob("*.md")))
    
    assert len(chars) == 14, f"Expected 14 characteristics, got {len(chars)}"
    assert len(rules) == 41, f"Expected 41 rules, got {len(rules)}"
    
    # Kiểm tra Characteristics
    for cf in chars:
        content = cf.read_text(encoding="utf-8")
        assert content.startswith("---")
        parts = content.split("---", 2)
        meta = yaml.safe_load(parts[1])
        assert meta["type"] == "characteristic"
        assert meta["id"].startswith("C")
        assert "target_scope" in meta
        assert "supporting_rules" in meta
        assert isinstance(meta["page"], int)
        body = parts[2].strip()
        assert len(body) > 100
        assert "### Definition" in body or "Definition" in body
    
    # Kiểm tra Rules
    for rf in rules:
        content = rf.read_text(encoding="utf-8")
        assert content.startswith("---")
        parts = content.split("---", 2)
        meta = yaml.safe_load(parts[1])
        assert meta["type"] == "rule"
        assert meta["id"].startswith("R")
        assert "target_scope" in meta
        assert "established_characteristics" in meta
        assert "related_rules" in meta
        assert isinstance(meta["page"], int)
        body = parts[2].strip()
        assert len(body) > 100
        assert "### Elaboration" in body or "Elaboration" in body


def test_aspice_clean_text():
    parser = AspiceParser()
    sample = (
        "© VDA Quality Management Center\n\n"
        "36\n\n"
        "PUBLIC\n\n"
        "# **Process purpose**\n\n"
        "The purpose is to establish...\n\n"
        "**SYS.2.BP1: Specify system requirements.** Use the stakeholder requirements...\n"
    )
    cleaned = parser.clean_text(sample)
    assert "VDA Quality Management Center" not in cleaned
    assert "PUBLIC" not in cleaned
    assert "## Process Purpose" in cleaned
    assert "### SYS.2.BP1: Specify system requirements" in cleaned


def test_aspice_parse_integration():
    from pathlib import Path
    sys2_file = Path("data/processed/aspice/SYS.2_SystemRequirementsAnalysis.md")
    assert sys2_file.exists(), "SYS.2 markdown file must exist"
    
    content = sys2_file.read_text(encoding="utf-8")
    assert content.startswith("---")
    parts = content.split("---", 2)
    meta = yaml.safe_load(parts[1])
    
    assert meta["id"] == "SYS.2"
    assert meta["name"] == "System Requirements Analysis"
    assert meta["type"] == "process"
    assert len(meta["base_practices"]) == 6
    assert "output_information_items" in meta
    assert len(meta["output_information_items"]) == 5
    
    body = parts[2].strip()
    assert "## Process Purpose" in body
    assert "## Process Outcomes" in body
    assert "### SYS.2.BP1: Specify system requirements" in body
    assert "### SYS.2.BP6: Communicate agreed system requirements and impact on the system context" in body
    assert "## Work Products & Practice Mapping" in body
    assert "|**SYS.2 System Requirements Analysis**|Outcome 1|Outcome 2|" in body
    
    # Kiểm tra phần Annex B Output Information Items
    assert "## Output Information Item Characteristics (Annex B)" in body
    assert "### 17-00: Requirement" in body
    assert "### 17-54: Requirement Attribute" in body
    assert "### 15-51: Analysis Results" in body
    assert "### 13-51: Consistency Evidence" in body
    assert "### 13-52: Communication Evidence" in body
    assert "Design Constraint" in body
    assert "bidirectional traceability" in body


def test_aspice_annex_b_extraction():
    parser = AspiceParser()
    pdf_path = "data/raw/Automotive-SPICE-PAM-v40.pdf"
    target_ids = ["17-00", "17-54", "15-51", "13-51", "13-52"]
    names, md = parser.extract_annex_b_items(pdf_path, target_ids)
    
    assert len(names) == 5
    assert names["17-00"] == "Requirement"
    assert names["17-54"] == "Requirement Attribute"
    assert names["15-51"] == "Analysis Results"
    assert names["13-51"] == "Consistency Evidence"
    assert names["13-52"] == "Communication Evidence"
    assert "### 17-00: Requirement" in md
    assert "- An expectation of functions and capabilities" in md


