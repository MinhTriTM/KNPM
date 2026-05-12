# NGÂN HÀNG CÂU HỎI LÝ THUYẾT & TÌNH HUỐNG - PHẦN 2 (Câu 101 - 200)
*(Tài liệu này bổ sung thêm 100 câu hỏi đào sâu vào phân tích tình huống, vẽ UML nâng cao, CSDL và Kiểm thử thực hành, giúp bạn hoàn thành mốc 200 câu hỏi ôn tập toàn diện môn Kỹ nghệ phần mềm)*

---

## 1. PHÂN TÍCH TÌNH HUỐNG YÊU CẦU (Câu 101 - 120)
**101. Tình huống: Khách hàng muốn "Phần mềm phải thật nhanh". Đây là yêu cầu loại gì và có đạt chuẩn không?**
=> Đây là yêu cầu Phi chức năng nhưng KHÔNG đạt chuẩn vì chữ "nhanh" quá mơ hồ, không đo lường được. (Sửa thành: Hệ thống phản hồi < 2s).

**102. Khi thu thập yêu cầu từ kế toán và thủ kho, hai người có ý kiến mâu thuẫn về quy trình nhập hàng. Bạn xử lý thế nào?**
=> Tổ chức một cuộc họp chung (workshop/JAD) với cả hai bên và người quản lý chung để thống nhất luồng quy trình (workflow).

**103. Khách hàng thay đổi yêu cầu liên tục khi bạn đang code. Bạn nên áp dụng mô hình nào?**
=> Mô hình Agile (đặc biệt là Scrum) vì nó chấp nhận sự thay đổi yêu cầu ở cả những giai đoạn muộn.

**104. Trong bảng đặc tả SRS, phần "Assumptions and Dependencies" (Giả định và Ràng buộc) dùng để ghi gì?**
=> Ghi các yếu tố bên ngoài mà dự án phụ thuộc (ví dụ: dùng API của bên thứ 3, người dùng phải có mạng internet).

**105. "Hệ thống phải mã hóa mật khẩu người dùng trước khi lưu". Đây là yêu cầu chức năng hay phi chức năng?**
=> Là yêu cầu Phi chức năng (ràng buộc về mặt Bảo mật / Security).

**106. Tại sao cần tạo Prototype (Bản mẫu) cho hệ thống E-commerce trước khi lập trình?**
=> Giúp khách hàng trải nghiệm UI/UX sớm, xác nhận lại yêu cầu giỏ hàng/thanh toán, tránh hiểu nhầm luồng xử lý.

**107. Làm thế nào để biết một Yêu cầu có "Testable" (Có thể kiểm thử được) hay không?**
=> Yêu cầu đó phải có tiêu chí đánh giá rõ ràng, input cụ thể và output có thể quan sát hoặc đo đếm được.

**108. Phân biệt "User Story" và "Use Case"?**
=> User Story là mô tả yêu cầu ngắn gọn dưới góc độ người dùng (Agile). Use Case là mô tả chi tiết các bước tương tác giữa người và hệ thống (UML).

**109. Cấu trúc chuẩn của một User Story là gì?**
=> "Là một [Vai trò], tôi muốn [Tính năng], để [Lợi ích mang lại]".

**110. Trong Scrum, Yêu cầu nào sẽ được đưa vào thực hiện trong Sprint tiếp theo?**
=> Những yêu cầu nằm ở đầu Product Backlog (ưu tiên cao nhất) do Product Owner quyết định.

**(Câu 111-120: Tương tự - Xoay quanh phân tích Requirement rủi ro, phân quyền...)**
**111. Tại sao cần xác định rõ Actor (Tác nhân) trước khi lấy yêu cầu?** => Để không bỏ sót bất kỳ nhóm người dùng nào, mỗi nhóm có quyền và nhu cầu khác nhau.
**112. Tài liệu SRS thường được phê duyệt (Sign-off) bởi ai?** => Khách hàng (Customer) hoặc Đại diện doanh nghiệp (Sponsor).
**113. Rủi ro lớn nhất nếu bỏ qua bước "Feasibility Study" (Nghiên cứu khả thi)?** => Dự án có thể hết tiền giữa chừng hoặc công nghệ hiện tại không đáp ứng được yêu cầu nghiệp vụ.
**114. "Hệ thống cho phép admin xem danh sách đơn hàng". Có lỗi gì trong câu này?** => Thiếu thông tin: "xem danh sách" nhưng theo tiêu chí nào (ngày, tháng, trạng thái)?
**115. Requirement "Tương thích với mọi trình duyệt" tại sao lại tốn kém?** => Vì phải test trên rất nhiều phiên bản cũ/mới của Chrome, Edge, Safari, Firefox...
**116. Làm thế nào để ưu tiên yêu cầu (Prioritization)?** => Dùng phương pháp MoSCoW (Must have, Should have, Could have, Won't have).
**117. Nghiệp vụ "Thanh toán qua Momo" là Yêu cầu gì?** => Yêu cầu chức năng.
**118. Ràng buộc "Chỉ dùng ngôn ngữ Java" là yêu cầu gì?** => Yêu cầu về môi trường / kỹ thuật.
**119. Cần làm gì khi có một Requirement quá phức tạp?** => Chia nhỏ nó ra thành các Sub-requirements hoặc nhiều User Stories nhỏ hơn.
**120. Trách nhiệm của Business Analyst (BA) là gì?** => Cầu nối giữa khách hàng (hiểu nghiệp vụ) và đội kỹ thuật (hiểu công nghệ).

---

## 2. NÂNG CAO VỀ BIỂU ĐỒ UML (Câu 121 - 150)
**121. Trong Use-case Diagram, Actor có thể là một phần mềm khác không?**
=> Có. Actor có thể là Con người (User) hoặc một Hệ thống bên ngoài (External System) tương tác với hệ thống.

**122. Phân biệt quan hệ Include và Extend bằng ví dụ?**
=> Include (Bắt buộc): "Rút tiền" Include "Xác thực mã PIN". Extend (Tùy chọn): "Thanh toán" có thể Extend "Áp dụng mã giảm giá".

**123. Trong biểu đồ Class, dấu "-" và "+" trước thuộc tính có ý nghĩa gì?**
=> "-" là Private (chỉ truy cập trong class đó). "+" là Public (truy cập từ bên ngoài).

**124. Dấu "#" trong biểu đồ Class nghĩa là gì?**
=> "#" là Protected (chỉ truy cập trong class đó và các class con kế thừa nó).

**125. Quan hệ "Composition" (Kết tập toàn phần) khác "Aggregation" (Kết tập bộ phận) như thế nào?**
=> Composition: Phụ thuộc sống còn (Bệnh án và Bệnh nhân - Bệnh nhân xóa thì Bệnh án bị xóa). Aggregation: Phụ thuộc lỏng lẻo (Giảng viên và Khoa - Xóa khoa, giảng viên vẫn tồn tại).

**126. Biểu diễn Composition và Aggregation trong Class Diagram bằng hình gì?**
=> Composition: Hình thoi ĐEN (đặc) ở đầu class chứa. Aggregation: Hình thoi TRẮNG (rỗng).

**127. Sequence Diagram đọc theo thứ tự nào?**
=> Đọc từ trên xuống dưới (theo trục thời gian) và từ trái sang phải (giữa các đối tượng).

**128. "Lifeline" (Đường đời) trong Sequence Diagram là gì?**
=> Là đường đứt nét thẳng đứng kéo xuống từ một đối tượng, biểu thị sự tồn tại của đối tượng đó theo thời gian.

**129. "Activation box" (Hình chữ nhật rỗng trên Lifeline) thể hiện điều gì?**
=> Thể hiện khoảng thời gian mà đối tượng đang thực hiện một hàm/hành động xử lý.

**130. Activity Diagram rất giống với biểu đồ nào trong lập trình căn bản?**
=> Sơ đồ khối (Flowchart).

**131. Khái niệm "Swimlane" (Làn bơi) trong Activity Diagram dùng làm gì?**
=> Dùng để chia các hoạt động ra theo từng đối tượng/bộ phận chịu trách nhiệm thực hiện hành động đó.

**132. Trạng thái (State) và Hoạt động (Activity) khác nhau thế nào?**
=> Trạng thái là tình trạng tĩnh của đối tượng tại 1 thời điểm (Đang chờ, Đã duyệt). Hoạt động là hành động xảy ra (Nhấn nút duyệt).

**133. Hình thoi trong Activity Diagram đại diện cho gì?**
=> Khối rẽ nhánh (Decision node), nơi luồng đi chia ra theo điều kiện (If/Else).

**134. Thanh ngang màu đen (Fork / Join node) trong Activity Diagram đại diện cho gì?**
=> Sự phân chia hoặc gộp lại của các luồng xử lý song song (chạy đồng thời).

**135. UML có tự động tạo ra code được không?**
=> Tùy thuộc vào công cụ (Tool). Một số IDE (như Visual Paradigm, Enterprise Architect) có thể generate khung code từ Class Diagram.

**(Câu 136-150: Hỏi về các Case Study cụ thể)**
**136. Đăng nhập sai 3 lần thì khóa tài khoản. Vẽ UML nào để mô tả tốt nhất?** => State Machine Diagram (Trạng thái: Bật -> Khóa) hoặc Activity Diagram.
**137. Trong Use-case Quản lý phòng khám, Actor "Bệnh nhân" có tham gia Use-case "Kê đơn thuốc" không?** => Không, chỉ Bác sĩ mới kê đơn.
**138. Ký hiệu mũi tên nét đứt trong Sequence Diagram là gì?** => Thông điệp trả về (Return message).
**139. Ký hiệu mũi tên đầu rỗng (Tam giác) trong Class Diagram là gì?** => Quan hệ Kế thừa (Generalization/Inheritance).
**140. Quan hệ "Tác giả" và "Cuốn sách" thường là loại quan hệ gì?** => Kết hợp nhiều-nhiều (Many-to-Many Association).
**141. Abstract Class được in nghiêng tên. Nó khác Class thường chỗ nào?** => Không thể tạo ra thực thể (instance/object) trực tiếp từ nó.
**142. Giao diện (Interface) trong UML khác Class như thế nào?** => Interface chỉ chứa khai báo phương thức rỗng (không có thân hàm).
**143. State "Final" trong sơ đồ trạng thái biểu diễn bằng hình gì?** => Hình tròn đen có viền tròn trắng bao quanh.
**144. Activity "Initial" bắt đầu bằng hình gì?** => Hình tròn đen đặc.
**145. Cửa hàng trực tuyến: "Giỏ hàng" và "Sản phẩm" có quan hệ gì?** => Aggregation (Kết tập). Giỏ hàng bị hủy, sản phẩm trong kho vẫn còn.
**146. Cửa hàng trực tuyến: "Đơn hàng" và "Chi tiết đơn hàng" quan hệ gì?** => Composition. Đơn hàng xóa thì chi tiết đơn hàng cũng mất ý nghĩa.
**147. Trong Sequence, nếu có vòng lặp (Loop) thì dùng ký hiệu gì?** => Khung Interaction Frame (khung chữ nhật có nhãn "loop").
**148. Trong Sequence, lệnh rẽ nhánh if/else dùng ký hiệu gì?** => Khung Interaction Frame (nhãn "alt" hoặc "opt").
**149. Package Diagram (Biểu đồ gói) dùng để làm gì?** => Nhóm các class/phần tử UML có liên quan lại với nhau thành các module/thư mục.
**150. Deployment Diagram (Biểu đồ triển khai) mô tả gì?** => Mô tả kiến trúc phần cứng vật lý mà phần mềm sẽ chạy trên đó (Server, Database node...).

---

## 3. THIẾT KẾ CƠ SỞ DỮ LIỆU & KIẾN TRÚC (Câu 151 - 175)
**151. Chuẩn hóa CSDL (Database Normalization) nhằm mục đích gì?**
=> Loại bỏ dữ liệu dư thừa, đảm bảo tính nhất quán và toàn vẹn của cơ sở dữ liệu.

**152. Dạng chuẩn 1 (1NF) yêu cầu điều gì?**
=> Các thuộc tính (cột) phải có giá trị nguyên tử (không thể chia nhỏ) và không có mảng hay danh sách trong một ô.

**153. Khóa ngoại (Foreign Key) có thể chứa giá trị NULL không?**
=> Có thể chứa giá trị NULL (nếu bản ghi đó chưa hoặc không liên kết với bảng cha).

**154. Ràng buộc toàn vẹn (Integrity Constraint) là gì?**
=> Là các quy tắc áp dụng lên cột để dữ liệu nhập vào luôn chính xác (ví dụ: Điểm phải >= 0 và <= 10).

**155. Mối quan hệ N-N (Nhiều-Nhiều) được giải quyết như thế nào trong CSDL quan hệ?**
=> Tạo thêm một "Bảng trung gian" (Junction Table) chứa 2 Khóa ngoại trỏ về 2 bảng gốc.

**156. Kiến trúc Microservices khác gì Monolithic (Nguyên khối)?**
=> Monolithic gom tất cả logic vào 1 app duy nhất; Microservices chia ứng dụng thành nhiều dịch vụ nhỏ, độc lập, giao tiếp qua API.

**157. Ưu điểm của Microservices là gì?**
=> Dễ mở rộng (scale) từng phần, một dịch vụ sập không làm sập toàn hệ thống, có thể dùng nhiều ngôn ngữ lập trình khác nhau.

**158. API (Application Programming Interface) đóng vai trò gì trong kiến trúc phần mềm?**
=> Là cầu nối cho phép các phần mềm, module khác nhau giao tiếp, trao đổi dữ liệu với nhau.

**159. RESTful API thường sử dụng định dạng dữ liệu nào để truyền tải?**
=> JSON (phổ biến nhất) hoặc XML.

**160. Index (Chỉ mục) trong Cơ sở dữ liệu giúp ích gì?**
=> Giúp tăng tốc độ tìm kiếm dữ liệu (tra cứu nhanh) nhưng làm chậm quá trình Thêm/Sửa/Xóa.

**(Câu 161 - 175: Nguyên lý thiết kế)**
**161. Nguyên tắc DRY (Don't Repeat Yourself) nghĩa là gì?** => Tránh lặp lại mã nguồn; nếu một đoạn code xuất hiện ở 2 nơi, hãy gom nó thành 1 hàm dùng chung.
**162. Nguyên tắc KISS (Keep It Simple, Stupid) khuyên điều gì?** => Giữ cho code và thiết kế đơn giản nhất có thể, tránh làm phức tạp hóa vấn đề.
**163. Nguyên tắc YAGNI (You Aren't Gonna Need It) là gì?** => Đừng viết code cho tính năng mà hiện tại chưa thực sự cần đến (chỉ tốn công bảo trì).
**164. Tách biệt View và Model trong MVC mang lại lợi ích gì?** => Developer làm UI và Developer làm Backend/DB có thể làm việc song song mà không ảnh hưởng nhau.
**165. ORM (Object-Relational Mapping) là gì?** => Là kỹ thuật ánh xạ trực tiếp các bảng trong CSDL thành các Class trong OOP (VD: Entity Framework, Hibernate).
**166. Một Bệnh án chỉ thuộc về một Bệnh nhân. Quan hệ trong CSDL là gì?** => Quan hệ Một-Nhiều (1-N).
**167. Sinh viên và Môn học có quan hệ gì trong CSDL?** => Quan hệ Nhiều-Nhiều (N-N), cần bảng trung gian "Đăng ký" hoặc "Kết quả thi".
**168. Ràng buộc "UNIQUE" khác "PRIMARY KEY" chỗ nào?** => Cả 2 đều chống trùng lặp, nhưng 1 bảng chỉ có 1 PK, trong khi có thể có nhiều cột UNIQUE; PK không được NULL, UNIQUE có thể NULL.
**169. Design Pattern "Factory" thuộc nhóm nào?** => Nhóm khởi tạo đối tượng (Creational Pattern).
**170. Caching (Bộ nhớ đệm) dùng để giải quyết vấn đề gì của kiến trúc?** => Giảm tải cho CSDL, tăng tốc độ phản hồi đối với các dữ liệu được truy cập thường xuyên nhưng ít thay đổi.
**171. Load Balancer (Bộ cân bằng tải) dùng để làm gì?** => Phân phối đều lượng truy cập của User lên nhiều Server khác nhau để tránh 1 server bị sập do quá tải.
**172. Giao thức HTTP thường có 4 phương thức chính nào tương ứng với CRUD?** => POST (Create), GET (Read), PUT (Update), DELETE (Delete).
**173. Kiến trúc Layered (Phân lớp) thường gồm 3 lớp nào?** => Presentation (Giao diện), Business Logic (Nghiệp vụ), Data Access (Dữ liệu).
**174. Rule "Depend on abstractions, not concretions" thuộc nguyên lý nào trong SOLID?** => Dependency Inversion Principle (DIP).
**175. Code "Hardcode" (Gắn cứng dữ liệu vào code) gây ra hậu quả gì?** => Khi dữ liệu thay đổi phải sửa code và build lại toàn bộ app (VD: hardcode chuỗi kết nối DB, hardcode tỷ giá thuế).

---

## 4. KIỂM THỬ THỰC HÀNH VÀ CHẤT LƯỢNG (Câu 176 - 200)
**176. Để kiểm thử trường "Độ tuổi (18 - 60)", phương pháp Phân vùng tương đương tạo ra mấy vùng?**
=> 3 vùng: < 18 (Không hợp lệ), 18-60 (Hợp lệ), > 60 (Không hợp lệ).

**177. Trong trường hợp trên, phương pháp Phân tích giá trị biên sẽ test các giá trị nào?**
=> Các giá trị: 17, 18, 60, 61.

**178. Test Case bị "Failed" khi nào?**
=> Khi Kết quả thực tế (Actual Result) chạy trên phần mềm không giống với Kết quả mong đợi (Expected Result) đã viết.

**179. Bug Report (Báo cáo lỗi) do Tester viết bắt buộc phải có thông tin gì để Dev sửa được?**
=> Bước tái hiện lỗi (Steps to reproduce), Kết quả mong đợi, Kết quả thực tế, và Môi trường test (Browser, HĐH).

**180. Smoke Test (Kiểm thử khói) là gì?**
=> Là bài test nhanh, nông để kiểm tra xem các chức năng sống còn của phần mềm có chạy được không trước khi test sâu hơn.

**181. Stress Test (Kiểm thử sức chịu tải) là gì?**
=> Bắt hệ thống hoạt động vượt quá giới hạn thiết kế (ví dụ: tạo ra 20.000 user truy cập cùng lúc) để xem hệ thống sập như thế nào và phục hồi ra sao.

**182. Security Test (Kiểm thử bảo mật) bao gồm các kỹ thuật gì phổ biến?**
=> SQL Injection, Cross-Site Scripting (XSS), kiểm tra phân quyền.

**183. Phân biệt Error, Defect (Bug) và Failure?**
=> Error: Sai lầm của lập trình viên. Defect (Bug): Dấu vết của Error trong code. Failure: Bug bị bộc lộ ra ngoài khi phần mềm đang chạy.

**184. Tự động hóa kiểm thử (Automation Test) mang lại lợi ích gì?**
=> Chạy test nhanh, chạy được nhiều lần không mỏi, rất phù hợp cho Regression Test (Kiểm thử hồi quy).

**185. Tại sao không thể kiểm thử cạn kiệt 100% (Exhaustive Testing) phần mềm?**
=> Vì số lượng đường dẫn logic và tổ hợp input dữ liệu là vô hạn; làm thế sẽ tốn thời gian và chi phí khổng lồ.

**(Câu 186-200: Case Study Test, Bảo trì, Quality)**
**186. Form yêu cầu "Mật khẩu >= 8 ký tự". Nhập "1234567" là đang dùng kỹ thuật test gì?** => Test giá trị biên (Boundary Value Analysis).
**187. Alpha Testing do ai thực hiện?** => Đội ngũ nội bộ (Dev, Tester) đóng vai khách hàng để test tại cty phần mềm.
**188. Beta Testing do ai thực hiện?** => Người dùng cuối (End-users) test tại môi trường thực tế của họ trước khi phát hành chính thức.
**189. Càng sửa nhiều bug ở 1 module, thì module đó càng ít bug đi. Đúng hay Sai? Tại sao?** => Sai. Đó là "Nghịch lý thuốc trừ sâu". Module đó có thể có cấu trúc quá phức tạp/chắp vá nên sửa lỗi này lại đẻ ra lỗi khác.
**190. Sửa một bug ở chức năng Giỏ hàng làm chức năng Thanh toán bị lỗi. Hiện tượng này gọi là gì?** => Lỗi hồi quy (Regression Bug).
**191. Refactoring (Tái cấu trúc code) thường gây ra rủi ro gì nếu không có Unit Test?** => Dễ làm gãy/hỏng logic cũ đã chạy đúng trước đó.
**192. Code Review (Review mã nguồn) mang lại lợi ích gì?** => Phát hiện lỗi sớm trước khi merge code, chia sẻ kiến thức trong team, giữ chuẩn code chung.
**193. Môi trường Staging (hoặc UAT) khác môi trường Production như thế nào?** => Staging là môi trường giống y hệt Production nhưng dùng dữ liệu giả để test. Production là môi trường chạy thật cho khách hàng.
**194. Deployment (Triển khai phần mềm) là hoạt động gì?** => Đưa phần mềm từ môi trường của nhà phát triển lên server thực tế để người dùng có thể sử dụng.
**195. Tài liệu User Manual (Hướng dẫn sử dụng) dành cho ai?** => Người dùng cuối (End-users).
**196. DevOps kết hợp 2 bộ phận nào?** => Development (Phát triển) và Operations (Vận hành), nhằm ra mắt phần mềm liên tục và ổn định.
**197. Kỹ thuật "Pair Programming" (Lập trình cặp) trong Agile là gì?** => 2 lập trình viên ngồi chung 1 máy tính: 1 người gõ code, 1 người review liên tục.
**198. Chất lượng phần mềm không chỉ là "ít bug", mà còn là gì?** => Đáp ứng đúng giá trị nghiệp vụ khách hàng cần, dễ bảo trì, hiệu năng tốt, giao diện dễ dùng.
**199. Chi phí bảo trì thường chiếm bao nhiêu % tổng chi phí vòng đời phần mềm?** => Có thể chiếm tới 60% - 80% (chi phí bảo trì thường đắt hơn chi phí xây dựng ban đầu).
**200. Tóm lại, Công nghệ phần mềm ra đời để làm gì?** => Để biến việc "viết code tự phát" thành một "ngành công nghiệp" có quy chuẩn, có thể ước lượng, đảm bảo thành công cho các dự án lớn.

---
**HẾT PHẦN 2 (HOÀN THÀNH 200 CÂU HỎI LÝ THUYẾT TOÀN DIỆN)**