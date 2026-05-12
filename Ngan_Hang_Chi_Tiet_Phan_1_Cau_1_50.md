# NGÂN HÀNG CÂU HỎI LÝ THUYẾT SIÊU CHI TIẾT - PHẦN 1 (Câu 1 - 50)
*(Bao gồm Chương 1, Chương 2 và nửa đầu Chương 3)*

---

## CHƯƠNG 1: GIỚI THIỆU CÔNG NGHỆ PHẦN MỀM

**1. Phần mềm được định nghĩa như thế nào dưới góc nhìn chuyên viên tin học?**
- **Định nghĩa đầy đủ:** Phần mềm (Software) không chỉ là những dòng code (chương trình máy tính) mà nó là một tập hợp bao gồm 3 thành phần không thể tách rời:
  1. **Chương trình máy tính (Computer Programs):** Là các đoạn mã chỉ thị cho máy tính thực hiện các chức năng cụ thể.
  2. **Cấu trúc dữ liệu (Data Structures):** Cho phép chương trình thao tác, lưu trữ và quản lý thông tin một cách tối ưu.
  3. **Tài liệu liên quan (Documentation):** Bao gồm tài liệu đặc tả yêu cầu, tài liệu thiết kế, tài liệu hướng dẫn sử dụng và bảo trì. Nếu thiếu tài liệu, phần mềm đó không được coi là một sản phẩm kỹ nghệ hoàn chỉnh.

**2. Công nghệ phần mềm (Software Engineering) là gì?**
- Công nghệ phần mềm là một chuyên ngành kỹ thuật áp dụng các nguyên lý toán học, khoa học máy tính và kỹ thuật vào việc phát triển phần mềm. 
- Nó đặc trưng bởi việc sử dụng một "cách tiếp cận có hệ thống, có kỷ luật và có thể định lượng được" để phát triển, vận hành và bảo trì phần mềm. Mục đích cốt lõi là tạo ra các phần mềm đạt chất lượng cao, đúng tiến độ và nằm trong ngân sách cho phép, thay vì viết code một cách tự phát và hỗn loạn.

**3. Khủng hoảng phần mềm (Software Crisis) là hiện tượng gì?**
- **Bối cảnh:** Thuật ngữ này xuất hiện từ những năm 1960 khi phần cứng máy tính phát triển mạnh mẽ, dẫn đến nhu cầu phần mềm lớn và phức tạp hơn.
- **Biểu hiện:** Là tình trạng các dự án phần mềm liên tục gặp thất bại. Các biểu hiện cụ thể bao gồm:
  - Chi phí phát triển vượt xa ngân sách dự kiến.
  - Thời gian hoàn thành trễ hơn rất nhiều so với hạn chót.
  - Chất lượng phần mềm thấp, nhiều lỗi (bug), hoạt động không ổn định.
  - Phần mềm làm ra không đáp ứng đúng nhu cầu thực tế của khách hàng, bảo trì cực kỳ khó khăn.

**4. Hãy nêu 3 tiêu chí cốt lõi mà người sử dụng đánh giá chất lượng phần mềm?**
- Người sử dụng (End-users) thường không quan tâm đến mã nguồn bên trong mà đánh giá qua trải nghiệm:
  1. **Tính đúng đắn (Correctness):** Phần mềm phải thực hiện chính xác các chức năng đã được yêu cầu, không tính toán sai hoặc xuất ra dữ liệu rác.
  2. **Tính tiện dụng (Usability):** Giao diện phải trực quan, dễ học, dễ nhớ và thân thiện. Người dùng có thể hoàn thành công việc của họ một cách mượt mà nhất.
  3. **Tính hiệu quả (Efficiency):** Phần mềm phải chạy nhanh, phản hồi tức thời, không tiêu tốn quá nhiều tài nguyên hệ thống (RAM, CPU, Pin...).

**5. Nêu 3 đặc trưng cơ bản của phần mềm làm nó khác biệt hoàn toàn với phần cứng?**
- **Thứ nhất, phần mềm mang tính logic, không phải vật lý:** Nó là tập hợp các chỉ thị và dữ liệu trừu tượng, không có hình hài, khối lượng hay kích thước vật lý.
- **Thứ hai, phần mềm không bị "hao mòn" cơ học:** Khác với phần cứng sẽ bị cũ hỏng theo thời gian, phần mềm không bị mòn đi. Tuy nhiên, nó bị "thoái hóa" (Deterioration) do môi trường thay đổi (HĐH mới, yêu cầu mới) khiến nó trở nên lỗi thời nếu không được bảo trì.
- **Thứ ba, phần mềm thường được "đo ni đóng giày":** Trong khi phần cứng được lắp ráp từ các linh kiện tiêu chuẩn có sẵn (IC, chip), phần mềm (đặc biệt là phần mềm doanh nghiệp) thường được thiết kế và xây dựng mới hoàn toàn (custom-built) theo yêu cầu đặc thù của từng tổ chức.

**6. Công nghệ phần mềm nghiên cứu những khía cạnh cốt lõi nào?**
- Công nghệ phần mềm xây dựng trên nền tảng 3 trụ cột (cộng thêm 1 nền tảng chất lượng):
  1. **Phương pháp (Methods):** Cách thức kỹ thuật để xây dựng phần mềm (cách thu thập yêu cầu, cách thiết kế kiến trúc, cách viết code, cách kiểm thử).
  2. **Quy trình (Processes):** Các bước tuần tự hoặc lặp lại để gắn kết các phương pháp và công cụ lại với nhau (VD: Quy trình thác nước, Quy trình Scrum), quy định ai làm việc gì, khi nào.
  3. **Công cụ (Tools):** Cung cấp sự hỗ trợ tự động hoặc bán tự động cho quy trình và phương pháp (VD: Git để quản lý mã nguồn, Jira để quản lý task, Selenium để test tự động).

**7. "Stakeholder" (Người có liên quan) trong một dự án phần mềm là những ai?**
- Bất kỳ cá nhân, nhóm người hoặc tổ chức nào có quyền lợi, bị ảnh hưởng hoặc có thể tác động đến dự án phần mềm đều được gọi là Stakeholder.
- **Phân loại chính:**
  - *Khách hàng (Client/Sponsor):* Người bỏ tiền ra thuê viết phần mềm.
  - *Người dùng cuối (End-Users):* Người trực tiếp thao tác trên phần mềm hàng ngày.
  - *Đội ngũ phát triển (Development Team):* Quản trị dự án (PM), Lập trình viên (Dev), Chuyên viên kiểm thử (Tester), Chuyên viên phân tích nghiệp vụ (BA).
  - *Nhà quản lý (Managers):* Quản lý cấp cao của doanh nghiệp sử dụng phần mềm.

**8. Phần mềm tốt (Good Software) cần thỏa mãn 4 thuộc tính chất lượng (properties) quan trọng nào?**
- Theo tài liệu chuẩn của Ian Sommerville, 4 thuộc tính đó là:
  1. **Khả năng bảo trì (Maintainability):** Code phải được viết rõ ràng, có tài trúc tốt để có thể dễ dàng thay đổi nhằm đáp ứng yêu cầu mới của doanh nghiệp.
  2. **Sự tin cậy và An toàn (Dependability and Security):** Phần mềm không được gây thiệt hại về vật chất hoặc kinh tế khi hệ thống bị lỗi; đồng thời phải chống lại được các cuộc tấn công ác ý từ bên ngoài.
  3. **Tính hiệu quả (Efficiency):** Không lãng phí tài nguyên hệ thống như bộ nhớ hay chu kỳ xử lý, thời gian phản hồi (response time) phải tối ưu.
  4. **Tính chấp nhận được (Acceptability):** Phần mềm phải dễ hiểu, hữu dụng và tương thích với các hệ thống hiện có mà người dùng đang sử dụng.

**9. Mã nguồn mở (Open Source) là gì và lợi ích của nó?**
- **Định nghĩa:** Là phần mềm có mã nguồn được công bố công khai dưới các giấy phép mã nguồn mở (như GPL, MIT, Apache). Bất kỳ ai cũng có quyền tải về, nghiên cứu, sửa đổi và phân phối lại phần mềm đó.
- **Lợi ích:** Phát triển nhanh chóng nhờ sức mạnh của cộng đồng, tính minh bạch cao (dễ phát hiện lỗi bảo mật), tiết kiệm chi phí bản quyền, và không bị khóa chặt (vendor lock-in) vào một nhà cung cấp duy nhất.

**10. Thế nào là hệ thống "Legacy" (Hệ thống di sản)? Tại sao các tổ chức vẫn dùng chúng?**
- **Định nghĩa:** Là những hệ thống phần mềm đã cũ, thường được viết bằng các ngôn ngữ lỗi thời (như COBOL, Fortran), kiến trúc nguyên khối và khó bảo trì.
- **Lý do vẫn tồn tại:** Chúng chứa đựng các quy trình nghiệp vụ cốt lõi và dữ liệu lịch sử sống còn của doanh nghiệp (ví dụ: hệ thống ngân hàng cốt lõi). Việc thay thế hoàn toàn một hệ thống Legacy mang rủi ro cực lớn về gián đoạn kinh doanh và chi phí khổng lồ, nên các tổ chức thường chọn cách "chắp vá" hoặc xây API bọc bên ngoài để duy trì.

**11. Có những loại ứng dụng phần mềm cơ bản nào? (Nêu ví dụ cụ thể)**
- **Ứng dụng Web (Web Applications):** Chạy trên trình duyệt (VD: Facebook, Shopee, hệ thống CRM nội bộ).
- **Ứng dụng Di động (Mobile Apps):** Chạy trên hệ điều hành smartphone như iOS/Android (VD: Tiktok, Grab).
- **Phần mềm Nhúng (Embedded Software):** Code được nạp thẳng vào chip để điều khiển thiết bị phần cứng (VD: Phần mềm trong máy giặt, phanh ABS của ô tô, lò vi sóng).
- **Ứng dụng Trí tuệ nhân tạo (AI Software):** Phần mềm có khả năng học máy, phân tích dữ liệu lớn (VD: ChatGPT, hệ thống nhận diện khuôn mặt).
- **Phần mềm độc lập (Stand-alone/Desktop Apps):** Chạy trực tiếp trên máy tính cá nhân (VD: MS Word, Photoshop).

**12. Đạo đức nghề nghiệp của kỹ sư phần mềm đòi hỏi điều gì về "Bảo mật thông tin" (Confidentiality)?**
- Kỹ sư phần mềm thường xuyên tiếp cận với dữ liệu nhạy cảm của khách hàng (thông tin tài chính, mật khẩu, chiến lược kinh doanh).
- **Quy tắc đạo đức:** Phải tuyệt đối tôn trọng tính bảo mật của thông tin này. Kỹ sư không được phép tiết lộ, mua bán hay sử dụng dữ liệu khách hàng cho mục đích cá nhân, ngay cả khi tổ chức không có hợp đồng bảo mật (Non-Disclosure Agreement - NDA) bằng văn bản chính thức. Đó là sự liêm chính nghề nghiệp.

**13. Lỗi phần mềm (Software Bug) thường phát sinh từ những nguyên nhân sâu xa nào?**
- **Thiếu sót trong phân tích yêu cầu:** Hiểu sai ý khách hàng, dẫn đến lập trình đúng kỹ thuật nhưng sai nghiệp vụ (lỗi này tốn kém nhất).
- **Lỗi logic lập trình:** Developer code sai thuật toán, thiếu kiểm soát vòng lặp, tràn bộ nhớ, quên xử lý ngoại lệ (Exception).
- **Thiết kế tồi:** Kiến trúc chắp vá dẫn đến khi sửa tính năng A lại làm hỏng tính năng B (lỗi hồi quy).
- **Kiểm thử không đầy đủ:** Thiếu Unit test, không test kỹ các trường hợp giá trị biên hoặc trường hợp người dùng thao tác bất thường.

**14. Việc áp dụng phương pháp tiếp cận có hệ thống (Systematic approach) mang lại những lợi ích thiết thực nào?**
- Tránh được sự hỗn loạn của tư duy "code and fix" (vừa viết vừa sửa).
- Cho phép tổ chức chia nhỏ dự án lớn thành các phần việc quản lý được (WBS - Work Breakdown Structure).
- Đảm bảo chất lượng phần mềm được kiểm soát qua từng giai đoạn (ví dụ: có review thiết kế trước khi code, có test trước khi release).
- Giúp việc luân chuyển nhân sự dễ dàng hơn (vì mọi thứ đều được tài liệu hóa và làm theo chuẩn mực chung).

**15. Thách thức lớn nhất hiện nay của chuyên ngành Công nghệ phần mềm là gì?**
- **Tính đa dạng (Heterogeneity):** Phần mềm ngày nay phải chạy trên nhiều nền tảng, thiết bị, tích hợp với vô số API của bên thứ 3 và phải liên kết mượt mà với các hệ thống cũ (Legacy).
- **Giao hàng nhanh (Delivery / Time-to-market):** Áp lực từ kinh doanh đòi hỏi phần mềm phải ra mắt cực nhanh để bắt kịp đối thủ cạnh tranh, làm giảm thời gian dành cho thiết kế và kiểm thử.
- **Sự thay đổi liên tục của doanh nghiệp (Business Change):** Yêu cầu khách hàng không bao giờ tĩnh, chúng thay đổi ngay cả khi dự án đang code.

---

## CHƯƠNG 2: QUY TRÌNH PHÁT TRIỂN PHẦN MỀM (SDLC)

**16. Vòng đời phát triển phần mềm (SDLC) bao gồm 4 hoạt động cơ bản nào?**
- Dù sử dụng bất kỳ mô hình nào (Thác nước hay Agile), mọi phần mềm đều phải trải qua 4 hoạt động lõi:
  1. **Đặc tả phần mềm (Software Specification):** Trả lời câu hỏi "Phần mềm cần làm cái gì?". Khách hàng và kỹ sư xác định các chức năng và ràng buộc của hệ thống.
  2. **Phát triển phần mềm (Software Development/Design & Implementation):** Trả lời câu hỏi "Làm như thế nào?". Bao gồm việc thiết kế kiến trúc, cấu trúc dữ liệu và viết mã nguồn (coding).
  3. **Thẩm định phần mềm (Software Validation/Testing):** Kiểm tra xem phần mềm có thỏa mãn yêu cầu của khách hàng không, phát hiện và sửa lỗi.
  4. **Tiến hóa phần mềm (Software Evolution/Maintenance):** Sửa chữa, nâng cấp phần mềm để đáp ứng các yêu cầu thay đổi trong quá trình sử dụng thực tế.

**17. Phân tích chi tiết về Mô hình Thác nước (Waterfall Model)?**
- **Khái niệm:** Là mô hình cổ điển nhất, trong đó các pha phát triển (Yêu cầu -> Thiết kế -> Lập trình -> Kiểm thử -> Triển khai) diễn ra tuần tự như dòng thác chảy từ trên xuống.
- **Đặc trưng:** Một pha phải hoàn thành 100% (và có tài liệu đóng băng/sign-off) thì mới được chuyển sang pha tiếp theo. Không có sự quay lui (hoặc quay lui rất khó khăn và tốn kém).
- **Phù hợp cho:** Các dự án có yêu cầu cực kỳ rõ ràng ngay từ đầu, ít rủi ro thay đổi, hoặc các dự án phần mềm nhúng, hệ thống an toàn sinh mạng (hàng không, y tế) cần tài liệu chứng minh nghiêm ngặt.

**18. Những nhược điểm chí mạng của Mô hình Thác nước là gì?**
- Không linh hoạt: Việc thay đổi yêu cầu ở giai đoạn giữa hoặc cuối dự án là cực kỳ tốn kém và phá vỡ cấu trúc.
- Chậm thấy sản phẩm: Khách hàng chỉ nhìn thấy phần mềm chạy được ở giai đoạn rất muộn (cuối dự án), nếu lúc đó mới phát hiện sai lệch thì coi như thất bại toàn tập.
- Ảo tưởng về sự đóng băng yêu cầu: Thực tế, khách hàng rất hiếm khi biết chính xác họ muốn gì ở đầu dự án.

**19. Mô hình Bản mẫu (Prototyping) hoạt động như thế nào và dùng khi nào?**
- **Hoạt động:** Thay vì đi làm sản phẩm thật ngay, team dev làm nhanh một bản nháp (Prototype - có thể là mockup giao diện click được, hoặc code khung) để khách hàng dùng thử. Khách hàng dùng thử sẽ đưa ra feedback. Sau khi chốt được yêu cầu từ bản mẫu, bản mẫu thường bị vứt bỏ để xây dựng hệ thống thật từ đầu.
- **Sử dụng khi:** Yêu cầu quá mơ hồ, khách hàng không rành về kỹ thuật, hoặc dự án liên quan nhiều đến trải nghiệm giao diện người dùng (UI/UX).

**20. Điểm khác biệt lớn nhất giữa mô hình Xoắn ốc (Spiral Model) với các mô hình khác?**
- Điểm sáng cốt lõi của Xoắn ốc là việc tập trung vào **Quản trị Rủi ro (Risk Analysis)**.
- Dự án được phát triển theo nhiều vòng lặp (vòng xoắn). Mỗi vòng đều có 4 pha: Lập kế hoạch, Phân tích rủi ro, Phát triển & Kiểm thử, và Đánh giá. Nếu tại bước phân tích rủi ro thấy dự án không khả thi, dự án có thể bị hủy bỏ ngay lập tức để tiết kiệm chi phí. Phù hợp với dự án lớn, phức tạp và đắt tiền.

**21. Tuyên ngôn Agile (Agile Manifesto) ra đời nhằm mục đích gì và có 4 giá trị cốt lõi nào?**
- Ra đời để khắc phục sự quan liêu, chậm chạp và quá nặng về tài liệu của các quy trình truyền thống (Thác nước).
- **4 giá trị cốt lõi:**
  1. Đề cao **Cá nhân và sự tương tác** hơn là *quy trình và công cụ*.
  2. Đề cao **Phần mềm chạy tốt** hơn là *tài liệu đầy đủ*.
  3. Đề cao **Cộng tác với khách hàng** hơn là *đàm phán hợp đồng*.
  4. Đề cao **Phản hồi với sự thay đổi** hơn là *bám sát một kế hoạch đã định*.

**22. Tại sao Mô hình Agile lại cực kỳ phù hợp với thế giới công nghệ hiện đại?**
- Môi trường kinh doanh ngày nay thay đổi theo từng ngày. Agile chia dự án thành các vòng lặp ngắn (Iterative & Incremental). 
- Ở mỗi chu kỳ (thường 2 tuần), một phần của phần mềm (có thể chạy được) sẽ được giao cho khách hàng. Điều này giúp khách hàng liên tục thấy tiến độ, dễ dàng điều chỉnh yêu cầu mới, giúp sản phẩm ra mắt thị trường nhanh (time-to-market) và tối đa hóa giá trị nghiệp vụ.

**23. Scrum là gì và nó liên quan thế nào đến Agile?**
- Agile là một triết lý (mindset), còn Scrum là một bộ khung thực hành (Framework) cụ thể và phổ biến nhất để áp dụng triết lý Agile.
- Scrum tổ chức công việc thông qua các chu kỳ nước rút gọi là **Sprint**, đảm bảo tính minh bạch, kiểm tra và thích nghi liên tục thông qua các cuộc họp định kỳ có cấu trúc chặt chẽ.

**24. Phân tích chi tiết về khái niệm "Sprint" trong Scrum?**
- Sprint là một "hộp thời gian" (Time-box) cố định, thường kéo dài từ 1 đến 4 tuần.
- Trong Sprint, nhóm cam kết hoàn thành một số yêu cầu nhất định để tạo ra một phần sản phẩm (Increment) có khả năng phát hành được.
- Khi một Sprint bắt đầu, mục tiêu của Sprint đó không được phép thay đổi. Khi Sprint kết thúc, nhóm tổ chức họp Đánh giá (Review) và Cải tiến (Retrospective) rồi lập tức bắt tay vào Sprint mới.

**25. Trình bày chi tiết về 3 vai trò (Roles) chính trong một nhóm Scrum?**
- **Product Owner (PO):** Đại diện cho tiếng nói của khách hàng/nghiệp vụ. Quyết định phần mềm sẽ có tính năng gì, sắp xếp độ ưu tiên của chúng trong Product Backlog để tối đa hóa ROI (Lợi tức đầu tư).
- **Scrum Master (SM):** Là một "người phục vụ dẫn dắt" (Servant-Leader). SM không quản lý con người mà quản lý quy trình Scrum, đảm bảo mọi người hiểu và làm đúng Scrum, loại bỏ các trở ngại (impediments) cản bước nhóm lập trình.
- **Development Team (Đội phát triển):** Các chuyên gia (Dev, QA, UI/UX) tự quản lý, tự tổ chức công việc để biến các yêu cầu trong Backlog thành sản phẩm chạy được ở cuối mỗi Sprint.

**26. Trách nhiệm sinh tử của Product Owner là gì?**
- Quản lý **Product Backlog** (Danh sách các yêu cầu). PO phải đảm bảo Backlog luôn rõ ràng, minh bạch và các tính năng mang lại giá trị cao nhất phải được đưa lên đầu để team ưu tiên làm trước. Nếu PO làm sai, team có thể code rất nhanh nhưng sản phẩm làm ra không ai cần.

**27. Một Scrum Master khác với một Project Manager (PM) truyền thống như thế nào?**
- PM truyền thống: Giao việc cho từng người, theo dõi tiến độ (timesheet), kiểm soát ngân sách, chịu trách nhiệm chính về sự thành bại của dự án.
- Scrum Master: Không giao việc (team tự nhận việc), không đánh giá KPI cá nhân. SM tập trung vào việc huấn luyện (coaching), bảo vệ team khỏi sự can thiệp của các bên ngoài trong lúc đang chạy Sprint, và tối ưu hóa môi trường làm việc.

**28. Product Backlog và Sprint Backlog khác nhau ở điểm nào?**
- **Product Backlog:** Là danh sách "ước mơ", chứa TẤT CẢ mọi yêu cầu, ý tưởng, bug của toàn bộ dự án từ đầu đến cuối. Nó do Product Owner giữ và thay đổi liên tục.
- **Sprint Backlog:** Là một danh sách công việc "thực tế", được đội Development trích xuất từ Product Backlog ra để cam kết hoàn thành TRONG MỘT SPRINT cụ thể. Khi Sprint bắt đầu, Sprint Backlog bị đóng băng (không được thêm tính năng mới).

**29. Sự kiện Daily Scrum (Họp giao ban hằng ngày) có mục đích và nguyên tắc gì?**
- **Mục đích:** Để đội phát triển đồng bộ hóa công việc, kiểm tra tiến độ hướng tới mục tiêu Sprint và điều chỉnh kế hoạch trong 24 giờ tới.
- **Nguyên tắc:** Thường họp đứng (Stand-up meeting), chỉ diễn ra tối đa 15 phút. Mỗi người trả lời 3 câu: (1) Hôm qua đã làm gì để đạt mục tiêu? (2) Hôm nay sẽ làm gì? (3) Có khó khăn rào cản nào không? Đây không phải là cuộc họp để giải quyết vấn đề kỹ thuật sâu.

**30. Quá trình RUP (Rational Unified Process) là gì và có điểm gì nổi bật?**
- RUP là một quy trình phát triển phần mềm cung cấp một bộ công cụ nghiêm ngặt hơn Agile nhưng linh hoạt hơn Thác nước.
- **Đặc trưng:** Nó dựa trên ngôn ngữ UML, lấy kiến trúc làm trung tâm (Architecture-centric), được dẫn dắt bởi Use-case (Use-case driven) và phát triển theo hướng Lặp và Tăng dần. RUP chia dự án thành 4 pha: Khởi tạo (Inception), Lập chi tiết (Elaboration), Xây dựng (Construction), và Chuyển giao (Transition).

---

## CHƯƠNG 3: YÊU CẦU PHẦN MỀM (Phần đầu)

**31. Đặc tả yêu cầu phần mềm (SRS - Software Requirements Specification) là tài liệu gì?**
- Đây là "bản hợp đồng kỹ thuật" giữa khách hàng và nhóm phát triển. Nó mô tả một cách hoàn chỉnh, nhất quán, không mơ hồ về TẤT CẢ những gì phần mềm phải thực hiện (Yêu cầu chức năng) và các giới hạn, ràng buộc mà phần mềm phải tuân thủ (Yêu cầu phi chức năng). Tài liệu này là cơ sở để thiết kế, lập trình và viết kịch bản kiểm thử (Test Case).

**32. Yêu cầu chức năng (Functional Requirement) được hiểu sâu sắc như thế nào?**
- Là các báo cáo trực tiếp về những dịch vụ mà hệ thống phải cung cấp. Nó trả lời cho câu hỏi: "Người dùng có thể làm gì với hệ thống?".
- **Ví dụ:** "Hệ thống phải cho phép người dùng đăng nhập bằng Email và Mật khẩu", "Hệ thống phải tự động tính toán tổng tiền đơn hàng bao gồm 10% thuế VAT", "Admin có quyền xóa tài khoản vi phạm".

**33. Yêu cầu phi chức năng (Non-functional Requirement) quan trọng ra sao? Hãy nêu ví dụ.**
- Nếu Yêu cầu chức năng là "Hệ thống phải làm gì", thì YC phi chức năng là "Hệ thống phải làm việc đó TỐT NHƯ THẾ NÀO". Nó bao gồm các ràng buộc về hệ thống. Đôi khi, YC phi chức năng còn quan trọng hơn chức năng, vì nếu hệ thống có đủ chức năng nhưng quá chậm hoặc không bảo mật thì sẽ bị tẩy chay.
- **Ví dụ phân loại:**
  - *Hiệu năng (Performance):* Thời gian load trang không quá 3 giây.
  - *Bảo mật (Security):* Mật khẩu phải được băm (hash) bằng SHA-256.
  - *Độ tin cậy (Reliability):* Hệ thống phải hoạt động 99.9% thời gian trong năm (Uptime).
  - *Môi trường (Environmental):* Phần mềm phải chạy được trên iOS 15 trở lên.

**34. Nêu và phân tích ưu/nhược điểm của 3 phương pháp thu thập yêu cầu phổ biến?**
1. **Phỏng vấn (Interviews):** Gặp gỡ trực tiếp (1-1 hoặc nhóm). *Ưu điểm:* Khai thác được thông tin sâu, ý kiến cá nhân. *Nhược điểm:* Tốn thời gian, người được phỏng vấn có thể nói theo cảm tính.
2. **Khảo sát bằng bảng hỏi (Questionnaires):** Phát phiếu câu hỏi cho diện rộng người dùng. *Ưu điểm:* Nhanh, thu thập được số liệu thống kê lớn. *Nhược điểm:* Câu trả lời hời hợt, không hỏi đào sâu thêm được.
3. **Quan sát thực tế (Observation / Ethnography):** BA xuống tận nơi làm việc của user để xem họ làm việc. *Ưu điểm:* Phát hiện ra những thói quen thực tế mà user quên không kể. *Nhược điểm:* Tốn rất nhiều thời gian.

**35. Tại sao bước "Nghiên cứu tính khả thi" (Feasibility Study) lại mang tính chất sống còn trước khi nhận dự án?**
- Đây là bước phân tích sơ bộ để quyết định "GO" hay "NO-GO" (Tiếp tục hay Dừng lại). 
- Cần đánh giá 3 góc độ:
  1. *Khả thi kỹ thuật:* Công nghệ hiện tại có làm được yêu cầu của khách không?
  2. *Khả thi kinh tế:* Lợi ích thu về có lớn hơn chi phí phát triển không? Dự án có đủ ngân sách không?
  3. *Khả thi thời gian:* Có kịp làm xong trước thời điểm vàng để tung ra thị trường (ví dụ: kịp dịp lễ Tết) không?
- Bỏ qua bước này dễ dẫn đến dự án "chết yểu" vì hết tiền hoặc đụng giới hạn công nghệ.

**36. Các bên liên quan (Stakeholders) thường gây ra những thảm họa gì trong việc thu thập yêu cầu?**
- **Hiểu biết mơ hồ:** Khách hàng biết họ đang có vấn đề gì, nhưng không biết phần mềm giải quyết nó thế nào, nên đưa ra yêu cầu rất mông lung ("Tôi muốn một phần mềm quản lý thông minh").
- **Xung đột quyền lợi:** Trưởng phòng A muốn luồng đi thế này, nhưng Trưởng phòng B lại muốn thế khác để có lợi cho bộ phận của họ.
- **Dùng từ lóng (Jargon):** Khách hàng dùng ngôn ngữ chuyên ngành y tế/tài chính khiến đội IT nghe không hiểu gì.
- **Thay đổi chóng mặt:** Yêu cầu đã chốt hôm qua, hôm nay khách hàng đi hội thảo về lại đổi ý muốn làm kiểu khác.

**37. Yêu cầu nghiệp vụ (Business Requirements) khác gì Yêu cầu người dùng (User Requirements)?**
- **Business Requirements (Mức cao nhất):** Mô tả mục tiêu chiến lược của công ty. Vd: "Tăng doanh số bán hàng online lên 30% trong năm nay". Nó không mô tả phần mềm làm gì.
- **User Requirements (Mức người dùng):** Mô tả các tác vụ người dùng cần làm để đạt được mục tiêu kinh doanh đó. Vd: "Người mua hàng phải dễ dàng tìm kiếm và lọc sản phẩm theo giá và thương hiệu".

**38. Đặc tả yêu cầu tốt cần đạt được những tính chất cốt lõi nào?**
- **Rõ ràng và Không mơ hồ (Unambiguous):** Chỉ có một cách hiểu duy nhất. Không dùng các từ như "nhanh", "tốt", "đẹp".
- **Đầy đủ (Complete):** Mô tả mọi kịch bản, kể cả kịch bản lỗi (ví dụ: nhập đúng thì sao, nhập sai password thì hệ thống báo gì).
- **Nhất quán (Consistent):** Yêu cầu ở trang 5 không được đá nhau/mâu thuẫn với yêu cầu ở trang 20.
- **Kiểm thử được (Testable):** Có thể viết ra một Test Case để chạy và xác nhận là Đạt hay Trượt.

**39. Kịch bản (Scenario) trong phân tích yêu cầu được sử dụng để làm gì?**
- Rất khó để khách hàng hiểu các mô hình kỹ thuật trừu tượng. Kịch bản là mô tả dạng câu chuyện về cách một người dùng thực tế tương tác với hệ thống. 
- *Cấu trúc kịch bản:* Bắt đầu bằng bối cảnh -> Hành động của người dùng -> Phản hồi của hệ thống -> Kết thúc. Điều này giúp khách hàng dễ dàng mường tượng và xác nhận xem "Câu chuyện này có đúng với thực tế không?".

**40. Phân biệt Validation (Thẩm định/Xác nhận) và Verification (Kiểm chứng) trong Quản lý Yêu cầu?**
- **Validation (Are we building the right product?):** Đi gặp khách hàng để xác nhận lại "Tài liệu SRS này đã ghi ĐÚNG và ĐỦ những gì anh/chị mong muốn chưa?". Mục đích là đảm bảo sản phẩm giải quyết đúng nỗi đau của khách hàng.
- **Verification (Are we building the product right?):** Việc nội bộ của team (BA, PM) xem xét lại tài liệu SRS xem nó có được viết đúng format công ty không, có lỗi chính tả không, các yêu cầu có đánh số thứ tự đàng hoàng chưa. Mục đích là đảm bảo tài liệu chuẩn chỉ về mặt hình thức và logic.

**41. Tại sao Verification (Kiểm chứng yêu cầu) lại quan trọng?**
- Giúp loại bỏ sớm các mâu thuẫn (VD: Yêu cầu 1 ghi "Chỉ admin được xóa tài khoản", Yêu cầu 25 lại ghi "Hệ thống tự động xóa tài khoản không đăng nhập 30 ngày"). Nếu không Verify, Developer sẽ bị bối rối và code sai logic, dẫn đến phải đập đi làm lại.

**42. Quản lý yêu cầu (Requirements Management) đóng vai trò gì trong suốt vòng đời dự án?**
- Yêu cầu KHÔNG BAO GIỜ đứng yên. Nhiệm vụ của Quản lý yêu cầu là: Khi khách hàng đòi thêm một tính năng C ở giữa dự án, hệ thống quản lý phải phân tích xem tính năng C sẽ tốn thêm bao nhiêu giờ làm, tốn bao nhiêu tiền, và nó có làm hỏng tính năng A, B đang có hay không. Từ đó mới quyết định có chấp nhận thay đổi hay không.

**43. Ma trận truy vết yêu cầu (Traceability Matrix - RTM) dùng để làm gì?**
- Là một bảng tính (thường là Excel) lập bản đồ liên kết giữa Yêu cầu gốc ban đầu với Thiết kế, Code, và Test Case.
- **Tác dụng 1:** Đảm bảo 100% yêu cầu của khách hàng đều đã được thiết kế, code và test (không bị bỏ sót).
- **Tác dụng 2:** Khi một yêu cầu thay đổi, nhìn vào ma trận sẽ biết ngay phải cập nhật những bản thiết kế nào và phải sửa những Test Case nào.

**44. "Mô hình ngôn ngữ tự nhiên" (viết đặc tả bằng lời văn bình thường) thường gặp rủi ro gì lớn nhất?**
- **Sự mơ hồ (Ambiguity):** Tiếng Việt hay Tiếng Anh đều có tính đa nghĩa. 
- **Thiếu cấu trúc:** Dễ dẫn đến viết lan man, nhầm lẫn giữa Yêu cầu (phần mềm làm gì) và Thiết kế (màn hình màu gì, đặt nút ở đâu).
- **Trộn lẫn (Confusion):** Viết gộp chung yêu cầu chức năng và phi chức năng vào một câu gây khó khăn cho việc phân tích và chia task cho lập trình viên.

**45. Giải pháp thay thế ngôn ngữ tự nhiên là Ngôn ngữ đặc tả hình thức (Formal Specification). Nó là gì?**
- Là phương pháp sử dụng các ký hiệu toán học, logic học và tập hợp để định nghĩa hệ thống. 
- *Lợi ích:* Tuyệt đối chính xác, không thể hiểu sai, có thể dùng máy tính để tự động kiểm tra tính đúng đắn của logic.
- *Hạn chế:* Rất khó học, tốn nhiều thời gian, và khách hàng (người không rành toán/IT) hoàn toàn không thể đọc hiểu để xác nhận được. Chỉ dùng cho các hệ thống mang tính sinh tử (như điều khiển tàu vũ trụ, nhà máy điện hạt nhân).

**46. Trong biểu đồ Class, dấu "-" và "+" trước thuộc tính có ý nghĩa gì?**
- **"-" (Private):** Thể hiện thuộc tính/phương thức ở trạng thái Private. Nó chỉ có thể được truy cập và chỉnh sửa bởi chính các hàm nằm bên trong class đó. Đây là nền tảng của Tính Đóng Gói (Encapsulation).
- **"+" (Public):** Thể hiện trạng thái Public. Bất kỳ đối tượng, class nào bên ngoài cũng có thể gọi phương thức hoặc xem/sửa thuộc tính này.

**47. Dấu "#" trong biểu đồ Class nghĩa là gì?**
- **"#" (Protected):** Một trạng thái trung gian giữa Private và Public. Các thuộc tính/phương thức Protected chỉ cho phép chính class đó và **các class con (kế thừa từ nó)** được phép truy cập. Các class ngoại đạo hoàn toàn không thể gọi được.

**48. Quan hệ "Composition" (Kết tập toàn phần) khác "Aggregation" (Kết tập bộ phận) như thế nào? Cung cấp ví dụ.**
- **Composition (Sống cùng sống, chết cùng chết):** Thể hiện mối quan hệ phụ thuộc cấu thành cực kỳ chặt chẽ. Nếu đối tượng cha bị hủy, các đối tượng con bên trong lập tức bị hủy theo. Ký hiệu: Hình thoi ĐEN đặc.
  - *Ví dụ:* Ngôi nhà và Căn phòng. Nếu Ngôi nhà bị phá bỏ, các Căn phòng bên trong cũng không còn tồn tại.
  - *Ví dụ IT:* Hóa đơn và Chi tiết hóa đơn.
- **Aggregation (Tập hợp lỏng lẻo):** Đối tượng con có thể tồn tại độc lập ngay cả khi đối tượng cha bị hủy. Ký hiệu: Hình thoi TRẮNG rỗng.
  - *Ví dụ:* Khoa CNTT và Giảng viên. Nếu Khoa CNTT giải thể, các Giảng viên vẫn tồn tại và có thể chuyển sang khoa khác.

**49. Sơ đồ tuần tự (Sequence Diagram) đọc theo thứ tự và trục nào?**
- Biểu đồ tuần tự được ánh xạ qua 2 chiều không gian:
  - **Trục tung (Từ trên xuống dưới):** Thể hiện sự trôi qua của thời gian. Thông điệp (Message) nào nằm bên trên sẽ được thực thi trước.
  - **Trục hoành (Từ trái sang phải):** Thể hiện danh sách các đối tượng (Objects) hoặc Actor tham gia vào quá trình tương tác, được phân tách bằng các đường đời (Lifelines).

**50. "Lifeline" (Đường đời) và "Activation box" trong Sequence Diagram mang ý nghĩa gì?**
- **Lifeline:** Là đường đứt nét thả dọc xuống dưới tên của Đối tượng. Nó biểu hiện rằng đối tượng này đang "sống" và tồn tại trong bộ nhớ tại khoảng thời gian đó. Nếu đối tượng bị hủy, lifeline sẽ kết thúc bằng dấu "X".
- **Activation box (Hộp kích hoạt):** Là một hình chữ nhật dài (hình trụ) vẽ đè lên Lifeline. Nó biểu thị khoảng thời gian chính xác mà đối tượng đó đang chiếm quyền điều khiển CPU để xử lý một hàm, chạy một thuật toán, hoặc chờ đợi phản hồi từ database.
