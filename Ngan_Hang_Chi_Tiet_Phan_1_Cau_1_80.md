# NGÂN HÀNG CÂU HỎI LÝ THUYẾT SIÊU CHI TIẾT - PHẦN 2 (Câu 51 - 100)
*(Bao gồm nửa sau Chương 3, Chương 4 và Chương 5)*

---

## CHƯƠNG 4: MÔ HÌNH HÓA PHẦN MỀM (Phần tiếp theo)

**51. Mô hình hóa phần mềm (Software Modeling) mang lại những lợi ích cốt lõi nào cho dự án?**
- Mô hình hóa giống như việc vẽ bản vẽ thiết kế (blueprint) trước khi xây nhà. Lợi ích bao gồm:
  1. **Trực quan hóa (Visualization):** Giúp nhìn thấy hệ thống một cách trực quan, hình dung được hệ thống sẽ hoạt động ra sao trước khi viết một dòng code nào.
  2. **Đặc tả kiến trúc (Specification):** Chỉ định rõ cấu trúc dữ liệu và hành vi của hệ thống.
  3. **Tài liệu hóa (Documentation):** Lưu lại các quyết định thiết kế cho thế hệ Lập trình viên sau này bảo trì hệ thống.
  4. **Giao tiếp (Communication):** Là ngôn ngữ chung để Khách hàng, BA, Dev và Tester thảo luận mà không bị rào cản về thuật ngữ ngôn ngữ lập trình.

**52. UML (Unified Modeling Language) là gì và có phải là một ngôn ngữ lập trình không?**
- **Định nghĩa:** UML là Ngôn ngữ Mô hình hóa Thống nhất. Nó là một ngôn ngữ chuẩn mực bao gồm tập hợp các biểu đồ, ký hiệu đồ họa dùng để trực quan hóa, đặc tả, thiết kế và lập tài liệu cho các hệ thống phần mềm hướng đối tượng.
- **Lưu ý:** UML KHÔNG PHẢI là ngôn ngữ lập trình (như Java hay Python). Nó không tạo ra chương trình thực thi được, nó chỉ tạo ra "Bản thiết kế" hệ thống.

**53. Sơ đồ Use-case (Usecase Diagram) có mục đích chính là gì?**
- Mục đích chính là nắm bắt các **Yêu cầu chức năng** của hệ thống dưới lăng kính của người dùng (End-users).
- Nó không mô tả cách phần mềm hoạt động bên trong hay luồng dữ liệu (thuật toán), mà chỉ mô tả "Hệ thống cung cấp những giá trị/tính năng gì" và "Ai là người được phép sử dụng những tính năng đó". Sơ đồ này cực kỳ hữu ích để thảo luận trực tiếp với khách hàng.

**54. Trong Sơ đồ Use-case, "Actor" (Tác nhân) có những đặc điểm gì?**
- Actor đại diện cho một vai trò (Role) tương tác với hệ thống, chứ không phải một con người cụ thể. (VD: "Thủ thư", "Sinh viên" là vai trò).
- Actor luôn nằm bên ngoài ranh giới hệ thống (System Boundary).
- Actor có thể là người dùng, một phần cứng bên ngoài, hoặc một phần mềm/API bên ngoài (Ví dụ: Cổng thanh toán VNPay, Máy quẹt thẻ).

**55. Phân tích chi tiết sự khác biệt giữa quan hệ "Include" và "Extend" trong sơ đồ Use-case?**
- Cả hai đều dùng để kết nối giữa 2 Use-case (không kết nối Actor với Use-case).
- **<<include>> (Sự bao hàm - Bắt buộc):** Một Use-case cơ sở bắt buộc phải thực thi Use-case bị include thì chức năng mới hoàn tất. Nó giống như việc gọi một hàm tái sử dụng.
  - *Ví dụ:* UC "Rút tiền", UC "Chuyển khoản", UC "Xem số dư" đều có mũi tên đứt nét mũi tên trỏ vào UC "Xác thực mã PIN" với nhãn <<include>>. Vì nếu không nhập mã PIN thì không làm được 3 việc kia.
- **<<extend>> (Sự mở rộng - Tùy chọn):** Use-case mở rộng chỉ được thực thi khi một điều kiện nhất định xảy ra. Mũi tên đứt nét hướng TỪ Use-case phụ về Use-case cơ sở.
  - *Ví dụ:* UC cơ sở là "Lập hóa đơn thanh toán". Nếu khách hàng có thẻ VIP, họ sẽ kích hoạt thêm UC "Áp dụng mã giảm giá" (nhãn <<extend>>). Nếu không có thẻ, UC cơ sở vẫn hoàn tất bình thường.

**56. Biểu đồ lớp (Class Diagram) thể hiện khía cạnh nào của hệ thống?**
- Thể hiện khía cạnh **Tĩnh (Static)** của hệ thống hướng đối tượng.
- Nó mô tả các loại đối tượng (Class) sẽ được tạo ra trong code, bao gồm: Tên Class, Danh sách thuộc tính (Attributes - các biến), Danh sách phương thức (Operations - các hàm), và mối quan hệ giữa các Class (Class này kế thừa Class nào, kết nối với Class nào).

**57. Sơ đồ hoạt động (Activity Diagram) có vai trò gì và giống với công cụ nào trong tin học cơ bản?**
- **Vai trò:** Dùng để mô tả luồng công việc (Workflow) của một nghiệp vụ từ đầu đến cuối, hoặc mô tả luồng thực thi (thuật toán) chi tiết bên trong một Use-case/Phương thức phức tạp. Nó biểu diễn hành động, các luồng phân nhánh (If/Else) và các luồng chạy song song (Parallel/Concurrent).
- **Tương đồng:** Nó rất giống với Sơ đồ khối (Flowchart) truyền thống nhưng mạnh mẽ hơn nhiều nhờ hỗ trợ các luồng đồng thời (qua thanh Fork/Join) và phân chia trách nhiệm (qua Swimlane).

**58. Khái niệm "Swimlane" (Làn bơi) trong Activity Diagram dùng để làm gì?**
- Swimlane là kỹ thuật vẽ các đường thẳng dọc/ngang chia biểu đồ thành nhiều cột/hàng. Mỗi cột đại diện cho một Actor, một bộ phận phòng ban hoặc một hệ thống con cụ thể.
- **Tác dụng:** Giúp người xem nhìn ngay vào biểu đồ là biết hành động A do ai thực hiện (VD: Khách hàng "Đặt hàng" -> Hệ thống "Kiểm tra tồn kho" -> Kế toán "Xác nhận thanh toán").

**59. Sơ đồ trạng thái (State Machine Diagram) tập trung vào điều gì?**
- Nó tập trung mô tả **Vòng đời (Lifecycle)** của duy nhất một đối tượng cụ thể (Object) từ khi nó được tạo ra cho đến khi bị hủy bỏ.
- Nó biểu diễn các "Trạng thái" (States) mà đối tượng có thể trải qua, và các "Sự kiện/Hành động" (Transitions/Triggers) khiến đối tượng chuyển từ trạng thái này sang trạng thái khác. 
- *Ví dụ đối với đối tượng "Đơn hàng":* Khởi tạo -> Chờ thanh toán -> Đã thanh toán -> Đang giao hàng -> Hoàn thành.

**60. UML được chia làm 2 nhóm biểu đồ chính là gì? Hãy kể tên một vài biểu đồ trong mỗi nhóm.**
- **Nhóm biểu đồ Cấu trúc (Structural Diagrams):** Mô tả các thành phần tĩnh, không phụ thuộc thời gian. (VD: Class Diagram, Component Diagram, Deployment Diagram, Object Diagram).
- **Nhóm biểu đồ Hành vi (Behavioral Diagrams):** Mô tả cách hệ thống vận hành, thay đổi theo thời gian và tương tác với nhau. (VD: Use-case Diagram, Sequence Diagram, Activity Diagram, State Machine Diagram).

---

## CHƯƠNG 5: THIẾT KẾ PHẦN MỀM

**61. Thiết kế kiến trúc phần mềm (Software Architecture Design) là gì?**
- Là quy trình sáng tạo kỹ thuật đầu tiên sau khi đã chốt yêu cầu. 
- Đây là quá trình định nghĩa các khối hệ thống (Subsystems/Components) lớn, sự liên kết, giao tiếp và nguyên tắc hoạt động chung giữa chúng. Nó quyết định các nền tảng công nghệ sẽ dùng, tổ chức phân bổ dữ liệu, và cấu trúc vật lý của hệ thống. Nếu kiến trúc sai từ đầu, dự án gần như không thể cứu vãn.

**62. Kể tên và giải thích ngắn gọn 2 mẫu kiến trúc phần mềm (Architecture Patterns) kinh điển?**
1. **Kiến trúc Client-Server (Khách-Chủ):** Hệ thống được chia thành 2 phần tách biệt. Máy chủ (Server) tập trung, mạnh mẽ, quản lý dữ liệu và xử lý nghiệp vụ lõi. Các máy khách (Client - như app mobile, trình duyệt) xử lý giao diện người dùng và gửi request lên Server lấy dữ liệu.
2. **Kiến trúc phân lớp (Layered Architecture):** Mã nguồn được tổ chức thành các lớp ngang chồng lên nhau (thường là 3 lớp: Presentation/UI Layer -> Business Logic Layer -> Data Access Layer). Mỗi lớp chỉ giao tiếp với lớp ngay bên dưới nó. Rất dễ bảo trì vì thay đổi DB ở lớp Data không làm hỏng giao diện ở lớp UI.

**63. Mô hình MVC (Model-View-Controller) phân chia công việc như thế nào?**
- Đây là một Architectural Pattern siêu phổ biến cho thiết kế UI/Web:
  - **Model:** Đại diện cho Cấu trúc dữ liệu và Logic nghiệp vụ cốt lõi. Chịu trách nhiệm truy xuất/cập nhật DB.
  - **View:** Là giao diện (HTML/CSS, nút bấm). Nó lắng nghe và hiển thị dữ liệu từ Model, không chứa bất kỳ thuật toán tính toán nào.
  - **Controller:** Đóng vai trò làm "Bộ điều phối". Nhận Request từ người dùng trên View, gọi Model để xử lý, lấy kết quả từ Model và chỉ định một View phù hợp để render kết quả trả về cho user.

**64. Nguyên lý "Cohesion" (Độ gắn kết) trong thiết kế module là gì?**
- Cohesion đo lường mức độ tập trung và thống nhất của các dòng code, các hàm bên trong một Class hoặc một Module.
- Nếu một Module có **High Cohesion (Gắn kết cao)**, nghĩa là nó chỉ thực hiện ĐÚNG MỘT nhiệm vụ duy nhất và hoàn thành xuất sắc nhiệm vụ đó (Single Responsibility). Ví dụ: Class "Máy tính toán" chỉ chứa các hàm + - * /, không chứa hàm kết nối Database. Gắn kết cao là mục tiêu thiết kế tối thượng.

**65. Nguyên lý "Coupling" (Độ phụ thuộc) trong thiết kế module là gì?**
- Coupling đo lường mức độ phụ thuộc, ràng buộc chéo lẫn nhau giữa các Modules/Classes khác nhau trong hệ thống.
- Nếu hệ thống có **High Coupling (Phụ thuộc cao)**, các class gọi hàm và truy cập trực tiếp biến nội bộ của nhau quá nhiều. Hậu quả là khi bạn thay đổi code ở Class A, Class B và C sẽ bị lỗi theo (hiệu ứng domino). 
- Mục tiêu thiết kế là **Low Coupling (Phụ thuộc thấp)**: Các class độc lập nhất có thể, chỉ giao tiếp với nhau qua các Interface chuẩn mực.

**66. Thiết kế giao diện người dùng (UI) cần tuân thủ nguyên tắc "Nhất quán" (Consistency) nghĩa là gì?**
- **Nhất quán:** Là sự đồng bộ trong toàn bộ phần mềm.
  - *Trực quan:* Màu sắc (ví dụ nút Lưu luôn màu xanh, Xóa luôn màu đỏ), Font chữ, Kích thước icon phải giống nhau ở mọi màn hình.
  - *Hành vi:* Các phím tắt (Ctrl+C, Ctrl+V), luồng cảnh báo lỗi, vị trí đặt Menu phải ở những nơi người dùng dễ đoán nhất. Sự nhất quán giúp người dùng mới học cách sử dụng phần mềm cực kỳ nhanh.

**67. Nguyên tắc "Phản hồi" (Feedback) trong thiết kế UI quan trọng như thế nào?**
- Không có gì tệ hơn việc nhấn một nút và hệ thống... đứng im, khiến người dùng không biết hệ thống bị đơ, mất mạng hay đang xử lý ngầm.
- **Nguyên tắc Phản hồi:** Mọi thao tác của người dùng phải được đáp lại ngay lập tức bằng tín hiệu thị giác/thính giác. Ví dụ: Đổi màu nút bấm khi hover, hiển thị thanh tiến trình (Loading/Spinner) khi thao tác mất > 1 giây, hiện thông báo "Lưu thành công" (Toast message) ở góc màn hình.

**68. UX (User Experience - Trải nghiệm người dùng) khác UI (User Interface - Giao diện người dùng) như thế nào?**
- **UI:** Là bề nổi, những gì mắt thấy tay chạm (Nút bấm này màu gì? Font chữ này to bao nhiêu? Bố cục sắp xếp thế nào?). UI chú trọng vào tính thẩm mỹ.
- **UX:** Là bề chìm, cảm xúc và trải nghiệm tổng thể của user khi dùng phần mềm (Luồng mua hàng này có mượt không? Có khiến user bực mình vì phải click quá nhiều không? Trang web có tải nhanh không?). Một sản phẩm UI rất đẹp nhưng UX tồi (khó dùng) thì vẫn là sản phẩm thất bại.

**69. Giai đoạn thiết kế hệ thống đứng ở vị trí nào trong quy trình phần mềm chuẩn?**
- Thiết kế luôn là cầu nối. Nó nằm **sau** giai đoạn "Phân tích và Đặc tả Yêu cầu" (Biết cần làm gì) và nằm **trước** giai đoạn "Lập trình/Coding" (Bắt tay vào gõ code). Nhiệm vụ của nó là vạch ra con đường kiến trúc tối ưu để lập trình viên cứ thế mà code theo, không cần vừa code vừa suy nghĩ thuật toán.

**70. "Design Pattern" (Mẫu thiết kế) trong lập trình OOP là gì?**
- Khi thiết kế phần mềm trong nhiều thập kỷ, các kỹ sư nhận ra có những "bài toán khó" lặp đi lặp lại rất nhiều lần ở các dự án khác nhau.
- Design Pattern (Mẫu thiết kế) là **các giải pháp tổng quát, chuẩn mực và đã được chứng minh tính hiệu quả** để giải quyết các bài toán lặp lại đó. Áp dụng Pattern giúp mã nguồn dễ hiểu, dễ mở rộng và tránh các sai lầm thiết kế ngớ ngẩn (Antipatterns).
- *Ví dụ:* Mẫu Singleton, Mẫu Factory, Mẫu Observer, Mẫu Strategy.

**71. Phân tích Mẫu thiết kế Singleton (Singleton Pattern)?**
- **Vấn đề:** Trong ứng dụng, có những đối tượng mà nếu tạo ra nhiều phiên bản (instances) sẽ gây xung đột tài nguyên hoặc tốn RAM khủng khiếp (ví dụ: Kết nối Database, Trình ghi Log hệ thống).
- **Giải pháp Singleton:** Khóa chặt Constructor (Private Constructor) để ngăn không cho lệnh `new` hoạt động từ bên ngoài. Tạo một hàm tĩnh (Static method) chuyên trả về ĐÚNG MỘT instance duy nhất đã khởi tạo từ trước. Mọi nơi trong dự án khi gọi đến Class đó đều đang thao tác trên cùng 1 instance duy nhất ở bộ nhớ.

**72. Mục đích chính của việc Thiết kế Cơ sở dữ liệu (Database Design) là gì?**
- Thiết kế CSDL (Đặc biệt là Relational DB) nhằm tổ chức lưu trữ lượng lớn dữ liệu nghiệp vụ một cách hiệu quả nhất:
  - **Giảm dư thừa dữ liệu (Data Redundancy):** Chuẩn hóa bảng để thông tin không lặp lại vô ích (Tiết kiệm ổ cứng).
  - **Bảo đảm toàn vẹn dữ liệu (Data Integrity):** Dùng Khóa chính, Khóa ngoại, Ràng buộc Check để không bao giờ có dữ liệu rác/vô lý chui vào CSDL.
  - **Tối ưu tốc độ truy xuất:** Cấu trúc bảng hợp lý, gắn Index đúng chỗ để câu truy vấn SQL tìm kiếm mất mili-giây thay vì vài phút.

**73. Mô hình hóa dữ liệu thường dùng biểu đồ gì? (ERD)**
- Biểu đồ Thực thể - Mối kết hợp (ERD - Entity Relationship Diagram). 
- Nó vẽ ra các Thực thể (Entities - ví dụ: Khách hàng, Sản phẩm), các Thuộc tính (Attributes - ví dụ: Tên, SĐT), và vẽ đường kẻ nối mô tả Quan hệ (Relationships - ví dụ: Khách hàng *Mua* Sản phẩm, Tỷ lệ 1-N).

**74. Trong thiết kế CSDL quan hệ, "Khóa chính" (Primary Key) hoạt động như thế nào?**
- **Định nghĩa:** Là một thuộc tính (hoặc nhóm thuộc tính) mang giá trị ĐỘC NHẤT dùng để định danh riêng biệt cho TỪNG bản ghi (dòng) trong một bảng.
- **Tính chất bắt buộc:** Giá trị của Khóa chính không bao giờ được phép trùng lặp (Unique) và tuyệt đối không bao giờ được rỗng (NOT NULL). Ví dụ: CCCD, Mã Sinh viên.

**75. "Khóa ngoại" (Foreign Key) đảm nhiệm vai trò gì trong CSDL?**
- Khóa ngoại là cầu nối "bắt tay" giữa hai bảng dữ liệu. 
- Nó là một cột trong bảng A (bảng con), chứa giá trị trỏ trực tiếp đến Khóa chính của bảng B (bảng cha). Nhờ Khóa ngoại, CSDL bảo vệ được tính Toàn vẹn tham chiếu (Referential Integrity) - nghĩa là bạn không thể nhập một sinh viên vào "Lớp X" nếu Lớp X đó không tồn tại ở bảng Danh Mục Lớp.

**76. Thiết kế dữ liệu bao gồm 3 mức thiết kế nào?**
1. **Thiết kế mức Khái niệm (Conceptual Design):** Trừu tượng hóa nghiệp vụ khách hàng thành các biểu đồ ERD (vẽ hình chữ nhật, hình thoi). Không dính dáng gì đến công nghệ.
2. **Thiết kế mức Logic (Logical Design):** Chuyển đổi ERD thành Lược đồ quan hệ (Relational Schema) gồm các Table, Cột, Khóa chính, Khóa ngoại. Vẫn độc lập với phần mềm hệ quản trị.
3. **Thiết kế mức Vật lý (Physical Design):** Triển khai lược đồ logic đó vào một Hệ quản trị CSDL cụ thể (như MySQL, SQL Server, Oracle). Ở đây sẽ xét đến Kiểu dữ liệu (INT, VARCHAR), tạo Index, chia vùng đĩa (Partitioning).

**77. Chuẩn hóa CSDL (Database Normalization) là gì và tại sao cần thiết?**
- **Chuẩn hóa:** Là quá trình phân rã một bảng dữ liệu lớn (chứa nhiều thông tin hỗn độn, dư thừa) thành nhiều bảng nhỏ hơn, kết nối chúng qua Khóa ngoại theo các quy tắc nghiêm ngặt (Các Dạng chuẩn - Normal Forms: 1NF, 2NF, 3NF).
- **Sự cần thiết:** Khắc phục các hiện tượng "Dị thường" (Anomalies) khi Thêm/Sửa/Xóa. (Ví dụ dị thường sửa: Một khách hàng đổi SĐT, nếu thiết kế bảng không chuẩn hóa, ta phải đi Update SĐT đó ở 1000 dòng hóa đơn cũ, rất dễ sót dữ liệu dẫn đến sai lệch).

**78. Nguyên tắc "Cho phép phục hồi lỗi" (Forgiveness/Reversibility) trong UI được thực hiện bằng cách nào?**
- Người dùng luôn có xu hướng nhấp chuột nhầm hoặc gõ phím nhầm. UI tốt phải "khoan dung" với lỗi lầm này:
  - Cung cấp nút tính năng "Hoàn tác" (Undo - Ctrl+Z).
  - Yêu cầu xác nhận (Confirmation Dialog) trước các hành động nguy hiểm không thể đảo ngược (VD: "Bạn có chắc chắn muốn xóa toàn bộ database không?").
  - Xóa mềm (Soft Delete - đưa vào thùng rác) thay vì Xóa cứng (Hard Delete - xóa vĩnh viễn trong CSDL).

**79. Kiến trúc Microservices giải quyết nhược điểm gì của kiến trúc Monolithic (Nguyên khối)?**
- **Nhược điểm Monolithic:** Toàn bộ code (UI, DB logic, Xử lý thanh toán, Gửi mail) gộp chung vào 1 source code duy nhất. Khi code quá lớn, thời gian build app rất lâu; 1 module nhỏ bị lỗi tràn RAM có thể kéo sập TOÀN BỘ hệ thống; không thể scale độc lập 1 tính năng.
- **Giải pháp Microservices:** Chia nhỏ phần mềm thành hàng chục ứng dụng (services) tí hon chạy hoàn toàn độc lập trên các server khác nhau (Ví dụ: Service Thanh toán riêng, Service Kho riêng). Giao tiếp qua API. Nếu Module Thanh Toán sập, người dùng vẫn có thể xem Giỏ Hàng bình thường. Dễ dàng dùng nhiều ngôn ngữ lập trình cho nhiều service.

**80. API (Application Programming Interface) là khái niệm thiết kế vô cùng quan trọng. Nó là gì?**
- Giao diện lập trình ứng dụng (API) là các bộ quy tắc, giao thức và định dạng dữ liệu (thường là JSON/XML) cho phép các ứng dụng/phần mềm ĐỘC LẬP có thể "nói chuyện", gọi hàm và chia sẻ dữ liệu với nhau mà không cần biết mã nguồn bên trong của nhau.
- *Ví dụ:* Ứng dụng Grab không tự vẽ bản đồ mà gọi Google Maps API; App bán hàng gọi Momo API để thanh toán. Mọi thiết kế hiện đại đều là "API-first".

---
*(Xem tiếp Phần 2 để hoàn thành từ câu 101 - 200 về Lập trình OOP, Agile và Kiểm thử phần mềm chuyên sâu)*