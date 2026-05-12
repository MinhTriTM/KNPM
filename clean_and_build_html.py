import os
import re
import markdown

base_dir = r"D:\Download\Thi\KNPM"
input_md = os.path.join(base_dir, "GIAO_TRINH_TOAN_DIEN_TU_SLIDE_TRUONG.md")
output_html = os.path.join(base_dir, "Giao_Trinh_Full_Slide_Dep.html")

if not os.path.exists(input_md):
    print("Không tìm thấy file nguồn. Vui lòng chạy merge_slides.py trước.")
    exit()

with open(input_md, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Dọn dẹp rác từ Slide PDF (Footer, Email, Chữ dư thừa)
content = re.sub(r'tkhuong@dthu\.edu\.vn', '', content)
content = re.sub(r'Software Engineering(\s+\d+)?', '', content)
content = re.sub(r'LOGO', '', content)
content = re.sub(r'', '', content) # Xóa ký tự ngắt trang đặc biệt của PDF

# 1.5 Dọn dẹp các bảng giả (do PDF chuyển sang Markdown tạo ra các ký tự |)
# Xóa thông minh: Chỉ xóa bảng giả, giữ lại bảng thật.
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip().startswith('|') and line.strip().endswith('|') and len(line.strip()) > 1:
        table_block = []
        while i < len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|') and len(lines[i].strip()) > 1:
            table_block.append(lines[i])
            i += 1
            
        is_fake = False
        empty_cells = 0
        total_cells = 0
        for r in table_block:
            cells = r.split('|')
            if '---' in r: continue
            total_cells += len(cells) - 2
            for c in cells[1:-1]:
                if not c.strip():
                    empty_cells += 1
                    
        text_content = '\n'.join(table_block)
        if '❖' in text_content or (total_cells > 0 and empty_cells / total_cells > 0.25):
            is_fake = True
            
        if is_fake:
            for r in table_block:
                if re.match(r'^\|[-\s\|]+\|$', r.strip()):
                    continue
                l = r.strip()[1:-1].replace('|', ' ')
                l = re.sub(r'\s+', ' ', l).strip()
                if l:
                    new_lines.append(l)
        else:
            new_lines.extend(table_block)
        continue
    else:
        new_lines.append(line)
        i += 1

content = '\n'.join(new_lines)
content = re.sub(r'\n{3,}', '\n\n', content)

# 2. Chuyển Markdown sang HTML
html_body = markdown.markdown(content, extensions=['tables', 'fenced_code'])

# 3. Bọc HTML Body vào một Template in ấn cực đẹp (Giống file 36h)
html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Giáo Trình KNPM - Tổng Hợp Toàn Bộ Slide Trường</title>
    <style>
        :root {{
            --primary: #1a365d;
            --secondary: #2b6cb0;
            --bg-light: #f7fafc;
            --text-main: #2d3748;
            --border: #e2e8f0;
        }}
        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            color: var(--text-main);
            background-color: #fff;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px 40px;
        }}
        h1, h2, h3, h4 {{
            color: var(--primary);
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            page-break-after: avoid;
        }}
        h1 {{
            font-size: 2.2em;
            text-align: center;
            border-bottom: 4px solid var(--primary);
            padding-bottom: 15px;
            margin-bottom: 40px;
        }}
        h2 {{
            font-size: 1.8em;
            border-bottom: 2px solid var(--secondary);
            background-color: var(--bg-light);
            padding: 8px 10px;
            border-left: 6px solid var(--primary);
        }}
        h3 {{
            color: var(--secondary);
            border-bottom: 1px dashed var(--border);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            page-break-inside: avoid;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        th, td {{
            border: 1px solid var(--border);
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: var(--secondary);
            color: white;
        }}
        tr:nth-child(even) {{ background-color: var(--bg-light); }}
        
        .print-btn {{
            display: block;
            width: 250px;
            margin: 30px auto;
            padding: 15px;
            text-align: center;
            background-color: var(--primary);
            color: white;
            text-decoration: none;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
        }}
        
        @media print {{
            body {{ font-size: 11pt; }}
            .container {{ max-width: 100%; padding: 0 10mm; }}
            .print-btn {{ display: none; }}
            .page-break {{ page-break-before: always; }}
            h1, h2, h3 {{ page-break-after: avoid; }}
            table, img {{ page-break-inside: avoid; }}
            * {{ -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
        
        <button class="print-btn" onclick="window.print()">🖨️ In Giáo Trình Này (Ctrl+P)</button>
    </div>
</body>
</html>"""

with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Thành công! Đã dọn dẹp rác và tạo file giao diện đẹp tại: {output_html}")
