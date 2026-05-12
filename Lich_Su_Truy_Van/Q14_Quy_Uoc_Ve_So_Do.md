# Q14: Quy Ước Về Sơ Đồ

## 1. Câu hỏi
các sơ đồ là code để markdown review ra sơ đồ, biểu đồ rõ ràng đúng chuẩn EDR...

## 2. Suy nghĩ (Thinking)
Người dùng muốn thiết lập quy ước: khi tạo các sơ đồ, biểu đồ trong file Markdown, phải dùng định dạng mã code (ví dụ Mermaid hoặc PlantUML) để trình hiển thị (reviewer) có thể render trực tiếp thành hình ảnh, và tuân thủ đúng các chuẩn thiết kế (chẳng hạn ERD, UML, DFD...). Tôi cần xác nhận và áp dụng quy tắc này (sử dụng MermaidJS vì đây là chuẩn phổ biến nhất cho Markdown) vào các lần tạo sơ đồ tiếp theo. Đồng thời, tôi sẽ hỏi người dùng có muốn lưu quy tắc này vào file `GEMINI.md` để áp dụng lâu dài cho toàn dự án không.

## 3. Câu trả lời
Đã ghi nhận yêu cầu! Từ giờ, khi có yêu cầu thiết kế sơ đồ (như Sơ đồ thực thể liên kết - ERD, Use Case, Activity, Class diagram, DFD...), tôi sẽ sử dụng cú pháp mã code như **Mermaid.js** ngay bên trong Markdown. Cách này giúp bạn dễ dàng xem (render/review) trực tiếp ra biểu đồ rõ ràng, chuẩn xác theo yêu cầu.

Bạn có muốn tôi lưu hẳn quy tắc "luôn dùng Mermaid cho các sơ đồ Markdown" này vào file `GEMINI.md` của dự án để đảm bảo mọi thao tác sau này đều tự động tuân thủ không?