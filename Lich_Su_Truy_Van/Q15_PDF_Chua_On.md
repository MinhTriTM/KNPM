# Câu hỏi: PDF chưa ổn

## Câu hỏi
Người dùng nói file `Tổng Hợp Tài Liệu KNPM Toàn Diện - PDF Ready.pdf` "chưa ổn".

## Suy nghĩ (Thinking)
1. **Phân tích vấn đề:** File PDF chỉ 283KB trong khi file Markdown nguồn có 173KB (2035 dòng) - rõ ràng nội dung bị thiếu hoặc không render đúng.
2. **Nguyên nhân gốc:** File `md_to_pdf.html` dùng XHR để đọc file `.md` - khi mở bằng giao thức `file://`, trình duyệt chặn do CORS policy → không đọc được nội dung → PDF bị trống/thiếu.
3. **Thêm vấn đề:** Mermaid `usecaseDiagram` không được thư viện Mermaid hỗ trợ chính thức → các sơ đồ Use-case bị lỗi render.
4. **Giải pháp:** 
   - Cải tiến `md_to_pdf.html` với CSS tối ưu hơn, xử lý lỗi Mermaid từng block riêng lẻ
   - Tạo script `build_pdf.ps1` để nhúng toàn bộ markdown dưới dạng Base64 vào HTML → file tự chứa, không cần HTTP server
   - Hoặc dùng HTTP server (`npx serve .`) rồi mở qua `http://localhost:3000`

## Câu trả lời
- Đã cải tiến file `md_to_pdf.html` với:
  - CSS tối ưu cho in PDF (font nhỏ hơn, margin chặt hơn)
  - Xử lý lỗi Mermaid từng block riêng lẻ 
  - Fallback đẹp cho usecaseDiagram (không được Mermaid hỗ trợ)
  - Thông báo lỗi CORS rõ ràng với hướng dẫn giải pháp
- Đã tạo script `build_pdf.ps1` để build HTML tự chứa
- Hướng dẫn: Chạy `powershell -ExecutionPolicy Bypass -File build_pdf.ps1` hoặc `npx serve .` rồi mở `http://localhost:3000/md_to_pdf.html`
