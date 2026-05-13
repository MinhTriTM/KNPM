# CHƯƠNG 3: PHÂN TÍCH & ĐẶC TẢ YÊU CẦU PHẦN MỀM

### 1. Kỹ nghệ yêu cầu (Requirement Engineering - RE)
* **Định nghĩa:** Là quá trình hệ thống hóa việc thu thập, phân tích, lập tài liệu và thẩm định các chức năng/dịch vụ mà hệ thống phần mềm phải cung cấp, cũng như các ràng buộc mà hệ thống phải tuân thủ.
* **4 bước cơ bản (Phải theo đúng thứ tự):**
  1. **Khám phá/Thu thập (Elicitation / Discovery):** Tương tác với khách hàng, các bên liên quan (stakeholders) để khám phá nhu cầu và mong muốn thực sự của họ.
  2. **Phân tích & Thương lượng (Analysis & Negotiation):** Phân loại, đánh giá tính khả thi và giải quyết các xung đột yêu cầu giữa các bên liên quan để đi đến thống nhất.
  3. **Đặc tả (Specification):** Viết và mô hình hóa các yêu cầu đã thống nhất thành một tài liệu chính thức, chi tiết, rõ ràng (SRS).
  4. **Thẩm định (Validation):** Kiểm tra lại với khách hàng để chắc chắn rằng tài liệu đặc tả đã phản ánh chính xác 100% những gì họ cần.

---

### 2. Phân loại yêu cầu
* **Yêu cầu chức năng (Functional Requirements):**
  * **Định nghĩa:** Phát biểu mô tả các chức năng, dịch vụ mà hệ thống cung cấp. Hệ thống phản ứng thế nào với các đầu vào cụ thể (Hệ thống PHẢI LÀM GÌ).
  * **Ví dụ:** "Hệ thống cho phép người dùng đăng nhập bằng Email và Mật khẩu"; "Hệ thống tính tổng tiền giỏ hàng và áp dụng mã giảm giá".
* **Yêu cầu phi chức năng (Non-functional Requirements):**
  * **Định nghĩa:** Là các ràng buộc về dịch vụ, phương thức hoạt động của hệ thống. Nó quyết định CHẤT LƯỢNG của hệ thống (Hệ thống PHẢI HOẠT ĐỘNG NHƯ THẾ NÀO).
  * **Ví dụ (theo các nhóm chính):**
    * *Hiệu năng (Performance):* "Hệ thống phản hồi thao tác tìm kiếm trong vòng tối đa 2 giây".
    * *Bảo mật (Security):* "Mật khẩu của người dùng phải được mã hóa theo chuẩn SHA-256".
    * *Khả dụng (Usability):* "Người dùng mới có thể thao tác đặt hàng mà không cần tài liệu hướng dẫn".
    * *Khả năng mở rộng (Scalability):* "Hệ thống chịu tải được 10.000 người dùng truy cập đồng thời".
* **Yêu cầu miền ứng dụng (Domain Requirements):**
  * **Định nghĩa:** Yêu cầu xuất phát từ tính đặc thù của lĩnh vực nghiệp vụ áp dụng phần mềm (luật pháp, công thức tính toán vật lý, quy định kế toán...). Nó có thể là chức năng hoặc phi chức năng.
  * **Ví dụ:** "Phần mềm kế toán phải tính thuế VAT là 8% hoặc 10% tùy thuộc vào mặt hàng theo đúng Quy định hiện hành của Bộ Tài chính".

---

### 3. Các kỹ thuật thu thập yêu cầu phổ biến
* **Phỏng vấn (Interviews):** Trao đổi trực tiếp (câu hỏi đóng hoặc mở) với các bên liên quan.
  * *Ví dụ:* Phỏng vấn Giám đốc nhân sự để hiểu quy trình chấm công hiện tại.
* **Khảo sát (Surveys/Questionnaires):** Dùng biểu mẫu để thu thập thông tin từ một tập người dùng lớn. Nhược điểm là thiếu độ sâu.
  * *Ví dụ:* Gửi form khảo sát cho 500 sinh viên về tính năng họ mong muốn trên ứng dụng E-learning của trường.
* **Quan sát / Dân tộc học (Observation / Ethnography):** Phân tích viên trực tiếp hòa mình vào môi trường làm việc của người dùng để xem họ làm việc như thế nào.
  * *Ví dụ:* Đứng xem và ghi chép lại các bước nhân viên thu ngân thao tác tính tiền để làm phần mềm quản lý siêu thị.
* **Use-case:** Sử dụng sơ đồ hình vẽ kết hợp kịch bản text để mô tả tương tác giữa người dùng (Actor) và hệ thống nhằm đạt được một mục tiêu.
  * *Ví dụ:* Use-case "Rút tiền ATM" mô tả bước: Bỏ thẻ -> Nhập PIN -> Chọn số tiền -> Nhận tiền -> Nhận thẻ.
* **Kịch bản (Scenario / User Story):** Lời kể mô tả chi tiết một chuỗi sự kiện cụ thể từ góc nhìn của người dùng.
  * *Ví dụ:* "Là một khách hàng, tôi muốn lọc sản phẩm theo mức giá từ thấp đến cao để tìm được đồ phù hợp túi tiền".

---

### 4. Tài liệu SRS (Software Requirement Specification)
* **Cấu trúc & Tầm quan trọng:**
  * Là tài liệu chính thức và quan trọng nhất của giai đoạn phân tích. Nó đóng vai trò là "bản hợp đồng" giữa Khách hàng và Đội ngũ phát triển (Dev, Test).
  * *Cấu trúc cơ bản (Theo chuẩn IEEE 830):* 1. Giới thiệu tổng quan -> 2. Mô tả chung về hệ thống -> 3. Yêu cầu chi tiết (Giao diện, Chức năng, Phi chức năng).
* **5 Tiêu chí của một tài liệu SRS tốt:**
  1. **Đúng (Correct):** Phản ánh chính xác mong muốn thực sự của khách hàng.
  2. **Đầy đủ (Complete):** Định nghĩa tất cả các chức năng, các trường hợp ngoại lệ, không bỏ sót.
  3. **Nhất quán (Consistent):** Các yêu cầu không được mâu thuẫn hay đá nhau (VD: Yêu cầu 1 cấm đổi mật khẩu, Yêu cầu 2 lại có nút đổi mật khẩu).
  4. **Test được (Testable):** Yêu cầu phải có tính định lượng để có thể viết Test Case kiểm tra (VD: Thay vì viết "Hệ thống phải nhanh", phải viết "Hệ thống tải trang dưới 3s").
  5. **Không mơ hồ (Unambiguous):** Mỗi yêu cầu chỉ có đúng MỘT cách hiểu duy nhất.

---

### 5. So sánh: Thẩm định (Validation) vs Kiểm chứng (Verification)
* **Thẩm định yêu cầu (Validation):**
  * **Câu hỏi cốt lõi:** *"Are we building the RIGHT product?"* (Chúng ta có đang xây dựng đúng sản phẩm khách hàng cần không?)
  * **Mục đích:** Kiểm tra xem bộ yêu cầu có giải quyết đúng vấn đề thực tế, nghiệp vụ của người dùng hay không. Phải mang lại giá trị thực tế.
  * **Ví dụ:** Đưa bản demo/bản đặc tả cho khách hàng xem và họ chốt: "Đúng, tính năng thanh toán này đúng là thứ chúng tôi cần".
* **Kiểm chứng yêu cầu (Verification):**
  * **Câu hỏi cốt lõi:** *"Are we building the product RIGHT?"* (Chúng ta có đang làm đúng quy trình, đúng tài liệu không?)
  * **Mục đích:** Kiểm tra tài liệu SRS có được viết đúng ngữ pháp, chuẩn định dạng cấu trúc, không bị lỗi logic, không mâu thuẫn nội bộ hay không.
  * **Ví dụ:** Đội QA review tài liệu SRS để đảm bảo các yêu cầu được đánh mã ID không bị trùng lặp, đúng template quy định của công ty.

---

### 6. Quản lý yêu cầu & Ma trận truy vết (Traceability Matrix)
* **Quản lý yêu cầu (Requirement Management):** Là quá trình quản lý sự thay đổi của các yêu cầu trong suốt vòng đời dự án phần mềm. Nhằm đảm bảo kiểm soát được sự ảnh hưởng về chi phí và thời gian khi có yêu cầu mới/thay đổi.
* **Ma trận truy vết (Requirement Traceability Matrix - RTM):**
  * **Định nghĩa:** Là một bảng liên kết (mapping) hai chiều, theo dõi một yêu cầu từ lúc sinh ra (nguồn gốc) cho tới các thành phần thiết kế, file mã nguồn (code) và các kịch bản kiểm thử (test case) tương ứng.
  * **Tầm quan trọng:**
    1. Đảm bảo không có yêu cầu nào của khách hàng bị bỏ sót (100% requirement được dev và test).
    2. Khi có sự thay đổi yêu cầu, RTM giúp đánh giá ngay lập tức xem phải sửa ở file code nào, update lại test case nào.
  * **Ví dụ:** Trong ma trận, `Yêu cầu Đăng nhập (REQ-01)` -> liên kết tới module code `Login.java` -> liên kết tới kịch bản test `TC-01: Đăng nhập sai pass`.
