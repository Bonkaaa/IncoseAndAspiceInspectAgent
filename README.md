# IncoseAndAspiceInspectAgent

Hệ thống Agent tự động thẩm định và đánh giá chất lượng yêu cầu kỹ thuật (Requirements Engineering) dựa trên tiêu chuẩn **INCOSE Guide to Writing Requirements (v3.1)** và quy trình **Automotive SPICE (ASPICE) SYS.2**.

---

## 📁 Cấu Trúc Thư Mục

```text
IncoseAndAspiceInspectAgent/
├── data/
│   ├── raw/                  # Chứa các file PDF tài liệu tiêu chuẩn gốc
│   │   ├── INCOSE_RWG_Guide_to_Writing_Requirements_V3.1_041822.pdf
│   │   └── Automotive-SPICE-PAM-v40.pdf
│   └── processed/            # Dữ liệu Markdown sau khi parse theo tiêu chí
│       ├── characteristics/  # 14 file đặc tính INCOSE (C01 - C14)
│       ├── rules/            # 41 file quy tắc INCOSE (R01 - R41)
│       └── aspice/           # Quy trình Automotive SPICE SYS.2
│           └── SYS.2_SystemRequirementsAnalysis.md
├── docs/                     # Tài liệu kiến trúc và hướng dẫn kỹ thuật
│   └── incose_parsing_guide.md
├── scripts/                  # Các script tiện ích thực thi
│   └── run_parser.py         # Script chạy công cụ parse PDF (INCOSE & ASPICE)
├── src/                      # Mã nguồn chính
│   └── pdf_converter.py      # IncoseParser & AspiceParser
├── tests/                    # Bộ kiểm thử theo quy trình TDD
│   └── test_pdf_converter.py
└── requirements.txt
```

---

## 🚀 Hướng Dẫn Sử Dụng

### 1. Cài đặt môi trường
```powershell
pip install -r requirements.txt
```

### 2. Chạy chuyển đổi PDF sang Markdown
Bạn có thể chạy trực tiếp file script tại [scripts/run_parser.py](scripts/run_parser.py):

```powershell
# Chạy chuyển đổi cả INCOSE và Automotive SPICE SYS.2 (mặc định)
python scripts/run_parser.py --target all

# Chỉ chuyển đổi Automotive SPICE SYS.2 (Trang 36-37)
python scripts/run_parser.py --target aspice

# Chỉ chuyển đổi INCOSE Guide (55 tiêu chí)
python scripts/run_parser.py --target incose
```

### 3. Chạy kiểm thử tự động (Unit & Integration Tests)
```powershell
pytest tests/test_pdf_converter.py -v
```
