#!/usr/bin/env python3
"""
Script thực thi chuyển đổi tài liệu tiêu chuẩn sang Markdown:
1. INCOSE Guide to Writing Requirements (v3.1) -> data/processed/characteristics & rules
2. Automotive SPICE PAM v4.0 (SYS.2) -> data/processed/aspice

Cách sử dụng:
    python scripts/run_parser.py
    python scripts/run_parser.py --target aspice
    python scripts/run_parser.py --target incose
    python scripts/run_parser.py --target all
"""

import argparse
import sys
import time
from pathlib import Path

# Thêm thư mục gốc của project vào sys.path để import module từ src/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.pdf_converter import IncoseParser, AspiceParser


def parse_args():
    parser = argparse.ArgumentParser(
        description="Chuyển đổi tài liệu INCOSE & Automotive SPICE PDF sang các file Markdown chuẩn hóa."
    )
    parser.add_argument(
        "--target",
        choices=["all", "incose", "aspice"],
        default="all",
        help="Mục tiêu chuyển đổi: 'all' (cả 2), 'incose' (chỉ INCOSE), 'aspice' (chỉ ASPICE SYS.2) (mặc định: all)"
    )
    parser.add_argument(
        "--incose-pdf",
        type=str,
        default=str(PROJECT_ROOT / "data" / "raw" / "INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf"),
        help="Đường dẫn file PDF INCOSE"
    )
    parser.add_argument(
        "--aspice-pdf",
        type=str,
        default=str(PROJECT_ROOT / "data" / "raw" / "Automotive-SPICE-PAM-v40.pdf"),
        help="Đường dẫn file PDF Automotive SPICE"
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
    output_dir = Path(args.output)
    incose_pdf = Path(args.incose_pdf)
    aspice_pdf = Path(args.aspice_pdf)

    print("=" * 65)
    print("🚀 Requirements Specification Parser (INCOSE & ASPICE SYS.2)")
    print("=" * 65)
    print(f"🎯 Mục tiêu chuyển đổi : {args.target}")
    print(f"📁 Thư mục đầu ra      : {output_dir}")

    start_time = time.time()

    # 1. Chuyển đổi INCOSE
    if args.target in ["all", "incose"]:
        print(f"\n--- [1/2] BẮT ĐẦU PARSE INCOSE GUIDE ---")
        if not incose_pdf.exists():
            print(f"⚠️ Cảnh báo: Không tìm thấy file INCOSE tại {incose_pdf}")
        else:
            print(f"📄 File nguồn : {incose_pdf}")
            incose_parser = IncoseParser()
            results = incose_parser.parse_pdf(str(incose_pdf), str(output_dir))
            char_count = len(results.get("characteristics", []))
            rule_count = len(results.get("rules", []))
            print(f"✅ Characteristics : {char_count} files -> {output_dir / 'characteristics'}")
            print(f"✅ Rules           : {rule_count} files -> {output_dir / 'rules'}")

    # 2. Chuyển đổi Automotive SPICE SYS.2
    if args.target in ["all", "aspice"]:
        print(f"\n--- [2/2] BẮT ĐẦU PARSE AUTOMOTIVE SPICE SYS.2 ---")
        if not aspice_pdf.exists():
            print(f"⚠️ Cảnh báo: Không tìm thấy file ASPICE tại {aspice_pdf}")
        else:
            print(f"📄 File nguồn : {aspice_pdf} (Trang 36-37)")
            aspice_parser = AspiceParser()
            sys2_file = aspice_parser.parse_sys2(str(aspice_pdf), str(output_dir))
            print(f"✅ ASPICE SYS.2   : 1 file  -> {sys2_file}")

    elapsed_time = time.time() - start_time
    print("\n" + "=" * 65)
    print("🎉 HOÀN TẤT TOÀN BỘ TIẾN TRÌNH!")
    print(f"⏱️  Tổng thời gian : {elapsed_time:.2f} giây")
    print("=" * 65)


if __name__ == "__main__":
    main()
