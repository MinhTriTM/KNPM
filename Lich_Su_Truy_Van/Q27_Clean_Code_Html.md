# Câu hỏi
@Giao_Trinh_Full_Slide_Dep.html clean lại cho đẹp hơn hoàn thiện hơn, đúng hơn...

# Suy nghĩ (Thinking)
CRITICAL INSTRUCTION 1: Sử dụng `write_file` thay vì chạy bash cat/echo để tạo file script.
CRITICAL INSTRUCTION 2: Các công cụ liên quan: `write_file` (ghi mã Python), `run_shell_command` (chạy script).

Tôi đã quan sát thấy file `GIAO_TRINH_TOAN_DIEN_TU_SLIDE_TRUONG.md` được sinh ra từ các file `.md` gốc. Tuy nhiên, các file `.md` gốc này dường như là kết quả của một bộ công cụ OCR/Extract Text từ PDF. Nó tạo ra các BẢNG MARKDOWN bị vỡ vụn (chứa đầy các ký tự `| --- | --- |`), các Header vô nghĩa, dòng số trang, và hàng trăm dòng text bị ngắt dòng sai vị trí. 

Vì file HTML hiện tại chỉ render trực tiếp từ file Markdown hỏng đó, nên kết quả HTML cũng bị hỏng (chứa hàng loạt các bảng vỡ).
Tôi cần cập nhật file `clean_and_build_html.py` với một bộ lọc bằng Regular Expression (Regex) cực kỳ mạnh mẽ để "giết" hết đống rác này:
- Quét sạch các dòng `| --- | --- |` vô nghĩa.
- Xóa bỏ các dòng chỉ chứa ký tự phân cách `---` và `|`.
- Loại bỏ các dòng chỉ chứa số trang lẻ loi.
- Nối các câu bị ngắt dòng ngang chừng lại với nhau.

# Câu trả lời
Phản hồi với user về việc cập nhật kịch bản Python mới để dọn dẹp triệt để các cấu trúc rác.