# CHƯƠNG 2: QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SDLC)

## PHẦN 1: CÂU HỎI TỰ LUẬN NGẮN

1. **Vòng đời phát triển phần mềm (SDLC) là gì?**
   *Đáp án:* Vòng đời phát triển phần mềm (Software Development Life Cycle - SDLC) là một quy trình cấu trúc bao gồm các pha để thiết kế, phát triển và kiểm thử phần mềm chất lượng cao. Mục đích là tạo ra phần mềm đáp ứng hoặc vượt quá sự mong đợi của khách hàng, hoàn thành trong khung thời gian và ước tính chi phí.

2. **Liệt kê 5-7 pha cơ bản của SDLC và chức năng của từng pha?**
   *Đáp án:*
   - **Khảo sát (Planning/Requirements Analysis):** Xác định mục tiêu, thu thập và phân tích yêu cầu từ khách hàng/người dùng, đánh giá tính khả thi.
   - **Thiết kế (Design):** Xây dựng kiến trúc hệ thống, thiết kế giao diện, cơ sở dữ liệu và các thành phần dựa trên yêu cầu.
   - **Lập trình/Code (Implementation/Coding):** Viết mã nguồn (code) để hiện thực hóa các thiết kế thành phần mềm thực tế.
   - **Kiểm thử (Testing):** Kiểm tra phần mềm để phát hiện và sửa lỗi, đảm bảo phần mềm hoạt động đúng theo yêu cầu.
   - **Triển khai (Deployment):** Đưa phần mềm vào môi trường thực tế cho người dùng sử dụng.
   - **Bảo trì (Maintenance):** Sửa lỗi phát sinh, nâng cấp, cải tiến và thêm tính năng mới sau khi triển khai.

3. **Mô hình Thác nước (Waterfall) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Các pha diễn ra tuần tự từ trên xuống dưới, không quay lui. Pha sau chỉ bắt đầu khi pha trước đã hoàn thành.
   - **Ưu điểm:** Dễ hiểu, dễ quản lý do các giai đoạn rõ ràng, tài liệu đầy đủ ở mỗi bước.
   - **Nhược điểm:** Thiếu linh hoạt, khó thay đổi yêu cầu ở giai đoạn sau, rủi ro cao vì khách hàng chỉ thấy sản phẩm ở cuối quy trình.
   - **Trường hợp áp dụng:** Dự án nhỏ, yêu cầu rõ ràng ngay từ đầu, công nghệ quen thuộc.

4. **Mô hình chữ V (V-Model) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Mở rộng từ Waterfall, mỗi pha phát triển (nhánh trái) đều tương ứng với một pha kiểm thử (nhánh phải), tạo thành hình chữ V.
   - **Ưu điểm:** Chú trọng kiểm thử ngay từ đầu, giảm lỗi ở giai đoạn cuối, dễ theo dõi tiến độ.
   - **Nhược điểm:** Kém linh hoạt với sự thay đổi, tốn thời gian và nguồn lực.
   - **Trường hợp áp dụng:** Hệ thống y tế, hàng không, quân sự đòi hỏi độ tin cậy và an toàn cao, yêu cầu rõ ràng.

5. **Mô hình Bản mẫu (Prototyping) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Xây dựng nhanh một bản mẫu (prototype) để khách hàng trải nghiệm và góp ý, sau đó tinh chỉnh lại yêu cầu trước khi phát triển hệ thống thật.
   - **Ưu điểm:** Khách hàng tham gia sớm, làm rõ yêu cầu mập mờ, giảm rủi ro làm sai ý khách.
   - **Nhược điểm:** Tốn chi phí/thời gian làm bản mẫu, khách hàng có thể nhầm bản mẫu là sản phẩm hoàn chỉnh, code bản mẫu thường kém chất lượng.
   - **Trường hợp áp dụng:** Khách hàng chưa nắm rõ yêu cầu, hệ thống tương tác người dùng phức tạp.

6. **Mô hình Tăng dần / Lặp (Incremental / Iterative) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Phát triển phần mềm theo nhiều vòng lặp nhỏ. Mỗi vòng lặp bổ sung (incremental) các tính năng mới cho đến khi hoàn thiện.
   - **Ưu điểm:** Có sản phẩm sớm để sử dụng, dễ thích ứng với thay đổi, rủi ro phân tán ra nhiều vòng lặp.
   - **Nhược điểm:** Cần thiết kế kiến trúc tốt từ đầu để dễ mở rộng, khó quản lý tổng thể nếu vòng lặp không rõ ràng.
   - **Trường hợp áp dụng:** Dự án lớn, yêu cầu có thể thay đổi, cần đưa sản phẩm ra thị trường sớm.

7. **Mô hình Xoắn ốc (Spiral) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Kết hợp giữa lặp lại (Iterative) và tuần tự (Waterfall), đặc biệt nhấn mạnh vào **pha Phân tích rủi ro**. Mỗi vòng xoắn gồm: Lập kế hoạch, Phân tích rủi ro, Kỹ nghệ/Thực thi, Đánh giá.
   - **Phân tích rủi ro:** Đánh giá các phương án, nhận diện rủi ro kỹ thuật, quản lý và tìm cách giảm thiểu rủi ro (vd: làm prototype).
   - **Ưu điểm:** Quản lý rủi ro xuất sắc, phù hợp dự án rủi ro cao, dễ thay đổi.
   - **Nhược điểm:** Phức tạp, chi phí cao, đòi hỏi chuyên gia đánh giá rủi ro giỏi.
   - **Trường hợp áp dụng:** Dự án cực lớn, quan trọng, độ rủi ro công nghệ hoặc nghiệp vụ rất cao.

8. **Mô hình RUP (Rational Unified Process) có đặc điểm, ưu điểm, nhược điểm và trường hợp áp dụng là gì?**
   *Đáp án:*
   - **Đặc điểm:** Quy trình nặng tính tài liệu, hướng đối tượng, dựa trên UML, gồm 4 pha: Khởi tạo (Inception), Xây dựng (Elaboration), Triển khai (Construction), Chuyển giao (Transition).
   - **Ưu điểm:** Quản lý rủi ro tốt, tài liệu đầy đủ, tái sử dụng component.
   - **Nhược điểm:** Quá cồng kềnh, phức tạp, tốn thời gian cho tài liệu.
   - **Trường hợp áp dụng:** Dự án quy mô lớn, đội ngũ đông, đòi hỏi cấu trúc hệ thống rõ ràng và quản lý rủi ro chặt chẽ.

9. **Tuyên ngôn Agile (Agile Manifesto) bao gồm 4 giá trị cốt lõi nào?**
   *Đáp án:*
   - **Cá nhân và sự tương tác** quan trọng hơn quy trình và công cụ.
   - **Phần mềm chạy tốt** quan trọng hơn tài liệu đầy đủ.
   - **Cộng tác với khách hàng** quan trọng hơn đàm phán hợp đồng.
   - **Phản hồi với sự thay đổi** quan trọng hơn việc bám sát kế hoạch.

10. **Scrum là gì?**
    *Đáp án:* Scrum là một framework phổ biến của Agile, giúp các nhóm làm việc cùng nhau để phát triển, chuyển giao và duy trì các sản phẩm phức tạp thông qua cách tiếp cận lặp đi lặp lại và tăng dần (Sprints).

11. **Trong Scrum có những vai trò (Roles) nào?**
    *Đáp án:*
    - **Product Owner (PO):** Đại diện khách hàng, tối ưu hóa giá trị sản phẩm, quản lý Product Backlog.
    - **Scrum Master:** Đảm bảo Scrum được hiểu và thực hiện đúng, loại bỏ rào cản cho nhóm.
    - **Development Team:** Đội ngũ tự quản lý, liên chức năng trực tiếp xây dựng sản phẩm.

12. **Trong Scrum có những Artifacts (tạo tác/kết quả) nào?**
    *Đáp án:*
    - **Product Backlog:** Danh sách sắp xếp ưu tiên tất cả yêu cầu, tính năng của sản phẩm.
    - **Sprint Backlog:** Danh sách các công việc được chọn từ Product Backlog để hoàn thành trong một Sprint.
    - **Increment:** Phần mềm hoạt động được ở cuối mỗi Sprint, cộng dồn vào các Increment trước đó.

13. **Liệt kê và giải thích ngắn gọn các sự kiện (Events) trong Scrum?**
    *Đáp án:*
    - **Sprint:** Khung thời gian cố định (1-4 tuần) để tạo ra phần mềm sử dụng được.
    - **Sprint Planning:** Lập kế hoạch công việc cho Sprint.
    - **Daily Standup (Daily Scrum):** Họp 15 phút hằng ngày để đồng bộ công việc.
    - **Sprint Review:** Trình diễn Increment cho khách hàng và nhận phản hồi cuối Sprint.
    - **Sprint Retrospective:** Nhóm tự đánh giá lại quy trình làm việc để cải tiến cho Sprint sau.

14. **Sự khác biệt chính giữa Mô hình Thác nước (Waterfall) và Phát triển linh hoạt (Agile) là gì?**
    *Đáp án:* Waterfall đi theo trình tự tuyến tính nghiêm ngặt, ít linh hoạt với thay đổi, phù hợp dự án yêu cầu cố định. Agile chia nhỏ dự án thành nhiều phần lặp, liên tục nhận phản hồi, cực kỳ linh hoạt và thích ứng với thay đổi liên tục.

15. **Daily Standup (Daily Scrum) thường trả lời 3 câu hỏi nào?**
    *Đáp án:* Hôm qua tôi đã làm gì? Hôm nay tôi sẽ làm gì? Có trở ngại nào đang cản trở công việc của tôi không?

16. **Pha "Khảo sát / Phân tích yêu cầu" trong SDLC sẽ trả lời cho câu hỏi nào?**
    *Đáp án:* Trả lời câu hỏi: "Hệ thống cần làm cái gì?" (What the system should do).

17. **Trong mô hình chữ V, Unit Test tương ứng với pha thiết kế nào?**
    *Đáp án:* Unit Test tương ứng với pha Low-level Design (Thiết kế chi tiết/Mô-đun) hoặc pha Coding.

18. **Mô hình nào khách hàng có thể dùng thử một "phiên bản nháp" của sản phẩm để đưa ra phản hồi sớm?**
    *Đáp án:* Mô hình Bản mẫu (Prototyping).

19. **Trong mô hình RUP, pha nào tập trung vào việc xác định phạm vi dự án và lập kế hoạch sơ bộ?**
    *Đáp án:* Pha Khởi tạo (Inception).

20. **Trong Scrum, ai là người chịu trách nhiệm tối đa hóa giá trị của sản phẩm?**
    *Đáp án:* Product Owner.

21. **Mô hình xoắn ốc (Spiral Model) được đề xuất bởi ai?**
    *Đáp án:* Barry Boehm (1986).

22. **Sự khác biệt giữa Iterative và Incremental là gì?**
    *Đáp án:*
    - Iterative (Lặp): Làm đi làm lại để tinh chỉnh, cải thiện tính năng.
    - Incremental (Tăng dần): Xây dựng từng phần riêng biệt và ghép lại để hoàn thành hệ thống.
    (Thực tế thường kết hợp cả hai).

23. **Tại sao mô hình Waterfall được gọi là mô hình truyền thống / kinh điển?**
    *Đáp án:* Vì nó là mô hình đầu tiên được áp dụng rộng rãi trong kỹ nghệ phần mềm, chuyển giao tư duy sản xuất công nghiệp sang làm phần mềm.

24. **Hoạt động "Review" trong Sprint Review của Scrum có mục đích chính là gì?**
    *Đáp án:* Trình bày Increment (sản phẩm phần mềm chạy được) cho các bên liên quan và thu thập phản hồi.

25. **Nếu một dự án không rõ yêu cầu ngay từ đầu và khách hàng liên tục đổi ý, mô hình nào là TỆ nhất?**
    *Đáp án:* Mô hình Thác nước (Waterfall).


## PHẦN 2: CÂU HỎI TRẮC NGHIỆM

**Câu 1:** SDLC là viết tắt của từ gì?
A. System Development Life Cycle
B. Software Design Life Cycle
C. Software Development Life Cycle
D. System Design Life Cycle
*Đáp án: C*

**Câu 2:** Pha nào trong SDLC tập trung vào việc xác định hệ thống cần "làm gì"?
A. Thiết kế (Design)
B. Phân tích yêu cầu (Requirements Analysis)
C. Lập trình (Coding)
D. Kiểm thử (Testing)
*Đáp án: B*

**Câu 3:** Trong mô hình Thác nước (Waterfall), kết quả của pha trước sẽ là:
A. Đầu vào của pha tiếp theo
B. Được bỏ qua nếu không cần thiết
C. Khách hàng sử dụng ngay
D. Đưa vào kiểm thử luôn
*Đáp án: A*

**Câu 4:** Ưu điểm lớn nhất của mô hình Thác nước (Waterfall) là gì?
A. Linh hoạt với thay đổi yêu cầu
B. Dễ quản lý do các giai đoạn rõ ràng và có mốc thời gian
C. Khách hàng nhìn thấy sản phẩm sớm
D. Rủi ro thấp
*Đáp án: B*

**Câu 5:** Mô hình nào coi kiểm thử là một hoạt động song song với từng giai đoạn phát triển?
A. Waterfall
B. Spiral
C. V-Model
D. Prototyping
*Đáp án: C*

**Câu 6:** Trong mô hình chữ V, Acceptance Testing tương ứng với giai đoạn nào bên nhánh phát triển?
A. Coding
B. System Design
C. Architecture Design
D. Requirement Analysis
*Đáp án: D*

**Câu 7:** Nhược điểm chính của mô hình Bản mẫu (Prototyping) là gì?
A. Khách hàng không được tham gia sớm
B. Rất khó sửa đổi yêu cầu
C. Khách hàng có thể hiểu lầm bản mẫu là sản phẩm hoàn chỉnh
D. Không cần thiết kế
*Đáp án: C*

**Câu 8:** Mô hình Tăng dần (Incremental) có đặc điểm nào dưới đây?
A. Xây dựng toàn bộ hệ thống trong 1 lần
B. Bàn giao sản phẩm theo từng phần (chức năng) hoàn chỉnh
C. Chỉ phân tích rủi ro ở cuối dự án
D. Không cho phép khách hàng đánh giá
*Đáp án: B*

**Câu 9:** Mô hình Xoắn ốc (Spiral Model) đặc trưng bởi hoạt động nào sau đây?
A. Viết code nhanh
B. Phân tích rủi ro (Risk Analysis)
C. Thiết kế giao diện
D. Kiểm thử tự động
*Đáp án: B*

**Câu 10:** Mô hình Xoắn ốc kết hợp giữa các tính chất của mô hình nào?
A. Waterfall và V-Model
B. Prototyping và Agile
C. Iterative/Prototyping và Waterfall
D. RUP và Scrum
*Đáp án: C*

**Câu 11:** RUP (Rational Unified Process) là một framework quy trình phát triển phần mềm được chia làm mấy pha?
A. 3
B. 4
C. 5
D. 6
*Đáp án: B*

**Câu 12:** Trong RUP, pha Xây dựng (Elaboration) có mục tiêu chính là gì?
A. Xác định phạm vi dự án
B. Chuyển giao phần mềm cho người dùng
C. Xây dựng kiến trúc hệ thống và phân tích rủi ro lớn nhất
D. Lập trình và kiểm thử tất cả chức năng
*Đáp án: C*

**Câu 13:** Theo Tuyên ngôn Agile, yếu tố nào quan trọng HƠN "Quy trình và Công cụ"?
A. Tài liệu đầy đủ
B. Cá nhân và sự tương tác
C. Đàm phán hợp đồng
D. Kế hoạch chặt chẽ
*Đáp án: B*

**Câu 14:** Theo Tuyên ngôn Agile, "Phản hồi với sự thay đổi" được ưu tiên hơn điều gì?
A. Hợp tác với khách hàng
B. Công cụ lập trình
C. Bám sát kế hoạch
D. Phần mềm chạy tốt
*Đáp án: C*

**Câu 15:** Trong Scrum, ai là người duy nhất có quyền quản lý Product Backlog?
A. Scrum Master
B. Development Team
C. Khách hàng
D. Product Owner
*Đáp án: D*

**Câu 16:** Vai trò của Scrum Master là gì?
A. Viết mã nguồn
B. Đảm bảo quy trình Scrum được tuân thủ và loại bỏ trở ngại
C. Chỉ định công việc hằng ngày cho thành viên
D. Đàm phán giá cả với khách hàng
*Đáp án: B*

**Câu 17:** Sprint là gì trong Scrum?
A. Một loại tài liệu
B. Một khung thời gian cố định để hoàn thành một khối lượng công việc
C. Buổi họp cuối dự án
D. Một kỹ thuật lập trình
*Đáp án: B*

**Câu 18:** Cuộc họp Daily Standup (Daily Scrum) thường diễn ra trong bao lâu?
A. 1 giờ
B. 30 phút
C. Tối đa 15 phút
D. Không giới hạn thời gian
*Đáp án: C*

**Câu 19:** Kết quả (Artifact) được tạo ra ở cuối mỗi Sprint trong Scrum gọi là gì?
A. Product Backlog
B. Sprint Review
C. Increment
D. Retrospective
*Đáp án: C*

**Câu 20:** Nếu một dự án có yêu cầu không thể xác định rõ ràng từ đầu và thị trường thay đổi liên tục, phương pháp nào nên áp dụng?
A. Waterfall
B. Agile
C. V-Model
D. Không sử dụng mô hình nào
*Đáp án: B*
