import os
import re

base_dir = r"D:\Download\Thi\KNPM"
files_to_merge = [
    "C0_DCCT_MH_v3.md",
    "C1_GioiThieuCNPM_v2.md",
    "C2_QuyTrinhPM_send.md",
    "C3_YeuCauPM.md",
    "C4_MoHinhHoaPM.md",
    "C5_1ThietKePM_KN.md",
    "C5_2ThietKePM_KienTruc.md",
    "C5_3ThietKePM_TKDuLieu_HDT.md",
    "C5_4ThietKePM_TKGiaoDien.md",
    "C5_5ThietKePM_Gioithieu_tpXuLy.md",
    "C6_LapTrinh.md",
    "C7_KiemThuPM.md"
]

def clean_fake_tables(text):
    # Xóa các dòng phân cách bảng (ví dụ: | --- | --- |)
    text = re.sub(r'^\|[-\s\|]+\|\n?', '', text, flags=re.MULTILINE)
    
    # Xử lý các dòng còn lại
    lines = text.split('\n')
    cleaned_lines = []
    
    in_table_block = False
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|') and len(line.strip()) > 1:
            # Dòng này là dòng bảng giả
            l = line.strip()[1:-1] # Bỏ | ở đầu và cuối
            l = l.replace('|', ' ') # Thay thế | bên trong bằng khoảng trắng
            l = re.sub(r'\s+', ' ', l).strip() # Xóa khoảng trắng thừa
            cleaned_lines.append(l)
        else:
            cleaned_lines.append(line)
            
    return '\n'.join(cleaned_lines)

for filename in files_to_merge:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = clean_fake_tables(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Đã dọn dẹp: {filename}")

print("Xong!")
