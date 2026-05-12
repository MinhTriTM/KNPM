import re
from pathlib import Path

def reorganize():
    path = Path("d:/Download/Thi/KNPM/Giao_Trinh_KNPM_Toc_Hanh_36h.html")
    content = path.read_text(encoding="utf-8")
    
    # 1. Extract the questions
    q_pattern = re.compile(r"<h3>CHƯƠNG (\d+):.*?\((Câu \d+ - Câu \d+)\)</h3>(.*?)((?=<h3>CHƯƠNG)|(?=<!-- ========================================== -->)|(?=<div class=\"box\"))", re.DOTALL)
    
    questions = {}
    for match in q_pattern.finditer(content):
        ch_num = int(match.group(1))
        q_html = match.group(3).strip()
        questions[ch_num] = q_html
        
    # 2. Extract the theory sections
    # They are separated by:
    # <!-- ========================================== -->
    # CHƯƠNG X: ...
    # <!-- ========================================== -->
    
    parts = re.split(r"<!-- ========================================== -->\s*<!-- CHƯƠNG \d+:.*?-->\s*<!-- ========================================== -->", content)
    
    # parts[0] is everything before CHƯƠNG 1
    header = parts[0]
    
    # Let's extract the actual theory chunks
    t_pattern = re.compile(r"<h2>CHƯƠNG \d+: (.*?)</h2>(.*)", re.DOTALL)
    
    # We will build the new body manually based on the parts
    # Wait, the structure in the file currently:
    # parts[1] -> CHƯƠNG 1: TỔNG QUAN & CÁC MÔ HÌNH PHÁT TRIỂN (SDLC)
    # parts[2] -> CHƯƠNG 2: PHÂN TÍCH & ĐẶC TẢ YÊU CẦU
    # parts[3] -> CHƯƠNG 3: THIẾT KẾ PHẦN MỀM CƠ BẢN
    # parts[4] -> CHƯƠNG 4: ĐẠI CHIẾN SƠ ĐỒ UML & ERD
    # parts[5] -> CHƯƠNG 5: KIỂM THỬ PHẦN MỀM CỰC KỲ CHI TIẾT
    # parts[6] -> CHƯƠNG 6: BẢO TRÌ VÀ QUẢN LÝ DỰ ÁN
    # parts[7] -> CHƯƠNG 7: NGÂN HÀNG 100 CÂU HỎI
    # Then there is the BỘ ĐỀ THI at the end.
    
    # Let's verify parts length
    if len(parts) < 8:
        print("Could not split by comments properly. Let's use h2 instead.")
        # Fallback to splitting by <h2>
        parts = re.split(r"(<h2>CHƯƠNG \d+: .*?</h2>)", content)
        # parts[0] = header
        # parts[1] = <h2>CHƯƠNG 1...</h2>
        # parts[2] = content of CH1
        # etc.
    
    print("Parts length:", len(parts))
    
reorganize()
