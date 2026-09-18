#!/usr/bin/env python3
"""
Script thực thi chuyển đổi INCOSE Guide to Writing Requirements (v3.1)
từ PDF sang Markdown theo từng tiêu chí (Characteristics & Rules).

Cách sử dụng:
    python scripts/run_parser.py
    python scripts/run_parser.py --pdf data/raw/INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf --output data/processed
"""

import argparse
import sys
import time
from pathlib import Path

# Thêm thư mục gốc của project vào sys.path để import module từ src/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.pdf_converter import IncoseParser


def parse_args():
    parser = argparse.ArgumentParser(
        description="Chuyển đổi tài liệu INCOSE PDF sang các file Markdown theo từng tiêu chí."
    )
    parser.add_argument(
        "--pdf",
        type=str,
        default=str(PROJECT_ROOT / "data" / "raw" / "INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf"),
        help="Đường dẫn đến file PDF INCOSE (mặc định: data/raw/INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=str(PROJECT_ROOT / "data" / "processed"),
        help="Thư mục xuất kết quả (mặc định: data/processed)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    pdf_path = Path(args.pdf)
    output_dir = Path(args.output)

    print("=" * 60)
    print("🚀 INCOSE PDF to Markdown Parser")
    print("=" * 60)
    print(f"📄 File PDF nguồn : {pdf_path}")
    print(f"📁 Thư mục đầu ra : {output_dir}")

    if not pdf_path.exists():
        print(f"\n❌ LỖI: Không tìm thấy file PDF tại: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    start_time = time.time()
    try:
        parser = IncoseParser()
        print("\n⏳ Đang xử lý bóc tách các tiêu chí...")
        results = parser.parse_pdf(str(pdf_path), str(output_dir))

        elapsed_time = time.time() - start_time
        char_count = len(results.get("characteristics", []))
        rule_count = len(results.get("rules", []))
        total_count = char_count + rule_count

        print("\n" + "=" * 60)
        print("✅ QUÁ TRÌNH CHUYỂN ĐỔI HOÀN TẤT THÀNH CÔNG!")
        print("=" * 60)
        print(f"⏱️  Thời gian thực thi : {elapsed_time:.2f} giây")
        print(f"📋 Characteristics    : {char_count:2d} files  ->  {output_dir / 'characteristics'}")
        print(f"📏 Rules              : {rule_count:2d} files  ->  {output_dir / 'rules'}")
        print(f"🎯 Tổng số tiêu chí   : {total_count:2d} files")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Đã xảy ra lỗi trong quá trình xử lý: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
