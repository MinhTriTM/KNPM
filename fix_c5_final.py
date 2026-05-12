import re

with open("chương 5.md", "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("## PHẦN 2: Câu hỏi trắc nghiệm (Multiple Choice)")
part1 = parts[0]
part2 = parts[1]

# We need to rewrite questions from 165 to 200 in chapter 5.
q165_index = part2.find("**Câu 165:**")
part2_head = part2[:q165_index]

questions = [
    ("Thiết kế giao diện API: Trạng thái HTTP 201 Created thường trả về sau khi thực hiện lệnh HTTP nào thành công?", "GET.", "POST.", "PUT.", "DELETE.", "B"),
    ("Mẫu thiết kế 'Command' (Mệnh lệnh) thuộc nhóm Behavior có tác dụng gì?", "Chạy lệnh trên Command Prompt.", "Đóng gói một yêu cầu dưới dạng một Đối tượng, cho phép truyền tham số, xếp hàng (queue), ghi log các yêu cầu và hỗ trợ tính năng Hoàn tác (Undo).", "Chỉ huy lập trình viên.", "Thiết kế giao diện.", "B"),
    ("Khái niệm 'Coupling' (Ghép nối) giữa các Microservices được đánh giá bằng gì?", "Bằng số lượng dây cáp mạng.", "Mức độ phụ thuộc về giao tiếp và chia sẻ dữ liệu. Lý tưởng là Ghép nối lỏng lẻo (Loose Coupling), nơi một service sập không kéo theo service khác sập.", "Độ lớn của CSDL.", "Kích thước của Service.", "B"),
    ("Thiết kế 'API Rate Limiting' có mục đích gì?", "Tăng tốc độ truy cập web.", "Giới hạn số lượng request từ một Client/IP trong một khoảng thời gian nhất định để tránh bị quá tải Server (hoặc tấn công DDoS).", "Bảo vệ mật khẩu.", "Đổi định dạng JSON sang XML.", "B"),
    ("Mẫu thiết kế 'State' (Trạng thái) giúp ích gì trong lập trình hướng đối tượng?", "Giữ màn hình đứng yên.", "Cho phép một đối tượng thay đổi hành vi của nó khi trạng thái bên trong của nó thay đổi (nhìn như thể lớp của đối tượng bị thay đổi). Rất tốt để thay thế câu lệnh switch-case dài dòng.", "Tắt hệ điều hành.", "Vẽ biểu đồ State.", "B"),
    ("Kiến trúc 'MVC' và 'MVP' (Model-View-Presenter) khác nhau điểm cốt lõi nào?", "Không khác.", "Trong MVP, View và Model HOÀN TOÀN cách ly nhau, Presenter làm trung gian 100%. Trong MVC cổ điển, View có thể đọc trực tiếp từ Model.", "MVP là phần cứng.", "MVC dùng cho Java.", "B"),
    ("Khái niệm 'Bất biến' (Immutable) trong thiết kế CSDL (như Event Sourcing) nghĩa là:", "Dữ liệu bị lỗi.", "Dữ liệu một khi đã ghi vào CSDL thì KHÔNG BAO GIỜ bị sửa đổi (UPDATE) hoặc xóa (DELETE), chỉ có các bản ghi mới (INSERT) được thêm vào.", "CSDL không thể đọc.", "Bảng không có khóa chính.", "B"),
    ("Trong thiết kế API, kỹ thuật 'Webhook' khác 'Polling' ở điểm nào?", "Webhook chạy chậm hơn.", "Webhook là cơ chế Push: Server chủ động gọi URL của Client để báo có dữ liệu mới. Polling là Client liên tục gọi Server để hỏi (rất tốn tài nguyên).", "Polling dùng cho HTML.", "Webhook không an toàn.", "B"),
    ("Một lập trình viên thiết kế Lớp 'XeHoi' kế thừa từ Lớp 'ĐộngCơ'. Lỗi thiết kế này là gì?", "XeHoi không có động cơ.", "Vi phạm ngữ nghĩa. Mối quan hệ ở đây là 'XeHoi CÓ (Has-a) ĐộngCơ' (Composition/Aggregation), chứ không phải 'XeHoi LÀ MỘT (Is-a) ĐộngCơ'.", "Kế thừa sai ngôn ngữ.", "XeHoi phải kế thừa BánhXe.", "B"),
    ("Thiết kế 'Phòng thủ' (Defensive Design) trong bảo mật phần mềm khuyên gì về thông báo lỗi (Error messages)?", "Thông báo càng chi tiết càng tốt.", "Không bao giờ được tiết lộ chi tiết kỹ thuật nhạy cảm (như Tên bảng SQL, Phiên bản Server) cho người dùng cuối khi có lỗi xảy ra.", "Giấu nhẹm mọi thông báo lỗi.", "Gửi thông báo qua email cho hacker.", "B"),
    ("Mô hình kiến trúc 'CQRS' chia hệ thống thành 2 phần Command và Query. Mục tiêu lớn nhất là:", "Giảm số lượng code.", "Tối ưu hóa độc lập. Dữ liệu ghi (Command) yêu cầu xử lý logic phức tạp/Toàn vẹn; Dữ liệu đọc (Query) yêu cầu tốc độ phản hồi cực cao.", "Mã hóa CSDL.", "Chạy trên 2 màn hình.", "B"),
    ("Trong UML, 'Biểu đồ Đối tượng' (Object Diagram) thường được sử dụng khi nào?", "Chỉ vẽ chơi.", "Khi muốn minh họa một kịch bản dữ liệu cụ thể (Snapshot) của Biểu đồ Lớp để kiểm tra xem thiết kế lớp đó hoạt động với dữ liệu thật thế nào.", "Khi muốn sinh code tự động.", "Khi cần vẽ CSDL.", "B"),
    ("Thiết kế 'Nhà cung cấp Danh tính' (Identity Provider) tập trung như OAuth2/OIDC giải quyết bài toán gì?", "Mua bán tài khoản.", "Single Sign-On (SSO): Người dùng chỉ cần đăng nhập 1 lần ở một nơi (như Google/Facebook), sau đó được cấp quyền truy cập vào nhiều ứng dụng vệ tinh khác.", "Thiết kế màn hình Login.", "Mã hóa thẻ tín dụng.", "B"),
    ("Mẫu thiết kế 'Template Method' thuộc nhóm Khởi tạo (Creational) hay Hành vi (Behavioral)?", "Thuộc nhóm Creational.", "Thuộc nhóm Behavioral. Nó định nghĩa bộ khung của một thuật toán trong Lớp cha, nhưng nhường một số bước chi tiết cho Lớp con tự cài đặt.", "Nhóm Structural.", "Không thuộc nhóm nào.", "B"),
    ("Trong Thiết kế CSDL, 'Khóa siêu cấp' (Super Key) là gì?", "Là khóa chính.", "Là một tập hợp gồm một hay nhiều thuộc tính có thể định danh DUY NHẤT một bản ghi trong bảng (Ví dụ: ID, hoặc ID+Tên, hoặc CMND).", "Là mật khẩu CSDL.", "Là khóa ngoại.", "B"),
    ("Trong thiết kế CSDL, 'Khóa ứng viên' (Candidate Key) là gì?", "Là khóa dự phòng.", "Là một Siêu khóa (Super key) TỐI THIỂU - tức là không thể bỏ bớt bất kỳ thuộc tính nào mà vẫn giữ được tính duy nhất.", "Là khóa ngoại.", "Là ID tự tăng.", "B"),
    ("Nguyên lý 'Thay thế Liskov' (LSP) thất bại trong ví dụ kinh điển nào?", "Chó kế thừa Động vật.", "Hình Vuông kế thừa Hình Chữ Nhật. Khi ta thay đổi Chiều Dài của Hình Chữ Nhật thì Hình Vuông sẽ bị sai logic (vì Dài phải bằng Rộng).", "Sinh viên kế thừa Người.", "Ô tô kế thừa Xe cộ.", "B"),
    ("Thiết kế 'Trang đơn' (Single Page Application - SPA) đòi hỏi kiến trúc Backend phải cung cấp gì?", "Cung cấp mã HTML.", "Cung cấp các API (JSON/XML) thay vì trả về giao diện HTML. Frontend sẽ tự gọi API và vẽ lại giao diện cục bộ.", "Cung cấp CSS.", "Không cần Backend.", "B"),
    ("Một Lớp (Class) A sử dụng biến toàn cục để lưu trạng thái, Lớp B cũng sử dụng biến toàn cục đó. Hai lớp này bị ghép nối theo kiểu gì?", "Data Coupling.", "Common Coupling (Ghép nối Môi trường chung/Toàn cục).", "Control Coupling.", "No Coupling.", "B"),
    ("Khi thiết kế hệ thống có tính năng Tìm kiếm toàn văn bản (Full-text Search) khổng lồ, kỹ sư thường chọn giải pháp kiến trúc nào?", "Dùng lệnh LIKE '%...%' của SQL Server.", "Sử dụng một Search Engine chuyên dụng (như Elasticsearch, Solr) được đồng bộ dữ liệu từ CSDL gốc, vì CSDL quan hệ không tối ưu cho Full-text search.", "Chạy vòng lặp trong Code.", "Không làm tính năng tìm kiếm.", "B"),
    ("Khái niệm 'Dependency Injection Container' (IoC Container) là một công cụ giúp:", "Xóa thư mục dự án.", "Tự động quản lý vòng đời và tự động tiêm (Inject) các đối tượng phụ thuộc vào nhau lúc khởi chạy ứng dụng, giúp lập trình viên không phải viết chữ `new`.", "Vẽ giao diện web.", "Cài đặt Windows.", "B"),
    ("Trong Biểu đồ Lớp, nếu Lớp 'HọcSinh' và Lớp 'LớpHọc' có quan hệ 1-N (Một LớpHọc có nhiều HọcSinh), thì mũi tên kết hợp hướng từ đâu đến đâu?", "Từ HọcSinh sang LớpHọc.", "Tuyệt nhất là hướng từ LớpHọc -> HọcSinh (LớpHọc chứa danh sách HọcSinh), điều này thể hiện LớpHọc gọi đến HọcSinh (Navigability).", "Hai chiều.", "Không có mũi tên.", "B"),
    ("Mô hình kiến trúc 'Micro-frontend' là sự áp dụng triết lý Microservices vào đâu?", "Vào CSDL.", "Vào phía Giao diện Người dùng. Chia một ứng dụng Web lớn (Frontend) thành nhiều mảnh giao diện nhỏ do các Team độc lập phát triển và ghép lại.", "Vào Mạng LAN.", "Vào API Gateway.", "B"),
    ("Khi Thiết kế CSDL, 'Tính nguyên tử' (Atomicity) của Dạng chuẩn 1 (1NF) cấm việc lưu dữ liệu gì?", "Lưu số thập phân.", "Cấm lưu một mảng/danh sách các giá trị vào trong cùng MỘT cột (Ví dụ: Cột SoDienThoai chứa '0901, 0902').", "Cấm lưu tên dài.", "Cấm lưu ngày tháng.", "B"),
    ("Trong Thiết kế CSDL, Dạng chuẩn 2 (2NF) bắt buộc điều kiện gì ngoài việc phải đạt 1NF?", "Khóa chính phải là Auto-increment.", "Các thuộc tính không khóa phải phụ thuộc HOÀN TOÀN vào TOÀN BỘ khóa chính (Loại bỏ phụ thuộc một phần).", "Mỗi bảng chỉ có 1 cột.", "Bảng không có dữ liệu null.", "B"),
    ("Thiết kế Giao diện (UI) tốt phải tính đến yếu tố 'Khả năng truy cập' (Accessibility - a11y). Nó nghĩa là gì?", "Ứng dụng tải thật nhanh.", "Giao diện phải được thiết kế để người khuyết tật (mù màu, khiếm thị dùng trình đọc màn hình, người già) cũng có thể sử dụng được.", "Truy cập không cần mật khẩu.", "Truy cập được trên mọi trình duyệt.", "B"),
    ("Sự kết dính Truyền thông (Communicational Cohesion) trong thiết kế module xảy ra khi nào?", "Khi module có mạng LAN.", "Khi các hành động trong module thực thi trên CÙNG một khối dữ liệu đầu vào hoặc đầu ra.", "Khi module nói chuyện với nhau.", "Khi module chạy ngẫu nhiên.", "B"),
    ("Việc áp dụng 'Mã sạch' (Clean Code) trong Thiết kế Lớp (Class Design) yêu cầu quy tắc đặt tên như thế nào?", "Tên lớp bằng chữ viết thường.", "Tên Lớp (Class) phải là Danh từ hoặc Cụm danh từ (VD: Customer, Account). Tên Phương thức (Method) phải là Động từ (VD: save(), deleteAccount()).", "Tên Lớp phải là số.", "Tên hàm phải là Danh từ.", "B"),
    ("Trong kiến trúc REST API, khi muốn XÓA một tài nguyên, ta dùng phương thức HTTP gì?", "GET.", "DELETE.", "POST.", "PUT.", "B"),
    ("Kỹ thuật 'Soft Delete' (Xóa mềm) trong CSDL khác 'Hard Delete' (Xóa cứng) ở điểm nào?", "Xóa mềm chạy chậm.", "Soft Delete không xóa dữ liệu thật khỏi ổ cứng, mà chỉ cập nhật một cờ (ví dụ: `is_deleted = true`), giúp dễ khôi phục và giữ toàn vẹn dữ liệu lịch sử.", "Xóa cứng giữ lại dữ liệu.", "Không có gì khác biệt.", "B"),
    ("Khái niệm 'Mẫu kiến trúc' (Architectural Pattern) khác 'Mẫu thiết kế' (Design Pattern) ở điểm nào?", "Mẫu kiến trúc chỉ dùng cho mạng.", "Mẫu kiến trúc mô tả giải pháp cấu trúc vĩ mô toàn hệ thống (VD: MVC, Microservices). Mẫu thiết kế giải quyết vấn đề cục bộ của code (VD: Singleton, Observer).", "Không khác nhau.", "Mẫu kiến trúc rẻ hơn.", "B"),
    ("Trong Thiết kế Phần mềm, 'Bộ đêm' (Cache) hoạt động tốt nhất cho loại dữ liệu nào?", "Dữ liệu cập nhật liên tục mỗi giây.", "Dữ liệu được đọc thường xuyên (Read-heavy) nhưng rất hiếm khi thay đổi (VD: Cấu hình hệ thống, Danh mục tỉnh thành).", "Mật khẩu người dùng.", "Không nên dùng Cache.", "B"),
    ("Điều gì tạo nên sự phức tạp của việc 'Đồng bộ Cache' (Cache Invalidation)?", "Vì RAM quá nhỏ.", "Phải đảm bảo khi dữ liệu gốc dưới CSDL thay đổi, dữ liệu trong Cache cũng phải bị xóa/cập nhật ngay lập tức để người dùng không đọc phải dữ liệu cũ/sai.", "Vì CSDL không hỗ trợ.", "Vì mạng bị trễ.", "B"),
    ("Trong RUP, pha nào thực hiện và chốt hầu hết các vấn đề về Thiết kế Kiến trúc (Architectural Design)?", "Pha Inception.", "Pha Elaboration (Khảo sát tỉ mỉ).", "Pha Construction.", "Pha Transition.", "B"),
    ("Để giảm thiểu thời gian Downtime (chết hệ thống) khi triển khai phiên bản mới, ta dùng kiến trúc triển khai gì?", "Tắt hệ thống ban đêm.", "Kiến trúc Blue-Green Deployment hoặc Canary Release. Triển khai song song 2 môi trường, chuyển luồng Traffic dần dần từ bản cũ sang bản mới.", "Khởi động lại Server.", "Xóa bản cũ đi trước.", "B"),
    ("Cuối cùng, 'Thiết kế phần mềm' tốt không phải là làm cho hệ thống trông phức tạp để thể hiện trí tuệ, mà là:", "Làm hệ thống chạy nhanh nhất thế giới.", "Giấu đi sự phức tạp đó đằng sau những giao diện (Interface) đơn giản, thanh lịch, biến một bài toán khổng lồ thành những khối xếp hình dễ quản lý.", "Làm cho không ai đọc được code.", "Bắt khách hàng trả nhiều tiền.", "B")
]

new_part2_tail = ""
for i, (q, a, b, c, d, ans) in enumerate(questions, 165):
    new_part2_tail += f"**Câu {i}:** {q}\n"
    new_part2_tail += f"A. {a}\nB. {b}\nC. {c}\nD. {d}\n*Đáp án: {ans}*\n\n"

with open("chương 5.md", "w", encoding="utf-8") as f:
    f.write(part1 + "## PHẦN 2: Câu hỏi trắc nghiệm (Multiple Choice)\n" + part2_head + new_part2_tail)
