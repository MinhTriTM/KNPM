# NGÂN HÀNG CÂU HỎI LÝ THUYẾT SIÊU CHI TIẾT - PHẦN 2 (Câu 81 - 150)
*(Bao gồm Chương 6: Lập trình OOP, Clean Code, SOLID và Chương 7: Kiểm thử phần mềm chuyên sâu)*

---

## CHƯƠNG 6: LẬP TRÌNH & XÂY DỰNG MÃ NGUỒN

**81. Trình bày chi tiết về 4 tính chất cơ bản của Lập trình hướng đối tượng (OOP)?**
- OOP được xây dựng dựa trên 4 trụ cột không thể thiếu:
  1. **Tính Đóng gói (Encapsulation):** Gói gọn dữ liệu (thuộc tính) và các hàm thao tác trên dữ liệu đó vào trong một khoang chứa (Class). Bảo vệ dữ liệu bằng các access modifiers (Private) và chỉ cho phép giao tiếp qua các kênh Public (Getter/Setter).
  2. **Tính Kế thừa (Inheritance):** Cho phép một Class con (Sub-class) thừa hưởng lại toàn bộ thuộc tính và phương thức của một Class cha (Super-class) đã có sẵn. Giúp tái sử dụng code tối đa (Ví dụ: Class Chó kế thừa Class ĐộngVật).
  3. **Tính Đa hình (Polymorphism):** Cùng một tên hàm, nhưng khi gọi trên các đối tượng khác nhau (hoặc truyền tham số khác nhau) sẽ thực thi các hành động khác nhau. Nó được thực hiện qua Ghi đè hàm (Overriding) và Ghi chồng hàm (Overloading).
  4. **Tính Trừu tượng (Abstraction):** Bỏ qua các chi tiết triển khai phức tạp bên trong, chỉ bộc lộ ra ngoài những đặc điểm thiết yếu, giao diện cốt lõi mà người sử dụng cần biết (thông qua Abstract Class hoặc Interface).

**82. Mã nguồn sạch (Clean Code) là thuật ngữ rất nổi tiếng trong phát triển phần mềm. Nó ám chỉ điều gì?**
- Đoạn code được máy tính biên dịch và chạy đúng chưa chắc đã là code tốt. Theo triết lý của Robert C. Martin (Uncle Bob), **Clean Code** là đoạn code được viết ra để "Con người có thể đọc và hiểu được một cách dễ dàng", giống như đọc một bài văn xuôi rõ ràng.
- Đặc trưng của Clean Code: Tên biến/hàm mang ý nghĩa rõ ràng (không dùng a, b, x, y), các hàm rất ngắn (thường < 20 dòng) và thực hiện duy nhất 1 nhiệm vụ, cấu trúc thụt lề chuẩn, không có các khối mã bị lặp lại dư thừa (DRY) và hạn chế lạm dụng comment giải thích (vì code tốt tự nó giải thích cho nó).

**83. Tái cấu trúc mã nguồn (Refactoring) nghĩa là gì và tại sao lại cần thiết?**
- **Định nghĩa:** Là quá trình "dọn dẹp" và tổ chức lại cấu trúc mã nguồn bên trong để code sạch hơn, tối ưu hơn, dễ bảo trì hơn, **NHƯNG tuyệt đối không làm thay đổi hành vi bên ngoài** hay tính năng của phần mềm đối với người dùng cuối.
- **Sự cần thiết:** Dự án phần mềm càng chạy lâu, code càng phình to, lộn xộn, bị "bốc mùi" (Code Smells). Nếu không thường xuyên Refactoring (ví dụ: tách 1 class khổng lồ 2000 dòng thành 3 class nhỏ), mã nguồn sẽ chết yểu vì kỹ sư không ai dám chạm vào để sửa lỗi.

**84. Coding Convention (Chuẩn lập trình) mang lại lợi ích thực tế nào cho đội phát triển (Team)?**
- Khi dự án có 10 developer, mỗi người có thói quen đặt tên biến, thụt lề, để dấu ngoặc nhọn `{` ở vị trí khác nhau sẽ tạo ra mớ hỗn độn, đọc chéo code cực kỳ ức chế.
- **Lợi ích:** Áp dụng Coding Convention (Chuẩn chung của công ty hoặc cộng đồng - VD: PEP8 cho Python, PSR cho Python, CamelCase cho Java) giúp code của toàn team trông như do 1 người viết duy nhất. Điều này giúp đẩy nhanh tốc độ Code Review, phát hiện bug lẩn khuất dễ hơn, hạn chế các xung đột (Merge Conflict) vô lý khi gộp code trên Git.

**85. Nguyên lý SOLID trong thiết kế và lập trình OOP là viết tắt của 5 nguyên tắc vàng nào?**
- Đây là 5 nguyên tắc giúp thiết kế hệ thống OOP cực kỳ mạnh mẽ, dễ bảo trì, dễ thay đổi:
  - **[S] Single Responsibility Principle (Đơn trách nhiệm):** Một Class chỉ nên có duy nhất 1 lý do để thay đổi (Chỉ làm 1 việc duy nhất).
  - **[O] Open/Closed Principle (Đóng/Mở):** Class nên Đóng đối với việc sửa đổi trực tiếp (sửa code cũ dễ gây bug), nhưng Mở đối với việc mở rộng (thêm tính năng mới bằng cách kế thừa).
  - **[L] Liskov Substitution Principle (Thay thế Liskov):** Đối tượng thuộc Class con có thể thay thế hoàn hảo cho Class cha trong mọi tình huống mà không làm gãy logic hệ thống.
  - **[I] Interface Segregation Principle (Phân tách Interface):** Đừng ép các class phải implements một Interface khổng lồ chứa những hàm mà nó không dùng. Hãy băm nhỏ Interface ra.
  - **[D] Dependency Inversion Principle (Đảo ngược phụ thuộc):** Các module cấp cao (Logic nghiệp vụ) không được phụ thuộc vào các module cấp thấp (Database/UI). Cả 2 đều phải phụ thuộc vào Abstraction (Interface).

**86. Git và Quản lý phiên bản (Version Control System - VCS) sinh ra để giải quyết vấn đề gì?**
- **Vấn đề:** Khi nhiều người cùng sửa chung 1 file code, nếu copy qua USB thì sẽ ghi đè xóa sạch code của nhau. Khi code bị lỗi nghiêm trọng, không thể "Undo" về phiên bản ổn định của tuần trước.
- **Giải pháp:** Git lưu trữ mọi lịch sử thay đổi của từng dòng code, ai sửa, lúc nào. Nó cho phép các lập trình viên làm việc song song trên các "nhánh" (Branches) khác nhau. Sau khi hoàn thiện, tính năng tự động hòa trộn (Merge) sẽ gom code lại một cách an toàn mà không làm mất dữ liệu. GitHub/GitLab là các máy chủ lưu trữ nền tảng Git.

**87. Tự động hóa tích hợp và triển khai liên tục (CI/CD) trong lập trình hiện đại nhằm mục đích gì?**
- **CI (Continuous Integration):** Khi dev đẩy code mới lên Git, hệ thống CI tự động build app và chạy hàng ngàn bài Unit Test tự động. Nếu có dòng code nào phá hỏng hệ thống, nó sẽ báo đỏ (Fail) ngay lập tức từ chối nhận code.
- **CD (Continuous Deployment):** Nếu CI xanh (Pass), hệ thống tự động đóng gói ứng dụng và đẩy (Deploy) thẳng lên Server cho khách hàng sử dụng mà không cần con người copy/dán file thủ công ban đêm.
- **Mục đích:** Phóng thích tính năng mới siêu nhanh, an toàn tuyệt đối, loại bỏ rủi ro do thao tác thủ công (Human Error).

---

## CHƯƠNG 7: KIỂM THỬ VÀ BẢO TRÌ PHẦN MỀM

**88. Mục đích tối thượng của Kiểm thử phần mềm (Software Testing) là gì?**
- Kiểm thử KHÔNG THỂ chứng minh phần mềm không có lỗi (vì không thể test cạn kiệt), nhưng nó nhằm các mục đích:
  1. Phát hiện càng nhiều lỗi (Defects/Bugs) càng tốt trước khi sản phẩm đến tay khách hàng.
  2. Xác minh rằng hệ thống đáp ứng ĐÚNG và ĐỦ các yêu cầu đã ghi trong tài liệu đặc tả (SRS).
  3. Cung cấp thông tin khách quan, đo lường được về chất lượng phần mềm để Quản lý dự án quyết định có nên phát hành (Release) hay không.

**89. Kiểm thử hộp đen (Black-box testing) có phương pháp luận như thế nào?**
- **Góc nhìn:** Tester đóng vai trò như một người dùng cuối. Phần mềm là một "Chiếc hộp đen" mù mịt, tester không cần biết ngôn ngữ lập trình là gì, thuật toán bên trong code viết ra sao.
- **Cách test:** Tester chỉ cung cấp Đầu vào (Input) -> Chờ phần mềm chạy -> Kiểm tra Đầu ra (Output) có giống với Kết quả mong đợi trong tài liệu thiết kế hay không. Các kỹ thuật phổ biến: Phân vùng tương đương, Phân tích giá trị biên, Bảng quyết định.

**90. Kiểm thử hộp trắng (White-box testing) thì dành cho đối tượng nào và test cái gì?**
- **Góc nhìn:** Phần mềm là "Chiếc hộp trong suốt". Người test (thường là Developer hoặc Automation Tester chuyên sâu) có quyền truy cập vào mã nguồn (Source Code).
- **Cách test:** Kiểm tra cấu trúc logic nội bộ, rẽ nhánh thuật toán, vòng lặp for/while. Dùng để xem tất cả các dòng code đã được chạy (Coverage) qua chưa, có đoạn code "chết" nào không. Đây là cốt lõi của Unit Testing.

**91. Hãy kể tên và giải thích 4 cấp độ kiểm thử phần mềm (Testing Levels) từ thấp đến cao?**
1. **Kiểm thử đơn vị (Unit Testing):** Test mức nhỏ nhất (từng hàm, từng class). Thường do Lập trình viên tự viết tự chạy (Hộp trắng). Giúp tìm lỗi rễ sớm nhất.
2. **Kiểm thử tích hợp (Integration Testing):** Ghép các Unit lại với nhau (VD: Ghép Module Thanh toán với Database) để xem chúng tương tác, truyền dữ liệu qua lại có bị gãy hay mất mát gì không.
3. **Kiểm thử hệ thống (System Testing):** Test toàn bộ hệ thống phần mềm hoàn chỉnh chạy trong môi trường giống thực tế. (Hộp đen).
4. **Kiểm thử chấp nhận (Acceptance Testing - UAT):** Do chính Khách hàng (End-Users) thực hiện. Họ kiểm tra xem hệ thống có giải quyết được quy trình kinh doanh nghiệp vụ của họ không. Nếu họ "Pass", công ty phần mềm mới được nhận tiền thanh toán.

**92. Phân biệt Error, Defect (Bug) và Failure trong kiểm thử phần mềm?**
- Mọi thứ bắt nguồn từ con người.
  - **Error (Lỗi lầm):** Là sự nhầm lẫn trong suy nghĩ hoặc hành động của Developer/BA (Ví dụ: Dev hiểu sai công thức tính thuế).
  - **Defect / Bug (Khuyết tật):** Là kết quả của Error, nó biến thành một đoạn code sai bị chôn vùi bên trong mã nguồn hệ thống.
  - **Failure (Sự thất bại):** Khi hệ thống đang chạy (Runtime), đoạn code chứa Bug vô tình được người dùng kích hoạt, dẫn đến phần mềm bị sập (Crash) hoặc hiện ra số liệu sai. Lúc này Bug đã trở thành Failure hiển hiện ra ngoài.

**93. Kỹ thuật "Phân tích giá trị biên" (Boundary Value Analysis) hoạt động dựa trên triết lý gì?**
- Qua thực tiễn, người ta phát hiện rằng các Lập trình viên hay code sai nhất ở các phép toán so sánh điều kiện (`>`, `<`, `>=`, `<=`).
- Do đó, số lượng Bug tập trung dày đặc nhất ở ranh giới (Biên) giữa vùng giá trị hợp lệ và vùng giá trị không hợp lệ. Thay vì test các số ở giữa an toàn, Tester sẽ tập trung test các giá trị sát sát mép biên (VD: Giới hạn độ tuổi 18 - 60. Các giá trị biên cần test cực gắt là: 17, 18, 60, 61). Kỹ thuật này giúp phát hiện lỗi hiệu quả nhất với số lượng Test case ít nhất.

**94. Kiểm thử khói (Smoke Testing) có vai trò gì trong quá trình nhận bản Build mới?**
- Thuật ngữ "Khói" bắt nguồn từ kỹ thuật phần cứng (Cắm điện vào board mạch, nếu không bốc khói thì mới tiếp tục test chi tiết).
- Tương tự trong phần mềm, trước khi Tester bỏ ra hàng ngày trời để test chi tiết 500 Test Cases, họ sẽ chạy vài Test case cơ bản nhất (Mất 15 phút) để xem: Ứng dụng có cài đặt được không? Nút Login có chạy không? Màn hình chính có load lên không? Nếu những chức năng sống còn này mà chết (Fail), bản Build này bị trả về (Reject) ngay lập tức cho Dev, từ chối test tiếp để khỏi mất thời gian.

**95. Kiểm thử hồi quy (Regression Testing) giải quyết rủi ro tâm lý cực kỳ phổ biến nào của lập trình viên?**
- Lập trình viên vừa sửa xong Bug A, hoặc thêm tính năng B mới toanh. Do tính chất phụ thuộc lỏng lẻo của code (Coupling), việc sửa ở chỗ này rất dễ làm vô tình gãy (vỡ code) ở một chức năng C cũ kĩ đã chạy ngon lành từ tháng trước.
- **Kiểm thử hồi quy:** Là hành động chạy lại toàn bộ (hoặc một phần) các Test Case cũ đang "Pass" để đảm bảo rằng phần code mới thêm vào không "đầu độc" phần mềm hiện tại. Quá trình này cực kỳ nhàm chán nếu làm bằng tay, nên Automation Test là cứu cánh tuyệt đối cho Regression Test.

**96. Tại sao người ta nói "Kiểm thử cạn kiệt 100% (Exhaustive Testing) là điều bất khả thi"?**
- Để test cạn kiệt, bạn phải quét qua TẤT CẢ các tổ hợp đầu vào và các nhánh logic luồng thuật toán của phần mềm. Đối với một trang web đơn giản có 10 ô nhập liệu, số tổ hợp biến ngẫu nhiên có thể lên tới hàng tỷ trường hợp. Mất hàng chục năm để test xong 1 nút bấm.
- Do đó, Tester giỏi không phải là test tất cả, mà là người biết dùng các kỹ thuật (Phân vùng, Giá trị biên, Phân tích rủi ro) để chọn ra một lượng ít Test Case nhất (Representative sample) có khả năng phát hiện được nhiều Bug nhất.

**97. Một Test case (Ca kiểm thử) tiêu chuẩn, dùng để nghiệm thu chuyên nghiệp, phải chứa các trường thông tin sống còn nào?**
1. **ID Test Case:** Mã định danh duy nhất (VD: TC_LOGIN_001) để dễ truy vết.
2. **Tiêu đề / Mục đích Test:** Câu ngắn gọn (VD: Kiểm tra đăng nhập với password sai).
3. **Tiền điều kiện (Pre-conditions):** Trạng thái bắt buộc trước khi test (VD: Đã có account tồn tại, Đang ở màn hình Login).
4. **Các bước thực hiện (Test Steps):** Cụ thể từng bước click chuột, gõ phím.
5. **Dữ liệu kiểm thử (Test Data):** Account: "user1", Pass: "sai123".
6. **Kết quả mong đợi (Expected Result):** Hệ thống hiện thông báo đỏ "Mật khẩu không đúng" và không cho chuyển trang.
7. **Kết quả thực tế (Actual Result) & Status:** Khi chạy thực tế nó ra sao, đánh dấu là PASS (Đạt) hay FAIL (Thất bại).

**98. Bug Report (Báo cáo lỗi) chất lượng cao dành cho Developer cần có gì?**
- Đừng bao giờ chỉ báo "App bị lỗi rồi em ơi". Một Bug Report chuẩn phải giúp Developer hiểu và "tái hiện" (Reproduce) được lỗi trên máy của họ:
  1. *Tóm tắt lỗi rõ ràng.*
  2. *Môi trường bị lỗi:* Hệ điều hành gì, Trình duyệt gì, Test trên mạng Wifi hay 4G. Lỗi có hay xảy ra ngẫu nhiên (Intermittent) không.
  3. *Các bước tái hiện (Steps to Reproduce):* Cực kỳ quan trọng, ghi từng bước 1, 2, 3 dẫn đến crash.
  4. *Bằng chứng (Evidence):* Đính kèm ảnh chụp màn hình (Screenshot), video quay màn hình hoặc File Log của hệ thống.

**99. Bảo trì phần mềm (Software Maintenance) - Tại sao chi phí bảo trì thường chiếm đến 60%-80% tổng chi phí vòng đời dự án?**
- Một phần mềm có thể mất 6 tháng để viết, nhưng có thể phải vận hành trong 10 năm. Việc bảo trì không chỉ đơn thuần là "Sửa bug" mà nó còn khổng lồ hơn:
  - **Bảo trì thích nghi (Adaptive):** Khi HĐH Windows nâng cấp lên bản mới, hoặc đổi Server CSDL, phần mềm phải viết lại code để chạy được trên nền tảng mới.
  - **Bảo trì hoàn thiện (Perfective):** Khách hàng kinh doanh phát triển, đòi thêm tính năng mới, báo cáo mới, cải tiến tốc độ UI nhanh hơn. Chiếm phần lớn thời gian bảo trì.
  - **Bảo trì sửa lỗi (Corrective):** Sửa các Bug ẩn sâu, chỉ lòi ra khi người dùng làm thao tác dị.
  - **Bảo trì phòng ngừa (Preventive):** Tái cấu trúc code (Refactoring), dọn rác bộ nhớ để tránh phần mềm sập trong tương lai. Lập trình viên mới vào dự án đọc code cũ cũng làm chi phí đội lên.

**100. Vai trò thực sự của Kỹ sư Kiểm thử (QA/QC) có phải chỉ là tìm ráng tìm lỗi để hạ bệ Lập trình viên (Dev)?**
- Hoàn toàn KHÔNG. Định kiến QA và Dev là "kẻ thù" là tư duy cổ hủ. Trong Công nghệ phần mềm hiện đại (đặc biệt là Agile/Scrum), QA và Dev là một đội (One Team). 
- QA giúp Dev đảm bảo an toàn tâm lý trước khi đưa code ra thị trường. QA thậm chí phân tích yêu cầu ngay từ đầu dự án cùng BA, đặt ra các câu hỏi để lấp lỗ hổng tư duy của Dev trước khi Dev gõ dòng code đầu tiên (Shift-left testing). Đảm bảo chất lượng (Quality Assurance) là trách nhiệm của toàn bộ team chứ không phải của riêng Tester.

---
**HẾT PHẦN 1 (Câu 1 - 100 ĐÁP ÁN CHI TIẾT DÀNH CHO ÔN THI ĐIỂM GIỎI)**