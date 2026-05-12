import re
import os

md_file = r'D:\Download\Thi\KNPM\Ngan_Hang_100_Cau_Hoi_KNPM.md'
html_file = r'D:\Download\Thi\KNPM\Giao_Trinh_KNPM_Toc_Hanh_36h.html'

with open(md_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

html_content = ["<div class=\"page-break\"></div>", "<h2>CHƯƠNG 7: NGÂN HÀNG 100 CÂU HỎI LÝ THUYẾT TRỌNG TÂM</h2>"]
html_content.append("<div class=\"tip-box\"><h4>💡 Mục tiêu:</h4><p>Học thuộc lòng 100 câu hỏi này để đảm bảo ăn trọn điểm phần lý thuyết (thường là 5 điểm) trong bài thi tự luận hoặc trắc nghiệm.</p></div>")

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith('## '):
        # Chapter header
        html_content.append(f"<h3>{line[3:]}</h3>")
    elif line.startswith('**') and line.endswith('**') and re.match(r'\*\*\d+\.', line):
        # Question
        q = line.strip('*')
        html_content.append(f"<p class=\"kw\" style=\"margin-top: 15px;\">{q}</p>")
    elif line.startswith('=>'):
        # Answer
        ans = line[2:].strip()
        html_content.append(f"<p style=\"margin-left: 20px; border-left: 3px solid var(--secondary); padding-left: 10px;\"><strong>Đáp án:</strong> {ans}</p>")
    elif line.startswith('*(') and line.endswith(')*'):
        pass
    elif line.startswith('#'):
        pass
    else:
        pass # ignore other lines for now

html_to_inject = "\n".join(html_content)

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before the closing message
insert_marker = '<div style="text-align: center; margin-top: 60px; font-size: 1.2em; border-top: 2px solid var(--primary); padding-top: 20px;">'
if insert_marker in content:
    content = content.replace(insert_marker, html_to_inject + "\n\n" + insert_marker)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injection successful.")
else:
    print("Marker not found.")
