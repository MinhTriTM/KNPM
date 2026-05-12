import os
import re
import markdown

base_dir = r"D:\Download\Thi\KNPM"
input_md = os.path.join(base_dir, "Bo_De_Thi_KNPM_Toan_Dien.md")
output_html = os.path.join(base_dir, "Giao_Trinh_KNPM_Toc_Hanh_36h.html")

if not os.path.exists(input_md):
    print("Không tìm thấy file nguồn MD.")
    exit()

if not os.path.exists(output_html):
    print("Không tìm thấy file HTML đích.")
    exit()

with open(input_md, "r", encoding="utf-8") as f:
    md_content = f.read()

# Chuyển đổi Markdown sang HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br'])

# Bọc nội dung vào một div
injected_html = f"""
        <div class="box" style="background-color: white; border: 2px solid var(--secondary); margin-top: 40px; page-break-before: always;">
            {html_content}
        </div>
"""

with open(output_html, "r", encoding="utf-8") as f:
    html_target = f.read()

# Chèn vào trước phần footer
target_marker = """<div style="text-align: center; margin-top: 60px; font-size: 1.2em; border-top: 2px solid var(--primary); padding-top: 20px;">"""

if target_marker in html_target:
    new_html = html_target.replace(target_marker, injected_html + "\n" + target_marker)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Đã chèn thành công bộ đề thi vào file HTML!")
else:
    print("Không tìm thấy vị trí chèn trong file HTML.")
