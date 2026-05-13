Some content
## PHẦN 2: Câu hỏi trắc nghiệm (Multiple Choice)

Other content
**Câu 165:** Thiết kế giao diện API: Trạng thái HTTP 201 Created thường trả về sau khi thực hiện lệnh HTTP nào thành công?
A. GET.
B. POST.
C. PUT.
D. DELETE.
*Đáp án: B*

**Câu 166:** Mẫu thiết kế 'Command' (Mệnh lệnh) thuộc nhóm Behavior có tác dụng gì?
A. Chạy lệnh trên Command Prompt.
B. Đóng gói một yêu cầu dưới dạng một Đối tượng, cho phép truyền tham số, xếp hàng (queue), ghi log các yêu cầu và hỗ trợ tính năng Hoàn tác (Undo).
C. Chỉ huy lập trình viên.
D. Thiết kế giao diện.
*Đáp án: B*

**Câu 167:** Khái niệm 'Coupling' (Ghép nối) giữa các Microservices được đánh giá bằng gì?
A. Bằng số lượng dây cáp mạng.
B. Mức độ phụ thuộc về giao tiếp và chia sẻ dữ liệu. Lý tưởng là Ghép nối lỏng lẻo (Loose Coupling), nơi một service sập không kéo theo service khác sập.
C. Độ lớn của CSDL.
D. Kích thước của Service.
*Đáp án: B*

**Câu 168:** Thiết kế 'API Rate Limiting' có mục đích gì?
A. Tăng tốc độ truy cập web.
B. Giới hạn số lượng request từ một Client/IP trong một khoảng thời gian nhất định để tránh bị quá tải Server (hoặc tấn công DDoS).
C. Bảo vệ mật khẩu.
D. Đổi định dạng JSON sang XML.
*Đáp án: B*

**Câu 169:** Mẫu thiết kế 'State' (Trạng thái) giúp ích gì trong lập trình hướng đối tượng?
A. Giữ màn hình đứng yên.
B. Cho phép một đối tượng thay đổi hành vi của nó khi trạng thái bên trong của nó thay đổi (nhìn như thể lớp của đối tượng bị thay đổi). Rất tốt để thay thế câu lệnh switch-case dài dòng.
C. Tắt hệ điều hành.
D. Vẽ biểu đồ State.
*Đáp án: B*

**Câu 170:** Kiến trúc 'MVC' và 'MVP' (Model-View-Presenter) khác nhau điểm cốt lõi nào?
A. Không khác.
B. Trong MVP, View và Model HOÀN TOÀN cách ly nhau, Presenter làm trung gian 100%. Trong MVC cổ điển, View có thể đọc trực tiếp từ Model.
C. MVP là phần cứng.
D. MVC dùng cho Java.
*Đáp án: B*

**Câu 171:** Khái niệm 'Bất biến' (Immutable) trong thiết kế CSDL (như Event Sourcing) nghĩa là:
A. Dữ liệu bị lỗi.
B. Dữ liệu một khi đã ghi vào CSDL thì KHÔNG BAO GIỜ bị sửa đổi (UPDATE) hoặc xóa (DELETE), chỉ có các bản ghi mới (INSERT) được thêm vào.
C. CSDL không thể đọc.
D. Bảng không có khóa chính.
*Đáp án: B*

**Câu 172:** Trong thiết kế API, kỹ thuật 'Webhook' khác 'Polling' ở điểm nào?
A. Webhook chạy chậm hơn.
B. Webhook là cơ chế Push: Server chủ động gọi URL của Client để báo có dữ liệu mới. Polling là Client liên tục gọi Server để hỏi (rất tốn tài nguyên).
C. Polling dùng cho HTML.
D. Webhook không an toàn.
*Đáp án: B*

**Câu 173:** Một lập trình viên thiết kế Lớp 'XeHoi' kế thừa từ Lớp 'ĐộngCơ'. Lỗi thiết kế này là gì?
A. XeHoi không có động cơ.
B. Vi phạm ngữ nghĩa. Mối quan hệ ở đây là 'XeHoi CÓ (Has-a) ĐộngCơ' (Composition/Aggregation), chứ không phải 'XeHoi LÀ MỘT (Is-a) ĐộngCơ'.
C. Kế thừa sai ngôn ngữ.
D. XeHoi phải kế thừa BánhXe.
*Đáp án: B*

**Câu 174:** Thiết kế 'Phòng thủ' (Defensive Design) trong bảo mật phần mềm khuyên gì về thông báo lỗi (Error messages)?
A. Thông báo càng chi tiết càng tốt.
B. Không bao giờ được tiết lộ chi tiết kỹ thuật nhạy cảm (như Tên bảng SQL, Phiên bản Server) cho người dùng cuối khi có lỗi xảy ra.
C. Giấu nhẹm mọi thông báo lỗi.
D. Gửi thông báo qua email cho hacker.
*Đáp án: B*

**Câu 175:** Mô hình kiến trúc 'CQRS' chia hệ thống thành 2 phần Command và Query. Mục tiêu lớn nhất là:
A. Giảm số lượng code.
B. Tối ưu hóa độc lập. Dữ liệu ghi (Command) yêu cầu xử lý logic phức tạp/Toàn vẹn; Dữ liệu đọc (Query) yêu cầu tốc độ phản hồi cực cao.
C. Mã hóa CSDL.
D. Chạy trên 2 màn hình.
*Đáp án: B*

**Câu 176:** Trong UML, 'Biểu đồ Đối tượng' (Object Diagram) thường được sử dụng khi nào?
A. Chỉ vẽ chơi.
B. Khi muốn minh họa một kịch bản dữ liệu cụ thể (Snapshot) của Biểu đồ Lớp để kiểm tra xem thiết kế lớp đó hoạt động với dữ liệu thật thế nào.
C. Khi muốn sinh code tự động.
D. Khi cần vẽ CSDL.
*Đáp án: B*

**Câu 177:** Thiết kế 'Nhà cung cấp Danh tính' (Identity Provider) tập trung như OAuth2/OIDC giải quyết bài toán gì?
A. Mua bán tài khoản.
B. Single Sign-On (SSO): Người dùng chỉ cần đăng nhập 1 lần ở một nơi (như Google/Facebook), sau đó được cấp quyền truy cập vào nhiều ứng dụng vệ tinh khác.
C. Thiết kế màn hình Login.
D. Mã hóa thẻ tín dụng.
*Đáp án: B*

**Câu 178:** Mẫu thiết kế 'Template Method' thuộc nhóm Khởi tạo (Creational) hay Hành vi (Behavioral)?
A. Thuộc nhóm Creational.
B. Thuộc nhóm Behavioral. Nó định nghĩa bộ khung của một thuật toán trong Lớp cha, nhưng nhường một số bước chi tiết cho Lớp con tự cài đặt.
C. Nhóm Structural.
D. Không thuộc nhóm nào.
*Đáp án: B*

**Câu 179:** Trong Thiết kế CSDL, 'Khóa siêu cấp' (Super Key) là gì?
A. Là khóa chính.
B. Là một tập hợp gồm một hay nhiều thuộc tính có thể định danh DUY NHẤT một bản ghi trong bảng (Ví dụ: ID, hoặc ID+Tên, hoặc CMND).
C. Là mật khẩu CSDL.
D. Là khóa ngoại.
*Đáp án: B*

**Câu 180:** Trong thiết kế CSDL, 'Khóa ứng viên' (Candidate Key) là gì?
A. Là khóa dự phòng.
B. Là một Siêu khóa (Super key) TỐI THIỂU - tức là không thể bỏ bớt bất kỳ thuộc tính nào mà vẫn giữ được tính duy nhất.
C. Là khóa ngoại.
D. Là ID tự tăng.
*Đáp án: B*

**Câu 181:** Nguyên lý 'Thay thế Liskov' (LSP) thất bại trong ví dụ kinh điển nào?
A. Chó kế thừa Động vật.
B. Hình Vuông kế thừa Hình Chữ Nhật. Khi ta thay đổi Chiều Dài của Hình Chữ Nhật thì Hình Vuông sẽ bị sai logic (vì Dài phải bằng Rộng).
C. Sinh viên kế thừa Người.
D. Ô tô kế thừa Xe cộ.
*Đáp án: B*

**Câu 182:** Thiết kế 'Trang đơn' (Single Page Application - SPA) đòi hỏi kiến trúc Backend phải cung cấp gì?
A. Cung cấp mã HTML.
B. Cung cấp các API (JSON/XML) thay vì trả về giao diện HTML. Frontend sẽ tự gọi API và vẽ lại giao diện cục bộ.
C. Cung cấp CSS.
D. Không cần Backend.
*Đáp án: B*

**Câu 183:** Một Lớp (Class) A sử dụng biến toàn cục để lưu trạng thái, Lớp B cũng sử dụng biến toàn cục đó. Hai lớp này bị ghép nối theo kiểu gì?
A. Data Coupling.
B. Common Coupling (Ghép nối Môi trường chung/Toàn cục).
C. Control Coupling.
D. No Coupling.
*Đáp án: B*

**Câu 184:** Khi thiết kế hệ thống có tính năng Tìm kiếm toàn văn bản (Full-text Search) khổng lồ, kỹ sư thường chọn giải pháp kiến trúc nào?
A. Dùng lệnh LIKE '%...%' của SQL Server.
B. Sử dụng một Search Engine chuyên dụng (như Elasticsearch, Solr) được đồng bộ dữ liệu từ CSDL gốc, vì CSDL quan hệ không tối ưu cho Full-text search.
C. Chạy vòng lặp trong Code.
D. Không làm tính năng tìm kiếm.
*Đáp án: B*

**Câu 185:** Khái niệm 'Dependency Injection Container' (IoC Container) là một công cụ giúp:
A. Xóa thư mục dự án.
B. Tự động quản lý vòng đời và tự động tiêm (Inject) các đối tượng phụ thuộc vào nhau lúc khởi chạy ứng dụng, giúp lập trình viên không phải viết chữ `new`.
C. Vẽ giao diện web.
D. Cài đặt Windows.
*Đáp án: B*

**Câu 186:** Trong Biểu đồ Lớp, nếu Lớp 'HọcSinh' và Lớp 'LớpHọc' có quan hệ 1-N (Một LớpHọc có nhiều HọcSinh), thì mũi tên kết hợp hướng từ đâu đến đâu?
A. Từ HọcSinh sang LớpHọc.
B. Tuyệt nhất là hướng từ LớpHọc -> HọcSinh (LớpHọc chứa danh sách HọcSinh), điều này thể hiện LớpHọc gọi đến HọcSinh (Navigability).
C. Hai chiều.
D. Không có mũi tên.
*Đáp án: B*

**Câu 187:** Mô hình kiến trúc 'Micro-frontend' là sự áp dụng triết lý Microservices vào đâu?
A. Vào CSDL.
B. Vào phía Giao diện Người dùng. Chia một ứng dụng Web lớn (Frontend) thành nhiều mảnh giao diện nhỏ do các Team độc lập phát triển và ghép lại.
C. Vào Mạng LAN.
D. Vào API Gateway.
*Đáp án: B*

**Câu 188:** Khi Thiết kế CSDL, 'Tính nguyên tử' (Atomicity) của Dạng chuẩn 1 (1NF) cấm việc lưu dữ liệu gì?
A. Lưu số thập phân.
B. Cấm lưu một mảng/danh sách các giá trị vào trong cùng MỘT cột (Ví dụ: Cột SoDienThoai chứa '0901, 0902').
C. Cấm lưu tên dài.
D. Cấm lưu ngày tháng.
*Đáp án: B*

**Câu 189:** Trong Thiết kế CSDL, Dạng chuẩn 2 (2NF) bắt buộc điều kiện gì ngoài việc phải đạt 1NF?
A. Khóa chính phải là Auto-increment.
B. Các thuộc tính không khóa phải phụ thuộc HOÀN TOÀN vào TOÀN BỘ khóa chính (Loại bỏ phụ thuộc một phần).
C. Mỗi bảng chỉ có 1 cột.
D. Bảng không có dữ liệu null.
*Đáp án: B*

**Câu 190:** Thiết kế Giao diện (UI) tốt phải tính đến yếu tố 'Khả năng truy cập' (Accessibility - a11y). Nó nghĩa là gì?
A. Ứng dụng tải thật nhanh.
B. Giao diện phải được thiết kế để người khuyết tật (mù màu, khiếm thị dùng trình đọc màn hình, người già) cũng có thể sử dụng được.
C. Truy cập không cần mật khẩu.
D. Truy cập được trên mọi trình duyệt.
*Đáp án: B*

**Câu 191:** Sự kết dính Truyền thông (Communicational Cohesion) trong thiết kế module xảy ra khi nào?
A. Khi module có mạng LAN.
B. Khi các hành động trong module thực thi trên CÙNG một khối dữ liệu đầu vào hoặc đầu ra.
C. Khi module nói chuyện với nhau.
D. Khi module chạy ngẫu nhiên.
*Đáp án: B*

**Câu 192:** Việc áp dụng 'Mã sạch' (Clean Code) trong Thiết kế Lớp (Class Design) yêu cầu quy tắc đặt tên như thế nào?
A. Tên lớp bằng chữ viết thường.
B. Tên Lớp (Class) phải là Danh từ hoặc Cụm danh từ (VD: Customer, Account). Tên Phương thức (Method) phải là Động từ (VD: save(), deleteAccount()).
C. Tên Lớp phải là số.
D. Tên hàm phải là Danh từ.
*Đáp án: B*

**Câu 193:** Trong kiến trúc REST API, khi muốn XÓA một tài nguyên, ta dùng phương thức HTTP gì?
A. GET.
B. DELETE.
C. POST.
D. PUT.
*Đáp án: B*

**Câu 194:** Kỹ thuật 'Soft Delete' (Xóa mềm) trong CSDL khác 'Hard Delete' (Xóa cứng) ở điểm nào?
A. Xóa mềm chạy chậm.
B. Soft Delete không xóa dữ liệu thật khỏi ổ cứng, mà chỉ cập nhật một cờ (ví dụ: `is_deleted = true`), giúp dễ khôi phục và giữ toàn vẹn dữ liệu lịch sử.
C. Xóa cứng giữ lại dữ liệu.
D. Không có gì khác biệt.
*Đáp án: B*

**Câu 195:** Khái niệm 'Mẫu kiến trúc' (Architectural Pattern) khác 'Mẫu thiết kế' (Design Pattern) ở điểm nào?
A. Mẫu kiến trúc chỉ dùng cho mạng.
B. Mẫu kiến trúc mô tả giải pháp cấu trúc vĩ mô toàn hệ thống (VD: MVC, Microservices). Mẫu thiết kế giải quyết vấn đề cục bộ của code (VD: Singleton, Observer).
C. Không khác nhau.
D. Mẫu kiến trúc rẻ hơn.
*Đáp án: B*

**Câu 196:** Trong Thiết kế Phần mềm, 'Bộ đêm' (Cache) hoạt động tốt nhất cho loại dữ liệu nào?
A. Dữ liệu cập nhật liên tục mỗi giây.
B. Dữ liệu được đọc thường xuyên (Read-heavy) nhưng rất hiếm khi thay đổi (VD: Cấu hình hệ thống, Danh mục tỉnh thành).
C. Mật khẩu người dùng.
D. Không nên dùng Cache.
*Đáp án: B*

**Câu 197:** Điều gì tạo nên sự phức tạp của việc 'Đồng bộ Cache' (Cache Invalidation)?
A. Vì RAM quá nhỏ.
B. Phải đảm bảo khi dữ liệu gốc dưới CSDL thay đổi, dữ liệu trong Cache cũng phải bị xóa/cập nhật ngay lập tức để người dùng không đọc phải dữ liệu cũ/sai.
C. Vì CSDL không hỗ trợ.
D. Vì mạng bị trễ.
*Đáp án: B*

**Câu 198:** Trong RUP, pha nào thực hiện và chốt hầu hết các vấn đề về Thiết kế Kiến trúc (Architectural Design)?
A. Pha Inception.
B. Pha Elaboration (Khảo sát tỉ mỉ).
C. Pha Construction.
D. Pha Transition.
*Đáp án: B*

**Câu 199:** Để giảm thiểu thời gian Downtime (chết hệ thống) khi triển khai phiên bản mới, ta dùng kiến trúc triển khai gì?
A. Tắt hệ thống ban đêm.
B. Kiến trúc Blue-Green Deployment hoặc Canary Release. Triển khai song song 2 môi trường, chuyển luồng Traffic dần dần từ bản cũ sang bản mới.
C. Khởi động lại Server.
D. Xóa bản cũ đi trước.
*Đáp án: B*

**Câu 200:** Cuối cùng, 'Thiết kế phần mềm' tốt không phải là làm cho hệ thống trông phức tạp để thể hiện trí tuệ, mà là:
A. Làm hệ thống chạy nhanh nhất thế giới.
B. Giấu đi sự phức tạp đó đằng sau những giao diện (Interface) đơn giản, thanh lịch, biến một bài toán khổng lồ thành những khối xếp hình dễ quản lý.
C. Làm cho không ai đọc được code.
D. Bắt khách hàng trả nhiều tiền.
*Đáp án: B*
