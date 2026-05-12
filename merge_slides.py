import os

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

output_md = os.path.join(base_dir, "GIAO_TRINH_TOAN_DIEN_TU_SLIDE_TRUONG.md")

with open(output_md, "w", encoding="utf-8") as outfile:
    output_title = "# GIÁO TRÌNH TOÀN DIỆN KỸ NGHỆ PHẦN MỀM (TỔNG HỢP TỪ SLIDE BÀI GIẢNG)\n\n"
    output_title += "> Tài liệu này được tổng hợp tự động từ toàn bộ các slide bài giảng từ Chương 0 đến Chương 7 để ôn thi chuẩn sát nhất với chương trình học.\n\n---\n\n"
    outfile.write(output_title)
    
    for filename in files_to_merge:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as infile:
                content = infile.read()
                outfile.write(f"\n\n<!-- BẮT ĐẦU FILE: {filename} -->\n")
                outfile.write(content)
                outfile.write(f"\n<!-- KẾT THÚC FILE: {filename} -->\n\n---\n")
            print(f"Đã gộp: {filename}")
        else:
            print(f"LỖI: Không tìm thấy file {filename}")

print(f"\nHoàn tất! File tổng hợp đã được lưu tại: {output_md}")
