# -*- coding: utf-8 -*-
"""
Script tạo file HTML tự chứa nội dung Markdown để in PDF.
Chạy: python build_html.py
Kết quả: KNPM_Print.html (mở trực tiếp trình duyệt → Ctrl+P để in PDF)
"""
import os
import base64

script_dir = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(script_dir, "Tong_Hop_Tai_Lieu_KNPM_Toan_Dien_Full.md")
html_path = os.path.join(script_dir, "KNPM_Print.html")

print("=" * 50)
print("  KNPM Markdown → PDF Builder")
print("=" * 50)
print()

print("[1/3] Đang đọc file Markdown...")
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Encode content sang Base64 để tránh mọi vấn đề escape
md_b64 = base64.b64encode(md_content.encode("utf-8")).decode("ascii")

print(f"      Kích thước: {len(md_content):,} ký tự")
print(f"      Base64: {len(md_b64):,} ký tự")

print("[2/3] Đang tạo file HTML tự chứa...")

html_out = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tổng Hợp Tài Liệu KNPM Toàn Diện - PDF Ready</title>
    <script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', 'Noto Sans', Arial, sans-serif;
            font-size: 13px; line-height: 1.65; color: #1a1a2e;
            background: #fff; padding: 18px 28px;
            max-width: 210mm; margin: 0 auto;
        }
        h1 { font-size: 20px; color: #0d1b2a; text-align: center; border-bottom: 3px solid #1b4965; padding-bottom: 8px; margin-bottom: 6px; page-break-after: avoid; }
        h2 { font-size: 16px; color: #1b4965; border-bottom: 2px solid #62b6cb; padding-bottom: 4px; margin-top: 20px; margin-bottom: 8px; page-break-after: avoid; }
        h3 { font-size: 14.5px; color: #274c77; margin-top: 14px; margin-bottom: 6px; page-break-after: avoid; }
        h4 { font-size: 13px; color: #3a6ea5; margin-top: 10px; margin-bottom: 4px; page-break-after: avoid; }
        p { margin-bottom: 6px; text-align: justify; }
        em { color: #555; } strong { color: #0d1b2a; }
        ul, ol { margin-left: 22px; margin-bottom: 6px; }
        li { margin-bottom: 3px; }
        table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 11.5px; page-break-inside: avoid; }
        th { background: #1b4965; color: #fff; padding: 5px 7px; text-align: left; font-weight: 600; }
        td { padding: 4px 7px; border: 1px solid #ccc; vertical-align: top; }
        tr:nth-child(even) td { background: #f0f4f8; }
        code { background: #e8eef3; padding: 1px 4px; border-radius: 3px; font-family: Consolas, monospace; font-size: 12px; color: #c7254e; }
        pre { background: #f5f7fa; border: 1px solid #d0d7de; border-left: 4px solid #1b4965; padding: 8px 12px; margin: 8px 0; overflow-x: auto; border-radius: 4px; page-break-inside: avoid; font-size: 11px; line-height: 1.45; }
        pre code { background: none; padding: 0; color: #24292f; }
        .mermaid { text-align: center; margin: 10px 0; page-break-inside: avoid; }
        .mermaid svg { max-width: 100%; height: auto; }
        hr { border: none; border-top: 2px solid #bee3f8; margin: 18px 0; }
        blockquote { border-left: 4px solid #62b6cb; padding: 6px 14px; margin: 8px 0; background: #f0f9ff; color: #333; font-size: 12.5px; }

        /* In ấn */
        @media print {
            body { padding: 0; margin: 0; font-size: 11px; line-height: 1.5; max-width: none; }
            h1 { font-size: 16px; margin-top: 0; }
            h2 { font-size: 13.5px; margin-top: 12px; }
            h3 { font-size: 12px; }
            h4 { font-size: 11px; }
            pre { font-size: 9px; padding: 4px 8px; }
            table { font-size: 9.5px; }
            th { padding: 3px 4px; }
            td { padding: 2px 4px; }
            .mermaid svg { max-height: 220px; }
            h1, h2, h3, h4 { page-break-after: avoid; }
            table, pre, .mermaid { page-break-inside: avoid; }
            p { orphans: 3; widows: 3; }
            .no-print { display: none !important; }
            @page { size: A4; margin: 10mm 12mm; }
        }

        .print-bar {
            position: fixed; top: 0; left: 0; right: 0;
            background: linear-gradient(135deg, #1b4965, #3a6ea5);
            color: #fff; padding: 10px 20px;
            display: flex; align-items: center; justify-content: space-between;
            z-index: 9999; box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        .print-bar span { font-size: 14px; font-weight: 600; }
        .print-bar button {
            background: #fff; color: #1b4965; border: none;
            padding: 8px 24px; font-size: 14px; font-weight: 700;
            border-radius: 6px; cursor: pointer; transition: background 0.2s;
        }
        .print-bar button:hover { background: #bee3f8; }
        #content { margin-top: 55px; }
        #loading {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: #fff; display: flex; flex-direction: column;
            align-items: center; justify-content: center; z-index: 99999;
            font-size: 18px; color: #1b4965;
        }
        .spinner {
            width: 50px; height: 50px; border: 4px solid #e0e0e0;
            border-top: 4px solid #1b4965; border-radius: 50%;
            animation: spin 1s linear infinite; margin-bottom: 16px;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div id="loading">
        <div class="spinner"></div>
        <p>Đang render tài liệu & sơ đồ Mermaid... Vui lòng đợi vài giây</p>
    </div>

    <div class="print-bar no-print">
        <span>📄 Tổng Hợp Tài Liệu KNPM Toàn Diện</span>
        <button onclick="window.print()">🖨️ In PDF (Ctrl+P)</button>
    </div>

    <div id="content"></div>

    <script>
    // Nội dung MD được mã hóa Base64, nhúng trực tiếp
    var MD_BASE64 = "''' + md_b64 + '''";

    (function() {
        // Giải mã Base64 → UTF-8
        var raw = decodeURIComponent(escape(atob(MD_BASE64)));

        // Tách mermaid blocks ra thành HTML div
        var processed = raw.replace(/```mermaid\\s*\\n([\\s\\S]*?)```/g, function(m, code) {
            return '\\n<div class="mermaid">' + code.trim() + '</div>\\n';
        });

        // Render markdown bằng markdown-it
        var md = window.markdownit({ html: true, breaks: true, typographer: true });
        document.getElementById('content').innerHTML = md.render(processed);

        // Khởi tạo và render Mermaid diagrams
        mermaid.initialize({
            startOnLoad: false,
            theme: 'default',
            securityLevel: 'loose',
            fontSize: 12,
            flowchart: { useMaxWidth: true }
        });

        setTimeout(function() {
            try {
                mermaid.run().then(function() {
                    document.getElementById('loading').style.display = 'none';
                }).catch(function(e) {
                    console.warn('Mermaid partial error (some diagrams may use unsupported syntax):', e);
                    document.getElementById('loading').style.display = 'none';
                });
            } catch(e) {
                console.warn('Mermaid init error:', e);
                document.getElementById('loading').style.display = 'none';
            }
        }, 500);
    })();
    </script>
</body>
</html>'''

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_out)

size_kb = os.path.getsize(html_path) / 1024
print(f"      File: KNPM_Print.html ({size_kb:.0f} KB)")

print("[3/3] Đang mở file trong trình duyệt...")
# os.startfile(html_path)

print()
print("✅ HOÀN THÀNH!")
print()
print("📋 HƯỚNG DẪN IN PDF:")
print("   1. File đã mở trong trình duyệt (đợi vài giây để render)")
print("   2. Nhấn Ctrl+P (hoặc nút 'In PDF' trên trang)")
print("   3. Destination: chọn 'Save as PDF'")
print("   4. Layout: Portrait")
print("   5. Margins: Default hoặc Minimum")
print("   6. Nhấn Save")
print()
# input
