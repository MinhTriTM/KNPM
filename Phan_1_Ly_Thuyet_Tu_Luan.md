# TỔNG HỢP ÔN THI KỸ NGHỆ PHẦN MỀM - PHẦN 1
**TOÀN BỘ LÝ THUYẾT TRỌNG TÂM (Trình bày theo phong cách tự luận chi tiết)**

*Lưu ý: Dưới đây là các câu hỏi lý thuyết thường gặp nhất trong đề thi. Đáp án được trình bày dưới dạng một bài thi tự luận hoàn chỉnh của sinh viên (giải thích rõ ràng, có diễn giải, không chỉ gạch đầu dòng vắn tắt như barem giáo viên) để giúp bạn đạt điểm tối đa.*

---

**Câu 1: Hãy nêu những tiêu chí mà người sử dụng đánh giá chất lượng phần mềm?**
**Bài làm:**
Dưới góc nhìn của người sử dụng (người không quan tâm đến mã nguồn hay kiến trúc hệ thống), một phần mềm được đánh giá là có chất lượng tốt khi nó thỏa mãn các tiêu chí cốt lõi sau:
1. **Tính đúng đắn (Correctness):** Phần mềm phải thực hiện chính xác các chức năng mà người dùng mong muốn. Kết quả tính toán hoặc xử lý dữ liệu phải chuẩn xác, không xảy ra sai sót.
2. **Tính tiện dụng (Usability):** Giao diện phải trực quan, thân thiện, dễ học và dễ sử dụng. Hệ thống cần điều hướng logic để người dùng không mất quá nhiều thời gian làm quen.
3. **Tính hiệu quả (Efficiency):** Phần mềm phải phản hồi thao tác nhanh chóng, không bị giật lag, đồng thời không ngốn quá nhiều tài nguyên của thiết bị (như RAM, CPU, hoặc làm hao pin nhanh).
4. **Tính tương thích (Compatibility):** Ứng dụng có thể chạy ổn định trên các nền tảng, hệ điều hành (Windows, macOS) hoặc trình duyệt (Chrome, Safari) mà người dùng đang sử dụng.
5. **Khả năng phục hồi và an toàn (Dependability & Recoverability):** Khi người dùng thao tác sai hoặc rớt mạng, phần mềm không bị "sập" (crash) mà phải đưa ra thông báo lỗi rõ ràng và bảo vệ dữ liệu không bị mất mát.

**Câu 2: Công nghệ phần mềm là gì? Công nghệ phần mềm nghiên cứu những vấn đề gì?**
**Bài làm:**
- **Định nghĩa:** Công nghệ phần mềm (Software Engineering) là một chuyên ngành kỹ thuật áp dụng một cách tiếp cận có hệ thống, có kỷ luật và có thể định lượng được vào việc phát triển, vận hành và bảo trì phần mềm. Nó biến việc lập trình tự phát thành một quy trình sản xuất mang tính công nghiệp nhằm tạo ra phần mềm chất lượng cao, đúng tiến độ và trong phạm vi ngân sách.
- **Những vấn đề nghiên cứu cốt lõi:** Công nghệ phần mềm tập trung nghiên cứu 3 nền tảng chính:
  1. *Phương pháp (Methods):* Cung cấp các kỹ thuật chuyên môn để xây dựng phần mềm (cách thu thập yêu cầu, cách vẽ biểu đồ thiết kế kiến trúc, cách viết mã nguồn và kiểm thử).
  2. *Quy trình (Process):* Nghiên cứu các mô hình vòng đời phát triển phần mềm (như Thác nước, Agile, Scrum) để kết nối các phương pháp lại với nhau, quy định rõ ai làm việc gì, vào lúc nào.
  3. *Công cụ (Tools):* Nghiên cứu và phát triển các phần mềm hỗ trợ tự động hoặc bán tự động cho phương pháp và quy trình (như công cụ quản lý code Git, công cụ vẽ UML, phần mềm test tự động).

**Câu 3: Quy trình phát triển phần mềm gồm có mấy hoạt động cơ bản? Kể tên?**
**Bài làm:**
Bất kể áp dụng mô hình phát triển nào (cổ điển hay hiện đại), một quy trình phát triển phần mềm chuẩn luôn phải đi qua 4 hoạt động cơ bản không thể thiếu:
1. **Đặc tả phần mềm (Software Specification):** Hoạt động định nghĩa phần mềm phải làm những chức năng gì, đáp ứng những ràng buộc nào từ phía người dùng và hệ thống.
2. **Phát triển phần mềm (Software Development/Design & Implementation):** Hoạt động thiết kế cấu trúc hệ thống, cơ sở dữ liệu, giao diện và tiến hành viết mã nguồn (coding) để tạo ra phần mềm.
3. **Thẩm định phần mềm (Software Validation/Testing):** Hoạt động kiểm thử để xác minh rằng phần mềm không có lỗi và đáp ứng chính xác những gì khách hàng đã yêu cầu ban đầu.
4. **Tiến hóa phần mềm (Software Evolution/Maintenance):** Hoạt động bảo trì, sửa lỗi và nâng cấp, thêm tính năng mới cho phần mềm sau khi đã bàn giao để đáp ứng sự thay đổi của môi trường kinh doanh.

**Câu 4: Nêu 3 mô hình quy trình phát triển phần mềm mà em đã tìm hiểu? Phân tích ngắn gọn.**
**Bài làm:**
1. **Mô hình Thác nước (Waterfall Model):** Là mô hình tuần tự tuyến tính. Các pha (Yêu cầu, Thiết kế, Code, Test, Triển khai) nối tiếp nhau như dòng thác. Một pha phải hoàn thành xong 100% và chốt tài liệu thì mới chuyển sang pha tiếp theo. Ưu điểm là dễ quản lý, nhược điểm là không linh hoạt với sự thay đổi.
2. **Mô hình Xoắn ốc (Spiral Model):** Là mô hình phát triển theo vòng lặp, kết hợp giữa yếu tố lặp lại và kiểm soát theo từng pha. Điểm nổi bật nhất của Xoắn ốc là có khâu **Phân tích và Quản trị rủi ro** rất mạnh mẽ ở mỗi vòng lặp, phù hợp cho các dự án lớn, đắt tiền và độ rủi ro cao.
3. **Mô hình Agile / Scrum:** Là mô hình phát triển linh hoạt, chia dự án thành các chu kỳ ngắn (Iterative) gọi là Sprint (2-4 tuần). Cuối mỗi Sprint sẽ giao cho khách hàng một phần mềm chạy được. Agile đề cao sự tương tác với khách hàng, phản hồi nhanh với thay đổi thay vì cứng nhắc bám theo tài liệu ban đầu.

**Câu 5: Trình bày 4 nguyên tắc trong thiết kế giao diện người dùng (UI)?**
**Bài làm:**
Khi thiết kế giao diện người dùng, lập trình viên cần tuân thủ 4 nguyên tắc thiết yếu sau để đảm bảo trải nghiệm tốt nhất (UX):
1. **Tính quen thuộc và Thân thiện (User Familiarity):** Giao diện nên sử dụng các thuật ngữ, biểu tượng và cách bố trí quen thuộc với thói quen của người dùng (ví dụ: biểu tượng đĩa mềm để Lưu, thùng rác để Xóa) thay vì bắt họ học các ký hiệu công nghệ khó hiểu.
2. **Tính nhất quán (Consistency):** Thiết kế phải đồng bộ trên toàn bộ phần mềm. Màu sắc của các nút cảnh báo (đỏ), nút đồng ý (xanh), font chữ, và vị trí các menu phải được giữ nguyên ở tất cả các màn hình để tránh gây bối rối.
3. **Có khả năng phục hồi lỗi (Recoverability / Forgiveness):** Người dùng luôn có xu hướng thao tác sai. Hệ thống phải cho phép họ hoàn tác (Undo) hoặc yêu cầu hộp thoại xác nhận (Ví dụ: "Bạn có chắc chắn muốn xóa không?") trước những thao tác phá hủy dữ liệu.
4. **Cung cấp phản hồi (Feedback):** Mọi thao tác của người dùng phải được hệ thống phản hồi lại ngay lập tức (bằng hình ảnh hoặc âm thanh). Ví dụ: hiển thị vòng xoay loading khi đang tải dữ liệu, hoặc hiện thông báo "Lưu thành công" để người dùng biết lệnh của họ đã được xử lý.

**Câu 6: Trình bày nguyên lý Coupling (Độ phụ thuộc) và nguyên lý Cohesion (Độ gắn kết) trong thiết kế module?**
**Bài làm:**
Trong thiết kế kiến trúc và viết mã nguồn phần mềm, đây là 2 nguyên lý đo lường chất lượng cốt lõi:
- **Nguyên lý Cohesion (Độ gắn kết):** Đo lường mức độ liên quan và tập trung thực hiện nhiệm vụ của các hàm/dữ liệu *bên trong cùng một module* (hoặc một Class). Một thiết kế tốt đòi hỏi **Cohesion cao (High Cohesion)**, nghĩa là module đó chỉ tập trung làm duy nhất một nhiệm vụ chuyên biệt và làm thật tốt nhiệm vụ đó (Single Responsibility), không ôm đồm việc khác.
- **Nguyên lý Coupling (Độ phụ thuộc):** Đo lường mức độ phụ thuộc, ràng buộc chéo lẫn nhau *giữa các module khác nhau* trong hệ thống. Một thiết kế tốt đòi hỏi **Coupling thấp (Low Coupling)**, nghĩa là các module hoạt động độc lập nhất có thể. Nếu Coupling thấp, khi ta sửa lỗi hoặc thay đổi code ở Module A thì Module B không bị sập theo.

**Câu 7: Kể tên các phương pháp sử dụng để thu thập và đặc tả yêu cầu phần mềm?**
**Bài làm:**
Để lấy được yêu cầu chính xác từ khách hàng, Kỹ sư phân tích nghiệp vụ (BA) thường dùng các phương pháp sau:
- **Phỏng vấn (Interviewing):** Gặp gỡ và trao đổi trực tiếp với khách hàng hoặc người dùng cuối để hỏi sâu về mong muốn, khó khăn của họ.
- **Khảo sát bằng bảng hỏi (Questionnaires):** Thiết kế các câu hỏi trắc nghiệm phát cho số lượng lớn người dùng để thống kê nhu cầu chung một cách nhanh chóng.
- **Quan sát thực tế (Observation):** Kỹ sư trực tiếp đến môi trường làm việc của khách hàng để quan sát cách họ làm việc thủ công, từ đó phát hiện ra những yêu cầu ẩn mà khách hàng quên không kể.
- **Nghiên cứu tài liệu (Document Analysis):** Đọc các biểu mẫu, hóa đơn, quy trình giấy tờ hiện tại của công ty khách hàng để ánh xạ vào phần mềm.

**Câu 8: Nêu 2 phương pháp lập trình mà em đã sử dụng trong lập trình phần mềm?**
**Bài làm:**
Trong quá trình học tập và làm việc, em thường áp dụng 2 phương pháp lập trình sau:
1. **Lập trình hướng cấu trúc / thủ tục (Procedural Programming):** Viết mã nguồn bằng cách chia nhỏ bài toán thành các hàm (function/procedure) chạy theo trình tự logic từ trên xuống dưới (sử dụng ngôn ngữ C). Thích hợp cho các bài toán thuật toán nhỏ.
2. **Lập trình hướng đối tượng (Object-Oriented Programming - OOP):** Biến mọi thứ thành các Đối tượng (Object) có thuộc tính và hành vi, tương tác với nhau. Phương pháp này vận dụng 4 tính chất: Đóng gói, Kế thừa, Đa hình và Trừu tượng (sử dụng Java, C# hoặc C++). Nó giúp tổ chức mã nguồn rõ ràng, dễ bảo trì và tái sử dụng cho các dự án lớn.

**Câu 9: Phần mềm được định nghĩa như thế nào dưới góc nhìn của chuyên viên tin học?**
**Bài làm:**
Dưới góc nhìn của chuyên viên tin học, phần mềm không đơn thuần chỉ là những dòng code. Phần mềm là một thực thể hoàn chỉnh bao gồm 3 thành tố:
1. Tập hợp các câu lệnh, chương trình máy tính (Computer Programs) có khả năng thực thi và sinh ra chức năng mong muốn.
2. Cấu trúc dữ liệu (Data Structures) cho phép chương trình xử lý và thao tác thông tin một cách tối ưu.
3. Các tài liệu liên quan (Documentation) như đặc tả yêu cầu, thiết kế kiến trúc, và sổ tay hướng dẫn sử dụng để đảm bảo hệ thống có thể được bảo trì và vận hành lâu dài.

**Câu 10: Nêu 3 công nghệ / nền tảng giao diện mà em biết?**
**Bài làm:**
Trong phát triển ứng dụng, em biết 3 công nghệ giao diện phổ biến sau:
1. **Giao diện Web (Web UI):** Xây dựng bằng HTML, CSS, JavaScript kết hợp với các Framework như ReactJS, VueJS. Ứng dụng chạy trực tiếp trên trình duyệt.
2. **Giao diện Desktop (Window Form / WPF):** Xây dựng bằng C# (.NET) hoặc Java (Swing/JavaFX) để tạo ra các phần mềm cài đặt và chạy trực tiếp trên máy tính Windows/macOS.
3. **Giao diện Di động (Mobile UI):** Xây dựng bằng Kotlin/Swift cho ứng dụng native hoặc Flutter/React Native cho ứng dụng đa nền tảng, chạy trên màn hình cảm ứng của điện thoại smartphone.