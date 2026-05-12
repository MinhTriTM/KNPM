# GIÁO TRÌNH TOÀN DIỆN KỸ NGHỆ PHẦN MỀM (TỔNG HỢP TỪ SLIDE BÀI GIẢNG)

> Tài liệu này được tổng hợp tự động từ toàn bộ các slide bài giảng từ Chương 0 đến Chương 7 để ôn thi chuẩn sát nhất với chương trình học.

---



<!-- BẮT ĐẦU FILE: C0_DCCT_MH_v3.md -->
LOGO

KHOA CÔNG NGHỆ & KỸ THUẬT

Nhập môn
KỸ NGHỆ
PHẦN MỀM

GV biên soạn: ThS. Trần Kim Hương

tkhuong@dthu.edu.vn

tkhuong@dthu.edu.vn

Software Engineering

GIỚI THIỆU MÔN HỌC

❖Thời lượng: 30 tiết (2TC)

▪ Lý thuyết: 30 tiết

▪ Thực hành: 0 tiết

▪ Tự học: 60 tiết

❖Công cụ học tập:

▪ StarUML

▪ C#

▪ SQL Server

tkhuong@dthu.edu.vn

MỤC TIÊU MÔN HỌC

❖ Sau khi học xong môn này sinh viên có thể:

▪ Phần mềm và công nghệ phần mềm

▪ Các quy trình phát triển phần mềm

▪ Yêu cầu chức năng và yêu cầu phi chức

▪ Lập hồ sơ phân tích yêu cầu

▪ Lập hồ sơ thiết kế phần mềm: thiết kế kiến trúc, giao diện, dữ

liệu, xử lý

▪ Các kỹ thuật lập trình, kiểm thử sản phẩm phần mềm

▪ Vận dụng kiến thức đã học để phát triển phần mềm theo yêu cầu
khách hàng và trình bày tài liệu về quy trình phát triển phần mềm.

tkhuong@dthu.edu.vn

NỘI DUNG

C1: GIỚI THIỆU VỀ CÔNG NGHỆ PHẦN MỀM

C2: QUY TRÌNH PHẦN MỀM

C3: YÊU CẦU PHẦN MỀM

C4: MÔ HÌNH HÓA PHẦN MỀM

C5: THIẾT KẾ PHẦN MỀM

C6: LẬP TRÌNH PHẦN MỀM

C7: KIỂM THỬ PHẦN MỀM

C8: QUẢN LÝ DỰ ÁN PHẦN MỀM (NC)

C9: TÍCH HỢP, CHUYỂN GIAO, BẢO TRÌ (NC)

tkhuong@dthu.edu.vn

Software Engineering

4

HÌNH THỨC ĐÁNH GIÁ

❖Kiểm tra – đánh giá thường xuyên: 0.5

▪ Chuyên cần

▪ kiểm tra trắc nghiệm

▪ Báo cáo

• 3 sv/ nhóm, thực hiện theo yêu cầu đề tài

❖Kiểm tra – đánh giá cuối kỳ: 0.5

▪ Thi tự luận (không sử dụng tài liệu)

tkhuong@dthu.edu.vn

TÀI LIỆU THAM KHẢO

❖Đỗ Văn Nhơn, Nhập môn công nghệ phần

mềm, ĐH CNTT

❖Lương Mạnh Bá, Cơ sở công nghệ phần mềm, ĐH

Bách khoa HN.

❖Pressman, Software Engineering A Practitioners

Approach, 5th Edition, McGraw Hill, 2001

❖Sommerville, Software Engineering, 8th Edition,

Addison Wesley, 2007

tkhuong@dthu.edu.vn

Câu hỏi thảo luận

tkhuong@dthu.edu.vn

Software Engineering


<!-- KẾT THÚC FILE: C0_DCCT_MH_v3.md -->

---


<!-- BẮT ĐẦU FILE: C1_GioiThieuCNPM_v2.md -->
LOGO

KHOA SƯ PHẠM TOÁN - TIN

Chương 1
GIỚI THIỆU VỀ CÔNG
NGHỆ PHẦN MỀM

GV biên soạn: Trần Kim Hương

tkhuong@dthu.edu.vn

tkhuong@dthu.edu.vn

Software Engineering

MỤC TIÊU CHƯƠNG 1

❖ Hiểu  được  tiêu  chí  đánh  giá  chất  lượng  của  phần

mềm

❖ Biết vai trò của ngành công nghệ phần mềm và nội

dung ngành công nghệ phần mềm nghiên cứu

tkhuong@dthu.edu.vn

Software Engineering

2

NỘI DUNG

PHẦN MỀM

CÔNG NGHỆ PHẦN MỀM

THẢO LUẬN

tkhuong@dthu.edu.vn

Software Engineering

3

1. PHẦN MỀM

ĐỊNH NGHĨA

VAI TRÒ

1

4

2

3

TIÊU CHÍ CỦA 1

PM TỐT

PHÂN LOẠI

tkhuong@dthu.edu.vn

Software Engineering

4

1.1 Định nghĩa (1)

❖ Bạn có thường xuyên sử dụng phần mềm không?

❖ Theo bạn, phần mềm là gì?

❖ Phần mềm khác với chương trình như thế nào?

tkhuong@dthu.edu.vn

Software Engineering

5

1.1 Định nghĩa (2)

❖ Ví dụ: xét một số phần mềm sau

▪ Phần mềm quản lý học sinh

▪ Phần mềm quản lý thư viện

▪ Phần mềm quản lý nhà sách

▪ Phần mềm quản lý khách sạn

▪ Phần mềm quản lý phòng mạch tư

▪ Phần mềm quản lý thời khóa biểu

▪ …

tkhuong@dthu.edu.vn

Software Engineering

6

Hệ thống QL học sinh – window App

tkhuong@dthu.edu.vn

Software Engineering

8

Hệ thống QL học sinh – Web App

tkhuong@dthu.edu.vn

Software Engineering

9

1.1 Định nghĩa (4)

❖ Phần mềm (software)

▪ Là  một  tập  hợp  những  câu  lệnh  được  viết  bằng  một
hoặc  nhiều  ngôn  ngữ  lập  trình  theo  một  trật  tự  xác
định nhằm tự động thực hiện một số chức năng hoặc
giải quyết một bài toán nào đó.

Phần mềm = Chương trình + Dữ liệu + Sưu liệu

Môi trường triển khai phần mềm???

-  Sưu  liệu:  đặc  tả  yêu  cầu  phần  mềm,  tài  liệu  thiết  kế,  test  cases,
hướng dẫn sử dụng,…

tkhuong@dthu.edu.vn

Software Engineering

10

1.1 Định nghĩa (5)

❖ Phần mềm dưới góc nhìn của người sử dụng:

▪ Phần  mềm  là  công  cụ  gồm  nhiều  chức  năng  hỗ  trợ
người  sử  dụng  thực  hiện  tốt  các  nghiệp  vụ  trên  máy
tính.

-

tkhuong@dthu.edu.vn

Software Engineering

11

1.1 Định nghĩa (6)

❖ Phần mềm dưới góc nhìn của chuyên viên Tin học:

▪ Phần mềm gồm 3 thành phần cơ bản:

• Thành phần giao tiếp người dùng

• Thành phần xử lý

• Thành phần lưu trữ dữ liệu

Cần được xây dựng để thực hiện theo yêu cầu của người sử dụng

tkhuong@dthu.edu.vn

Software Engineering

13

1.2 Vai trò phần mềm (1)

❖ Phần mềm thường gặp trong cuộc sống hàng ngày?

❖ Hệ thống nào được điều khiển bởi phần mềm?

❖ Phần mềm có những đặc điểm gì?

tkhuong@dthu.edu.vn

Software Engineering

14

1.2 Vai trò phần mềm (2)

❖ Ảnh hưởng gần như tất cả các khía cạnh của cuộc sống.

❖ Ngày càng nhiều  hệ thống được điều  khiển bằng phần

mềm.

❖ Ảnh hưởng đến kinh tế của các quốc gia

▪ Nền kinh tế của các nước phát triển đều phụ thuộc vào

phần mềm.

▪ Chi phí cho phần mềm chiếm một tỷ lệ quan  trọng trong

GNP của tất cả các nước phát triển.

tkhuong@dthu.edu.vn

Software Engineering

15

1.2 Vai trò phần mềm (2)

❖ Tạo nên sự khác biệt giữa các tổ chức:

▪ Phong cách

▪ Năng suất lao động

tkhuong@dthu.edu.vn

Software Engineering

16

Đặc trưng của phần mềm

❖ Không mòn cũ, nhưng thoái hóa theo thời gian

▪ Môi trường sử dụng, nhu cầu thay đổi → không dùng

▪ Lỗi phát sinh tăng do nâng cấp → quá mức

❖ Không được lắp ráp từ mẫu có sẵn:

▪ Không có danh mục chi tiết cho trước

▪ Sản phẩm đặt hàng theo từng yêu cầu riêng

tkhuong@dthu.edu.vn

Software Engineering

17

Đặc trưng của phần mềm

❖ Phức tạp, khó hiểu, vô hình:

▪ Phần mềm là hệ thống logic khó hiểu

• Nhiều khái niệm khác nhau, khó hiểu

• Mối liên kết là logic (không thấy)

• Để hiểu phải tư duy trừu tượng

▪ Không nhìn thấy

• Không phải vật thể vật lý

• Mỗi  biểu  diễn  chỉ  một  khía  cạnh  (dữ  liệu,  hành  vi,  cấu

trúc, giao diện), không phải hệ thống tổng thể

tkhuong@dthu.edu.vn

Software Engineering

18

Đặc trưng của phần mềm

❖ Thay đổi là bản chất

▪ Là mô hình thế giới thực, thay đổi theo thời gian

• Môi trường nghiệp vụ thay đổi

• Nhu cầu con người thay đổi

→Thay đổi để đáp ứng người dùng

▪ Thay đổi thích ứng với môi trường vận hành

• Các hệ phần mềm nền (hệ điều hành,…)

• Thiết bị phần cứng (chip,…)

tkhuong@dthu.edu.vn

Software Engineering

19

Đặc trưng của phần mềm

❖ Cần phát triển theo nhóm

▪ Quy mô càng lớn và yêu cầu kỹ năng khác nhau

▪ Nhu cầu bàn giao nhanh

▪ Năng xuất nhóm không tỷ lệ với số thành viên

(1 người giỏi > 5 lần người trung bình)

tkhuong@dthu.edu.vn

Software Engineering

20

1.3 Phân loại phần mềm (1)

❖ Theo  bạn,  phần  mềm  được  chia  thành  bao  nhiêu

loại?

❖ Theo cách thức hoạt động?

❖ Theo khả năng ứng dụng?

tkhuong@dthu.edu.vn

Software Engineering

21

1.3 Phân loại phần mềm (1)

❖ Theo phương thức hoạt động:

▪ Phần mềm hệ thống (System Software)

▪ Phần mềm ứng dụng (Application Software)

▪ Phần mềm công cụ (Tool)

tkhuong@dthu.edu.vn

Software Engineering

22

1.3 Phân loại phần mềm (2)

❖ Theo khả năng ứng dụng (1)

▪ Phần mềm đặt hàng: viết theo đơn đặt hàng của một

khách hàng cụ thể

• Phần mềm hỗ trợ bán hàng, phần mềm điều khiển,…

• Ưu  điểm:  có  tính  uyển  chuyển,  tùy  biến  cao  đáp  ứng

nhu cầu của một nhóm người sử dụng

• Khuyết điểm: ứng dụng trong chuyên ngành hẹp

tkhuong@dthu.edu.vn

Software Engineering

23

1.3 Phân loại phần mềm (2)

❖ Theo khả năng ứng dụng (2)

▪ Phần mềm dùng chung: có thể bán cho bất kỳ khách

hàng nào

• Hệ quản trị csdl, Microsoft office, corel, photoshop,..

• Ưu  điểm:  có  khả  năng  ứng  dụng  rộng  rãi  cho  nhiều

người

• Khuyết điểm: thiếu tính uyển chuyển tùy biến

tkhuong@dthu.edu.vn

Software Engineering

24

Tiến hóa phần mềm

❖ Giai đoạn 1: 1950 → 1960

▪ Chương trình nhỏ, tính toán chuyên dụng

▪ Ngôn ngữ: mã máy, hợp ngữ, đặc thù cho từng máy

▪ Tiêu chí đánh giá:

• Tính nhanh

• Giải được bài toán lớn (dùng bộ nhớ hiệu quả)

▪ Công nghệ: bóng điện tử (tính chậm, bộ nhớ nhỏ)

tkhuong@dthu.edu.vn

Software Engineering

25

Tiến hóa phần mềm

❖ Giai đoạn 2: → giữa thập niên 70

▪ Là sản phẩm: đa nhiệm, đa người sử dụng

▪ Xử lý số, ký tự, và thời gian thực

▪ Xuất hiện lưu trữ trực tuyến (CSDL)

▪ Ngôn ngữ có cấu trúc: PL1, Algol 60, Fortran, COBOL

▪ Tiêu chí đánh giá:

• Tính nhanh, giải được bài toán lớn

• Nhiều người dùng

▪ Công  nghệ:  bán  dẫn  (tính  nhanh  hơn,  bộ  nhớ  khác),

CSDL

tkhuong@dthu.edu.vn

Software Engineering

26

Tiến hóa phần mềm

❖ Giai đoạn 3: → 1990

▪ Phần mềm cá nhân + mạng, hệ lớn, chia sẻ được

▪ Ra đời phần mềm nhúng

▪ Xử  lý  số,  ký  tự,  âm  thanh,  hình  ảnh;  thời  gian  thực,  phân

tán, song song

▪ Truy nhập dữ liệu phát triển cả từ xa

▪ Ngôn ngữ: bậc cao, hướng đối tượng, logic

▪ Tiêu chí: tiện dụng, tin cậy và dễ bảo trì

▪ Công  nghệ:  mạch  tích  hợp  lớn,  vi  mạch,  các  cấu  hình

mạng, internet, csdl quan hệ

tkhuong@dthu.edu.vn

Software Engineering

27

Tiến hóa phần mềm

❖ Giai đoạn 1990 đến nay

▪ Phần mềm lớn, tinh vi, tin cậy, hướng người dùng

▪ Hệ  chuyên  gia,  trí  tuệ  nhân  tạo,  phần  mềm  nhúng,

webservice sử dụng rộng rãi, internet mở rộng

▪ CSDL hướng đối tượng, kho dữ liệu phát triển

▪ Ngôn ngữ: hướng đối tượng, thế hệ 4 (LIPS, PROLOG,…),

visual

▪ Tiêu chí đánh giá: tiện dụng, tinh vi, tin cậy, dễ bảo trì

▪ Công  nghệ:  vi  mạch  siêu  tích  hợp,  internet,  mạng  không

dây tốc độ cáo, hướng đối tượng, web

tkhuong@dthu.edu.vn

Software Engineering

28

1.4 Tiêu chí của một pm tốt

❖ Theo bạn, thế nào là một phần mềm tốt?

▪ Dưới góc nhìn người sử dụng?

▪ Dưới góc nhìn chuyên viên tin học?

tkhuong@dthu.edu.vn

Software Engineering

29

1.4 Tiêu chí của một phần mềm tốt (2)

tkhuong@dthu.edu.vn

Software Engineering

30

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (3)

tkhuong@dthu.edu.vn

Software Engineering

31

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (4)

tkhuong@dthu.edu.vn

Software Engineering

32

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (5)

tkhuong@dthu.edu.vn

Software Engineering

33

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (6)

tkhuong@dthu.edu.vn

Software Engineering

34

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (7)

tkhuong@dthu.edu.vn

Software Engineering

35

Dưới góc nhìn của người sử dụng

1.4 Tiêu chí của một phần mềm tốt (8)

❖ Tính dễ kiểm tra: việc kiểm tra các thành phần phù hợp với yêu cầu

phần mềm là dễ dàng nhất có thể được

❖ Tính bảo trì: các hàm xử lý bên trong phần mềm phải tổ chức sao
cho phát hiện lỗi nhanh, dễ dàng cải tiến chức năng hiện có, dễ
dàng bổ sung chức năng mới

❖ Tính tái sử dụng: các hàm xử lý bên trong phần mềm phải được tổ
chức sao cho có thể dễ dàng tái sử dụng lại (với các chức năng
khác nhau, với các phần mềm tương tự, phần mềm khác)

❖ Tính dễ mang chuyển: các hàm xử lý bên trong phần mềm phải

được tổ chức sao cho có thể dễ dàng chuyển sang môi trường công
nghệ khác

tkhuong@dthu.edu.vn

Software Engineering

Dưới góc nhìn của chuyên
viên tin học
36

1.4 Tiêu chí của một phần mềm tốt (1)

i

Mục tiêu của ngành Công nghệ phần mềm

✓ Xây dựng được phần mềm có chất lượng
✓ Dễ dàng xây dựng phần mềm mới từ các phần mềm có sẵn

cùng lớp

tkhuong@dthu.edu.vn

Software Engineering

37

BÀI TẬP

❖ Bạn hãy viết một bài mô tả về một phần mềm đang

sử dụng tại công ty/ cơ quan của mình

tkhuong@dthu.edu.vn

Software Engineering

38

Câu hỏi ôn tập

1. Định nghĩa phần mềm?

2. Tầm quan trọng của phần mềm?

3. Các đặc trưng của phần mềm và giải thích?

4. Các loại phần mềm? Giải thích nội dung mỗi loại?

5. Phân biệt chương trình và sản phẩm?

6. Để  đánh  giá  chất  lượng  của  phần  mềm,  người  ta  xem  xét

đến những yếu tố nào?

tkhuong@dthu.edu.vn

Software Engineering

39

NỘI DUNG

PHẦN MỀM

CÔNG NGHỆ PHẦN MỀM

THẢO LUẬN

tkhuong@dthu.edu.vn

Software Engineering

41

2. CÔNG NGHỆ PHẦN MỀM

❖ Bạn đã từng xây dựng phần mềm nào?

❖ Cá  nhân  hay  nhóm  xây  dựng  và  pm  cho  bạn  sử

dụng hay khách hàng?

❖ Hãy  cho  biết  những  khó  khăn  trong  quá  trình  xây

dựng phần mềm?

❖ Khi  xây  dựng  phần  mềm  bạn  phân  chia  thời  gian

như thế nào? Chi phí?

tkhuong@dthu.edu.vn

Software Engineering

42

2. CÔNG NGHỆ PHẦN MỀM

❖ Lịch sử ngành CNPM

❖ Định nghĩa

❖ Yếu tố của CNPM

tkhuong@dthu.edu.vn

Software Engineering

43

Kỹ sư PM sử dụng thời gian ?

❖ Ít hơn 10% thời gian cho việc viết code

❖ 90% thời gian còn lại cho các hoạt động:

1. Thu thập yêu cầu.

2. Phân tích yêu cầu.

3. Viết tài liệu yêu cầu phần mềm.

4. Phát triển thiết kế phần mềm.

5. Viết tài liệu thiết kế phần mềm

6. Nghiên  cứu  các  kỹ  thuật  CNPM  hay  tìm  hiểu  về  thông  tin  về

miền ứng dụng.

7. Học cách sử dụng hay cài đặt và cấu hình các công cụ phần

cứng và phần mềm mới.

tkhuong@dthu.edu.vn

Software Engineering

44

Các chi phí trong CNPM

❖ Để  xây  dựng  phần  mềm,  chúng  ta  cần  đầu  tư  cho

những hạng mục nào?

❖ Tất  cả  các  hệ  thống  phần  mềm  có  cùng  các  hạng

mục chi phí hay không? Vì sao?

❖ Chi phí phần mềm so với chi phí phần cứng?

❖ Chi phí cho vệc xây dựng so với chi phí cho việc bảo

trì

tkhuong@dthu.edu.vn

Software Engineering

45

2.1. Lịch sử của CNPM (1)

❖ Công nghệ phần mềm (CNPM)/Kỹ nghệ phần mềm

(Software Engineering).

❖ Thuật ngữ “Công nghệ phần mềm” được đưa ra tại hội
nghị do NATO tổ chức vào năm 1968 để thảo luận về
vấn đề “khủng hoảng phần mềm” (software crisis).

❖ Khủng hoảng phần mềm

▪ Khái niệm được đưa ra để chỉ những khó khăn gặp phải
trong quá trình phát triển những dự án lớn, phức tạp vào
những năm 1960.

tkhuong@dthu.edu.vn

Software Engineering

46

2.1. Lịch sử của CNPM (2)

❖ Cuộc khủng hoảng phần mềm:

▪ Số  lượng  các  phần  mềm  tăng  vọt  (do  sự  phát  triển  của

phần cứng: tăng khả năng, giá thành hạ)

▪ Có quá nhiều khuyết điểm trong các phần mềm được dùng

trong xã hội:

• Thực hiện không đúng yêu cầu (tính toán sai, không ổn định)

• Thời gian bảo trì nâng cấp quá lâu, chi phí cao, hiệu quả thấp

• Khó sử dụng

• Thực hiện chậm

• Không chuyển đổi dữ liệu giữa các phần mềm

• …

tkhuong@dthu.edu.vn

Software Engineering

47

2.1. Lịch sử của CNPM (3)

❖ Một số kết luận:

▪ Việc  tăng  vọt  số  lượng  phần  mềm  là  điều  hợp  lý  và  sẽ

còn tiếp diễn

▪ Các  khuyết  điểm  của  phần  mềm  có  nguồn  gốc  chính  từ
phương pháp, cách thức và quy trình tiến hành xây dựng
phần mềm:

• Cảm tính: mỗi người theo một phương pháp riêng

• Thô sơ, đơn giản: chỉ tập trung vào việc lập trình mà ít quan
tâm  đến  các  công  việc  cần  làm  khác  (khảo  sát  hiện  trạng,
phân tích yêu cầu, thiết kế,…)

• Thủ công: còn thiếu các công cụ hỗ trợ quy trình phát triển.

tkhuong@dthu.edu.vn

Software Engineering

48

2.2. Công nghệ phần mềm là gì?

❖ Công  nghệ  phần  mềm  là  ngành  khoa  học  nghiên
cứu  việc  xây  dựng  các  phần  mềm  có  chất  lượng
cao,  có  giá  thành  phù  hợp,  trong  khoảng  thời  gian
hợp lý.

tkhuong@dthu.edu.vn

Software Engineering

49

2.3. Các yếu tố cơ bản của SE (1)

❖ Công nghệ phần mềm nghiên cứu?

▪ Quy trình xây dựng phần mềm

▪ Phương pháp phát triển phần mềm

▪ Công cụ và môi trường phát triển phần mềm

tkhuong@dthu.edu.vn

Software Engineering

50

2.3. Các yếu tố cơ bản của SE (2)

❖ Quy  trình  xây  dựng  phần  mềm:  hệ  thống  các  giai
đoạn mà quá trình phát triển phần mềm phải trải qua

❖ Phương  pháp  phát  triển  phần  mềm:  phương  pháp
thực  hiện  cho  từng  giai  đoạn  trong  quy  trình  phát
triển phần mềm

❖ Công  cụ  và  môi  trường  phát  triển  phần  mềm:  các
phương tiện hỗ trợ tự động hay bán tự động cho một
giai  đoạn  nào  đó  trong  quá  trình  xây  dựng  phần
mềm

tkhuong@dthu.edu.vn

Software Engineering

51

Quy trình phát triển phần mềm

❖ Chương 2 sẽ phân tích tiếp

tkhuong@dthu.edu.vn

Software Engineering

52

Phương pháp phát triển phần mềm (1)

❖ Phương pháp hướng chức năng

▪ Xây dựng phần mềm dựa trên các chức năng mà hệ

thống cần thực hiện.

▪ Phương pháp chung để giải quyết vấn đề là áp dụng

nguyên lý “chia để trị”.

▪ Hạn chế: có khả năng các chức năng trong hệ thống
không tương thích với nhau khi thực hiện thay đổi các
thông tin trong hệ thống.

tkhuong@dthu.edu.vn

Software Engineering

53

Phương pháp phát triển phần mềm (2)

❖ Phương pháp hướng dữ liệu

▪ Chú trọng đến thành phần dữ liệu của hệ thống;

▪ Dùng mô hình thực thể kết hợp để biểu diễn các thực

thể và mối quan hệ giữa các thực thể.

▪ Hạn chế: phần mềm chỉ có chức năng chính là lưu trữ
và  các  thao  tác  trên  đối  tượng  dữ  liệu,  không  quan
tâm  đến  các  chức  năng  khác  của  hệ  thống  nên  hệ
thống  thu  được  sau  khi  thiết  kế  có  thể  thiếu  một  số
chức năng cần thiết

tkhuong@dthu.edu.vn

Software Engineering

54

Phương pháp phát triển phần mềm (3)

❖ Phương pháp hướng đối tượng

▪ Chú  trọng đến  thành  phần  dữ  liệu  và  chức  năng  của

hệ thống;

▪ Hệ thống phần mềm là một tập hợp các đối tượng có

khả năng tương tác với  nhau.

▪ Mỗi  đối  tượng  bao  gồm  dữ  liệu  và  các  thao  tác  thực

hiện trên dữ liệu của đối tượng.

tkhuong@dthu.edu.vn

Software Engineering

55

Công cụ và môi trường phát triển pm (1)

❖ CASE (Computer Aided Software Engineering) tools.

❖ CASE tools hỗ trợ phát sinh kết quả chuyển giao cho

giai đoạn kế tiếp.

❖ CASE tools hỗ trợ việc lưu trữ, cập nhật trên kết quả

chuyển giao

tkhuong@dthu.edu.vn

Software Engineering

56

Công cụ và môi trường phát triển pm (2)

tkhuong@dthu.edu.vn

Software Engineering

57

Công cụ và môi trường phát triển pm (3)

tkhuong@dthu.edu.vn

Software Engineering

58

http://stevereads.com/img/tire_swing_software_design.jpg

tkhuong@dthu.edu.vn

Software Engineering

59

CÂU HỎI ÔN TẬP

1) Trình bày sự ra đời của ngành công nghệ phần mềm

2) Định nghĩa công nghệ phần mềm?

3) Nêu các đối tượng (yếu tố) mà ngành CNPM nghiên cứu

tkhuong@dthu.edu.vn

Software Engineering

60

LOGO

Thank You!

tkhuong@dthu.edu.vn

62

Software Engineering


<!-- KẾT THÚC FILE: C1_GioiThieuCNPM_v2.md -->

---


<!-- BẮT ĐẦU FILE: C2_QuyTrinhPM_send.md -->
LOGO
KHOA SƯ PHẠM TOÁN - TIN
Chương 2
QUY TRÌNH
PHẦN MỀM
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

MỤC TIÊU CHƯƠNG 2
| ❖ Trình | bày      | được | một  | số   | mô hình | phát  | triển | phần |       | mềm  |
| ------- | -------- | ---- | ---- | ---- | ------- | ----- | ----- | ---- | ----- | ---- |
| cơ      | bản      |      |      |      |         |       |       |      |       |      |
| ❖ Phân  | biệt     | được | sự   | khác | nhau    | giữa  | các   | mô   | hình; | ưu   |
| và      | nhược    | điểm | của  | từng | mô      | hình  |       |      |       |      |
| ❖ Lựa   | chọn     | được | mô   | hình | phát    | triển | phù   | hợp  | với   | từng |
| loại    | hệ thống |      | phần | mềm  |         |       |       |      |       |      |
Software Engineering 2
tkhuong@dthu.edu.vn

|         | Đặt |       | vấn  |      | đề   |     |      |         |      |       |        |      |      |      |
| ------- | --- | ----- | ---- | ---- | ---- | --- | ---- | ------- | ---- | ----- | ------ | ---- | ---- | ---- |
| ❖ Hãy   |     | cho   | biết |      | để   | tạo |      | ra được |      | một   | sản    | phẩm |      | phần |
| mềm,    |     | người |      | ta   | phải |     | thực | hiện    |      | những | công   |      | việc | nào? |
| ❖ Trình |     | lại   | sơ   | lược |      | quá |      | trình   | tiến | hành  | xây    | dựng |      | phần |
| mềm     |     | từ    | khi  | nhận |      |     | yêu  | cầu     | đến  | khi   | chuyển |      | giao | sản  |
phẩm?
Software Engineering 3
tkhuong@dthu.edu.vn

NỘI DUNG
1 KHÁI NIỆM QUY TRÌNH PHẦN MỀM
2 MÔ HÌNH QUY TRÌNH PHẦN MỀM
43 HOẠT ĐỘNG CỦA QUY TRÌNH PM
34 QL THÍCH NGHI VỚI SỰ THAY ĐỔI
45 QUY TRÌNH RUP
Software Engineering 6
tkhuong@dthu.edu.vn

1. KHÁI NIỆM QUY TRÌNH PM
❖ Quy trình phần mềm(software process) là một tập có cấu trúc
| các  | hoạt  | động         | cần   | thiết để | phát  | triển | một hệ | thống | phần   | mềm.   |
| ---- | ----- | ------------ | ----- | -------- | ----- | ----- | ------ | ----- | ------ | ------ |
| ❖ Có | nhiều | quy          | trình | phần     | mềm   | khác  | nhau.  | Tuy   | nhiên, | tất cả |
| đều  | bao   | gồm          | những | hoạt     | động: |       |        |       |        |        |
| ▪    | Đặc   | tả           |       |          |       |       |        |       |        |        |
| ▪    | Phát  | triển (Thiết | kế    | và cài   | đặt)  |       |        |       |        |        |
| ▪    | Thẩm  | định         |       |          |       |       |        |       |        |        |
| ▪    | Cải   | tiến         |       |          |       |       |        |       |        |        |
Software Engineering 7
tkhuong@dthu.edu.vn

1. KHÁI NIỆM QUY TRÌNH PM
| ❖   | Những |      | hệ  | thống |     | khác | nhau | sẽ  | cần | những |     | quy | trình | phát | triển |
| --- | ----- | ---- | --- | ----- | --- | ---- | ---- | --- | --- | ----- | --- | --- | ----- | ---- | ----- |
|     | khác  | nhau |     |       |     |      |      |     |     |       |     |     |       |      |       |
❖ Ví dụ: hệ thống thời gian thực yêu cầu phải hoàn thành đặc tả
|     | hệ    | thống  |        | trước |       | khi   | chuyển               | sang |       | giai |       | đoạn | xây   | dựng   | nó.   |
| --- | ----- | ------ | ------ | ----- | ----- | ----- | -------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ------ | ----- |
|     | Nhưng |        | với    | hệ    | thống |       | thương               | mại  | điện  |      | tử,   | vừa  | đặc   | tả vừa | xây   |
|     | dựng  |        | chương |       | trình |       | một cách             | đồng |       | thời |       |      |       |        |       |
| ❖   | Tuy   | nhiên, |        | nếu   |       | không | sử                   | dụng | quy   |      | trình | phát | triển | hệ     | thống |
|     | thích |        | hợp    | có    | thể   | làm   | giảm                 | chất | lượng |      | của   | hệ   | thống | và     | tăng  |
|     | chi   | phí    | xây    | dựng. |       |       |                      |      |       |      |       |      |       |        |       |
|     |       |        |        |       |       |       | Software Engineering |      |       |      |       |      |       |        | 8     |
tkhuong@dthu.edu.vn

NỘI DUNG
1 KHÁI NIỆM QUY TRÌNH PHẦN MỀM
2 MÔ HÌNH QUY TRÌNH PHẦN MỀM
43 HOẠT ĐỘNG CỦA QUY TRÌNH PM
34 QL THÍCH NGHI VỚI SỰ THAY ĐỔI
45 QUY TRÌNH RUP
Software Engineering 9
tkhuong@dthu.edu.vn

2. MÔ HÌNH QUY TRÌNH PM
1 2
MÔ TẢ QUY TRÌNH QUY TRÌNH HOẠCH ĐỊNH
PHẦN MỀM SẴN VÀ QT LINH HOẠT
MÔ HÌNH QT PM
4 3
CÁC MÔ HÌNH QUY TRÌNH
Software Engineering 10
tkhuong@dthu.edu.vn

|     |     | 2.1 Mô |     |     | tả  |        | quy |     | trình  |     | phần |     | mềm |     |
| --- | --- | ------ | --- | --- | --- | ------ | --- | --- | ------ | --- | ---- | --- | --- | --- |
| ❖   | Khi | mô     | tả  | về  | quy | trình, |     | ta  | thường |     | nói  | về  |     |     |
▪ Các hoạt động trong những quy trình này. Ví dụ, đặc tả mô hình
|     |     | dữ  | liệu, | thiết  | kế  | giao  | diện |     | người | dùng, | …;   |       |     |     |
| --- | --- | --- | ----- | ------ | --- | ----- | ---- | --- | ----- | ----- | ---- | ----- | --- | --- |
|     | ▪   | Thứ | tự    | của    | các | hoạt  | động |     | này.  |       |      |       |     |     |
| ❖   | Các | mô  |       | tả quy |     | trình | có   | thể | gồm:  |       |      |       |     |     |
|     | ▪   | Sản | phẩm, |        | kết | quả   | đầu  | ra  | của   | một   | hoạt | động; |     |     |
▪ Vai trò, phản ánh trách nhiệm của những người tham gia vào quy
trình;
▪
Điều kiện trước và điều kiện sau (Pre- and post-conditions), là
|     |     | những |     | điều | kiện |     | phải | đảm | bảo  | trước |      | và sau | khi một | hoạt động |
| --- | --- | ----- | --- | ---- | ---- | --- | ---- | --- | ---- | ----- | ---- | ------ | ------- | --------- |
|     |     | được  |     | thực | hiện | hay | một  | sản | phẩm |       | được | tạo    | ra.     |           |
Software Engineering 11
tkhuong@dthu.edu.vn

|     | 2.2 QT hoạch |     |     |     |     |     |     | định |     | sẵn | và  | QT linh |     |     | hoạt |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- | --- | ---- | --- |
❖ Các quy trình hoạch định sẵn (plan-driven process) là các quy
|     | trình | mà  | trong   |     | đó      | tất | cả   | các  | hoạt | động |     | được |     | lên kế | hoạch |     |
| --- | ----- | --- | ------- | --- | ------- | --- | ---- | ---- | ---- | ---- | --- | ---- | --- | ------ | ----- | --- |
|     | trước |     | và tiến |     | độ thực |     | hiện | được |      | đánh | giá | dựa  |     | vào kế | hoạch |     |
này.
❖ Trong các quy trình linh hoạt (agile process), kế hoạch được
|     | phát | triển  |     | dần  | dần   | và   | dễ   | dàng  | thay  | đổi |       | quy | trình | để đáp |     | ứng |
| --- | ---- | ------ | --- | ---- | ----- | ---- | ---- | ----- | ----- | --- | ----- | --- | ----- | ------ | --- | --- |
|     | sự   | thay   | đổi | yêu  | cầu   | của  |      | khách | hàng. |     |       |     |       |        |     |     |
| ❖   | Hầu  | hết    | các | quy  | trình |      | thực | tế    | đều   | gồm | những |     | phần  | tử     | của | cả  |
|     | hai  | phương |     | pháp |       | này. |      |       |       |     |       |     |       |        |     |     |
Không có quy trình phần mềm đúng hay sai!
|     |     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     |     |     | 12  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

2.3 Các mô hình quy trình (1)
Mô hình thác nước
Mô hình hoạch định sẵn. Các pha đặc tả và phát triển phân biệt
và tách rời nhau.
Mô hình phát triển tiến hóa
Các pha đặc tả, phát triển và thẩm định đan xen nhau. Có thể là
mô hình hoạch định sẵn, có thể là mô hình linh hoạt.
Kỹ thuật phần mềm hướng tái sử dụng
Hệ thống được xây dựng từ những thành phần có sẵn. Có thể là
hoạch định sẵn, có thể là linh hoạt.
Mô hình xoắn ốc
Các pha vòng lặp có phân tích rủi ro. Có thể là hoạch định sẵn,
có thể là linh hoạt.
Software Engineering 15
tkhuong@dthu.edu.vn

| Mô  | hình | thác | nước | – Waterfall (1) |
| --- | ---- | ---- | ---- | --------------- |
Mô hình thác nước cổ điển
Software Engineering 17
tkhuong@dthu.edu.vn

| Mô  |     | hình |     |     | thác |     |     | nước |     |     | – Waterfall(2) |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | -------------- | --- |
❖ Đặc trưng:
| ▪ Các | pha   |     | diễn | ra  | tuần   | tự  | và  | độc | lập  | nhau. |        |       |
| ----- | ----- | --- | ---- | --- | ------ | --- | --- | --- | ---- | ----- | ------ | ----- |
| ▪ Kết | quả   |     | của  | mỗi | pha    | là  | đầu | vào | của  |       | pha kế | tiếp. |
| ▪ Chú | trọng |     | kiểm |     | nghiệm |     | tại | mỗi | pha. |       |        |       |
❖ Ưu điểm:
| ▪ Thực   |       | hiện | có    | hệ  | thống |      | và  | bài  | bản. |     |         |           |
| -------- | ----- | ---- | ----- | --- | ----- | ---- | --- | ---- | ---- | --- | ------- | --------- |
| ▪ Tiên   |       | liệu | chặt  | chẽ | trước |      | khi | làm. |      |     |         |           |
| ❖ Khuyết | điểm: |      |       |     |       |      |     |      |      |     |         |           |
| ▪ Khó    | khăn  |      | trong |     | việc  | thay |     | đổi  | các  | pha | đã được | thực hiện |
| → Chỉ    | thích |      | hợp   | với | dự    | án   | có  | yêu  | cầu  |     | rõ ràng |           |
Rất ít những hệ thống thương mại có yêu cầu ổn định!
Software Engineering 18
tkhuong@dthu.edu.vn

| Mô  | hình | thác | nước | – Waterfall(3) |
| --- | ---- | ---- | ---- | -------------- |
Mô hình thác nước cải tiến
Software Engineering 20
tkhuong@dthu.edu.vn

| Mô  | hình | phát | triển | tiến | hóa |
| --- | ---- | ---- | ----- | ---- | --- |
(Evolutionary development) (1)
Software Engineering 22
tkhuong@dthu.edu.vn

|     |     | Mô  |     | hình | phát |     | triển |     |     | tiến | hóa |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | ----- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
(Evolutionary development) (2)
| Có  | hai  | phương |     | pháp |     | thực         | hiện: |     |     |              |     |     |     |     |     |     |
| --- | ---- | ------ | --- | ---- | --- | ------------ | ----- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| ❖   | Phát | triển  |     | thăm | dò  | (exploratory |       |     |     | development) |     |     |     |     |     |     |
▪ Làm việc với khách hàng và từng bước phát triển từ bộ yêu cầu
|     |     | được |     | hiểu rõ | và  | bổ  | sung |     | các | tính | năng |     | mới khi | khách | hàng | yêu |
| --- | --- | ---- | --- | ------- | --- | --- | ---- | --- | --- | ---- | ---- | --- | ------- | ----- | ---- | --- |
cầu.
| ❖   | Các | phiên |     | bản | thử | nghiệm |     |     | (throw-away |     |     | prototyping) |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | ------ | --- | --- | ----------- | --- | --- | ------------ | --- | --- | --- | --- |
▪ Để hiểu các yêu cầu hệ thống: bắt đầu từ bộ yêu cầu không được
|     |     | hiểu   | rõ,   | để làm   |     | rõ đâu | là    | cái    | thực   |     | sự được |     | yêu cầu.    |     |     |     |
| --- | --- | ------ | ----- | -------- | --- | ------ | ----- | ------ | ------ | --- | ------- | --- | ----------- | --- | --- | --- |
| ❖   | Đặc | trưng: |       |          |     |        |       |        |        |     |         |     |             |     |     |     |
|     | ▪   | Phát   | triển | nhanh    |     | các    | phiên |        | bản    | thử | nghiệm  |     | (prototype) |     |     |     |
|     | ▪   | Nhận   |       | phản hồi |     | khách  | hàng  |        | thường |     | xuyên.  |     |             |     |     |     |
|     | ▪   | Không  |       | đặt nặng |     | tiên   | liệu  | trước. |        |     |         |     |             |     |     |     |
▪
|     |     | Cải | tiến | dần | phiên |     | bản | thử                  | nghiệm |     | thành | bản | chính | thức. |     |     |
| --- | --- | --- | ---- | --- | ----- | --- | --- | -------------------- | ------ | --- | ----- | --- | ----- | ----- | --- | --- |
|     |     |     |      |     |       |     |     | Software Engineering |        |     |       |     |       |       |     | 23  |
tkhuong@dthu.edu.vn

| Mô  | hình |     | phát |     |     | triển |     | tiến | hóa |     |     |
| --- | ---- | --- | ---- | --- | --- | ----- | --- | ---- | --- | --- | --- |
(Evolutionary development) (3)
❖ Ưu điểm:
| ▪ Yêu       | cầu   | ban   | đầu   | không |      | cần   | rõ   | ràng     | và    | ổn định. |       |
| ----------- | ----- | ----- | ----- | ----- | ---- | ----- | ---- | -------- | ----- | -------- | ----- |
| ▪ Thích     | ứng   | tốt   | với   | thay  |      | đổi.  |      |          |       |          |       |
| ❖ Khuyết    | điểm: |       |       |       |      |       |      |          |       |          |       |
| ▪ Tính      | quy   | trình | không |       | thể  | hiện  |      | rõ ràng  |       |          |       |
| ▪ Cấu       | trúc  | hệ    | thống | bị    | giảm | khi   |      | có yêu   | cầu   | thay     | đổi   |
| ❖ Ứng dụng: |       |       |       |       |      |       |      |          |       |          |       |
| ▪ Các       | hệ    | thống | kích  | thước |      | nhỏ   |      | và trung | bình; |          |       |
| ▪ Một       | phần  | của   | hệ    | thống |      | lớn   | (vd: | giao     | diện  | người    | dùng) |
| ▪ Các       | hệ    | thống | chỉ   | dùng  |      | trong | thời | gian     | ngắn. |          |       |
Software Engineering 24
tkhuong@dthu.edu.vn

CNPM HƯỚNG TÁI SỬ DỤNG - Reuse-
oriented software engineering (1)
Software Engineering 25
tkhuong@dthu.edu.vn

|     | CNPM HƯỚNG TÁI SỬ DỤNG - |     |     |     |     |     |     |     | Reuse- |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
oriented software engineering (2)
| ❖ Dựa | vào   | việc     | tái     | sử    | dụng một                    | cách     | có    | hệ thống |      |        |      |
| ----- | ----- | -------- | ------- | ----- | --------------------------- | -------- | ----- | -------- | ---- | ------ | ---- |
| ▪     | Các   | hệ thống |         | được  | tích hợp                    | từ những |       | thành    | phần | có sẵn | hoặc |
|       | từ    | các hệ   | thống   | COTS  | (Commercial-off-the-shelf). |          |       |          |      |        |      |
| ❖ Các | pha   | trong    | quy     | trình |                             |          |       |          |      |        |      |
| ▪     | Phân  | tích     | thành   | phần  | sẵn có                      |          |       |          |      |        |      |
| ▪     | Điều  | chỉnh    | yêu     | cầu;  |                             |          |       |          |      |        |      |
| ▪     | Thiết | kế hệ    | thống   | với   | kỹ thuật                    | tái sử   | dụng; |          |      |        |      |
| ▪     | Phát  | triển    | và tích | hợp   | hệ thống                    |          |       |          |      |        |      |
Hiện nay, việc tái sử dụng là phương pháp chuẩn cho việc
xây dựng nhiều loại hệ thống thương mại.
|     |     |     |     |     | Software Engineering |     |     |     |     |     | 26  |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|     | Mô   | hình  | tăng |      | dần  |      | (Incremental delivery) (1) |       |        |       |      |       |     |      |      |     |     |
| --- | ---- | ----- | ---- | ---- | ---- | ---- | -------------------------- | ----- | ------ | ----- | ---- | ----- | --- | ---- | ---- | --- | --- |
| ❖   | Hệ   | thống | sẽ   | được |      | chia |                            | thành |        | nhiều |      | vòng, |     |      | tăng | dần |     |
|     | thay | gì    | phải | xây  | dựng |      |                            | và    | chuyển |       | giao |       | một |      | lần. | Mỗi |     |
|     | vòng | là    | một  | kết  | quả  |      | của                        |       | một    | chức  |      | năng  |     | được |      | yêu |     |
cầu
| ❖   | Yêu   | cầu   | nào | có   | thứ |                      | tự  | ưu    | tiên |     | càng | cao |     | thì | càng |     | ở   |
| --- | ----- | ----- | --- | ---- | --- | -------------------- | --- | ----- | ---- | --- | ---- | --- | --- | --- | ---- | --- | --- |
|     | trong | những |     | vòng |     | phát                 |     | triển | sớm  |     | hơn  |     |     |     |      |     |     |
|     |       |       |     |      |     | Software Engineering |     |       |      |     |      |     |     |     |      |     | 30  |
tkhuong@dthu.edu.vn

| Mô  | hình | tăng | dần | (Incremental delivery) (2) |
| --- | ---- | ---- | --- | -------------------------- |
Software Engineering 31
tkhuong@dthu.edu.vn

| Mô   | hình  |       | tăng |       |      | dần   | (Incremental delivery) (3) |      |     |      |          |         |       |
| ---- | ----- | ----- | ---- | ----- | ---- | ----- | -------------------------- | ---- | --- | ---- | -------- | ------- | ----- |
| ❖ Ưu | điểm: |       |      |       |      |       |                            |      |     |      |          |         |       |
| ▪    | Khách |       | hàng |       | sớm  |       | thấy                       | được |     | chức | năng     | của hệ  | thống |
|      | sau   | mỗi   |      | lần   | tăng | vòng. |                            |      |     |      |          |         |       |
| ▪    | Các   | vòng  |      | trước |      | sẽ    | là                         | mẫu  | thử | để   | tìm hiểu | các yêu | cầu   |
|      | cho   | những |      |       | vòng | tiếp  | theo.                      |      |     |      |          |         |       |
| ▪    | Những |       | chức |       | năng |       | có                         | độ   | ưu  | tiên | càng     | cao sẽ  | được  |
|      | kiểm  |       | thử  | càng  |      | kỹ    |                            |      |     |      |          |         |       |
Software Engineering 32
tkhuong@dthu.edu.vn

| Mô  | hình | xoắn | ốc  | - Spiral development (1) |
| --- | ---- | ---- | --- | ------------------------ |
Software Engineering 34
tkhuong@dthu.edu.vn

|     |     | Mô   |       | hình      |      | xoắn |       | ốc    |      | - Spiral development (2) |        |      |      |      |      |           |     |
| --- | --- | ---- | ----- | --------- | ---- | ---- | ----- | ----- | ---- | ------------------------ | ------ | ---- | ---- | ---- | ---- | --------- | --- |
| ❖   | Các |      | pha   | trong     |      | quy  |       | trình | phát |                          | triển  | xoắn |      | ốc:  |      |           |     |
|     | ▪   | Lập  |       | kế hoạch: |      |      | xác   | định  |      | mục                      | tiêu,  | các  |      | giải | pháp | và        | các |
|     |     | ràng |       | buộc      |      |      |       |       |      |                          |        |      |      |      |      |           |     |
|     | ▪   | Phân |       | tích      | rủi  | ro:  | phân  |       | tích | các                      | phương |      |      | án   | và   | xác định/ |     |
|     |     | giải |       | quyết     | rủi  | ro   |       |       |      |                          |        |      |      |      |      |           |     |
|     | ▪   | Kỹ   | nghệ: |           | phát |      | triển | sản   |      | phẩm                     | mức    |      | tiếp | theo |      |           |     |
|     | ▪   | Đánh |       | giá:      | đánh |      | giá   | của   |      | khách                    | hàng   |      | về   | kết  | quả  | của       | kỹ  |
nghệ
|     |     |     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     |     |     | 35  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|     | Mô  | hình |     | xoắn |     | ốc  |     | - Spiral development (3) |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ---- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Ưu điểm
| ▪   | Hiểu | rõ   | và  | giải quyết |     | tốt   | các |     | nguy | cơ   | tại | mỗi   | mức |     | tiến   | hóa |
| --- | ---- | ---- | --- | ---------- | --- | ----- | --- | --- | ---- | ---- | --- | ----- | --- | --- | ------ | --- |
| ▪   | Áp   | dụng | bản | mẫu        |     | tại   | bất | cứ  | giai | đoạn |     | tiến  | hóa | nào |        |     |
| ▪   | Giảm | được |     | nguy       | cơ  | trước |     |     | khi  | nó   | trở | thành | vấn |     | đề của | hệ  |
thống
| ❖ Khuyết |      | điểm   |       |          |       |                      |      |      |       |       |       |          |     |     |          |        |
| -------- | ---- | ------ | ----- | -------- | ----- | -------------------- | ---- | ---- | ----- | ----- | ----- | -------- | --- | --- | -------- | ------ |
| ▪        | Khó  | thuyết |       | phục     | khách |                      | hàng |      | rằng  |       | cách  | tiếp     | cận |     | tiến hóa | là     |
|          | kiểm | soát   | được. |          |       |                      |      |      |       |       |       |          |     |     |          |        |
| ▪        | Cần  | tri    | thức  | chuyên   |       | gia                  |      | đánh |       | giá   | rủi   | ro chính |     | xác | và       | dựa    |
|          | trên | chuyên |       | gia      | để    | đạt                  | được |      | thành |       | công. |          |     |     |          |        |
| ▪        | Cần  | năng   |       | lực quản |       | lý                   | cao, |      | nếu   | không |       | quản     | lý  | tốt | sẽ       | dễ rơi |
|          | vào  | trạng  | thái  | sửa      |       | đổi                  | cục  | bộ   | không |       | kế    | hoạch    |     |     |          |        |
|          |      |        |       |          |       | Software Engineering |      |      |       |       |       |          |     |     |          | 36     |
tkhuong@dthu.edu.vn

NỘI DUNG
1 KHÁI NIỆM QUY TRÌNH PHẦN MỀM
2 MÔ HÌNH QUY TRÌNH PHẦN MỀM
43 HOẠT ĐỘNG CỦA QUY TRÌNH PM
34 QL THÍCH NGHI VỚI SỰ THAY ĐỔI
45 QUY TRÌNH RUP
Software Engineering 37
tkhuong@dthu.edu.vn

3. HOẠT ĐỘNG QUY TRÌNH PM
ĐẶC TẢ
CẢI TIẾN PHÁT TRIỂN
THẨM ĐỊNH
❖ Trong mô hình thác nước, chúng được tổ chức tuần tự
❖ Trong mô hình phát triển tiến hóa chúng được tổ chức đan xen
Software Engineering 38
tkhuong@dthu.edu.vn

3. HOẠT ĐỘNG QUY TRÌNH PM
| ❖ Mục  | tiêu: |       |       |       |      |      |                      |         |      |      |        |       |       |
| ------ | ----- | ----- | ----- | ----- | ---- | ---- | -------------------- | ------- | ---- | ---- | ------ | ----- | ----- |
| ▪ Xác  | định  |       | rõ    | những |      |      | công                 | việc    | cần  | phải | làm    | trong | quy   |
| trình  | phát  |       | triển |       | phần |      | mềm                  |         |      |      |        |       |       |
| ▪ Từng |       | công  |       | việc  |      | đó   | được                 | thực    | hiện | cụ   | thể ra | sao   |       |
| → Xây  |       | dựng  |       | bất   | kỳ   | phần |                      | mềm     | nào  | cũng | phải   | thực  | hiện  |
| 4 công |       | việc, |       | nhưng |      | việc |                      | sử dụng | các  | mô   | hình   | phát  | triển |
| phần   | mềm   |       | khác  |       | nhau |      | thì                  | trình   | tự   | thực | hiện   | các   | công  |
| việc   | trên  | cũng  |       | khác  |      | nhau |                      |         |      |      |        |       |       |
|        |       |       |       |       |      |      | Software Engineering |         |      |      |        |       | 39    |
tkhuong@dthu.edu.vn

|       | Đặt | vấn  |       | đề  |      |        |     |         |      |       |
| ----- | --- | ---- | ----- | --- | ---- | ------ | --- | ------- | ---- | ----- |
| ❖Công |     | việc |       | đầu | tiên | cần    | làm | trong   | quá  | trình |
| xây   |     | dựng | phần  |     | mềm  | là gì? |     |         |      |       |
| ❖Tầm  |     | quan | trọng |     | của  | việc   | đặc | tả phần | mềm? |       |
Software Engineering 40
tkhuong@dthu.edu.vn

|     |      | 3.1 Đặc  |       |     | tả     | phần |      | mềm  |              | (1)       |      |              |
| --- | ---- | -------- | ----- | --- | ------ | ---- | ---- | ---- | ------------ | --------- | ---- | ------------ |
| ❖   | Là   | quy      | trình | tìm |        | hiểu | và   | định | nghĩa        | những     | dịch | vụ nào       |
|     | được | yêu      | cầu   |     | và     | các  | ràng | buộc | trong        | quá trình |      | vận hành     |
|     | và   | xây dựng |       | hệ  | thống. |      |      |      |              |           |      |              |
| ❖   | Quy  | trình    | xác   |     | định   | yêu  | cầu: |      |              |           |      |              |
|     |      |          |       |     |        |      |      |      | Text in here |           |      | Text in here |
Requirements
|     | Feasibility study |     |     |     |     |     |     |     | Requirements  |     | Requirements |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- |
elicitation and
|     |     |     |     |     |     |     |     |     | specificatio |     |     |  validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----------- |
analysis
• Nghiên cứu khả thi: • Thu thập và phân tích  • Đặc tả yêu cầu:  • Thẩm định yêu cầu:
yêu cầu:
• Ước lượng xem những  •Định nghĩa chi tiết các  • Kiểm tra tính hợp lệ của
yêu cầu của người dùng  • Các stackholder hệ  yêu cầu.  yêu cầu.
| có khả thi về mặt kỹ       |     |     |     |     | thống yêu cầu và mong  |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| thuật và tài chính để xây  |     |     |     |     | muốn gì từ hệ thống?   |     |     |     |     |     |     |     |
dựng nên hệ thống hay
không
Software Engineering 41
tkhuong@dthu.edu.vn

| 3.1 Đặc | tả phần | mềm | (2) |
| ------- | ------- | --- | --- |
Quy trình xác định yêu cầu
Software Engineering 43
tkhuong@dthu.edu.vn

|       | Đặt    | vấn  | đề   |       |         |          |          |      |      |     |
| ----- | ------ | ---- | ---- | ----- | ------- | -------- | -------- | ---- | ---- | --- |
| ❖ Bỏ  | qua    | giai | đoạn | thiết | kế, sau | khi đặc  | tả và    | phân | tích |     |
| yêu   | cầu,   | có   | thể  | thực  | hiện    | cài đặt  | hệ thống |      | ngay |     |
| được  | không? |      |      |       |         |          |          |      |      |     |
| ❖ Vai | trò    | của  | bản  | thiết | kế đối  | với giai | đoạn     | cài  | đặt  | là  |
gì?
|     |     |     |     |     | Software Engineering |     |     |     |     | 44  |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|     |       | 3.2 Thiết |      |     |     | kế  | và        | cài |         | đặt | phần |     | mềm |     | (1) |
| --- | ----- | --------- | ---- | --- | --- | --- | --------- | --- | ------- | --- | ---- | --- | --- | --- | --- |
| ❖   | Thiết | kế        | phần |     |     | mềm | (software |     | design) |     |      |     |     |     |     |
▪
|     |     | Là    | quá              | trình |       | thiết     |       | kế cấu               | trúc     | của   | phần |     | mềm   | dựa | trên |
| --- | --- | ----- | ---------------- | ----- | ----- | --------- | ----- | -------------------- | -------- | ----- | ---- | --- | ----- | --- | ---- |
|     |     | những |                  | tài   | liệu  | đặc       | tả.   |                      |          |       |      |     |       |     |      |
|     | ▪   | Hoạt  | động             |       | thiết | kế        | gồm:  |                      |          |       |      |     |       |     |      |
|     |     | •     | Thiết            | kế    | kiến  | trúc      |       |                      |          |       |      |     |       |     |      |
|     |     | •     | Thiết            | kế    | giao  | diện      |       |                      |          |       |      |     |       |     |      |
|     |     | •     | Thiết            | kế    | xử    | lý (thuật |       | toán)                |          |       |      |     |       |     |      |
|     |     | •     | Thiết            | kế    | lưu   | trữ       | (cấu  | trúc                 | dữ liệu) |       |      |     |       |     |      |
| ❖   | Cài | đặt   | (implementation) |       |       |           |       |                      |          |       |      |     |       |     |      |
|     | ▪   | Dịch  | cấu              |       | trúc  | đó        | thành | chương               |          | trình | thực | thi | được. |     |      |
|     |     |       |                  |       |       |           |       | Software Engineering |          |       |      |     |       |     | 45   |
tkhuong@dthu.edu.vn

| 3.2 Thiết | kế và | cài | đặt | phần | mềm | (2) |
| --------- | ----- | --- | --- | ---- | --- | --- |
Mô hình chung của quy trình thiết kế
|     | Software Engineering |     |     |     |     | 47  |
| --- | -------------------- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|       | Đặt     | vấn     | đề      |                      |        |        |            |      |
| ----- | ------- | ------- | ------- | -------------------- | ------ | ------ | ---------- | ---- |
| ❖ Sau | khi     | cài đặt | phần    | mềm,                 | chúng  | ta có  | thể chuyển | giao |
| ngay  | cho     | người   | sử dụng | được                 | không? |        |            |      |
| ❖ Vai | trò của | việc    | đánh    | giá phần             | mềm    | là gì? |            |      |
|       |         |         |         | Software Engineering |        |        |            | 49   |
tkhuong@dthu.edu.vn

|     | 3.3 Thẩm |     |     |     | định |     | phần |     | mềm | (1)  |     |
| --- | -------- | --- | --- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
❖ Xác minh (verification) và thẩm định (validation) (V & V) nhằm
| mục |      | đích | chỉ   | ra rằng |      |      |       |        |         |     |     |
| --- | ---- | ---- | ----- | ------- | ---- | ---- | ----- | ------ | ------- | --- | --- |
| ▪   | Một  | hệ   | thống | đã      | thực | hiện | theo  | đặc tả | của nó; |     |     |
| ▪   | Thỏa |      | mãn   | mọi yêu | cầu  | của  | khách | hàng.  |         |     |     |
❖
| Bao   |     | gồm     | các | quy       | trình | kiểm |     | tra, xem | xét lại | và kiểm | thử hệ |
| ----- | --- | ------- | --- | --------- | ----- | ---- | --- | -------- | ------- | ------- | ------ |
| thống |     | (system |     | testing). |       |      |     |          |         |         |        |
Software Engineering 50
tkhuong@dthu.edu.vn

| 3.3 Thẩm | định | phần | mềm | (2)  |
| -------- | ---- | ---- | --- | ---- |
Quy trình kiểm thử
Software Engineering 52
tkhuong@dthu.edu.vn

|       | Đặt  | vấn    | đề       |        |          |           |         |         |
| ----- | ---- | ------ | -------- | ------ | -------- | --------- | ------- | ------- |
| ❖ Sau | khi  | chuyển | giao     | phần   | mềm      | cho khách | hàng,   | thì mọi |
| công  | việc | đã     | kết thúc | chưa?  |          |           |         |         |
| ❖ Cải | tiến | phần   | mềm      | để làm | gì?      |           |         |         |
| ❖ Tại | sao  | không  | xây      | dựng   | hệ thống | mới mà    | lại cải | tiến hệ |
| thống | cũ?  |        |          |        |          |           |         |         |
Software Engineering 54
tkhuong@dthu.edu.vn

|     |       | 3.4 Cải |        |     | tiến   |     |       | phần                 |          | mềm |      |      | (1)  |        |     |      |
| --- | ----- | ------- | ------ | --- | ------ | --- | ----- | -------------------- | -------- | --- | ---- | ---- | ---- | ------ | --- | ---- |
| ❖   | Khi   | các     | yêu    |     | cầu    | hệ  | thống |                      | thay     | đổi |      | theo | sự   | thay   | đổi | của  |
|     | các   | yêu     | cầu    |     | nghiệp |     | vụ    | thì                  | phần     | mềm |      | phải | cải  | tiến   | và  | thay |
|     | đổi   | để      | hỗ     | trợ | khách  |     | hàng. |                      |          |     |      |      |      |        |     |      |
| ❖   | Thông |         | thường |     | chi    |     | phí   | để                   | bảo      | trì | và   | cải  | tiến | thường |     | đắt  |
|     | hơn   | nhiều   |        | so  | với    | chi | phí   |                      | xây dựng |     | phần |      | mềm. |        |     |      |
|     |       |         |        |     |        |     |       | Software Engineering |          |     |      |      |      |        |     | 55   |
tkhuong@dthu.edu.vn

| 3.4 Cải | tiến | phần | mềm | (2) |
| ------- | ---- | ---- | --- | --- |
Quy trình cải tiến hệ thống
Software Engineering 56
tkhuong@dthu.edu.vn

|     |     | Tổng |     |     | kết | (1) |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Quy trình phần mềm là một tập có cấu trúc các hoạt động cần
|     | thiết |      | để     | phát | triển | một   | hệ thống             | phần |      | mềm.  |      |       |      |      |     |
| --- | ----- | ---- | ------ | ---- | ----- | ----- | -------------------- | ---- | ---- | ----- | ---- | ----- | ---- | ---- | --- |
| ❖   | Mô    | hình |        | quy  | trình | phần  | mềm                  | là   | biểu | diễn  | trừu | tượng |      | của  | một |
|     | quy   |      | trình. |      |       |       |                      |      |      |       |      |       |      |      |     |
| ❖   | Các   |      | mô     | hình | quy   | trình | tổng                 | quát | mô   | tả    | tổ   | chức  | của  | các  | quy |
|     | trình |      | phần   | mềm. |       |       |                      |      |      |       |      |       |      |      |     |
|     | ▪     | Ví   | dụ:    | Mô   | hình  | thác  | nước,                | mô   | hình |       | phát | triển | tiến | hóa, | mô  |
|     |       | hình |        | phát | triển | theo  | hướng                | tái  | sử   | dụng. |      |       |      |      |     |
|     |       |      |        |      |       |       | Software Engineering |      |      |       |      |       |      |      | 59  |
tkhuong@dthu.edu.vn

|     | Tổng |     |     | kết | (2) |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖
| Công |     | nghệ | yêu | cầu | là quy | trình | phát | triển | đặc | tả phần | mềm. |     |
| ---- | --- | ---- | --- | --- | ------ | ----- | ---- | ----- | --- | ------- | ---- | --- |
❖ Quy trình thiết kế và cài đặt liên quan đến việc chuyển đổi một
| đặc | tả  | yêu | cầu | thành | hệ  | thống | phần | mềm | chạy | được. |     |     |
| --- | --- | --- | --- | ----- | --- | ----- | ---- | --- | ---- | ----- | --- | --- |
❖ Thẩm định phần mềm là quy trình kiểm tra rằng hệ thống thỏa
| mãn   |      | đặc       | tả và | đáp | ứng                  | được | nhu     | cầu  | thực | của      | người | sử  |
| ----- | ---- | --------- | ----- | --- | -------------------- | ---- | ------- | ---- | ---- | -------- | ----- | --- |
| dụng  |      | hệ thống. |       |     |                      |      |         |      |      |          |       |     |
| ❖ Cải | tiến | phần      |       | mềm | xảy                  | ra   | khi bạn | thay | đổi  | hệ thống | phần  |     |
| mềm   |      | có sẵn    | để    | đáp | ứng                  | các  | yêu cầu | mới. |      |          |       |     |
|       |      |           |       |     | Software Engineering |      |         |      |      |          |       | 60  |
tkhuong@dthu.edu.vn

NỘI DUNG
1 KHÁI NIỆM QUY TRÌNH PHẦN MỀM
2 MÔ HÌNH QUY TRÌNH PHẦN MỀM
43 HOẠT ĐỘNG CỦA QUY TRÌNH PM
34 QL THÍCH NGHI VỚI SỰ THAY ĐỔI
45 QUY TRÌNH RUP
Software Engineering 61
tkhuong@dthu.edu.vn

4. THÍCH NGHI VỚI SỰ THAY ĐỔI
| ❖   | Sự  | thay | đổi | là điều | hiển |     | nhiên | trong | những | dự  | án phần | mềm |
| --- | --- | ---- | --- | ------- | ---- | --- | ----- | ----- | ----- | --- | ------- | --- |
lớn
▪ Những thay đổi thương mại dẫn đến việc thay đổi yêu cầu hoặc
|     | phát   |     | sinh | những    | yêu  | cầu    | mới. |         |            |     |      |     |
| --- | ------ | --- | ---- | -------- | ---- | ------ | ---- | ------- | ---------- | --- | ---- | --- |
|     | ▪ Công |     | nghệ | mới      | mở   | ra khả | năng | cải     | thiện việc | cài | đặt. |     |
|     | ▪ Thay |     | đổi  | platform | đòi  | hỏi    | thay | đổi ứng | dụng.      |     |      |     |
| ❖   | Thay   | đổi | dẫn  | đến      | việc | làm    | lại  |         |            |     |      |     |
▪ Vì vậy chi phí của việc thay đổi gồm cả chi phí làm lại và chi phí
|     | cài | đặt | tính | năng | mới. |     |                      |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | ---- | --- | -------------------- | --- | --- | --- | --- | --- |
|     |     |     |      |      |      |     | Software Engineering |     |     |     |     | 62  |
tkhuong@dthu.edu.vn

|     | Giảm  |       |      | thiểu   |     | chi phí    |          | làm  | lại |       |     |         |
| --- | ----- | ----- | ---- | ------- | --- | ---------- | -------- | ---- | --- | ----- | --- | ------- |
| ❖   | Tránh | thay  | đổi  | (change |     | avoidance) |          |      |     |       |     |         |
|     | ▪ Quy | trình | phần | mềm     |     | gồm        | các hoạt | động | mà  | nó có | thể | dự đoán |
trước những thay đổi có thể xảy ra khi việc làm lại được yêu cầu.
▪ Ví dụ: hệ thống nguyên mẫu (prototype system) có thể dùng để
|     | cho  | khách |      | hàng | xem     | những | tính năng  | chính | của | hệ  | thống. |     |
| --- | ---- | ----- | ---- | ---- | ------- | ----- | ---------- | ----- | --- | --- | ------ | --- |
| ❖   | Chấp | nhận  | thay | đổi  | (change |       | tolerance) |       |     |     |        |     |
▪ Quy trình được thiết kế sao cho thay đổi được thực hiện với chi
|     | phí      | khá | thấp. |      |     |      |        |      |      |     |              |     |
| --- | -------- | --- | ----- | ---- | --- | ---- | ------ | ---- | ---- | --- | ------------ | --- |
|     | ▪ Thường |     | sử    | dụng | mô  | hình | chuyển | giao | tăng | dần | (incremental |     |
delivery).
Software Engineering 63
tkhuong@dthu.edu.vn

|     | 4.1 Nguyên |     |     |     | mẫu |     | phần |     | mềm |     | (prototype) |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ----------- | --- | --- |
❖ Một nguyên mẫu (prototype) là phiên bản đầu tiên của một hệ
| thống |     | được  | dùng |     | để demo |     | những |     | khái | niệm | và thử | các | tùy |
| ----- | --- | ----- | ---- | --- | ------- | --- | ----- | --- | ---- | ---- | ------ | --- | --- |
| chọn  |     | thiết | kế.  |     |         |     |       |     |      |      |        |     |     |
❖
| Một |     | nguyên | mẫu | có  | thể | được |     | sử  | dụng | trong | các trường |     | hợp |
| --- | --- | ------ | --- | --- | --- | ---- | --- | --- | ---- | ----- | ---------- | --- | --- |
sau:
▪ Trong quy trình công nghệ yêu cầu để giúp cho quá trình thu thập
|     | yêu | cầu | và thẩm |     | định | yêu | cầu; |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
▪ Trong quy trình thiết kế để tìm ra các tùy chọn và phát triển thiết
|     | kế    | giao | diện người |      | dùng; |                      |         |     |      |     |     |     |     |
| --- | ----- | ---- | ---------- | ---- | ----- | -------------------- | ------- | --- | ---- | --- | --- | --- | --- |
| ▪   | Trong |      | quy trình  | kiểm | thử   |                      | để chạy | các | kiểm | thử |     |     |     |
|     |       |      |            |      |       | Software Engineering |         |     |      |     |     |     | 64  |
tkhuong@dthu.edu.vn

|     | 3.1 Nguyên |      |       |        |       | mẫu  |         | phần |           | mềm       | (prototype) |
| --- | ---------- | ---- | ----- | ------ | ----- | ---- | ------- | ---- | --------- | --------- | ----------- |
| ❖   | Lợi        | ích  | của   | nguyên |       | mẫu: |         |      |           |           |             |
|     | ▪          | Cải  | thiện | khả    | năng  |      | sử dụng |      | hệ        | thống.    |             |
|     | ▪          | Thoả | mãn   | tốt    | hơn   | nhu  |         | cầu  | thực      | của người | dùng.       |
|     | ▪          | Cải  | thiện | chất   | lượng |      | thiết   | kế.  |           |           |             |
|     | ▪          | Cải  | thiện | khả    | năng  |      | bảo     | trì  | hệ thống. |           |             |
|     | ▪          | Giảm | bớt   | nỗ     | lực   | phát | triển.  |      |           |           |             |
Software Engineering 65
tkhuong@dthu.edu.vn

|     | 3.1 Nguyên |          |        |       |       | mẫu  |      | phần    |        | mềm     |      | (prototype) |      |      |         |
| --- | ---------- | -------- | ------ | ----- | ----- | ---- | ---- | ------- | ------ | ------- | ---- | ----------- | ---- | ---- | ------- |
| ❖   | Phát       | triển    | nguyên |       |       | mẫu: |      |         |        |         |      |             |      |      |         |
|     | ▪          | Có thể   | dựa    |       | vào   |      | các  | công    | cụ     | và ngôn |      | ngữ         | để   | phát | triển   |
|     |            | nguyên   | mẫu.   |       |       |      |      |         |        |         |      |             |      |      |         |
|     | ▪          | Có thể   | bao    | gồm   |       | cả   | việc | loại    | bỏ     | bớt     | tính | năng        |      |      |         |
|     |            | • Nguyên |        | bản   |       | nên  | tập  | trung   | vào    | những   |      | tính        | năng | chưa | được    |
|     |            | hiểu     | rõ     | ràng; |       |      |      |         |        |         |      |             |      |      |         |
|     |            | • Kiểm   | tra    | lỗi   | không |      | nằm  | trong   | nguyên |         | mẫu; |             |      |      |         |
|     |            | • Tập    | trung  |       | vào   | các  |      | yêu cầu | chức   | năng    | hơn  | là          | các  | yêu  | cầu phi |
|     |            | chức     | năng.  |       |       |      |      |         |        |         |      |             |      |      |         |
Software Engineering 66
tkhuong@dthu.edu.vn

|     | 3.1 Nguyên |     |          |     |     | mẫu   |     |      | phần |     | mềm |     |     | (prototype) |       |       |      |
| --- | ---------- | --- | -------- | --- | --- | ----- | --- | ---- | ---- | --- | --- | --- | --- | ----------- | ----- | ----- | ---- |
| ❖   | Loại       | bỏ  | nguyên   |     | mẫu |       |     |      |      |     |     |     |     |             |       |       |      |
|     | ▪          | Các | nguyên   |     | mẫu |       | nên | bị   | loại | bỏ  |     | sau | khi | phát        | triển |       | phần |
|     |            | mềm | vì chúng |     |     | không |     | phải | là   | cái | cơ  | bản |     | để phát     |       | triển | hệ   |
thống:
|     |     | •   | Khó có     | thể    | điều  | chỉnh  |                      | hệ     | thống |      | để  | đáp  | ứng  | được    | các | yêu    | cầu   |
| --- | --- | --- | ---------- | ------ | ----- | ------ | -------------------- | ------ | ----- | ---- | --- | ---- | ---- | ------- | --- | ------ | ----- |
|     |     |     | phi chức   |        | năng; |        |                      |        |       |      |     |      |      |         |     |        |       |
|     |     | •   | Nguyên     | mẫu    |       | thường |                      | không  |       | được | tài | liệu | hóa; |         |     |        |       |
|     |     | •   | Cấu trúc   | nguyên |       |        | mẫu                  | thường |       | bị   | phá | vỡ   | do   | bị thay | đổi | nhanh; |       |
|     |     | •   | Nguyên     | mẫu    |       | có     | thể                  | không  |       | đáp  | ứng | được |      | những   |     | tiêu   | chuẩn |
|     |     |     | chất lượng |        | về    | mặt    | tổ                   | chức.  |       |      |     |      |      |         |     |        |       |
|     |     |     |            |        |       |        | Software Engineering |        |       |      |     |      |      |         |     |        | 67    |
tkhuong@dthu.edu.vn

|     |     | 3.2 Chuyển |     |     |     |     | giao |     | tăng |     | dần |     | (nhắc |     |     | lại) |     |
| --- | --- | ---------- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | ----- | --- | --- | ---- | --- |
❖ Thay vì phân phối hệ thống một lần, việc phát triển và phân
|     | phối  |     | được | chia  |     | ra    | thành |      | từng | phần |     | nhỏ   | (increment). |     |       |     | Mỗi phần  |
| --- | ----- | --- | ---- | ----- | --- | ----- | ----- | ---- | ---- | ---- | --- | ----- | ------------ | --- | ----- | --- | --------- |
|     | giao  |     | cho  | khách |     | hàng  |       | chứa | một  | phần |     | tính  | năng         |     | được  |     | yêu cầu.  |
| ❖   | Những |     |      | yêu   | cầu | người |       | dùng |      | được |     | ưu    | tiên         | và  | những |     | yêu cầu   |
|     | có    | độ  | ưu   | tiên  | cao |       | nhất  | sẽ   | được |      | đặt | trong | các          |     | phần  |     | đầu tiên. |
❖ Trong quá trình phát triển, việc phân tích yêu cầu cho phần
|     | tiếp |     | theo | có  | thể   | được |      | tiến |      | hành | nhưng |     | thay |     | đổi | yêu | cầu cho |
| --- | ---- | --- | ---- | --- | ----- | ---- | ---- | ---- | ---- | ---- | ----- | --- | ---- | --- | --- | --- | ------- |
|     | phần |     | hiện | tại | không |      | được |      | chấp |      | nhận. |     |      |     |     |     |         |
Software Engineering 68
tkhuong@dthu.edu.vn

|     | 3.2 Chuyển |       |     |     |     | giao |     | tăng | dần |     | (nhắc | lại) |     |
| --- | ---------- | ----- | --- | --- | --- | ---- | --- | ---- | --- | --- | ----- | ---- | --- |
| ❖   | Phát       | triển |     | dần | dần |      |     |      |     |     |       |      |     |
▪ Phát triển từng phần hệ thống và đánh giá mỗi phần trước khi
|     |     | tiến | hành | phát | triển |      | phần | tiếp theo; |      |      |            |          |       |
| --- | --- | ---- | ---- | ---- | ----- | ---- | ---- | ---------- | ---- | ---- | ---------- | -------- | ----- |
|     | ▪   | Được | sử   | dụng | trong |      | các  | phương     | pháp |      | linh hoạt; |          |       |
|     | ▪   | Đánh | giá  | được |       | thực | hiện | bởi        | đại  | diện | người      | sử dụng/ | khách |
hàng.
| ❖   | Chuyển |       | giao | dần  |      | dần  |                      |         |     |       |      |       |     |
| --- | ------ | ----- | ---- | ---- | ---- | ---- | -------------------- | ------- | --- | ----- | ---- | ----- | --- |
|     | ▪      | Triển | khai | một  | phần |      | để                   | sử dụng | cho | người | dùng | cuối; |     |
|     | ▪      | Đánh  | giá  | thực | tế   | hơn; |                      |         |     |       |      |       |     |
|     |        |       |      |      |      |      | Software Engineering |         |     |       |      |       | 69  |
tkhuong@dthu.edu.vn

|     | 3.2 Chuyển |      |      |          | giao |      | dần   |      | (incremental delivery) |        |       |        |        |     |
| --- | ---------- | ---- | ---- | -------- | ---- | ---- | ----- | ---- | ---------------------- | ------ | ----- | ------ | ------ | --- |
| ❖   | Ưu điểm    |      | của  | chuyển   |      | giao | dần   | dần: |                        |        |       |        |        |     |
|     | ▪ Khách    |      | hàng | sớm      | được |      | bàn   | giao | sản                    | phẩm   | (từng | phần). |        |     |
|     | ▪ Các      | phần | đầu  |          | được | xem  |       | như  | một                    | nguyên | mẫu   | để     | hỗ trợ | cho |
|     | việc       | làm  | lộ   | rõ những |      | yêu  | cầu   | cho  | phần                   | sau.   |       |        |        |     |
|     | ▪ Nguy     | cơ   | thất | bại      | toàn | hệ   | thống |      | là thấp.               |        |       |        |        |     |
▪ Duy trì được ưu điểm của phát triển từng phần, do đó dễ thích
|     | nghi | với | sự  | thay | đổi | của | hệ  | thống. |     |     |     |     |     |     |
| --- | ---- | --- | --- | ---- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
▪ Những dịch vụ hệ thống có độ ưu tiên cao nhất sẽ được kiểm thử
|     | nhiều | nhất |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• Khách hàng ít gặp lỗi phần mềm ở những phần quan trọng của hệ
thống.
|     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     |     | 70  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|     | Tự  | học | báo | cáo |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖
| Nghiên   |       | cứu mô   | hình | SCRUM |           |         |           |      |
| -------- | ----- | -------- | ---- | ----- | --------- | ------- | --------- | ---- |
| ❖ Nghiên |       | cứu mô   | hình | Agile |           |         |           |      |
| ❖ Nghiên |       | cứu mô   | hình | chữ   | V         |         |           |      |
| ❖ Nghiên |       | cứu mô   | hình | RUP   | (Rational | Unified | Process)  |      |
| → Trình  |       | bày cách | thức | hoạt  | động,     | ưu điểm | và khuyết | điểm |
| của      | 2     | mô hình  | trên |       |           |         |           |      |
| → Soạn   | slide | báo      | cáo  |       |           |         |           |      |
71
tkhuong@dthu.edu.vn
tkhuong@dthu.edu.vn

ƯU ĐIỂM CỦA RUP
| ❖   | Phát | triển | phần | mềm |     | theo | vòng | lặp |     |     |     |
| --- | ---- | ----- | ---- | --- | --- | ---- | ---- | --- | --- | --- | --- |
▪ Các phần được lên kế hoạch dựa vào độ ưu tiên của khách hàng
|     |      | và phân |     | phối những |     | phần | có  | độ ưu tiên | cao nhất | trước. |     |
| --- | ---- | ------- | --- | ---------- | --- | ---- | --- | ---------- | -------- | ------ | --- |
| ❖   | Quản | lý      | yêu | cầu        |     |      |     |            |          |        |     |
▪ Viết tài liệu một cách rõ ràng cho các yêu cầu khách hàng và
|     |     | theo    | dõi  | sự thay  | đổi | của | những     | yêu cầu | này.      |        |        |
| --- | --- | ------- | ---- | -------- | --- | --- | --------- | ------- | --------- | ------ | ------ |
| ❖   | Sử  | dụng    | kiến | trúc     | dựa | vào | component |         |           |        |        |
|     | ▪   | Tổ chức |      | hệ thống |     | như | một       | tập các | component | có thể | tái sử |
dụng.
|     |     |     |     |     |     |     | Software Engineering |     |     |     | 86  |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

ƯU ĐIỂM CỦA RUP
| ❖   | Mô  | hình | hóa |     | phần |     | mềm |     | một | cách | trực | quan |     |     |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- |
▪ Sử dụng các mô hình đồ họa UML để biểu diễn các góc nhìn tĩnh
|     |      | và động |      | của      | phần  |      | mềm. |      |      |     |      |        |       |       |            |
| --- | ---- | ------- | ---- | -------- | ----- | ---- | ---- | ---- | ---- | --- | ---- | ------ | ----- | ----- | ---------- |
| ❖   | Kiểm | tra     | chất |          | lượng |      | phần |      | mềm  |     |      |        |       |       |            |
|     | ▪    | Đảm     | bảo  |          | rằng  | phần |      | mềm  |      | đáp | ứng  | được   | các   | chuẩn | chất lượng |
|     |      | về mặt  |      | tổ       | chức. |      |      |      |      |     |      |        |       |       |            |
| ❖   | Điều | khiển   |      | các      |       | thay | đổi  | phần |      | mềm |      |        |       |       |            |
|     | ▪    | Quản    |      | lý những |       |      | thay | đổi  | phần |     | mềm  | sử     | dụng  | những | hệ thống   |
|     |      | quản    | lý   | thay     | đổi   |      | và   | các  | công | cụ  | quản | lý cấu | hình. |       |            |
Software Engineering 87
tkhuong@dthu.edu.vn

TỔNG KẾT
❖ Quy trình nên có các hoạt động để đối phó với sự thay đổi. Có
| thể   | có pha | nguyên  |     | bản |       | để  | hạn chế | những |     | thay | đổi | không | cần |
| ----- | ------ | ------- | --- | --- | ----- | --- | ------- | ----- | --- | ---- | --- | ----- | --- |
| thiết | trên   | yêu cầu |     | và  | thiết | kế. |         |       |     |      |     |       |     |
❖
| Quy  | trình | có thể |     | được |       | cấu | trúc   | hóa | cho | phát | triển | và   | phân |
| ---- | ----- | ------ | --- | ---- | ----- | --- | ------ | --- | --- | ---- | ----- | ---- | ---- |
| phối | dần   | dần    | sao | cho  | những |     | thay   | đổi | có  | thể  | được  | thực | hiện |
| mà   | không | phá    | vỡ  | toàn | bộ    | hệ  | thống. |     |     |      |       |      |      |
❖ RUP là một mô hình quy trình tổng quát hiện đại được tổ chức
| thành | các | pha | (khởi |     | động, |     | phát | triển, | xây |     | dựng | và chuyển |     |
| ----- | --- | --- | ----- | --- | ----- | --- | ---- | ------ | --- | --- | ---- | --------- | --- |
tiếp).
|     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     | 90  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

BÀI TẬP
| ❖ Tìm | hiểu   | và trình | bày                  | một | quy | trình | phần | mềm | (ví |
| ----- | ------ | -------- | -------------------- | --- | --- | ----- | ---- | --- | --- |
| dụ:   | SCRUM, | XP,      | 4GT,                 | …)  |     |       |      |     |     |
|       |        |          | Software Engineering |     |     |       |      |     | 91  |
tkhuong@dthu.edu.vn

CÂU HỎI ÔN TẬP
| 1) Có    | mấy    | loại  | mô hình  | tiến | trình? | Là loại  | nào? |       |          |
| -------- | ------ | ----- | -------- | ---- | ------ | -------- | ---- | ----- | -------- |
| 2) Trình | bày    |       | nội dung | của  | các    | mô hình: | thác | nước, | làm mẫu, |
| xoáy     | ốc,    | …RUP  |          |      |        |          |      |       |          |
| a)       | Nội    | dung  |          |      |        |          |      |       |          |
| b)       | Đặc    | trưng |          |      |        |          |      |       |          |
| c)       | Ưu     | nhược | điểm     |      |        |          |      |       |          |
| d)       | Cần    | yêu   | cầu gì?  |      |        |          |      |       |          |
| e)       | Thích  | hợp   | khi nào? |      |        |          |      |       |          |
| 3) Mô    | tả quy | trình | công     | nghệ | yêu    | cầu?     |      |       |          |
Software Engineering 92
tkhuong@dthu.edu.vn

CÂU HỎI ÔN TẬP
1) Ở trường hợp nào thì áp dụng quy trình phát triển phần mềm
| a) Thác      | nước    |            |         |      |      |      |        |
| ------------ | ------- | ---------- | ------- | ---- | ---- | ---- | ------ |
| b) Thác      | nước    | cải tiến   |         |      |      |      |        |
| c) Prototype |         |            |         |      |      |      |        |
| d) Xoắn      | trôn    | ốc         |         |      |      |      |        |
| 2) Trong     | các môn | học trước, | khi xây | dựng | phần | mềm, | bạn đã |
| áp dụng:     |         |            |         |      |      |      |        |
| a) Phương    | pháp    | nào?       |         |      |      |      |        |
| b) Quy       | trình   | nào?       |         |      |      |      |        |
| c) Công      | cụ nào? |            |         |      |      |      |        |
Software Engineering 93
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C2_QuyTrinhPM_send.md -->

---


<!-- BẮT ĐẦU FILE: C3_YeuCauPM.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 3
YÊU CẦU
PHẦN MỀM
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

MỤC TIÊU CHƯƠNG 3
| ❖ Tìm | hiểu | về  | các | yêu | cầu | hệ  | thống | và  | đặc | điểm | của |
| ----- | ---- | --- | --- | --- | --- | --- | ----- | --- | --- | ---- | --- |
chúng
| ❖ Phương |       | pháp  | xác | định  | yêu                  | cầu | hệ   | thống |     |      |     |
| -------- | ----- | ----- | --- | ----- | -------------------- | --- | ---- | ----- | --- | ---- | --- |
| ❖ Các    | kỹ    | thuật | đặc | tả    | yêu                  | cầu | hệ   | thống | và  | cách | áp  |
| dụng     | những |       | kỹ  | thuật | này                  | một | cách | phù   | hợp |      |     |
|          |       |       |     |       | Software Engineering |     |      |       |     |      | 2   |
tkhuong@dthu.edu.vn

NỘI DUNG
| 1   | YC CHỨC |     | NĂNG    | &   | YC PHI | CHỨC | NĂNG |
| --- | ------- | --- | ------- | --- | ------ | ---- | ---- |
|     | ĐẶC     | TẢ  | YÊU CẦU |     |        |      |      |
2
| 33  | QUY      | TRÌNH | CÔNG |      | NGHỆ | YÊU CẦU |     |
| --- | -------- | ----- | ---- | ---- | ---- | ------- | --- |
| 44  | THU      | THẬP  | VÀ   | PHÂN | TÍCH | YÊU     | CẦU |
| 5   | THẨM     | ĐỊNH  | YÊU  |      | CẦU  |         |     |
| 6   | QUẢN     | TRỊ   | YÊU  | CẦU  |      |         |     |
| 7   | TÀI LIỆU |       | YÊU  | CẦU  | PM   |         |     |
3
tkhuong@dthu.edu.vn

|        | Đặt | vấn    |      | đề  |       |      |         |      |       |      |
| ------ | --- | ------ | ---- | --- | ----- | ---- | ------- | ---- | ----- | ---- |
| ❖ Tiêu |     | chí gì | quan |     | trọng | nhất | đối với | chất | lượng | phần |
mềm???
| ➔Phần   |       | mềm      | phải  |     | thỏa | mãn    | yêu cầu  | của người |     | dùng |
| ------- | ----- | -------- | ----- | --- | ---- | ------ | -------- | --------- | --- | ---- |
| ❖ Yêu   |       | cầu phần |       | mềm |      | là gì? |          |           |     |      |
| → Những |       | gì       | người |     | ta   | muốn   | có trong | phần      | mềm | được |
| phát    | triển |          |       |     |      |        |          |           |     |      |
Software Engineering 4
tkhuong@dthu.edu.vn

YÊU CẦU PHẦN MỀM
| ❖ Yêu | cầu phần | mềm | là gì? |     |     |
| ----- | -------- | --- | ------ | --- | --- |
| Khách | hàng     |     |        |     |     |
Tôi muốn
phần mềm
|     |     |     |     | giúp tôi thực |     |
| --- | --- | --- | --- | ------------- | --- |
hiện nghiệp
vụ ….
Tôi muốn
|     | nghiệp vụ |     |     |     |     |
| --- | --------- | --- | --- | --- | --- |
phải được
|     | thực hiện |     |     | Phân tích | viên |
| --- | --------- | --- | --- | --------- | ---- |
….
Software Engineering 5
tkhuong@dthu.edu.vn

| Một | số  |     | ví dụ |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- |
❖ Tôi muốn pm giúp tôi thực hiện công việc tính lương, lập báo cáo tồn
| kho, đánh | cờ  | caro, | giải | bài tập | đại số,… |     |
| --------- | --- | ----- | ---- | ------- | -------- | --- |
❖ Tôi muốn pm giúp độc giả tra cứu sách muốn mượn, việc tra cứu
| này phải | được | thực | hiện | ở bất | kỳ nơi | nào. |
| -------- | ---- | ---- | ---- | ----- | ------ | ---- |
❖ Tôi muốn giúp tôi lập hóa đơn tiền điện và phải in được khoảng
20.000 hóa đơn của khu vực tp cao lãnh này chỉ diễn ra tối đa 1
ngày
❖
Tôi muốn pm giúp tra cứu các chuyến xe buýt trên địa bàn tỉnh đồng
tháp, việc tra cứu này được diễn ra trên sơ đồ của những tuyến xe
buýt
❖ …………………………………………
Software Engineering 6
tkhuong@dthu.edu.vn

YÊU CẦU PHẦN MỀM
| ❖   | Khái  | niệm |        |       |       |      |       |     |      |      |      |     |      |        |
| --- | ----- | ---- | ------ | ----- | ----- | ---- | ----- | --- | ---- | ---- | ---- | --- | ---- | ------ |
|     | ▪ Yêu |      | cầu    | của   |       | phần | mềm   |     | X là | mong | muốn |     | của  | người  |
|     | sử    |      | dụng   | về    | khả   | năng |       | mà  | phần | mềm  | X    | cần | phải | có để  |
|     | có    |      | thể hỗ | trợ   | cho   |      | người |     | dùng | thực | hiện | tốt | các  | nghiệp |
|     | vụ    | của  |        | mình. |       |      |       |     |      |      |      |     |      |        |
| ❖   | Yêu   | cầu  | phần   |       | mềm   |      | có    | 2   | loại |      |      |     |      |        |
|     | ▪ Yêu |      | cầu    | người |       | dùng |       |     |      |      |      |     |      |        |
|     | ▪ Yêu |      | cầu    | hệ    | thống |      |       |     |      |      |      |     |      |        |
Software Engineering 7
tkhuong@dthu.edu.vn

|     | VD1. Yêu |     |     |     | cầu |     | Người |     | dùng |
| --- | -------- | --- | --- | --- | --- | --- | ----- | --- | ---- |
❖ Một giáo viên yêu cầu viết phần mềm bài tập đại số hỗ trợ việc giải
| phương |     | trình | bậc | hai | như | sau: |     |     |     |
| ------ | --- | ----- | --- | --- | --- | ---- | --- | --- | --- |
▪ Phần mềm cho phép nhập các hệ số của phương trình ax2 + bx +
c = 0 (a,b,c là số thực khác 0) và tính toán cho ra kết quả theo
|     | quy | tắc         | giải | phương |     | trình | bậc | 2   |     |
| --- | --- | ----------- | ---- | ------ | --- | ----- | --- | --- | --- |
| Quy | tắc | giải phương |      | trình  | bậc | 2:    |     |     |     |
Cho phương trình bậc 2: ax2+bx+c=0 (với a,b,c là 3 số thực, a khác 0)
| Các      | bước | giải           | phương         | trình    |       | như sau:   |     |           |        |
| -------- | ---- | -------------- | -------------- | -------- | ----- | ---------- | --- | --------- | ------ |
| B1. Tính |      | delta = b2-4ac |                |          |       |            |     |           |        |
| B2. Xác  |      | đinh           | nghiệm         | theo     | delta |            |     |           |        |
|          |      | + Nếu          | delta<0: PT vô |          |       | nghiệm     |     |           |        |
|          |      | + Nếu          | delta=0: PT có |          |       | nghiệm     |     | kép x =x  | =-b/2a |
|          |      |                |                |          |       |            |     | 1         | 2      |
|          |      | + Nếu          | delta>0: PT có |          |       | 2 nghiệm   |     | phân biệt |        |
|          |      |                | x              | =(-b-căn |       | delta)/ 2a |     |           |        |
1
|     |     |     | x   | =(-b+căn |     | delta)/ 2a |     |     |     |
| --- | --- | --- | --- | -------- | --- | ---------- | --- | --- | --- |
2
Software Engineering 8
tkhuong@dthu.edu.vn

|     | VD2. Yêu |     |     |     |     | cầu |     | Người |     |     |     | dùng |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- |
❖
| Chủ  |     | khách  |       | sạn   | yêu      |        | cầu                  | việc     |      | phần |      | mềm  | hỗ trợ   | việc | tính |
| ---- | --- | ------ | ----- | ----- | -------- | ------ | -------------------- | -------- | ---- | ---- | ---- | ---- | -------- | ---- | ---- |
| tiền |     | thuê   | phòng |       | theo     |        | quy                  | tắc      | như  |      | sau: |      |          |      |      |
|      |     | Tính   |       | tiền  | thuê     | phòng  |                      |          |      |      |      |      |          |      |      |
|      |     | Tính   |       | tiền  | thuê     | phòng  | được                 |          | tính | theo |      | quy  | tắc sau: |      |      |
|      |     | Tiền   |       | = Số  | ngày     | thuê   | * đơn                |          | giá  | * Tỷ | lệ   | giảm | giá      |      |      |
|      |     | Số     | ngày  |       | thuê     | = Ngày | trả                  | phòng    |      | –    | Ngày | nhận | phòng    |      |      |
|      |     | Đơn    |       | giá   | dựa trên |        | bảng                 | đơn      | giá  | như  |      | sau: |          |      |      |
|      |     | -      | Loại  | phòng |          |        | Đơn                  | giá/Ngày |      |      |      |      |          |      |      |
|      |     | + Loại |       | A     |          |        | 240.000              |          |      |      |      |      |          |      |      |
|      |     | + Loại |       | B     |          |        | 220.000              |          |      |      |      |      |          |      |      |
|      |     | + Loại |       | C     |          |        | 200.000              |          |      |      |      |      |          |      |      |
|      |     | Tỷ     | lệ    | giảm  | giá      | dựa    | trên                 | quy      | tắc  | giảm |      | giá  |          |      |      |
|      |     | Nếu    | thuê  |       | quá      | 7 ngày | được                 |          | giảm |      | 10%  |      |          |      |      |
|      |     |        |       |       |          |        | Software Engineering |          |      |      |      |      |          |      | 9    |
tkhuong@dthu.edu.vn

|     | VD3. Yêu |     |     |     | cầu |     | Người |     | dùng |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- | --- | --- | --- |
❖
| Phòng |     | tổ    | chức  | cán  |     | bộ yêu | cầu  | viết | phần |     | mềm   | giúp |     | quản |
| ----- | --- | ----- | ----- | ---- | --- | ------ | ---- | ---- | ---- | --- | ----- | ---- | --- | ---- |
| lý    | hồ  | sơ    | nhân  | viên |     | (tra   | cứu, | thêm | nhân |     | viên  | mới, |     | cập  |
| nhật  |     | thông | tin   | nhân |     | viện,  | xóa, | lập  | báo  | cáo | thống |      | kê  | tình |
| hình  |     | nhân  | viên) | các  |     | thông  | tin  | cần  | quản | lý  | theo  | biểu |     | mẫu  |
sau:
|     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     |     | 10  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

VD4. Yêu cầu Người dùng
❖ Hãng du lịch TravelGood đến gặp bạn và đề nghị
làm dự án phần mềm sau:
▪ Mô tả bài toán / yêu cầu người dùng
TravelGood muốn cung cấp cho khách hàng của họ một
ứng dụng đặt vé và lập kế hoạch du lịch. Ứng dụng này
cần cho phép khách lập kế hoạch về các chuyến bay và
khách sạn. Đầu tiên, khách hàng có thể sắp xếp một
chuyến đi, sau đó đặt vé và đặt phòng khách sạn cho
chuyến đi đó. Người dùng có thể lập kế hoạch cho
nhiều chuyến đi. Ngoài ra, phần mềm còn cho phép hủy
các chuyến đã đặt.
Software Engineering 11
tkhuong@dthu.edu.vn

|     | VD5. Yêu |     |           |     | cầu  |                      | người |      | dùng |      |     |      |
| --- | -------- | --- | --------- | --- | ---- | -------------------- | ----- | ---- | ---- | ---- | --- | ---- |
| ❖   | Một      | cửa | hàng….đề  |     |      | nghị                 | xây   | dựng |      | phần | mềm | quản |
|     | lý việc  | thu | chi       | như | sau: |                      |       |      |      |      |     |      |
|     | ▪ Mô     | tả  | bài toán/ |     | yêu  | cầu                  | người | dùng |      |      |     |      |
|     |          |     |           |     |      | Software Engineering |       |      |      |      |     | 12   |
tkhuong@dthu.edu.vn

|         | Yêu  |      | cầu   |      | người |        | dùng |      |          |     |      |     |     |
| ------- | ---- | ---- | ----- | ---- | ----- | ------ | ---- | ---- | -------- | --- | ---- | --- | --- |
| ❖ Những |      | phát |       | biểu | bằng  | ngôn   |      | ngữ  | tự nhiên |     | kết  | hợp | với |
| các     | biểu |      | mẫu   | về   | các   | dịch   | vụ   | mà   | hệ thống |     | cung | cấp | và  |
| những   |      | ràng |       | buộc | (quy  | tắc)   | về   | hoạt | động     | của | nó.  |     |     |
| ❖ Dành  |      | cho  | khách |      | hàng  | (người |      | sử   | dụng)    |     |      |     |     |
❖ Đơn giản, dễ hiểu: không có kiến thức chi tiết về kỹ thuật/
| tin | học |     |     |     |     |                      |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     | 13  |
tkhuong@dthu.edu.vn

|        | Bài | tập  |       | 1    |        |          |         |     |     |        |
| ------ | --- | ---- | ----- | ---- | ------ | -------- | ------- | --- | --- | ------ |
| ❖ Với  | vai | trò  | người |      | dùng,  | bạn muốn | có phần |     | mềm | hỗ trợ |
| nghiệp |     | vụ   | đang  | thực | hiện,  | hãy mô   | tả yêu  | cầu | của | bạn về |
| dự     | án  | phần | mềm   |      | này??? |          |         |     |     |        |
Software Engineering 15
tkhuong@dthu.edu.vn

|     |      | VD1. Yêu |        |        |       |            | cầu   |                      |      | hệ   | thống   |     |       |      |       |     |        |      |
| --- | ---- | -------- | ------ | ------ | ----- | ---------- | ----- | -------------------- | ---- | ---- | ------- | --- | ----- | ---- | ----- | --- | ------ | ---- |
| ❖   | Sau  |          | khi    | nhận   |       | thực       |       | hiện                 | phần |      | mềm     |     | bài   | tập  | đại   | số  | hỗ     | trợ  |
|     | việc |          | giải   | phương |       |            | trình |                      | bậc  | 2,   | nhóm    |     | phát  |      | triển | sẽ  | chi    | tiết |
|     | ra   | thành    |        | yêu    |       | cầu        | hệ    | thống:               |      |      |         |     |       |      |       |     |        |      |
|     | ▪    | Hệ       | thống  |        | cho   |            | phép  | người                |      | dùng | nhập    |     | thông |      | tin   | của | phương |      |
|     |      | trình    |        | đúng   |       | theo       | quy   | tắc:                 | hệ   | số   | a,b,c   |     | là số | thực | và    |     | a khác | 0    |
|     | ▪    | Hệ       | thống  |        | tính  |            | toán  | và                   | cho  |      | ra kết  | quả |       | theo | các   |     | bước   | giải |
|     |      | phương   |        |        | trình |            |       |                      |      |      |         |     |       |      |       |     |        |      |
|     | ▪    | Hệ       | thống  |        | là    | ứng        |       | dụng                 | dạng |      | windows |     | form, |      | triển |     | khai   | trên |
|     |      | môi      | trường |        |       | windows….. |       |                      |      |      |         |     |       |      |       |     |        |      |
|     |      |          |        |        |       |            |       | Software Engineering |      |      |         |     |       |      |       |     |        | 16   |
tkhuong@dthu.edu.vn

|     | VD2. Yêu |      |      |       |     | cầu   |      | hệ   | thống |      |      |        |     |      |      |
| --- | -------- | ---- | ---- | ----- | --- | ----- | ---- | ---- | ----- | ---- | ---- | ------ | --- | ---- | ---- |
| ❖   | Phần     | mềm  |      | phải  | có  | các   | chức |      | năng  |      | sau: |        |     |      |      |
|     | ▪ Thêm,  |      | cập  | nhật  |     | (tên, |      | đơn  | giá), | xóa  | loại | phòng, |     | cập  | nhật |
|     | quy      | định |      | giảm  | giá |       |      |      |       |      |      |        |     |      |      |
|     | ▪ Cho    |      | phép | người |     | dùng  |      | nhập |       | ngày | nhận | phòng, |     | ngày | trả  |
phòng
|     | ▪ Tính  |        | toán | cho |       | ra số | ngày                 |      | ở và  | áp   | dụng | công | thức | tính | ra  |
| --- | ------- | ------ | ---- | --- | ----- | ----- | -------------------- | ---- | ----- | ---- | ---- | ---- | ---- | ---- | --- |
|     | số      | tiền   | thuê |     | phòng |       | -> lưu               | lại  | kết   | quả  |      |      |      |      |     |
|     | ▪ In    | ra hóa |      | đơn | tính  | tiền  |                      | cho  | khách | hàng |      |      |      |      |     |
|     | ▪ Ứng   | dụng   |      | xây | dựng  |       | với                  | giao | diện  | form |      |      |      |      |     |
|     | ▪ …………… |        |      |     |       |       |                      |      |       |      |      |      |      |      |     |
|     |         |        |      |     |       |       | Software Engineering |      |       |      |      |      |      |      | 17  |
tkhuong@dthu.edu.vn

|     | VD3. Yêu |      |      |       |       | cầu   |                      | hệ    |      | thống |      |      |      |         |         |         |     |
| --- | -------- | ---- | ---- | ----- | ----- | ----- | -------------------- | ----- | ---- | ----- | ---- | ---- | ---- | ------- | ------- | ------- | --- |
| ❖   | Phần     | mềm  |      | phải  | có    | chức  |                      | năng: |      |       |      |      |      |         |         |         |     |
|     | ▪ Cho    | phép |      | thêm, |       | cập   | nhật,                |       | xóa  |       | hồ   | sơ   | nhận | viên    | theo    | BM1     | -   |
|     | >        | lưu  | vào  | csdl  |       |       |                      |       |      |       |      |      |      |         |         |         |     |
|     | ▪ Tra    | cứu  |      | hồ    | sơ    | nhân  | viên;                |       | pm   |       | cho  | phép |      | nhập    | vào tên | hoặc    |     |
|     | địa      | chỉ, | hoặc |       | trình | độ    | của                  |       | nhận |       | viên | và   | sau  | đó      | xuất    | ra danh |     |
|     | sách     | các  |      | nhân  |       | viên  | thông                |       | tin  | tra   | cứu  | theo |      | BM1.    |         |         |     |
|     | ▪ Lập    | báo  |      | cáo   | thông |       | kê:                  | chọn  |      |       | thời | gian |      | muốn    | thống   | kê      | và  |
|     | xuất     | ra   | kết  | quả   |       | thống | kê                   | như   |      | BM2,  |      | in   | ra   | kết quả | thống   | kê.     |     |
|     |          |      |      |       |       |       | Software Engineering |       |      |       |      |      |      |         |         |         | 19  |
tkhuong@dthu.edu.vn

|     | VD4. Yêu |     |     |     | cầu | hệ  | thống |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
❖ Sau khi nhận làm phần mềm cho TravelGood đội phát triển chi tiết
| hóa | thành | các | yêu | cầu | hệ thống: |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
1. Người dùng có thể lập kế hoạch một chuyến đi bằng cách chọn
một trình tự các điểm đến, rồi lưu lại. (kèm theo sơ đồ mô tả
|     | kịch | bản   | ca  | sử dụng) |          |       |       |      |         |        |     |
| --- | ---- | ----- | --- | -------- | -------- | ----- | ----- | ---- | ------- | ------ | --- |
| 2.  | Hệ   | thống | cần | là       | ứng dụng | Web,  | chạy  | được | tại tất | cả các | hệ  |
|     | điều | hành  | và  | hầu      | hết các  | trình | duyệt |      |         |        |     |
3. Ứng dụng Web phải triển khai được tại các server tiêu chuẩn
|     | như | GlassFish |     | hoặc | Tomcat |     |     |     |     |     |     |
| --- | --- | --------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- |
4. Hệ thống phải dễ sử dụng: đạt một test usability (kèm chi tiết
cụ thể)
| 5.  | …   |     |     |     |                      |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | Software Engineering |     |     |     |     |     | 21  |
tkhuong@dthu.edu.vn

|     |        | Yêu |      | cầu |      | hệ  |      | thống |      |     |      |      |      |     |     |
| --- | ------ | --- | ---- | --- | ---- | --- | ---- | ----- | ---- | --- | ---- | ---- | ---- | --- | --- |
| ❖   | Một    | tài | liệu |     | có   | cấu | trúc | mô    | tả   | chi | tiết | chức | năng | của | hệ  |
|     | thống, |     | các  |     | dịch | vụ  | và   | ràng  | buộc |     | về   | hoạt | động | của | hệ  |
thống.
| ❖   | Định | nghĩa |     |      | chính | xác  |     | cái gì               | cần | được |     | cài  | đặt.  |      |     |
| --- | ---- | ----- | --- | ---- | ----- | ---- | --- | -------------------- | --- | ---- | --- | ---- | ----- | ---- | --- |
|     | ▪    | Có    | thể | là   | một   | phần |     | của                  | hợp | đồng |     | giữa | khách | hàng | và  |
|     |      | người |     | nhận | thầu  |      |     |                      |     |      |     |      |       |      |     |
|     |      |       |     |      |       |      |     | Software Engineering |     |      |     |      |       |      | 23  |
tkhuong@dthu.edu.vn

|     |     | Các |     | ví  | dụ    | khác |     |
| --- | --- | --- | --- | --- | ----- | ---- | --- |
|     | Đặc | tả  | yêu | cầu | người | dùng |     |
1. Phần mềm phải cung cấp một phương tiện để biểu diễn và truy nhập các
| file bên |     | ngoài | được | tạo | bằng | các công | cụ khác. |
| -------- | --- | ----- | ---- | --- | ---- | -------- | -------- |
|          | Đặc | tả    | yêu  | cầu | hệ   | thống    |          |
1.1. Người dùng cần được cung cấp tiện ích để định nghĩa kiểu của các file
ngoài.
1.2 Mỗi kiểu file ngoài có thể được biểu diễn dưới dạng một biểu tượng trên
| phần |     | hiển | thị của | người | dùng. |     |     |
| ---- | --- | ---- | ------- | ----- | ----- | --- | --- |
1.3 Mỗi kiểu file ngoài có thể có một công cụ có thể dùng cho loại file đó.
1.4 Cần cung cấp các tiện ích để người dùng có thể định nghĩa biểu tượng
cho file ngoài.
1.5 Khi một người dùng chọn một biểu tượng đại diện cho một file ngoài,
hiệu ứng của việc chọn đó là gọi công cụ tương ứng với kiểu của file đó để
| chạy | nó. |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 24
tkhuong@dthu.edu.vn

| Bài | tập | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖
| Với vai | trò  | phân  | tích  | viên,                | bạn | hãy | mô tả     | yêu | cầu     | hệ  |
| ------- | ---- | ----- | ----- | -------------------- | --- | --- | --------- | --- | ------- | --- |
| thống   | của  | dự án | phần  | mềm                  | từ  | yêu | cầu người |     | sử dụng |     |
| đã thu  | thập | được  | ở BT1 |                      |     |     |           |     |         |     |
|         |      |       |       | Software Engineering |     |     |           |     |         | 26  |
tkhuong@dthu.edu.vn

YÊU CẦU PHẦN MỀM
| Phân |     | loại   | yêu   | cầu  |      | theo | tính    | chất,   | có 2   | loại | yêu  | cầu |          |
| ---- | --- | ------ | ----- | ---- | ---- | ---- | ------- | ------- | ------ | ---- | ---- | --- | -------- |
| ❖    | Yêu | cầu    | chức  |      | năng |      | (nghiệp |         | vụ)    |      |      |     |          |
|      | ▪   | Nghiệp |       | vụ   | cần  | được |         | hỗ trợ  |        |      |      |     |          |
| ❖    | Yêu | cầu    | phi   | chức |      | năng |         | (chất   | lượng) |      |      |     |          |
|      | ▪   | Các    | ràng  | buộc |      | trên |         | yêu cầu | chức   | năng | (tốc | độ, | bảo mật, |
|      |     | giao   | diện, | …)   |      |      |         |         |        |      |      |     |          |
Software Engineering 27
tkhuong@dthu.edu.vn

|       | Đặt |     | vấn    |     | đề    |        |                      |          |      |       |       |     |         |      |
| ----- | --- | --- | ------ | --- | ----- | ------ | -------------------- | -------- | ---- | ----- | ----- | --- | ------- | ---- |
| ❖ Để  |     | xây | dựng   |     | được  | một    |                      | hệ thống |      | có    | thể   | sử  | dụng    | được |
| trong |     |     | thực   | tế, | trước | hết    | phải                 | đạt      | được |       | những |     | yêu cầu | gì?  |
| ❖ Yêu |     | cầu | chức   |     | năng  | có     | phải                 | quan     |      | trọng | nhất  |     | không?  |      |
| ❖ Nếu |     | ta  | không  |     | xác   | định   | đầy                  | đủ,      | rõ   | ràng  | các   | yêu | cầu     | chức |
| năng  |     |     | thì sẽ | xảy | ra    | chuyện |                      | gì?      |      |       |       |     |         |      |
|       |     |     |        |     |       |        | Software Engineering |          |      |       |       |     |         | 28   |
tkhuong@dthu.edu.vn

YÊU CẦU CHỨC NĂNG
| ❖ Yêu | cầu        | chức  | năng |      | mô                   | tả   | hệ thống |       | sẽ  | làm  | gì. Nghĩa |      | là  |
| ----- | ---------- | ----- | ---- | ---- | -------------------- | ---- | -------- | ----- | --- | ---- | --------- | ---- | --- |
| phần  | mềm        | có    | khả  | năng |                      | thực | hiện     | những |     | công | việc      | gì   | để  |
| hỗ    | trợ nghiệp |       | vụ.  |      |                      |      |          |       |     |      |           |      |     |
| ❖ Một | chức       | năng  |      | được | mô                   |      | tả thông |       | qua | dữ   | liệu đầu  | vào, |     |
| cách  | xử         | lý và | dữ   | liệu | được                 |      | kết xuất |       |     |      |           |      |     |
|       |            |       |      |      | Software Engineering |      |          |       |     |      |           |      | 29  |
tkhuong@dthu.edu.vn

| Một | số  | ví  | dụ  | - xét | yêu | cầu | chức | năng |
| --- | --- | --- | --- | ----- | --- | --- | ---- | ---- |
❖ Tôi muốn pm giúp tôi thực hiện công việc tính lương, lập báo cáo tồn
| kho, đánh | cờ  | caro, | giải bài | tập đại | số,… |     |     |     |
| --------- | --- | ----- | -------- | ------- | ---- | --- | --- | --- |
❖ Tôi muốn pm giúp độc giả tra cứu sách muốn mượn, việc tra cứu
| này phải | được | thực | hiện | ở bất kỳ | nơi nào. |     |     |     |
| -------- | ---- | ---- | ---- | -------- | -------- | --- | --- | --- |
❖ Tôi muốn giúp tôi lập hóa đơn tiền điện và phải in được khoảng
20.000 hóa đơn của khu vực tp cao lãnh này chỉ diễn ra tối đa 1
ngày
❖
Tôi muốn pm giúp tra cứu các chuyến xe buýt trên địa bàn tỉnh đồng
tháp, việc tra cứu này được diễn ra trên sơ đồ của những tuyến xe
buýt
❖ …………………………………………
Software Engineering 30
tkhuong@dthu.edu.vn

|     | Ví      |      | dụ1 - |     |               | Yêu |       |      | cầu |       | chức |     |     | năng   |     |         |     |     |
| --- | ------- | ---- | ----- | --- | ------------- | --- | ----- | ---- | --- | ----- | ---- | --- | --- | ------ | --- | ------- | --- | --- |
| ❖   | Trong   | phần |       | mềm | TouristTravel |     |       |      |     | thì:  |      |     |     |        |     |         |     |     |
|     | ▪ Người |      | dùng  |     | có            | thể |       | lập  | kế  | hoạch |      | một |     | chuyến |     | đi, đặt | vé, | đặt |
|     | phòng,  |      | lưu   | một |               | kế  | hoạch |      | để  | sau   | này  | sẽ  | đặt | vé     | đặt | phòng…  |     |     |
| ❖   | Trong   | phần |       | mềm | LIBSYS        |     |       | thì: |     |       |      |     |     |        |     |         |     |     |
▪ Người sử dụng có thể tìm kiếm tài liệu dựa trên các từ khóa có
|     | trong |     | tài     | liệu | hoặc |       | tên | tài     | liệu  |     |      |      |      |       |     |          |       |     |
| --- | ----- | --- | ------- | ---- | ---- | ----- | --- | ------- | ----- | --- | ---- | ---- | ---- | ----- | --- | -------- | ----- | --- |
|     | ▪ Hệ  |     | thống   | sẽ   | cung |       | cấp |         | những |     | giao | diện |      | thích | hợp | để       | người | sử  |
|     | dụng  |     | đọc     | được |      | các   |     | định    | dạng  |     | khác |      | nhau | của   |     | tài liệu | như:  | văn |
|     | bản   |     | (.txt), | PDF, |      | Word, |     | Excel,… |       |     |      |      |      |       |     |          |       |     |
▪ Tất cả những hoá đơn mà người sử dụng đăng ký để in sao tài
|     | liệu |     | có một |     | mã  | duy | nhất. |     |                      |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | ------ | --- | --- | --- | ----- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |      |     |        |     |     |     |       |     | Software Engineering |     |     |     |     |     |     |     |     | 31  |
tkhuong@dthu.edu.vn

|      | Yêu    | cầu  | chức    | năng | –   | tính | chất  |         |
| ---- | ------ | ---- | ------- | ---- | --- | ---- | ----- | ------- |
| ❖ Về | nguyên | tắc, | các yêu | cầu  | nên | hoàn | chỉnh | và nhất |
quán.
| ❖ Hoàn | chỉnh | (complete) |     |     |     |     |     |     |
| ------ | ----- | ---------- | --- | --- | --- | --- | --- | --- |
▪ Tất cả các dịch vụ mà người dùng yêu cầu phải được định nghĩa.
| ❖ Nhất | quán(consistent) |     |     |     |     |     |     |     |
| ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- |
▪ Không có bất cứ mâu thuẫn hay xung đột nào trong các mô tả về
|     | các yêu | cầu. |     |     |     |     |     |     |
| --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
Trên thực tế, không thể tạo ra tài liệu các yêu cầu vừa hoàn
chỉnh vừa nhất quán được!!
|     | Rất dễ mắc lỗi |     | hay bỏ sót yêu cầu khi viết đặc tả cho các hệ |     |     |     |     |     |
| --- | -------------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
thống phức tạp.
Các stakeholder có các nhu cầu khác nhau và thường không nhất
quán với nhau.
Software Engineering 34
tkhuong@dthu.edu.vn

YÊU CẦU CHỨC NĂNG
| ❖ Phân | loại      | yêu   | cầu | chức                 | năng | dựa       | trên  | ý nghĩa | sử  |
| ------ | --------- | ----- | --- | -------------------- | ---- | --------- | ----- | ------- | --- |
| dụng   | có 2      | nhóm  | yêu | cầu                  |      |           |       |         |     |
|        | Nhóm yêu  | cầu   |     |                      |      | Nhóm yêu  | cầu   |         |     |
|        |           |       |     |                      |      | khai thác | thông |         |     |
|        | tiếp nhận | thông |     |                      |      |           |       |         |     |
|        | tin       |       |     |                      |      | tin       |       |         |     |
|        |           |       |     | Software Engineering |      |           |       |         | 35  |
tkhuong@dthu.edu.vn

|       | Đặt      | vấn   | đề       |      |       |         |       |      |         |     |
| ----- | -------- | ----- | -------- | ---- | ----- | ------- | ----- | ---- | ------- | --- |
| ❖ Nếu | hệ       | thống | chỉ thỏa | mãn  | những | yêu     | cầu   | chức | năng    | thì |
| đã    | đủ chưa? |       |          |      |       |         |       |      |         |     |
| ❖ Ví  | dụ hệ    | thống | không    | tiện | dụng  | đối với | người |      | sử dụng | thì |
sao?
| ❖ Yêu | cầu | phi | chức năng | bao                  | gồm | những | vấn | đề  | gì? |     |
| ----- | --- | --- | --------- | -------------------- | --- | ----- | --- | --- | --- | --- |
|       |     |     |           | Software Engineering |     |       |     |     |     | 38  |
tkhuong@dthu.edu.vn

YÊU CẦU PHI CHỨC NĂNG
| ❖   | Là      | những |                                     | yêu  | cầu   | không   | liên | quan     |       | trực   | tiếp đến      |      | những |
| --- | ------- | ----- | ----------------------------------- | ---- | ----- | ------- | ---- | -------- | ----- | ------ | ------------- | ---- | ----- |
|     | dịch    | vụ    | mà                                  | hệ   | thống | cung    | cấp  | đến      | người |        | dùng.         |      |       |
| ❖   | Liên    | quan  |                                     | đến  | những | thuộc   |      | tính hệ  | thống |        | (độ tin       | cậy, | thời  |
|     | gian    | trả   | lời                                 | và   | yêu   | cầu về  | mặt  | lưu      | trữ)  |        | và các        | ràng | buộc  |
|     | (khả    | năng  |                                     | của  | thiết | bị      | vào  | ra, biểu |       | diễn   | dữ            | liệu | dùng  |
|     | trong   | các   |                                     | giao | diện  | với các |      | hệ thống |       | khác). |               |      |       |
|     | Yêu cầu |       | phi chức năng có thể quan trọng hơn |      |       |         |      |          |       |        | yêu cầu chức  |      |       |
năng!!
Nếu những yêu cầu này không đạt được, hệ thống sẽ trở nên vô
dụng.
|     |     |     |     |     |     | Software Engineering |     |     |     |     |     |     | 39  |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

Một số ví dụ - xét yc phi chức năng
❖ Tôi muốn pm giúp độc giả tra cứu sách muốn mượn, việc tra cứu
này phải được thực hiện ở bất kỳ nơi nào.
❖ Tôi muốn giúp tôi lập hóa đơn tiền điện và phải in được khoảng
20.000 hóa đơn của khu vực tp cao lãnh này chỉ diễn ra tối đa 1
ngày
❖ Tôi muốn pm giúp tra cứu các chuyến xe buýt trên địa bàn tỉnh đồng
tháp, việc tra cứu này được diễn ra trên sơ đồ của những tuyến xe
buýt
❖ …………………………………………
Software Engineering 40
tkhuong@dthu.edu.vn

|     |      | VD1. Yêu |      |       |      |           |     | cầu  | phi chức             |      |        |      |       | năng |       |           |        |
| --- | ---- | -------- | ---- | ----- | ---- | --------- | --- | ---- | -------------------- | ---- | ------ | ---- | ----- | ---- | ----- | --------- | ------ |
| ❖   | Xây  |          | dựng |       | phần |           | mềm |      | TouristTravel        |      |        |      |       | với  | các   | yêu       | cầu    |
|     | ràng |          | buộc |       | sau: |           |     |      |                      |      |        |      |       |      |       |           |        |
|     | ▪    | Hệ       |      | thống | cần  |           | là  | ứng  | dụng                 |      | Web,   |      | chạy  |      | được  | tại       | tất cả |
|     |      | các      |      | hệ    | điều | hành      |     | và   | hầu                  | hết  | các    |      | trình |      | duyệt |           |        |
|     | ▪    | Ứng      |      | dụng  |      | Web       |     | phải | triển                | khai |        | được |       | tại  | các   | server    | tiêu   |
|     |      | chuẩn    |      |       | như  | GlassFish |     |      | hoặc                 |      | Tomcat |      |       |      |       |           |        |
|     | ▪    | Hệ       |      | thống | phải |           | dễ  | sử   | dụng                 |      | – phải |      | đạt   | một  | test  | usability |        |
|     |      |          |      |       |      |           |     |      | Software Engineering |      |        |      |       |      |       |           | 41     |
tkhuong@dthu.edu.vn

| Phân | loại | yêu                  | cầu | phi chức           |     | năng              |
| ---- | ---- | -------------------- | --- | ------------------ | --- | ----------------- |
|      | •    | Những yêu cầu đặc tả |     | hay ràng buộc hành |     | vi của phần mềm.  |
•Ví dụ yêu cầu về hiệu năng của phần mềm liên quan đến tốc độ
YC SẢN PHẨM
|     | thực thi, | lượng bộ nhớ sử dụng, độ |     |     | tin cậy, ... |     |
| --- | --------- | ------------------------ | --- | --- | ------------ | --- |
• Những yc xuất phát từ các chính sách và thủ tục về mặt tổ chức.
•Vd: yc về quy trình hoạt động định nghĩa hệ thống được sử dụng?, yc
YC TỔ CHỨC
về quy trình phát triển đặc tả ngôn ngữ lập trình, môi trường phát
triển và chuẩn về quy trình được sử dụng...
• Những yêu cầu xuất phát từ những nhân tố bên ngoài ảnh hưởng
đến hệ thống và quy trình phát triển của nó.
YC BÊN NGOÀI
|     |     | •Ví dụ yêu | cầu về tương tác, yêu cầu về mặt pháp lý, ... |     |     |     |
| --- | --- | ---------- | --------------------------------------------- | --- | --- | --- |
Software Engineering 42
tkhuong@dthu.edu.vn

YÊU CẦU PHI CHỨC NĂNG
| ❖ Phân | loại yêu | cầu phi | chức | năng |
| ------ | -------- | ------- | ---- | ---- |
Software Engineering 43
tkhuong@dthu.edu.vn

|     |     | VD1. Yêu |      |        |        | cầu   |       |                      | phi chức |       |          | năng |     |           |      |     |
| --- | --- | -------- | ---- | ------ | ------ | ----- | ----- | -------------------- | -------- | ----- | -------- | ---- | --- | --------- | ---- | --- |
| ❖   | Yêu | cầu      | phi  | chức   |        | năng  | trong |                      | hệ thống |       | LIBSYS   |      |     |           |      |     |
|     | ▪   | Yêu      | cầu  | về     | sản    |       | phẩm: |                      | LIBSYS   |       | phải     | được |     | cài đặt   | bằng |     |
|     |     | HTML     |      | mà     | không  | có    | frame |                      | hoặc     | Java  | applets. |      |     |           |      |     |
|     | ▪   | Yêu      | cầu  | về     | mặt    | tổ    | chức: |                      | Quy      | trình | xây      | dựng |     | hệ thống  |      | và  |
|     |     | các      | tài  | liệu   | chuyển |       |       | giao                 | phải     | thoả  |          | mãn  | các | quy       | tắc  | đã  |
|     |     | được     | định |        | nghĩa  | trong |       | XYZCo-SP-STAN-95.    |          |       |          |      |     |           |      |     |
|     | ▪   | Yêu      | cầu  | ngoài: |        | Hệ    | thống |                      | không    |       | được     | để   | lộ  | các thông |      | tin |
|     |     | cá       | nhân | của    | khách  |       | hàng. |                      |          |       |          |      |     |           |      |     |
|     |     |          |      |        |        |       |       | Software Engineering |          |       |          |      |     |           |      | 44  |
tkhuong@dthu.edu.vn

VD2. Yêu cầu phi chức năng
❖ Yêu cầu phi chức năng trong hệ thống MHC-PMS
▪ Yêu cầu sản phẩm: Hệ thống MHC-PMS sẽ luôn hoạt động
để các phòng khám sử dụng trong suốt giờ làm việc (từ
thứ 2 đến thứ 6, 8.30 – 17.30). Thời gian ngừng hoạt động
trong suốt giờ làm việc sẽ không vượt quá sẽ không vượt
quá 5s trong bất kỳ ngày nào.
▪ Yêu cầu tổ chức: Người sử dụng hệ thống sẽ phải tự đăng
nhập bằng thẻ nhân viên của họ.
▪ Yêu cầu bên ngoài: Hệ thống sẽ cài đặt các quy định về
tính riêng tư của bệnh nhân.
Software Engineering 45
tkhuong@dthu.edu.vn

| Bài   |      | tập |     |      |      |        |     |          |
| ----- | ---- | --- | --- | ---- | ---- | ------ | --- | -------- |
| ❖ Xác | định | yêu | cầu | chức | năng | và yêu | cầu | phi chức |
| năng  | cho  | pm  | BT1 |      |      |        |     |          |
Software Engineering 46
tkhuong@dthu.edu.vn

NỘI DUNG
| 1   | YC CHỨC |     | NĂNG    | &   | YC PHI | CHỨC | NĂNG |
| --- | ------- | --- | ------- | --- | ------ | ---- | ---- |
|     | ĐẶC     | TẢ  | YÊU CẦU |     |        |      |      |
2
| 33  | QUY      | TRÌNH | CÔNG |      | NGHỆ | YÊU CẦU |     |
| --- | -------- | ----- | ---- | ---- | ---- | ------- | --- |
| 44  | THU      | THẬP  | VÀ   | PHÂN | TÍCH | YÊU     | CẦU |
| 5   | THẨM     | ĐỊNH  | YÊU  |      | CẦU  |         |     |
| 6   | QUẢN     | TRỊ   | YÊU  | CẦU  |      |         |     |
| 7   | TÀI LIỆU |       | YÊU  | CẦU  | PM   |         |     |
47
tkhuong@dthu.edu.vn

2. ĐẶC TẢ YÊU CẦU
❖ Khái niệm
❖ Tính chất
❖ Phương pháp
Software Engineering 48
tkhuong@dthu.edu.vn

|     |      | 2. ĐẶC TẢ YÊU CẦU – |           |        |       |        |       |                      |      |        |      |       | KHÁI NIỆM |       |       |        |      |
| --- | ---- | ------------------- | --------- | ------ | ----- | ------ | ----- | -------------------- | ---- | ------ | ---- | ----- | --------- | ----- | ----- | ------ | ---- |
| ❖   | Là   | tài                 | liệu      | mô     | tả    | chi    | tiết  |                      | các  | yêu    | cầu  |       | người     | dùng  |       | và     | yêu  |
|     | cầu  |                     | hệ thống. |        |       |        |       |                      |      |        |      |       |           |       |       |        |      |
| ❖   | Yêu  |                     | cầu       | người  |       | dùng   | phải  |                      | được |        | mô   | tả    | sao       | cho   | người |        | sử   |
|     |      |                     |           |        |       |        | Ai sẽ |                      | đọc  | tài    | liệu |       |           |       |       |        |      |
|     | dụng |                     | cuối      | và     | khách |        | hàng  |                      |      | (những |      | người |           | không |       | có     | kiến |
|     |      |                     |           |        |       |        | yêu   | cầu                  |      | này??? |      |       |           |       |       |        |      |
|     | thức |                     | về kỹ     | thuật) |       | có     | thể   | hiểu                 |      | được.  |      |       |           |       |       |        |      |
| ❖   | Yêu  |                     | cầu       | hệ     | thống | là     | những |                      |      | yêu    | cầu  | chi   | tiết      | và    | có    | thể    | bao  |
|     | gồm  |                     | những     |        | thông | tin    | về    | kỹ                   |      | thuật. |      |       |           |       |       |        |      |
| ❖   | Yêu  |                     | cầu có    | thể    |       | là một |       | phần                 |      | của    | hợp  | đồng. |           |       |       |        |      |
|     | ▪    | Do                  | đó        | việc   | đặc   | tả     | yêu   |                      | cầu  | hoàn   |      | chỉnh | đến       | mức   |       | có thể | là   |
|     |      | quan                | trọng.    |        |       |        |       |                      |      |        |      |       |           |       |       |        |      |
|     |      |                     |           |        |       |        |       | Software Engineering |      |        |      |       |           |       |       |        | 49   |
tkhuong@dthu.edu.vn

|     |     | 2. ĐẶC TẢ YÊU CẦU – |     |     |     |     |     |     |     |     |       | TÍNH CHẤT |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- | --- | --- |
| ❖   | Tài | liệu                |     | mô  | tả  | yêu |     | cầu | đòi | hỏi | phải: |           |     |     |     |     |
▪
|     |     | Đầy   |     | đủ:  | mọi   | yêu   |     | cầu | của   | người | dùng      | phải | được      | mô   | tả; |      |
| --- | --- | ----- | --- | ---- | ----- | ----- | --- | --- | ----- | ----- | --------- | ---- | --------- | ---- | --- | ---- |
|     | ▪   | Không |     | mâu  |       | thuẫn |     | với | nhau; |       |           |      |           |      |     |      |
|     | ▪   | Chính |     | xác: |       | yêu   | cầu |     | không | được  | hiểu      | mơ   | hồ, chỉ   | được |     | hiểu |
|     |     | theo  |     | một  | nghĩa |       | duy |     | nhất  | giữa  | các thành |      | viên tham |      | gia | xây  |
|     |     | dựng  |     | phần |       | mềm.  |     |     |       |       |           |      |           |      |     |      |
❖
|     | Một |     | đặc | tả   | yêu       | cầu   |      | tốt | cần                  | có:        |              |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --------- | ----- | ---- | --- | -------------------- | ---------- | ------------ | --- | --- | --- | --- | --- |
|     | ▪   | Ngữ |     | cảnh | (context) |       |      |     |                      |            |              |     |     |     |     |     |
|     | ▪   | Ứng |     | xử/  | ràng      |       | buộc |     | (behaviors/          |            | constraints) |     |     |     |     |     |
|     | ▪   | Có  | thể | kiểm |           | chứng |      |     | được                 | (testable) |              |     |     |     |     |     |
|     |     |     |     |      |           |       |      |     | Software Engineering |            |              |     |     |     |     | 50  |
tkhuong@dthu.edu.vn

|      | 2. ĐẶC TẢ YÊU CẦU – |      |        |        |        | PHƯƠNG PHÁP |
| ---- | ------------------- | ---- | ------ | ------ | ------ | ----------- |
| ❖ Có | 3 phương            |      | pháp   | để đặc | tả yêu | cầu         |
| ▪    | Dùng                | ngôn | ngữ tự | nhiên  |        |             |
▪
|     | Dùng | ngôn    | ngữ hình | thức |     |     |
| --- | ---- | ------- | -------- | ---- | --- | --- |
| ▪   | Dùng | mô hình |          |      |     |     |
Software Engineering 51
tkhuong@dthu.edu.vn

|     | Ngôn |     |     | ngữ | tự nhiên |     | – VD1 |
| --- | ---- | --- | --- | --- | -------- | --- | ----- |
❖ Một giáo viên yêu cầu viết phần mềm bài tập đại số hỗ trợ việc giải
| phương |     | trình |     | bậc hai như | sau: |     |     |
| ------ | --- | ----- | --- | ----------- | ---- | --- | --- |
▪ Phần mềm cho phép nhập các hệ số của phương trình ax2 + bx +
c = 0 (a,b,c là số thực khác 0) và tính toán cho ra kết quả theo
|     | quy | tắc         | giải | phương    | trình bậc | 2   |     |
| --- | --- | ----------- | ---- | --------- | --------- | --- | --- |
| Quy | tắc | giải phương |      | trình bậc | 2:        |     |     |
Cho phương trình bậc 2: ax2+bx+c=0 (với a,b,c là 3 số thực, a khac 0)
| Các      | bước | giải           | phương         | trình      | như sau: |          |        |
| -------- | ---- | -------------- | -------------- | ---------- | -------- | -------- | ------ |
| B1. Tính |      | delta = b2-4ac |                |            |          |          |        |
| B2. Xác  |      | đinh           | nghiệm         | theo delta |          |          |        |
|          |      | + Nếu          | delta<0: PT vô |            | nghiệm   |          |        |
|          |      | + Nếu          | delta=0: PT có |            | nghiệm   | kép x =x | =-b/2a |
1 2
|     |     | + Nếu | delta>0: PT có |            | 2 nghiệm   | phân | biệt |
| --- | --- | ----- | -------------- | ---------- | ---------- | ---- | ---- |
|     |     |       |                | x1=(-b-căn | delta)/ 2a |      |      |
|     |     |       |                | x2=(-b+căn | delta)/ 2a |      |      |
Software Engineering 52
tkhuong@dthu.edu.vn

|     |        | Ngôn |     |      | ngữ  |      |     | tự   | nhiên |     |      |      |      |     |        |       |      |     |
| --- | ------ | ---- | --- | ---- | ---- | ---- | --- | ---- | ----- | --- | ---- | ---- | ---- | --- | ------ | ----- | ---- | --- |
| ❖   | Yêu    | cầu  |     | được | viết | dưới |     | dạng | câu   |     | dùng |      | ngôn |     | ngữ tự | nhiên |      | với |
|     | sự     | hỗ   | trợ | của  |      | bảng | và  | biểu | đồ    | thì | dễ   | diễn |      | đạt | yêu    | cầu.  |      | Tuy |
|     | nhiên, |      | sử  | dụng |      | ngôn | ngữ | tự   | nhiên |     | sẽ   | có   | một  | số  | hạn    | chế   | như: |     |
▪ Không rõ ràng: tính chính xác rất khó đạt được nếu tài liệu khó
đọc;
|     | ▪   | Quá |     | mềm | dẻo: | cùng |     | một vấn | đề  | nhưng |     | có  | nhiều |     | cách | đặc | tả; |     |
| --- | --- | --- | --- | --- | ---- | ---- | --- | ------- | --- | ----- | --- | --- | ----- | --- | ---- | --- | --- | --- |
▪ Thiếu khả năng module hóa: cấu trúc ngôn ngữ tự nhiên không
|       |      | tương |     | xứng | với | cấu   | trúc   | của                  | các  | yêu | cầu  |     | hệ    | thống |         |     |       |     |
| ----- | ---- | ----- | --- | ---- | --- | ----- | ------ | -------------------- | ---- | --- | ---- | --- | ----- | ----- | ------- | --- | ----- | --- |
| →     | Ngôn |       | ngữ |      | tự  | nhiên | thường |                      | gây  |     | hiểu |     | nhầm, |       | và hiểu |     | không |     |
| thống |      | nhất  |     | giữa | các | thành |        | viên                 | tham | gia |      | xây | dựng  |       | phần    | mềm |       |     |
|       |      |       |     |      |     |       |        | Software Engineering |      |     |      |     |       |       |         |     |       | 54  |
tkhuong@dthu.edu.vn

|     |       | Ngôn  |      |       | ngữ |         | hình |      |        | thức |        |       |         |       |          |     |
| --- | ----- | ----- | ---- | ----- | --- | ------- | ---- | ---- | ------ | ---- | ------ | ----- | ------- | ----- | -------- | --- |
| ❖   | Yêu   |       | cầu  | được  |     | viết    | theo |      | chuẩn, |      |        | tương | tự      | ngôn  | ngữ      | lập |
|     | trình |       | hoặc | công  |     | thức    |      | toán | học.   |      |        |       |         |       |          |     |
|     | ▪     | Mô    | tả   | chính |     | xác     | rõ   | ràng |        | yêu  | cầu    | và    | kiểm    | chứng | tự động, |     |
|     |       | nhưng |      | phức  |     | tạp khó |      | diễn |        | đạt  | và hạn |       | chế khi | viết  | yêu cầu. |     |
❖
|     | Các |     | viết  | này | phù    | hợp     |     | với                  |     | một | số  | yêu | cầu, | ví dụ | yêu | cầu |
| --- | --- | --- | ----- | --- | ------ | ------- | --- | -------------------- | --- | --- | --- | --- | ---- | ----- | --- | --- |
|     | cho | hệ  | thống |     | nhúng. |         |     |                      |     |     |     |     |      |       |     |     |
| →   | Khó |     | hiểu, | khó |        | sử dụng |     |                      |     |     |     |     |      |       |     |     |
|     |     |     |       |     |        |         |     | Software Engineering |     |     |     |     |      |       |     | 55  |
tkhuong@dthu.edu.vn

|     |     | Đặc   |      | tả   |       | dùng |         | mô    | hình      |     |         |       |         |
| --- | --- | ----- | ---- | ---- | ----- | ---- | ------- | ----- | --------- | --- | ------- | ----- | ------- |
| ❖   | Yêu |       | cầu  | được |       | thể  | hiện    | dưới  | dạng      | ký  | hiệu    | hình  | vẽ, các |
|     | quy | tắc   | biểu |      | diễn, |      | các     | bước  | xây dựng  |     | và giải | thích |         |
| ❖   | Dễ  | hiểu, |      | ngắn |       | gọn, | súc     | tích  |           |     |         |       |         |
| ❖   | Ví  | dụ:   |      |      |       |      |         |       |           |     |         |       |         |
|     | ▪   | Mô    | hình |      | luồng |      | dữ liệu | DFD   |           |     |         |       |         |
|     | ▪   | Mô    | hình |      | thực  |      | thể kết | hợp   | ERD       |     |         |       |         |
|     | ▪   | Mô    | hình |      | phân  |      | tích    | hướng | đối tượng |     | UML     |       |         |
Software Engineering 56
tkhuong@dthu.edu.vn

|      | Ngôn      | ngữ     | mô  | hình             | – Ví               | dụ         |      |
| ---- | --------- | ------- | --- | ---------------- | ------------------ | ---------- | ---- |
| ❖ Sơ | đồ luồng  | dữ liệu | DFD |                  |                    |            |      |
|      | Giáo viên |         |     |                  |                    |            |      |
|      |           |         |     | Luồng            | dữ liệu            |            |      |
|      |           |         |     | D1:              | các hệ số          | a,b,c của  | tam  |
|      | D1        | D2      |     | thức bậc         | 2 P(x)=ax2+bx+c=0  |            |      |
|      |           |         |     | (a khác          | 0)                 |            |      |
|      |           |         |     | D2:              | Nghiệm             | của phương |      |
|      |           |         |     | trình P(x)=0 với |                    | 2 ký số    | thập |
Giải phương
phân
|     | trình bậc | 2   |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- |
Software Engineering 57
tkhuong@dthu.edu.vn

NỘI DUNG
| 1   | YC CHỨC |     | NĂNG    | &   | YC PHI | CHỨC | NĂNG |
| --- | ------- | --- | ------- | --- | ------ | ---- | ---- |
|     | ĐẶC     | TẢ  | YÊU CẦU |     |        |      |      |
2
| 33  | QUY      | TRÌNH | CÔNG |      | NGHỆ | YÊU CẦU |     |
| --- | -------- | ----- | ---- | ---- | ---- | ------- | --- |
| 44  | THU      | THẬP  | VÀ   | PHÂN | TÍCH | YÊU     | CẦU |
| 5   | THẨM     | ĐỊNH  | YÊU  |      | CẦU  |         |     |
| 6   | QUẢN     | TRỊ   | YÊU  | CẦU  |      |         |     |
| 7   | TÀI LIỆU |       | YÊU  | CẦU  | PM   |         |     |
58
tkhuong@dthu.edu.vn

3. QUY TRÌNH CÔNG NGHỆ YC (1) (nhắc lại)
| ❖ Khái | niệm | công | nghệ | yêu cầu |
| ------ | ---- | ---- | ---- | ------- |
| ❖ Hoạt | động | phân | tích | yêu cầu |
Software Engineering 59
tkhuong@dthu.edu.vn

|     | 3. QUY TRÌNH CÔNG NGHỆ YC (2) (nhắc |      |      |      |      |             |       |                      |     |          |        |     |      |      | lại) |
| --- | ----------------------------------- | ---- | ---- | ---- | ---- | ----------- | ----- | -------------------- | --- | -------- | ------ | --- | ---- | ---- | ---- |
| ❖   | Khái                                | niệm |      | công |      | nghệ        |       | yêu                  |     | cầu      |        |     |      |      |      |
|     | ▪ Requirements                      |      |      |      |      | engineering |       |                      |     | (RE)     |        |     |      |      |      |
|     | ▪ Tập                               |      | hợp  | các  |      | tác         | vụ    | và                   | kỹ  | thuật    | để dẫn |     | đến  | việc | hiểu |
|     | rõ                                  | các  | yêu  |      | cầu  | được        |       | gọi                  |     | là công  | nghệ   | yêu |      | cầu. |      |
|     | ▪ Đứng                              |      | ở    | góc  |      | độ          | quy   | trình                |     | phần     | mềm,   |     | công | nghệ | yêu  |
|     | cầu                                 | là   | hoạt |      | động |             | chính |                      | bắt | đầu      | trong  |     | suốt | hoạt | động |
|     | giao                                |      | tiếp | và   | tiếp |             | tục   | trong                |     | các hoạt | động   |     | mô   | hình | hóa. |
|     |                                     |      |      |      |      |             |       | Software Engineering |     |          |        |     |      |      | 60   |
tkhuong@dthu.edu.vn

3. QUY TRÌNH CÔNG NGHỆ YC (3) (nhắc lại)
| ❖   | Các   | hoạt   |      | động  |     | phân             |                  | tích yêu   | cầu? |         |               |       |     |
| --- | ----- | ------ | ---- | ----- | --- | ---------------- | ---------------- | ---------- | ---- | ------- | ------------- | ----- | --- |
|     | ▪     | Nghiên |      | cứu   |     | khả              | thi(Feasibility  |            |      | study); |               |       |     |
|     | ▪     | Thu    | thập |       | yêu | cầu(Requirements |                  |            |      |         | elicitation); |       |     |
|     | ▪     | Phân   | tích |       | yêu | cầu(Requirements |                  |            |      |         | analysis);    |       |     |
|     | ▪     | Thẩm   |      | định  |     | yêu              | cầu(Requirements |            |      |         | validation);  |       |     |
|     | ▪     | Quản   |      | trị   | yêu | cầu(Requirements |                  |            |      |         | management).  |       |     |
|     | Thực  |        | tế,  | RE    | là  | một              | hoạt             | động       | có   | tính    | lặp lại       | trong | đó  |
|     | những |        | quy  | trình |     | này              | đan              | xen nhau!! |      |         |               |       |     |
Software Engineering 61
tkhuong@dthu.edu.vn

3. QUY TRÌNH CÔNG NGHỆ YC (4) (nhắc lại)
Software Engineering 62
tkhuong@dthu.edu.vn

|     |     | Nghiên |        |        |       | cứu    |       | khả                  |      | thi    |       |     |        |        |      |       |       |
| --- | --- | ------ | ------ | ------ | ----- | ------ | ----- | -------------------- | ---- | ------ | ----- | --- | ------ | ------ | ---- | ----- | ----- |
| ❖   | Mục |        | tiêu   | của    |       | nghiên |       | cứu                  |      | khả    |       | thi | là     | đi     | đến  | kết   | luận: |
|     | Có  |        | nên    | phát   |       | triển  | hệ    | thống                |      |        | hay   |     | không? |        |      |       |       |
| ❖   | Một |        | nghiên |        | cứu   |        | ngắn, |                      | tập  | trung, |       |     | nhằm   |        | kiểm | tra   | xem   |
|     | ▪   | Hệ     | thống  |        | có    | đóng   |       | góp                  | cho  |        | các   |     | mục    | tiêu   | của  | tổ    | chức  |
|     |     | hay    |        | không? |       |        |       |                      |      |        |       |     |        |        |      |       |       |
|     | ▪   | Hệ     | thống  |        | có    | thể    | được  |                      | phát |        | triển |     | bằng   |        | công | nghệ  | hiện  |
|     |     | hành   |        | và     | trong | phạm   |       | vi                   | ngân |        | sách  |     | hay    | không? |      |       |       |
|     | ▪   | Hệ     | thống  |        | có    | thể    | được  |                      | tích |        | hợp   |     | với    | các    | hệ   | thống | khác  |
|     |     | đang   |        | được   |       | sử     | dụng  | hay                  |      | không? |       |     |        |        |      |       |       |
|     |     |        |        |        |       |        |       | Software Engineering |      |        |       |     |        |        |      |       | 64    |
tkhuong@dthu.edu.vn

|       | Câu | hỏi  | ôn  | tập    |     |     |      |     |          |
| ----- | --- | ---- | --- | ------ | --- | --- | ---- | --- | -------- |
| ❖ Yêu | cầu | phần | mềm | là gì? | Có  | mấy | loại | yêu | cầu phần |
mềm?
| ❖ Yêu    | cầu | chức | năng? | Yêu    | cầu  | phi | chức | năng? |        |
| -------- | --- | ---- | ----- | ------ | ---- | --- | ---- | ----- | ------ |
| ❖ Phương |     | pháp | mô    | tả tài | liệu | yêu | cầu  | (hồ   | sơ yêu |
cầu)?
| ❖ Các | hoạt | động | trong | quy | trình | công | nghệ | yêu | cầu? |
| ----- | ---- | ---- | ----- | --- | ----- | ---- | ---- | --- | ---- |
Software Engineering 66
tkhuong@dthu.edu.vn

NỘI DUNG
| 1   | YC CHỨC |     | NĂNG    | &   | YC PHI | CHỨC | NĂNG |
| --- | ------- | --- | ------- | --- | ------ | ---- | ---- |
|     | ĐẶC     | TẢ  | YÊU CẦU |     |        |      |      |
2
| 33  | QUY      | TRÌNH | CÔNG |      | NGHỆ | YÊU CẦU |     |
| --- | -------- | ----- | ---- | ---- | ---- | ------- | --- |
| 44  | THU      | THẬP  | VÀ   | PHÂN | TÍCH | YÊU     | CẦU |
| 5   | THẨM     | ĐỊNH  | YÊU  |      | CẦU  |         |     |
| 6   | QUẢN     | TRỊ   | YÊU  | CẦU  |      |         |     |
| 7   | TÀI LIỆU |       | YÊU  | CẦU  | PM   |         |     |
67
tkhuong@dthu.edu.vn

4. THU THẬP VÀ PHÂN TÍCH YC
| ❖ Các  | vấn  | đề khó | khăn  | thu thập | yêu cầu |
| ------ | ---- | ------ | ----- | -------- | ------- |
| ❖ Hoạt | động | quy    | trình | thu thập | yêu cầu |
| ❖ Lập  | danh | sách   | các   | yêu cầu  |         |
Software Engineering 68
tkhuong@dthu.edu.vn

THU THẬP YÊU CẦU
Khách hàng
Tôi muốn
….
Giải
thích về
…. Phân tích viên
Software Engineering 69
tkhuong@dthu.edu.vn

|     |       | Thu thập |       |     |        | yêu  |       | cầu |     |        |       |      |     |       |
| --- | ----- | -------- | ----- | --- | ------ | ---- | ----- | --- | --- | ------ | ----- | ---- | --- | ----- |
| ❖   | Quá   |          | trình | thu | thập   |      | yêu   | cầu | quá | quá    | trình | phối | hợp | giữa  |
|     | khách |          | hàng  |     | (người |      | dùng) |     | và  | chuyên | viên  | tin  | học | (phân |
|     | tích  | viên)    |       | để  | cùng   | hiểu |       | yêu | cầu | như    | nhau. |      |     |       |
| ❖   | Khách |          | hàng: |     |        |      |       |     |     |        |       |      |     |       |
|     | ▪     | Đưa      | ra    | các | yêu    | cầu; |       |     |     |        |       |      |     |       |
▪ Giải thích/ trình bày chi tiết về các nghiệp vụ có liên quan.
| ❖   | Chuyên |     |      | viên | tin học:  |       |      |      |        |     |      |     |     |     |
| --- | ------ | --- | ---- | ---- | --------- | ----- | ---- | ---- | ------ | --- | ---- | --- | --- | --- |
|     | ▪      | Tư  | vấn  | sự   | cần       | thiết | thực |      | sự của | yêu | cầu; |     |     |     |
|     | ▪      | Tìm | hiểu |      | về nghiệp |       | vụ   | liên | quan.  |     |      |     |     |     |
Software Engineering 70
tkhuong@dthu.edu.vn

|     |       | 4.1 Các |      |     |       | vấn | đề      | khó  |     | khăn |     |       | thu | thập  |     | yc    |
| --- | ----- | ------- | ---- | --- | ----- | --- | ------- | ---- | --- | ---- | --- | ----- | --- | ----- | --- | ----- |
| ❖   | Khách |         | hàng |     | không |     | biết họ | thật | sự  | cần  |     | gì;   |     |       |     |       |
| ❖   | Khách |         | hàng |     | diễn  | đạt | các     | yêu  | cầu | bằng |     | những |     | thuật | ngữ | riêng |
|     | của   | họ;     |      |     |       |     |         |      |     |      |     |       |     |       |     |       |
❖
|     | Các | khách |     | hàng |     | khác | nhau | có  | các |     | yêu | cầu | xung | đột | nhau; |     |
| --- | --- | ----- | --- | ---- | --- | ---- | ---- | --- | --- | --- | --- | --- | ---- | --- | ----- | --- |
❖ Các nhân tố về mặt tổ chức và chính trị có thể ảnh hưởng đến
|     | yêu | cầu  | hệ     | thống; |       |       |        |      |      |     |       |     |      |      |     |     |
| --- | --- | ---- | ------ | ------ | ----- | ----- | ------ | ---- | ---- | --- | ----- | --- | ---- | ---- | --- | --- |
| ❖   | Các | yêu  | cầu    |        | thay  | đổi   | trong  | suốt |      | quá | trình |     | phân | tích |     |     |
|     | ▪   | Phát | sinh   |        | các   | khách | hàng   | mới  |      |     |       |     |      |      |     |     |
|     | ▪   | Môi  | trường |        | doanh |       | nghiệp | thay | đổi. |     |       |     |      |      |     |     |
Software Engineering 71
tkhuong@dthu.edu.vn

|      | 4.2 Hoạt |           | động     | quy | trình | thu         | thập | yc (1) |
| ---- | -------- | --------- | -------- | --- | ----- | ----------- | ---- | ------ |
| ❖ Mô | hình     | xoắn      | ốc trong | quy | trình | thu thập    | yêu  | cầu    |
|      |          |           |          |     | Đánh  | giá độ ưu   | tiên |        |
|      |          | Phân loại | và tổ    |     |       |             |      |        |
|      |          |           |          |     | và    | thương thảo |      |        |
chức
Prioritization and
Classification and
negotiation
organization
|     |     | Phát hiện | mới |     | Viết          | tài liệu |     |     |
| --- | --- | --------- | --- | --- | ------------- | -------- | --- | --- |
|     |     | Discovery |     |     | Documentation |          |     |     |
Software Engineering 72
tkhuong@dthu.edu.vn

|     |      | 4.2 Hoạt |     |     |     | động |     | quy | trình |     | thu |     | thập | yc (2) |
| --- | ---- | -------- | --- | --- | --- | ---- | --- | --- | ----- | --- | --- | --- | ---- | ------ |
| ❖   | Phát | hiện     |     | yêu | cầu |      |     |     |       |     |     |     |      |        |
▪
|     |      | Tương |     | tác | với | khách | hàng | để  | tìm ra | yêu | cầu | của | họ. |     |
| --- | ---- | ----- | --- | --- | --- | ----- | ---- | --- | ------ | --- | --- | --- | --- | --- |
| ❖   | Phân | loại  |     | và  | tổ  | chức  |      |     |        |     |     |     |     |     |
▪ Phân nhóm các yêu cầu có liên quan đến nhau và tổ chức chúng
|     |     | thành | các |     | cụm | có quan |     | hệ gắn | kết | với | nhau. |     |     |     |
| --- | --- | ----- | --- | --- | --- | ------- | --- | ------ | --- | --- | ----- | --- | --- | --- |
❖ Đặt thứ tự ưu tiên và giải quyết mâu thuẫn giữa các yêu cầu
|     | ▪             | Xếp     | thứ | tự    |     | ưu tiên |     | cho các | yêu  | cầu | và  | giải | quyết | các xung |
| --- | ------------- | ------- | --- | ----- | --- | ------- | --- | ------- | ---- | --- | --- | ---- | ----- | -------- |
|     |               | đột/mâu |     | thuẫn |     | giữa    | các | yêu     | cầu. |     |     |      |       |          |
| ❖   | Documentation |         |     |       |     | – Viết  | tài | liệu    |      |     |     |      |       |          |
▪ Ghi lại các yêu cầu làm tài liệu đầu vào cho vòng xoắn tiếp theo.
tkhuong@dthu.edu.vn

| Phát |     | hiện | yêu | cầu | (1) |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
❖
| Quy | trình | thu thập | thông                | tin   | về hệ thống | đề xuất | và   | các |
| --- | ----- | -------- | -------------------- | ----- | ----------- | ------- | ---- | --- |
| hệ  | thống | sẵn có,  | gạn lọc              | ra    | các yêu cầu | người   | dùng | và  |
| yêu | cầu   | hệ thống | từ các               | thông | tin này.    |         |      |     |
|     |       |          | Software Engineering |       |             |         |      | 74  |
tkhuong@dthu.edu.vn

|     |       | Thu thập      |        |       |       |       | yêu   |        |                      | cầu   |        | từ     |           | đâu? (2) |       |       |     |
| --- | ----- | ------------- | ------ | ----- | ----- | ----- | ----- | ------ | -------------------- | ----- | ------ | ------ | --------- | -------- | ----- | ----- | --- |
| ❖   | Làm   |               | việc   | với   | khách |       |       | hàng   |                      | để    | tìm    |        | hiểu      | thông    | tin   | về    |     |
|     | ▪     | Miền          | ứng    |       | dụng, |       |       |        |                      |       |        |        |           |          |       |       |     |
|     | ▪     | Các           | dịch   |       | vụ    | mà    | hệ    | thống  |                      | cần   |        | cung   | cấp       | và       |       |       |     |
|     | ▪     | Các           | ràng   |       | buộc  |       | về    | vận    | hành                 |       | hệ     | thống. |           |          |       |       |     |
| ❖   | Những |               | người  |       |       | có    | thể   | cần    |                      | tham  |        | gia:   | khách     |          | hàng, | người | sử  |
|     | dụng, |               | lập    | trình |       | viên, |       | chuyên |                      |       | gia    | kĩ     | thuật,... |          |       |       |     |
|     | ▪     | stakeholders. |        |       |       |       |       |        |                      |       |        |        |           |          |       |       |     |
| ❖   | Tài   | liệu          | về     | hoạt  |       | động  |       | doanh  |                      |       | nghiệp |        |           |          |       |       |     |
| ❖   | Đặc   |               | tả của | các   |       | hệ    | thống |        |                      | tương |        | tự.    |           |          |       |       |     |
|     |       |               |        |       |       |       |       |        | Software Engineering |       |        |        |           |          |       |       | 75  |
tkhuong@dthu.edu.vn

|       | Các      | phương      |          |          | pháp                 | thu   | thập      | và phân |            | tích | yc  |
| ----- | -------- | ----------- | -------- | -------- | -------------------- | ----- | --------- | ------- | ---------- | ---- | --- |
| ❖ Lấy | yêu      |             | cầu      |          |                      |       |           |         |            |      |     |
|       | ▪ Phỏng  |             | vấn      |          |                      |       |           |         |            |      |     |
|       | ▪ Quan   |             | sát      |          |                      |       |           |         |            |      |     |
|       | ▪ Điều   | tra         | bằng     | bảng     | câu                  | hỏi   |           |         |            |      |     |
|       | ▪ Nghiên |             | cứu      | tài liệu |                      |       |           |         |            |      |     |
|       | ▪ Joint  | Application |          |          | Design               | – JAD |           |         |            |      |     |
|       | ▪ Làm    | bản         | mẫu      |          |                      |       |           |         |            |      |     |
| ❖ Đặc |          | tả yêu      | cầu      |          |                      |       |           |         |            |      |     |
|       | ▪ Danh   |             | mục các  | khái     | niệm                 |       |           |         |            |      |     |
|       | ▪ Mô     | hình        | hóa/Dùng |          | ký pháp              | đồ    | hoạ (kịch | bản     | - usecase) |      |     |
|       |          |             |          |          | Software Engineering |       |           |         |            |      | 78  |
tkhuong@dthu.edu.vn

|     |     | 4.3 Lập |     |      |        | danh  |      | sách                 |     | yêu |      | cầu  |     |     |     |      |
| --- | --- | ------- | --- | ---- | ------ | ----- | ---- | -------------------- | --- | --- | ---- | ---- | --- | --- | --- | ---- |
| ❖   | Mục | tiêu:   |     |      | xác    | định  |      | rõ các               |     | bộ  | phận | hỗ   | trợ | tin | học | hóa, |
|     | các | nghiệp  |     |      | vụ     | sẽ    | được |                      | hỗ  | trợ | và   | mức  | độ  | hỗ  | trợ |      |
| ❖   | Kết | quả:    |     | Danh |        | sách  |      | các                  |     | yêu | cầu  | phần |     | mềm | với | các  |
|     | yêu | cầu:    |     |      |        |       |      |                      |     |     |      |      |     |     |     |      |
|     | ▪   | Yêu     | cầu |      | nghiệp |       | vụ   |                      |     |     |      |      |     |     |     |      |
|     | ▪   | Yêu     | cầu |      | chất   | lượng |      |                      |     |     |      |      |     |     |     |      |
|     | ▪   | Yêu     | cầu |      | hệ     | thống |      |                      |     |     |      |      |     |     |     |      |
|     |     |         |     |      |        |       |      | Software Engineering |     |     |      |      |     |     |     | 79   |
tkhuong@dthu.edu.vn

| Yêu    | cầu  | nghiệp    | vụ  |
| ------ | ---- | --------- | --- |
| ❖ Công | việc |           |     |
| ❖ Biểu | mẫu  |           |     |
| ❖ Quy  | định |           |     |
| ❖ Công | thức |           |     |
| ❖ Cách | thức | tiến hành |     |
Software Engineering 80
tkhuong@dthu.edu.vn

| Yêu | cầu | chất | lượng |
| --- | --- | ---- | ----- |
❖
| Tính   | tiến  | hóa   |     |
| ------ | ----- | ----- | --- |
| ❖ Tính | hiệu  | quả   |     |
| ❖ Tính | dễ sử | dụng  |     |
| ❖ Tính | tương | thích |     |
Software Engineering 81
tkhuong@dthu.edu.vn

| Yêu    | cầu | hệ   | thống |
| ------ | --- | ---- | ----- |
| ❖ Tính | an  | toàn |       |
| ❖ Tính | bảo | mật  |       |
Software Engineering 82
tkhuong@dthu.edu.vn

NỘI DUNG
| 1   | YC CHỨC |     | NĂNG    | &   | YC PHI | CHỨC | NĂNG |
| --- | ------- | --- | ------- | --- | ------ | ---- | ---- |
|     | ĐẶC     | TẢ  | YÊU CẦU |     |        |      |      |
2
| 33  | QUY      | TRÌNH | CÔNG |      | NGHỆ | YÊU CẦU |     |
| --- | -------- | ----- | ---- | ---- | ---- | ------- | --- |
| 44  | THU      | THẬP  | VÀ   | PHÂN | TÍCH | YÊU     | CẦU |
| 5   | THẨM     | ĐỊNH  | YÊU  |      | CẦU  |         |     |
| 6   | QUẢN     | TRỊ   | YÊU  | CẦU  |      |         |     |
| 7   | TÀI LIỆU |       | YÊU  | CẦU  | PM   |         |     |
83
tkhuong@dthu.edu.vn

5. THẨM ĐỊNH YÊU CẦU
| ❖ Thẩm | định     | yêu           | cầu là chứng    | tỏ rằng | các  | yêu      | cầu định |
| ------ | -------- | ------------- | --------------- | ------- | ---- | -------- | -------- |
| nghĩa  | được     | hệ thống      | mà khách        | hàng    | thực | sự muốn. |          |
| ❖ Tiêu | chí thẩm | định          |                 |         |      |          |          |
| ▪ Hiệu | lực      | – Validity    |                 |         |      |          |          |
| ▪ Nhất | quán     | – Consistency |                 |         |      |          |          |
| ▪ Đầy  | đủ -     | completeness  |                 |         |      |          |          |
| ▪ Thực | tế       | - Realism     |                 |         |      |          |          |
| ▪ Kiểm | định     | được          | - Verifiability |         |      |          |          |
Software Engineering 84
tkhuong@dthu.edu.vn

5. THẨM ĐỊNH YÊU CẦU (2)
❖
| Phương |       |           | pháp  | thẩm  |            | định |                      | yêu         | cầu   |     |          |       |        |         |      |
| ------ | ----- | --------- | ----- | ----- | ---------- | ---- | -------------------- | ----------- | ----- | --- | -------- | ----- | ------ | ------- | ---- |
| ▪      | Xem   | xét       | lại   | yêu   | cầu        |      | (Requirements        |             |       |     | reviews) |       |        |         |      |
|        | −     | Phân      | tích  |       | một        | cách | có                   | hệ          | thống | các | yêu      | cầu   | (không |         | dùng |
|        |       | công      | cụ    | tự    | động);     |      | lấy                  | ý           | kiến  | của | khách    | hàng; |        | tiến    | hành |
|        |       | thường    |       | xuyên |            |      |                      |             |       |     |          |       |        |         |      |
| ▪      | Phiên |           | bản   | thử   | nghiệm     |      | (Prototyping)        |             |       |     |          |       |        |         |      |
|        | −     | Sử        | dụng  | một   | mô         | hình |                      | chạy        | được  |     | của hệ   | thống |        | để kiểm | tra  |
|        |       | các       | yêu   | cầu.  |            |      |                      |             |       |     |          |       |        |         |      |
| ▪      | Sinh  | test-case |       |       | (test-case |      |                      | generation) |       |     |          |       |        |         |      |
|        | −     | Phát      | triển |       | các        | test | cho                  | các         | yêu   | cầu | để       | kiểm  | tra    | khả     | năng |
|        |       | test      | được  | hay   | không.     |      |                      |             |       |     |          |       |        |         |      |
|        |       |           |       |       |            |      | Software Engineering |             |       |     |          |       |        |         | 85   |
tkhuong@dthu.edu.vn

6. QUẢN TRỊ YÊU CẦU (1)
|     |     |        | Yêu  | cầu   | phần |        | mềm  | luôn     | luôn | thay | đổi! |
| --- | --- | ------ | ---- | ----- | ---- | ------ | ---- | -------- | ---- | ---- | ---- |
| ❖   | Môi | trường |      | doanh |      | nghiệp | và   | kĩ thuật | thay | đổi  |      |
|     | ▪   | Phần   | cứng | mới   |      | → giao | diện | mới.     |      |      |      |
▪ Luật thay đổi, nhu cầu doanh nghiệp thay đổi → thay đổi chức
năng
| ❖   | Khách |      | hàng, | người |      | sử  | dụng | thay đổi |     |     |     |
| --- | ----- | ---- | ----- | ----- | ---- | --- | ---- | -------- | --- | --- | --- |
|     | ▪     | Thay | đổi   | chức  | năng |     |      |          |     |     |     |
❖ Xung đột giữa các yêu cầu mới nảy sinh, và giữa yêu cầu mới
|     | với | yêu | cầu | cũ  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 86
tkhuong@dthu.edu.vn

|     |     | Quản  |       | lý     | yêu   |      | cầu                  |       |      |              |         |        |     |       |       |      |          |
| --- | --- | ----- | ----- | ------ | ----- | ---- | -------------------- | ----- | ---- | ------------ | ------- | ------ | --- | ----- | ----- | ---- | -------- |
| ❖   | Để  | quản  | lý    | yêu    | cầu,  |      | cần                  | xác   | định |              |         |        |     |       |       |      |          |
|     | ▪   | Định  | danh  |        | yêu   | cầu: | Mỗi                  | yêu   | cầu  |              | có định | danh   |     | riêng |       | để   | tiện     |
|     |     | cho   | việc  | tham   | chiếu |      | giữa                 | các   |      | yêu          | cầu     | và lần |     | vết   |       |      |          |
|     | ▪   | Quy   | trình |        | quản  | lý   | thay                 | đổi:  |      | các          | hoạt    | động   |     | đánh  |       | giá  | ảnh      |
|     |     | hưởng |       | và chi | phí   | của  | thay                 |       | đổi  |              |         |        |     |       |       |      |          |
|     | ▪   | Chính |       | sách   | lần   | vết: | cách                 |       | ghi  | lại          | và lưu  |        | trữ | quan  |       | hệ   | giữa     |
|     |     | các   | yêu   | cầu    | và    | giữa | mỗi                  |       | yêu  | cầu          | với     | thiết  |     | kế    | tương |      | ứng      |
|     |     | với   | nó    |        |       |      |                      |       |      |              |         |        |     |       |       |      |          |
|     | ▪   | Công  | cụ    | hỗ     | trợ:  | hỗ   | trợ                  | thực  |      | hiện         | các     | công   |     | việc  |       | trên | một      |
|     |     | cách  | có    | hiệu   | quả.  |      | CASE                 | tool, |      | spreadsheet, |         |        | cơ  | sở    | dữ    |      | liệu.... |
|     |     |       |       |        |       |      | Software Engineering |       |      |              |         |        |     |       |       |      | 87       |
tkhuong@dthu.edu.vn

Quản lý thay đổi
Xác định
vấn đề
| Phân | tích vấn | đề,  | Phân | tích thay   | đổi | Thực hiện  |
| ---- | -------- | ---- | ---- | ----------- | --- | ---------- |
| đặc  | tả thay  | đổi  |      | &           |     | thay đổi   |
|      |          |      | đánh | giá chi phí |     |            |
Yêu cầu đã
chỉnh sửa
tkhuong@dthu.edu.vn

|       | Đặt   | vấn |     | đề   |     |                      |     |     |          |     |     |          |     |
| ----- | ----- | --- | --- | ---- | --- | -------------------- | --- | --- | -------- | --- | --- | -------- | --- |
| ❖ Sau | khi   | đã  | xác | định |     | yêu                  | cầu |     | hệ thống |     | và  | yêu      | cầu |
| của   | người |     | sử  | dụng | hệ  | thống                |     | thì | tiếp     | tục | làm | gì?      |     |
| ❖ Cấu | trúc  | của |     | một  | tài | liệu                 | đặc |     | tả yêu   |     | cầu | hệ thống |     |
| gồm   | những |     | nội | dung |     | gì?                  |     |     |          |     |     |          |     |
|       |       |     |     |      |     | Software Engineering |     |     |          |     |     |          | 90  |
tkhuong@dthu.edu.vn

7. CÁCH VIẾT TÀI LIỆU YÊU CẦU
❖
|     | Tài    | liệu  | yêu      |      | cầu    | phần   |                      | mềm   |       | là yêu  |      | cầu   | chính |      | thức  | về   |
| --- | ------ | ----- | -------- | ---- | ------ | ------ | -------------------- | ----- | ----- | ------- | ---- | ----- | ----- | ---- | ----- | ---- |
|     | những  |       | gì mà    |      | đội    | phát   | triển                |       | hệ    | thống   | phải |       | cài   | đặt. |       |      |
| ❖   | Nên    | bao   | gồm      |      | cả     | định   |                      | nghĩa |       | yêu cầu |      | người |       | dùng | và    | đặc  |
|     | tả yêu |       | cầu      | hệ   | thống. |        |                      |       |       |         |      |       |       |      |       |      |
| ❖   | Đây    | không |          | phải |        | là tài | liệu                 |       | thiết | kế,     | chỉ  | nên   |       | định | nghĩa | về   |
|     | cái    | gì    | hệ thống |      |        | sẽ hỗ  |                      | trợ,  | chứ   | không   |      | đi    | vào   | chi  | tiết  | việc |
|     | mô     | tả    | cài đặt  |      | như    | thế    | nào.                 |       |       |         |      |       |       |      |       |      |
|     |        |       |          |      |        |        | Software Engineering |       |       |         |      |       |       |      |       | 91   |
tkhuong@dthu.edu.vn

7. CÁCH VIẾT TÀI LIỆU YÊU CẦU
| ❖ Tài | liệu | đặc tả   | yêu cầu dựa | theo | chuẩn | IEEE |
| ----- | ---- | -------- | ----------- | ---- | ----- | ---- |
| 1.    | Giới | thiệu    |             |      |       |      |
| 2.    | Mô   | tả chung |             |      |       |      |
| 3.    | Yêu  | cầu chi  | tiết        |      |       |      |
| 4.    | Phụ  | lục (nếu | có)         |      |       |      |
Software Engineering 93
tkhuong@dthu.edu.vn

|      | Tài  | liệu      | đặc      | tả yc | chuẩn   | IEEE (1) |
| ---- | ---- | --------- | -------- | ----- | ------- | -------- |
| 1.   | Giới | thiệu     |          |       |         |          |
| 1.1. | Mục  | đích      |          |       |         |          |
| 1.2. | Phạm | vi        |          |       |         |          |
| 1.3. | Định | nghĩa     | (thuật   | ngữ,  | từ viết | tắt)     |
| 1.4. | Tài  | liệu tham | khảo     |       |         |          |
| 1.5. | Mô   | tả cấu    | trúc tài | liệu  |         |          |
Software Engineering 94
tkhuong@dthu.edu.vn

|      | Tài   | liệu  | đặc   | tả yc    | chuẩn | IEEE (2) |
| ---- | ----- | ----- | ----- | -------- | ----- | -------- |
| 2.   | Mô tả | chung |       |          |       |          |
| 2.1. | Tổng  | quan  | về    | sản phẩm |       |          |
| 2.2. | Chức  | năng  | sản   | phẩm     |       |          |
| 2.3. | Đối   | tượng | người | dùng     |       |          |
| 2.4. | Ràng  | buộc  | tổng  | thể      |       |          |
| 2.5. | Giả   | thiết | và sự | lệ thuộc |       |          |
Software Engineering 95
tkhuong@dthu.edu.vn

|          | Tài | liệu |       | đặc  |      | tả   | yc chuẩn | IEEE (2) |
| -------- | --- | ---- | ----- | ---- | ---- | ---- | -------- | -------- |
| 3.       | Yêu | cầu  | chi   |      | tiết | (1)  |          |          |
| 3.1.     | Yêu | cầu  | chức  |      | năng |      |          |          |
| 3.1.1.   | Yêu | cầu  |       | chức |      | năng | 1        |          |
| 3.1.1.1. |     | Giới | thiệu |      |      |      |          |          |
| 3.1.1.2. |     | Dữ   | liệu  | vào  |      |      |          |          |
| 3.1.1.3. |     | Xử   | lý    |      |      |      |          |          |
| 3.1.1.4. |     | Kết  | quả   |      |      |      |          |          |
| 3.1.2.   | Yêu | cầu  |       | chức |      | năng | 2        |          |
………………
Software Engineering 96
tkhuong@dthu.edu.vn

| Tài    |       | liệu | đặc    |       | tả yc | chuẩn |      | IEEE (2) |      |
| ------ | ----- | ---- | ------ | ----- | ----- | ----- | ---- | -------- | ---- |
| 3. Yêu |       | cầu  | chi    | tiết  | (2)   |       |      |          |      |
| 3.2.   | Yêu   | cầu  | giao   | diện  | ngoài |       |      |          |      |
| 3.2.1. | Giao  | diện | người  |       | dùng  |       |      |          |      |
| 3.2.2. | Giao  | diện | phần   |       | cứng  |       |      |          |      |
| 3.2.3. | Giao  | diện | phần   |       | mềm   |       |      |          |      |
| 3.2.4. | Giao  | diện | truyền |       | thông |       |      |          |      |
| 3.3.   | Yêu   | cầu  | hiệu   | suất  |       |       |      |          |      |
| 3.4.   | Ràng  | buộc |        | thiết | kế    |       |      |          |      |
| 3.5.   | Thuộc | tính | (tính  |       | bảo   | mật,  | tính | bảo      | trì) |
| 3.6.   | Các   | yêu  | cầu    | khác  |       |       |      |          |      |
| Phụ    | lục   |      |        |       |       |       |      |          |      |
Software Engineering 97
tkhuong@dthu.edu.vn

|          | Câu    |      | hỏi    |      |     |       |       |       |       |      |      |          |      |
| -------- | ------ | ---- | ------ | ---- | --- | ----- | ----- | ----- | ----- | ---- | ---- | -------- | ---- |
| 1) Phân  |        | tích | yêu    | cầu  |     | nghĩa | là    | gì?   |       |      |      |          |      |
| 2) Mục   | tiêu   |      | của    | phân |     | tích  | yêu   | cầu   | là    | gì?  |      |          |      |
| 3) Các   | công   |      | đoạn   |      | của | quy   | trình |       | phân  | tích |      | yêu cầu? |      |
| 4) Những |        | khó  |        | khăn | của |       | phân  | tích  | yêu   |      | cầu? |          |      |
| 5) Có    | những  |      | loại   | yêu  |     | cầu   | nào?  |       |       |      |      |          |      |
| 6) Nêu   | những  |      |        | yêu  | cầu | phi   | chức  |       | năng? |      |      |          |      |
| 7) Nêu   | các    |      | nguyên |      | lý  | của   | phân  |       | tích  | yêu  | cầu? |          |      |
| 8) Các   | phương |      |        | pháp |     | thu   | thập  | thông |       | tin  | cho  | các yêu  | cầu? |
| 9) Đặc   | tả     | yêu  |        | cầu  | cần | có    | những |       | tính  | chất |      | gì?      |      |
Software Engineering 98
tkhuong@dthu.edu.vn

|          | Câu  | hỏi     |      |         |         |      |       |         |      |
| -------- | ---- | ------- | ---- | ------- | ------- | ---- | ----- | ------- | ---- |
| 1) Nội   | dung | thẩm    | định | yêu cầu | là gì?  |      |       |         |      |
| 2) Các   |      | phương  | pháp | mô hình | hóa để  | phân | tích  | yêu cầu | là   |
| những    |      | phương  | pháp | nào?    |         |      |       |         |      |
| 3) Trình |      | bày nội | dung | đặc tả  | yêu cầu | theo | chuẩn | IEEE    | 830- |
1998
| 4) Ai | sẽ  | sử dụng | tài liệu | yêu cầu?             |     |     |     |     |     |
| ----- | --- | ------- | -------- | -------------------- | --- | --- | --- | --- | --- |
|       |     |         |          | Software Engineering |     |     |     |     | 99  |
tkhuong@dthu.edu.vn

BÀI TẬP
| ❖ Hãy | thu thập | và phân | tích | yêu | cầu theo | các đề | tài đã |
| ----- | -------- | ------- | ---- | --- | -------- | ------ | ------ |
chọn
| ▪ Viết | tài liệu | đặc tả | yêu cầu              | theo | chuẩn | IEEE |     |
| ------ | -------- | ------ | -------------------- | ---- | ----- | ---- | --- |
|        |          |        | Software Engineering |      |       |      | 100 |
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C3_YeuCauPM.md -->

---


<!-- BẮT ĐẦU FILE: C4_MoHinhHoaPM.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 4
MÔ HÌNH HÓA
PHẦN MỀM
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM MÔ HÌNH HÓA
MÔ HÌNH NGHIỆP VỤ
MÔ
HÌNH
HÓA PM
MÔ HÌNH QUAN NIỆM
MÔ HÌNH YÊU CẦU
Software Engineering 2
tkhuong@dthu.edu.vn

MỤC TIÊU
❖ Hiểu được mô hình hoá hệ thống là gì? Và tại sao phải mô
hình hoá hệ thống.
❖ Phân biệt được các mô hình hệ thống.
❖ Có khả năng lựa chọn và ứng dụng các mô hình hệ thống vào
từng trường hợp cụ thể
❖ Lập hồ sơ phân tích yêu cầu bằng mô hình UseCase
Software Engineering 3
tkhuong@dthu.edu.vn

|     | Các   |      | giai |        | đoạn | phân         | tích  | yêu  | cầu |
| --- | ----- | ---- | ---- | ------ | ---- | ------------ | ----- | ---- | --- |
| ❖   | Khảo  | sát  | hiện | trạng  |      |              |       |      |     |
|     | ▪ Tìm | hiểu | về   | nghiệp | vụ   | hiện nay của | khách | hàng |     |
| ❖   | Xác   | định | yêu  | cầu    |      |              |       |      |     |
▪ Thỏa thuận với khách hàng về các nghiệp vụ sẽ hỗ trợ thực hiện
|     | trên | máy   | tính |      |     |     |     |     |     |
| --- | ---- | ----- | ---- | ---- | --- | --- | --- | --- | --- |
| ❖   | Lập  | hồ sơ | phân | tích | yêu | cầu |     |     |     |
▪ Sử dụng một phương pháp phân tích yêu cầu cụ thể để trình bày
|     | hồ  | sơ  | phân | tích | yêu cầu |     |     |     |     |
| --- | --- | --- | ---- | ---- | ------- | --- | --- | --- | --- |
Software Engineering 4
tkhuong@dthu.edu.vn

| Nhắc | lại Xác | định | yêu | cầu |
| ---- | ------- | ---- | --- | --- |
Khách hàng
|     |     |     | Tôi muốn |     |
| --- | --- | --- | -------- | --- |
….
Giải
thích về
|     | ….  |     | Phân | tích viên |
| --- | --- | --- | ---- | --------- |
Software Engineering 5
tkhuong@dthu.edu.vn

| Phân      | tích | yêu | cầu |     |     |
| --------- | ---- | --- | --- | --- | --- |
| Phân tích | viên |     |     |     |     |
Hồ sơ
phân tích
Thắc
mắc về
|     | ….  |     |     | Phụ trách | thiết kế |
| --- | --- | --- | --- | --------- | -------- |
Software Engineering 6
tkhuong@dthu.edu.vn

|     |     |     |      |     | Yêu     | cầu: mô | tả      | về nghiệp |       | vụ f đang |      | thực | hiện |     |     |
| --- | --- | --- | ---- | --- | ------- | ------- | ------- | --------- | ----- | --------- | ---- | ---- | ---- | --- | --- |
| ❖   | Hồ  | sơ  | phân |     | tích    | yêu     |         | cầu       | là    | gì?       |      |      |      |     |     |
|     |     |     |      |     | - Thông |         | tin của | đối       | tượng | X         |      |      |      |     |     |
|     |     |     |      |     | - Các   | bước    |         | tiến hành |       | nghiệp    | vụ f |      |      |     |     |
▪ Tài liệu mô tả ngắn gọn, chính xác và đầy đủ các yêu cầu của
|     |     |       |     |     | - Quy | tắc | xử  | lý nghiệp |     | vụ f |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | người |     | sử  | dụng. |     |     |           |     |      |     |     |     |     |     |
Mong muốn về nghiệp vụ f sẽ được hỗ trợ khi thực hiện trên máy tính
|     |       |      |      |       | - Vị  | trí     | sử dụng, giao |              |       | diện     |      |      |       |          |     |
| --- | ----- | ---- | ---- | ----- | ----- | ------- | ------------- | ------------ | ----- | -------- | ---- | ---- | ----- | -------- | --- |
|     | ▪     | Tài  | liệu | thống |       | nhất    |               | chung        |       | của nhóm |      | phát | triển | phần     | mềm |
|     |       |      |      |       | - Tốc | độ, bào |               | mật, an toàn |       |          |      |      |       |          |     |
|     | ▪     | Tài  | liệu | được  |       | sử      | dụng          |              | chính | trong    |      | giai | đoạn  | thiết kế |     |
| ❖   | Ngôn  |      | ngữ  | xây   |       | dựng    |               | hồ           | sơ    | phân     | tích | yêu  | cầu:  |          |     |
|     | ▪     | Ngôn |      | ngữ   | tự    | nhiên   |               |              |       |          |      |      |       |          |     |
|     | ▪     | Ngôn |      | ngữ   | mô    | hình    |               | hóa          |       |          |      |      |       |          |     |
| ❖   | Trình |      | bày  | hồ    | sơ    | phân    |               | tích         |       | yêu      | cầu  | như  | thế   | nào?     |     |
▪ Có rất nhiều cách khác nhau để trình bày một hồ sơ phân tích
|     |     | yêu | cầu      | phụ |      | thuộc |      | vào  |     |         |         |     |         |     |     |
| --- | --- | --- | -------- | --- | ---- | ----- | ---- | ---- | --- | ------- | ------- | --- | ------- | --- | --- |
|     |     |     | • Phương |     | pháp |       | phân | tích |     | yêu cầu | được    |     | sử dụng |     |     |
|     |     |     | • Quy    | ước |      | riêng | của  | từng |     | công    | ty dịch | vụ  | phần    | mềm |     |
Software Engineering 7
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
| ❖ Mô | hình | hóa là cách | dùng   | hệ thống |      | ký hiệu | để mô   | tả nhiều |
| ---- | ---- | ----------- | ------ | -------- | ---- | ------- | ------- | -------- |
| khía | cạnh | của vấn     | đề một | cách     | ngắn | gọn     | và trực | quan     |
| ❖ Ví | dụ   |             |        |          |      |         |         |          |
Software Engineering 8
tkhuong@dthu.edu.vn

VD MÔ HÌNH HÓA
| ❖   | Mô tả   | theo  | toàn     |         | diện:     |        |      |     |
| --- | ------- | ----- | -------- | ------- | --------- | ------ | ---- | --- |
|     | ▪ Không |       | chi tiết |         | và chuyên |        | sâu  |     |
|     | ▪ Không |       | nhấn     | mạnh    |           | đặc    | điểm |     |
|     | ▪ Không |       | mô       | tả được |           | sự vật | phức | tạp |
| ❖   | Mô tả   | theo  | góc      | nhìn:   |           |        |      |     |
|     | ▪ Tập   | trung |          | mô tả   | một       | phần   |      |     |
|     | ▪ Thể   | hiện  | một      | khía    | cạnh      |        |      |     |
|     | ▪ Làm   | nổi   | bật      | một     | đặc       | điểm   |      |     |
|     | → Hiệu  | quả   |          | hơn.    |           |        |      |     |
Software Engineering 9
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
| ❖   | Mô  | hình | hóa  | phần     |      | mềm |      |       |          |           |         |
| --- | --- | ---- | ---- | -------- | ---- | --- | ---- | ----- | -------- | --------- | ------- |
|     | ▪   | Mô   | hình | hóa      | phần | mềm | theo | nhiều | góc nhìn | khác nhau | từ tổng |
|     |     | quát | đến  | chi tiết |      |     |      |       |          |           |         |
▪ Làm nổi bật một khía cạnh của phần mềm, giúp cho tất cả thành
|     |     | viên | trong | nhóm   |      | tham   | gia xây | dựng | phần mềm | hiểu được | chức |
| --- | --- | ---- | ----- | ------ | ---- | ------ | ------- | ---- | -------- | --------- | ---- |
|     |     | năng | của   | một    | hệ   | thống. |         |      |          |           |      |
| ❖   | Các | khía | cạnh  |        | mô   | hình   | hóa     | phần | mềm      |           |      |
|     | ▪   | Mô   | hình  | nghiệp | vụ   |        |         |      |          |           |      |
|     | ▪   | Mô   | hình  | quan   | niệm |        |         |      |          |           |      |
|     | ▪   | Mô   | hình  | yêu    | cầu  |        |         |      |          |           |      |
Software Engineering 10
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
| ❖ Một | số phương                         | pháp | mô hình   | hóa yêu | cầu phần | mềm | thông |
| ----- | --------------------------------- | ---- | --------- | ------- | -------- | --- | ----- |
| dụng  | hiện nay:                         |      |           |         |          |     |       |
| ▪     | DFD (Data Flow Diagram)           |      |           |         |          |     |       |
| ▪     | ERD (Entity Relationship Diagram) |      |           |         |          |     |       |
| ▪     | UML (Unified Modelling            |      | Language) |         |          |     |       |
Software Engineering 11
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
| ❖ UML (Unified Modelling |                                           |      |      |      | Language) |       |      |           |           |      |
| ------------------------ | ----------------------------------------- | ---- | ---- | ---- | --------- | ----- | ---- | --------- | --------- | ---- |
| ▪ Là                     | ngôn                                      | ngữ  | mô   | hình | hóa       | hướng |      | đối tượng |           |      |
| ▪ Được                   | thừa                                      | nhận |      | như  | một       | chuẩn |      | mặc định  | của ngành | CNTT |
| ▪ Có                     | nhiều                                     | công | cụ   | và   | phương    |       | pháp | dựa trên  | UML       |      |
|                          | • Enterprise Architecture / Rational Rose |      |      |      |           |       |      |           |           |      |
|                          | • Rational Unified Process (RUP)          |      |      |      |           |       |      |           |           |      |
| ▪ Gồm                    | 4+1 góc                                   |      | nhìn | với  | các       | sơ    | đồ:  |           |           |      |
Software Engineering 12
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
Software Engineering 13
tkhuong@dthu.edu.vn

1. KHÁI NIỆM MÔ HÌNH HÓA
Software Engineering 14
tkhuong@dthu.edu.vn

2. MÔ HÌNH NGHIỆP VỤ
| ❖ Sơ | đồ ngữ  | cảnh | (Context diagram) |
| ---- | ------- | ---- | ----------------- |
| ❖ Sơ | đồ hoạt | động |                   |
Software Engineering 15
tkhuong@dthu.edu.vn

2. MÔ HÌNH NGHIỆP VỤ
| ❖   | Sơ  | đồ   | ngữ  |       | cảnh  | (Context diagram) |            |     |      |        |        |
| --- | --- | ---- | ---- | ----- | ----- | ----------------- | ---------- | --- | ---- | ------ | ------ |
|     | ▪   | Thể  | hiện |       | môi   | trường            | xung quanh |     | phần | mềm    |        |
|     |     | •    | Xác  | định  | giới  | hạn               | của phần   | mềm |      |        |        |
|     | ▪   | Diễn | tả   | tương |       | tác với           | các thành  |     | phần | liên   | quan   |
|     |     | •    | Sự   | phụ   | thuộc | giữa              | hệ thống   | với | mội  | trường | của nó |
Software Engineering 16
tkhuong@dthu.edu.vn

| Sơ đồ | ngữ | cảnh | của | hệ thống | ngân | hàng |
| ----- | --- | ---- | --- | -------- | ---- | ---- |
http://www.ibm.com/developerworks/vn/library/ar-archdoc2/
Software Engineering 17
tkhuong@dthu.edu.vn

| VD. Sơ | đồ ngữ   | cảnh   | của       | HT ATM |
| ------ | -------- | ------ | --------- | ------ |
|        | Ngữ cảnh | của hệ | thống ATM |        |
Software Engineering 19
tkhuong@dthu.edu.vn

2. MÔ HÌNH NGHIỆP VỤ
| ❖ Sơ | đồ  | luồng    | dữ        | liệu (DFD)         |         |       |          |
| ---- | --- | -------- | --------- | ------------------ | ------- | ----- | -------- |
| ❖ Sơ | đồ  | hoạt     | động      | (Activity diagram) |         |       |          |
| ▪    | Mô  | tả trình | tự        | xử lý công         | việc    |       |          |
| ▪    | Làm | rõ       | quy trình | nghiệp             | vụ của  | doanh | nghiệp   |
| ▪    | Làm | rõ       | sự luân   | chuyển             | dữ liệu | trong | hệ thống |
| ▪    | Mô  | tả thuật | toán      |                    |         |       |          |
Software Engineering 20
tkhuong@dthu.edu.vn

Software Engineering 21
tkhuong@dthu.edu.vn

3. MÔ HÌNH QUAN NIỆM
| ❖ Sơ | đồ thực    | thể kết | hợp   |
| ---- | ---------- | ------- | ----- |
| ❖ Mô | hình hướng | đối     | tượng |
Software Engineering 22
tkhuong@dthu.edu.vn

3. MÔ HÌNH QUAN NIỆM
| ❖ Sơ | đồ thực   | thể  | - kết hợp | (ERD)        |         |
| ---- | --------- | ---- | --------- | ------------ | ------- |
| ▪    | Mô tả mối | liên | hệ giữa   | các thực thể | dữ liệu |
▪ Được sử dụng trong thiết kế CSDL và thường được cài đặt trong
|     | CSDL quan | hệ  |     |     |     |
| --- | --------- | --- | --- | --- | --- |
Software Engineering 23
tkhuong@dthu.edu.vn

3. MÔ HÌNH QUAN NIỆM
| ❖ Ví | dụ Sơ | đồ thực | thể | - kết hợp | (ERD) |
| ---- | ----- | ------- | --- | --------- | ----- |
Software Engineering 24
tkhuong@dthu.edu.vn

3. MÔ HÌNH QUAN NIỆM
| ❖ Ví | dụ Sơ | đồ thực | thể | - kết hợp | của LIBSYS |
| ---- | ----- | ------- | --- | --------- | ---------- |
Software Engineering 25
tkhuong@dthu.edu.vn

Software Engineering 26
tkhuong@dthu.edu.vn

3. MÔ HÌNH QUAN NIỆM
| ❖ Mô | hình | hướng |     | đối tượng |     |     |     |     |     |
| ---- | ---- | ----- | --- | --------- | --- | --- | --- | --- | --- |
▪ Mô hình đối tượng phản ánh các thực thể trong thế giới thực
|     | được  | vận | dụng | trong | hệ     | thống. Mô   | tả hệ thống           | dựa vào | lớp đối |
| --- | ----- | --- | ---- | ----- | ------ | ----------- | --------------------- | ------- | ------- |
|     | tượng | và  | các  | quan  | hệ của | nó. Một lớp | đối tượng là sự trừu  |         |         |
tượng hoá trên một tập các đối tượng có thuộc tính và phương
|       | thức | chung.    |     |       |     |     |     |     |     |
| ----- | ---- | --------- | --- | ----- | --- | --- | --- | --- | --- |
| ❖ Các | mô   | hình      | đối | tượng | gồm |     |     |     |     |
| ▪     | Mô   | hình thừa |     | kế    |     |     |     |     |     |
| ▪     | Mô   | hình kết  | hợp |       |     |     |     |     |     |
| ▪     | Mô   | hình ứng  | xử  |       |     |     |     |     |     |
Software Engineering 27
tkhuong@dthu.edu.vn

| Mô  | hình | đối | tượng | - thừa | kế  |
| --- | ---- | --- | ----- | ------ | --- |
❖ Mô hình thừa kế tổ chức các lớp đối tượng theo một cấu trúc
phân cấp
Software Engineering 28
tkhuong@dthu.edu.vn

| Mô  | hình | đối | tượng | – kết | hợp |
| --- | ---- | --- | ----- | ----- | --- |
❖ Mô hình kết hợp biểu diễn cách cấu tạo của một lớp từ
các lớp khác
Software Engineering 29
tkhuong@dthu.edu.vn

Software Engineering 30
tkhuong@dthu.edu.vn

Software Engineering 31
tkhuong@dthu.edu.vn

|               | Mô     | hình     |       | đối      | tượng                |          | – ứng   | xử    |          |     |
| ------------- | ------ | -------- | ----- | -------- | -------------------- | -------- | ------- | ----- | -------- | --- |
| ❖ Mô hình ứng |        |          | xử mô | tả tương |                      | tác giữa | các đối | tượng | nhằm     | tạo |
| ra            | một số | ứng      | xử cụ | thể      | của                  | hệ thống | mà đã   | được  | xác định |     |
| như           | là một | use case |       |          |                      |          |         |       |          |     |
|               |        |          |       |          | Software Engineering |          |         |       |          | 32  |
tkhuong@dthu.edu.vn

|          | Mô  | hình        | đối  | tượng |          | – ứng    | xử  |
| -------- | --- | ----------- | ---- | ----- | -------- | -------- | --- |
| ❖ VD: mô | tả  | use case sử | dụng | Rút   | tiền của | hệ thống | ATM |
Software Engineering 33
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖ Phương         | pháp     | Use Case |
| ---------------- | -------- | -------- |
| ❖ Sơ đồ Use Case |          |          |
| ❖ Đặc tả         | Use Case |          |
Software Engineering 35
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖   | Phương |     | pháp |     | Use Case |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
▪ Mô tả yêu cầu dựa trên PP phân tích tình huống, đưa ra một tập
|     |     | kịch  | bản  | tương  |      | tác   | giữa  | một  | hoặc    |       | vài tác | nhân (actor) với | hệ  |
| --- | --- | ----- | ---- | ------ | ---- | ----- | ----- | ---- | ------- | ----- | ------- | ---------------- | --- |
|     |     | thống | nhằm |        | thực |       | hiện  | một  | mục     | tiêu  | chung   |                  |     |
| ❖   | Các | kịch  | bản  |        | nên  | bao   | gồm   |      |         |       |         |                  |     |
|     | ▪   | Một   | miêu | tả     | về   | tình  | huống |      | ban đầu |       |         |                  |     |
|     | ▪   | Một   | miêu | tả     | về   | luồng | sự    | kiện |         | thông | thường  |                  |     |
|     | ▪   | Một   | miêu | tả     | về   | những |       | trục | trặc    | gì    | có thể  | xảy ra           |     |
|     | ▪   | Thông |      | tin về | các  | hoạt  | động  |      | xảy     | ra    | đồng    | thời             |     |
|     | ▪   | Một   | miêu | tả     | về   | trạng | thái  | khi  | kịch    | bản   | kết     | thúc             |     |
Software Engineering 36
tkhuong@dthu.edu.vn

Kịch bản LIBSYS (1)
Initial Assumption: Người dùng đã đăng nhập hệ thống LIBSYS và đã
tìm thấy tạp chí có đăng tài liệu cần tìm.
Normal:
•Người dùng chọn tài liệu cần copy. Hệ thống sẽ yêu cầu người dùng
nhập thông tin thuê bao hoặc chọn cách trả phí dùng tài liệu. Có thể
thanh toán bằng thẻ tín dụng hoặc dùng số tài khoản của một tổ chức.
•Sau đó người dùng được yêu cầu điền một form bản quyền trong đó
có chi tiết về giao dịch này, rồi submit form đó cho hệ thống LIBSYS.
•Hệ thống kiểm tra form bản quyền, nếu OK, bản PDF của tài liệu sẽ
được tải xuống máy tính của người dùng và người dùng được thông
báo về việc này. Sau đó người dùng được chọn một máy in, và tài liệu
sẽ được in tại đó. Nếu tài liệu đã được gắn cờ ‘print-only’ thì nó sẽ
được xóa khỏi máy của người dùng ngay sau khi người dùng khẳng
định rằng đã in xong.
tkhuong@dthu.edu.vn

|     | Kịch | bản |     | LIBSYS (2) |     |     |     |
| --- | ---- | --- | --- | ---------- | --- | --- | --- |
What can go wrong:
•Người dùng có thể điền form sai. Khi đó hệ thống cần hiện lại form để
người dùng sửa lại. Nếu form được submit sau đó vẫn sai thì hủy yêu
| cầu đọc | tài liệu | của | người | dùng.  |     |     |     |
| ------- | -------- | --- | ----- | ------ | --- | --- | --- |
•Hệ thống có thể không chấp nhận giao dịch thanh toán tiền. Hủy yêu
| cầu đọc | tài liệu | của | người | dùng.  |     |     |     |
| ------- | -------- | --- | ----- | ------ | --- | --- | --- |
•Việc download tài liệu có thể thất bại. Làm lại cho đến khi thành công
| hoặc | khi người | dùng | chấm | dứt phiên | làm | việc. |     |
| ---- | --------- | ---- | ---- | --------- | --- | ----- | --- |
•Có thể không in được tài liệu. Nếu bài báo không có gắn cờ ‘print-
only’ thì giữ nó trong workspace của LIBSYS. Nếu không, xóa tài liệu
| và hoàn                     | lại chi phí | cho | người | dùng.        |     |          |            |
| --------------------------- | ----------- | --- | ----- | ------------ | --- | -------- | ---------- |
| Other activities: Song song |             |     |       | download các |     | tài liệu | khác nhau. |
System state on completion: Người dùng đang ở trạng thái đăng
nhập. Nếu tài liệu có gắn cờ 'print-only' thì nó đã bị xóa khỏi LIBSYS
workspace.
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖ Sơ đồ | Use Case |         |      |          |                     |        |
| ------- | -------- | ------- | ---- | -------- | ------------------- | ------ |
| ▪ Sơ    | đồ mô    | tả tổng | quan | các chức | năng (Use case) của | một hệ |
thống và ai dùng chức năng nào (Actor), sử dụng ngôn ngữ UML.
❖ Sử dụng Đặc tả Use case (văn bản), Sơ đồ hoạt động (Activity
| Diagram), Sơ |     | đồ tuần  | tự  | (Sequence Diagram) để |     | bổ sung chi  |
| ------------ | --- | -------- | --- | --------------------- | --- | ------------ |
| tiết cho     | các | Use case |     |                       |     |              |
Software Engineering 39
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
❖ Sơ đồ Use Case
▪ Ký hiệu:
Actor Use Case
Software Engineering 40
tkhuong@dthu.edu.vn

|      |     | VD1. Giải |     |     |     |       | phương |     |        | trình |     | bậc |     | 2   |
| ---- | --- | --------- | --- | --- | --- | ----- | ------ | --- | ------ | ----- | --- | --- | --- | --- |
| Phân |     | tích      | yêu |     | cầu | (ngôn | ngữ    | tự  | nhiên) |       |     |     |     |     |
❖ Giáo viên muốn có phần mềm hỗ trợ học sinh tự rèn luyện bài
|     | tập | Giải |     | phương |        | trình | bậc   | 2 với | các | thông | tin như |     | sau: |     |
| --- | --- | ---- | --- | ------ | ------ | ----- | ----- | ----- | --- | ----- | ------- | --- | ---- | --- |
|     | ▪   | Hỗ   | trợ | giải   | phương |       | trình | bậc   | 2   |       |         |     |      |     |
• Học sinh nhập vào các hệ số a,b,c (a khác 0), phần mềm cho ra kết
|     |     |     | quả    | nghiệm |       | của | phương  | trình | với      | 2 ký số | thập  | phân   |     |     |
| --- | --- | --- | ------ | ------ | ----- | --- | ------- | ----- | -------- | ------- | ----- | ------ | --- | --- |
|     | ▪   | Tự  | rèn    | luyện  |       |     |         |       |          |         |       |        |     |     |
|     |     |     | • Học  | sinh   | nhập  |     | vào các | hệ    | số a,b,c | (a khác | 0) và | nghiệm |     | của |
|     |     |     | phương |        | trình | vừa | nhập    |       |          |         |       |        |     |     |
• Phần mềm cho kết quả đánh giá nghiệm đúng sai, nếu sai thì hiển
|     |     |     | thị | nghiệm |     | đúng |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 41
tkhuong@dthu.edu.vn

| VD1. Giải | phương | trình        | bậc | 2   |
| --------- | ------ | ------------ | --- | --- |
|           |        | Giải phương  |     |     |
|           |        | trình bậc    | 2   |     |
|           |        | Tự rèn luyện |     |     |
Học sinh
Software Engineering 42
tkhuong@dthu.edu.vn

|      | VD2. Quản |     |     |       | lý nhân |        | viên |     |     |
| ---- | --------- | --- | --- | ----- | ------- | ------ | ---- | --- | --- |
| Phân | tích yêu  |     | cầu | (Ngôn | ngữ tự  | nhiên) |      |     |     |
❖ Người dùng muốn phần mềm quản lý nhân viên cho phép thực hiện
| các    | chức | năng |     | như sau: |     |     |     |     |     |
| ------ | ---- | ---- | --- | -------- | --- | --- | --- | --- | --- |
| ❖ Nhân | viên |      |     |          |     |     |     |     |     |
▪ Quản lý hồ sơ nhân viên (Thêm mới, cập nhật, xóa) dựa theo BM1
▪ Tra cứu hồ sơ nhân viên: cho phép nhập vào tên hoặc địa chỉ, hoặc trình
độ của nhân viên và sau đó phần mềm sẽ xuất ra danh sách các nhân
|     | viên | (thông | tin hồ | sơ  | nhân | viên khi | tra cứu | theo | BM1) |
| --- | ---- | ------ | ------ | --- | ---- | -------- | ------- | ---- | ---- |
▪ Lập báo cáo thống kê: yêu cầu lập báo cáo thông kê theo BM2
❖ Ban giám đốc: chỉ sử dụng 1 chức năng là cập nhật quy định tiếp
| nhận  | nhận      |      | nhân | viên | mới        |      |      |     |            |
| ----- | --------- | ---- | ---- | ---- | ---------- | ---- | ---- | --- | ---------- |
| Ghi   | chú: chưa | xem  | xét  | hết  | tất cả các | chức | năng |     |            |
| → Hãy | mô        | hình | hóa  | phân | tích yêu   | cầu  | bằng | sơ  | đồ Usecase |
Software Engineering 43
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
❖ Sơ đồ Use Case
Software Engineering 45
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖ Sơ | đồ Use Case nâng | cấp |
| ---- | ---------------- | --- |
Software Engineering 46
tkhuong@dthu.edu.vn

Software Engineering 47
tkhuong@dthu.edu.vn

|       | Mô  | tả            | Use-Case hệ |      | thống |
| ----- | --- | ------------- | ----------- | ---- | ----- |
| ❖ Đặc | tả  | Use Case (văn |             | bản) |       |
▪ Mô tả chi tiết tương tác giữa người dùng (actor) với các chức
|     | năng | của hệ | thống | (Use Case) |     |
| --- | ---- | ------ | ----- | ---------- | --- |
Software Engineering 54
tkhuong@dthu.edu.vn

|       | Mô  | tả Use-Case hệ | thống |
| ----- | --- | -------------- | ----- |
| ❖ Mẫu | đặc | tả Use Case:   |       |
tkhuong@dthu.edu.vn

|           | Mô  | tả Use-Case hệ   |       | thống |
| --------- | --- | ---------------- | ----- | ----- |
| ❖ VD1 đặc |     | tả Use-case Giao | dịch: |       |
tkhuong@dthu.edu.vn

|           | Mô  | tả Use-Case hệ   |      | thống |
| --------- | --- | ---------------- | ---- | ----- |
| ❖ VD1 đặc |     | tả Use-case Giao | dịch | (tt): |
tkhuong@dthu.edu.vn

|           | Mô  | tả Use-Case hệ  |       | thống |
| --------- | --- | --------------- | ----- | ----- |
| ❖ VD2 đặc |     | tả Use-case Rút | tiền: |       |
tkhuong@dthu.edu.vn

| Mô        | tả Use-Case hệ  |            | thống |
| --------- | --------------- | ---------- | ----- |
| ❖ VD2 đặc | tả Use-case Rút | tiền (tt): |       |
tkhuong@dthu.edu.vn

|      |      | VD1. Giải |       |     | phương |        |     | trình | bậc | 2   |
| ---- | ---- | --------- | ----- | --- | ------ | ------ | --- | ----- | --- | --- |
| Phân | tích | yêu cầu   | (ngôn |     | ngữ tự | nhiên) |     |       |     |     |
❖ Giáo viên muốn có phần mềm hỗ trợ học sinh tự rèn luyện bài tập Giải phương
|     | trình | bậc 2 với | các    | thông | tin như |     | sau: |     |     |     |
| --- | ----- | --------- | ------ | ----- | ------- | --- | ---- | --- | --- | --- |
|     | ▪ Hỗ  | trợ giải  | phương |       | trình   | bậc | 2    |     |     |     |
Học sinh nhập vào các hệ số a,b,c (a khác 0), phần mềm cho ra kết quả nghiệm của
|     | phương | trình     | với | 2 ký số | thập | phân |     |     |     |     |
| --- | ------ | --------- | --- | ------- | ---- | ---- | --- | --- | --- | --- |
|     | ▪ Tự   | rèn luyện |     |         |      |      |     |     |     |     |
Học sinh nhập vào các hệ số a,b,c (a khác 0) và nghiệm của phương trình vừa nhập
Phần mềm cho kết quả đánh giá nghiệm đúng sai, nếu sai thì hiển thị nghiệm đúng
|     |     |     |     |     |     |     |     | Giải phương |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
|     |     |     |     |     |     |     |     | trình bậc   | 2   |     |
Học sinh
|     |     |     |     |     |     |     |     | Tự rèn | luyện |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- |
Hãy đặc tả UseCase Giải Phương trình bậc 2, Usecase Tự rèn luyện
Software Engineering 60
tkhuong@dthu.edu.vn

| Quy tắc | giải phương |     | trình bậc | 2:  |     |     |
| ------- | ----------- | --- | --------- | --- | --- | --- |
Cho phương trình bậc 2: ax2+bx+c=0 (với a,b,c là 3 số thực, a khác 0)
| Các bước | giải           | phương         | trình      | như sau: |          |        |
| -------- | -------------- | -------------- | ---------- | -------- | -------- | ------ |
| B1. Tính | delta = b2-4ac |                |            |          |          |        |
| B2. Xác  | đinh           | nghiệm         | theo delta |          |          |        |
|          | + Nếu          | delta<0: PT vô |            | nghiệm   |          |        |
|          | + Nếu          | delta=0: PT có |            | nghiệm   | kép x =x | =-b/2a |
1 2
|     | + Nếu | delta>0: PT có |     | 2 nghiệm   | phân biệt |     |
| --- | ----- | -------------- | --- | ---------- | --------- | --- |
|     |       | x =(-b-căn     |     | delta)/ 2a |           |     |
1
|     |     | x =(-b+căn |     | delta)/ 2a |     |     |
| --- | --- | ---------- | --- | ---------- | --- | --- |
2
Software Engineering 61
tkhuong@dthu.edu.vn

|      | VD2. Quản |     |       |     | lý nhân |        | viên |     |
| ---- | --------- | --- | ----- | --- | ------- | ------ | ---- | --- |
| Phân | tích yêu  | cầu | (Ngôn |     | ngữ tự  | nhiên) |      |     |
❖ Người dùng muốn phần mềm quản lý nhân viên cho phép thực hiện
| các    | chức | năng | như | sau: |     |     |     |     |
| ------ | ---- | ---- | --- | ---- | --- | --- | --- | --- |
| ❖ Nhân | viên |      |     |      |     |     |     |     |
▪ Quản lý hồ sơ nhân viên (Thêm mới, cập nhật, xóa) dựa theo BM1
▪ Tra cứu hồ sơ nhân viên: cho phép nhập vào tên hoặc địa chỉ, hoặc trình
độ của nhân viên và sau đó phần mềm sẽ xuất ra danh sách các nhân
|     | viên | (thông | tin hồ | sơ  | nhân | viên khi | tra cứu theo | BM1) |
| --- | ---- | ------ | ------ | --- | ---- | -------- | ------------ | ---- |
▪ Lập báo cáo thống kê: yêu cầu lập báo cáo thông kê theo BM2
❖ Ban giám đốc: chỉ sử dụng 1 chức năng là cập nhật quy định tiếp
| nhận | nhận      | nhân |     | viên | mới        |      |      |     |
| ---- | --------- | ---- | --- | ---- | ---------- | ---- | ---- | --- |
| Ghi  | chú: chưa | xem  | xét | hết  | tất cả các | chức | năng |     |
Software Engineering 62
tkhuong@dthu.edu.vn

|                     | VD2. Quản        |     |      |      |            | lý  | nhân |                                       | viên  |     |     |       |       |     |       |
| ------------------- | ---------------- | --- | ---- | ---- | ---------- | --- | ---- | ------------------------------------- | ----- | --- | --- | ----- | ----- | --- | ----- |
|                     |                  |     |      |      |            |     |      | BM2                             Thống |       |     |     | kê    | trình | độ  |       |
| BM1      Hồ         |                  | sơ  | nhân | viên |            |     |      |                                       |       |     |     |       |       |     |       |
|                     |                  |     |      |      |            |     |      |                                       | Trình | độ  | Số  | lượng |       |     | Tỷ lệ |
| Họ và               | tên: ………… Giới   |     |      |      | tính: ………  |     |      |                                       |       |     |     |       |       |     |       |
|                     |                  |     |      |      |            |     |      | Trung                                 | cấp   |     |     |       |       |     |       |
| Ngày                | sinh: ………... Địa |     |      |      | chỉ: ……….. |     |      |                                       |       |     |     |       |       |     |       |
| Đơn vị: …………… Trình |                  |     |      |      | độ: ……….   |     |      | Cao đẳng                              |       |     |     |       |       |     |       |
Ghi chú:
|           |         |        |           |        |           |        |     | Đại     | học       |             |      |         |      |     |     |
| --------- | ------- | ------ | --------- | ------ | --------- | ------ | --- | ------- | --------- | ----------- | ---- | ------- | ---- | --- | --- |
| - Tuổi    | nhân    |        | viên      | theo   | quy       | định   |     |         |           |             |      |         |      |     |     |
|           |         |        |           |        |           |        |     | Sau     | đại       | học         |      |         |      |     |     |
| Nam từ    |         | 18 đến |           | 60, Nữ | từ        | 18 đến | 55  |         |           |             |      |         |      |     |     |
| - Công    | ty      | có     | 5 đơn     | vị     | và chỉ    | chấp   |     | Ghi     | chú:      |             |      |         |      |     |     |
|           |         |        |           |        |           |        |     | Số      | lượng: Số | lượng       | nhân | viên    |      |     |     |
| nhận      | 4 trình |        | độ: Trung |        | cấp, Cao  |        |     |         |           |             |      |         |      |     |     |
|           |         |        |           |        |           |        |     | Tỷ      | lệ = Số   | lượng/ Tổng |      | số nhân | viên |     |     |
| đẳng, Đại |         |        | học, Sau  |        | đại học   |        |     |         |           |             |      |         |      |     |     |
| → Hãy     |         | đặc    | tả        | hoạt   | động      | của    | các | Usecase |           |             |      |         |      |     |     |
Software Engineering 63
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖ Sơ | đồ tuần | tự  |
| ---- | ------- | --- |
tkhuong@dthu.edu.vn

4. MÔ HÌNH YÊU CẦU
| ❖ Sơ | đồ Tuần | tự  |
| ---- | ------- | --- |
Software Engineering 74
tkhuong@dthu.edu.vn

| VD1. Giải | phương | trình | bậc | 2   |
| --------- | ------ | ----- | --- | --- |
Software Engineering 76
tkhuong@dthu.edu.vn

| VD2. Quản | lý nhân | viên |
| --------- | ------- | ---- |
Software Engineering 77
tkhuong@dthu.edu.vn

Bài tập
| 1) PM xếp | loại  | học     | lực học | sinh |     |
| --------- | ----- | ------- | ------- | ---- | --- |
| a) Vẽ     | sơ đồ | UseCase |         |      |     |
b) Chọn 1 UseCase để: đặc tả UseCase, Activity, Sequence, Class
Diagram
| 2) PM tính   | tiền | thuê   | phòng  | khách | sạn |
| ------------ | ---- | ------ | ------ | ----- | --- |
| 3) PM Quản   |      | lý học | sinh   |       |     |
| 4) PM Quản   |      | lý thu | chi    |       |     |
| 5) PM quản   | lý   | nhập   | xuất   |       |     |
| 6) PM quản   | lý   | khách  | sạn    |       |     |
| 7) PM QL thư |      | viện   | trường |       |     |
Software Engineering 78
tkhuong@dthu.edu.vn

|      |     | Đề   |     | BT1. Xếp |       |     |     | loại |        | học | lực | của | học | sinh |
| ---- | --- | ---- | --- | -------- | ----- | --- | --- | ---- | ------ | --- | --- | --- | --- | ---- |
| Phân |     | tích | yêu | cầu      | (Ngôn |     | ngữ | tự   | nhiên) |     |     |     |     |      |
❖ Với yêu cầu lập bảng xếp loại học lực, phần mềm bao gồm các
|     | người |     | sử   | dụng | và    | chức |      | năng   | như | sau: |        |      |     |     |
| --- | ----- | --- | ---- | ---- | ----- | ---- | ---- | ------ | --- | ---- | ------ | ---- | --- | --- |
| ❖   | Nhân  |     | viên | văn  | phòng |      | giáo | vụ: sử |     | dụng | 2 chức | năng |     |     |
|     | ▪     | Ghi | nhận |      | bảng  | điểm |      |        |     |      |        |      |     |     |
|     | ▪     | Lập | bảng |      | xếp   | loại | học  | lực    |     |      |        |      |     |     |
❖ Ban giám hiệu: chỉ sử dụng 1 chức năng là cập nhật quy tắc xếp loại
|     | học | lực |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ghi chú: Chi tiết các chức năng sẽ mô tả sau, chưa xem xét hết tất cả các chức
năng
| →   | Hãy | vẽ  | sơ  | đồ  | UseCase |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 79
tkhuong@dthu.edu.vn

|     | Đề       | BT1. Xếp |          |        |         |      | loại     |       | học      | lực |      | của | học | sinh |
| --- | -------- | -------- | -------- | ------ | ------- | ---- | -------- | ----- | -------- | --- | ---- | --- | --- | ---- |
|     |          |          |          | Bảng   | điểm    | môn  | ….       |       |          |     |      |     |     |      |
|     |          |          | Lớp      | … Niên |         | khóa | …        |       |          |     |      |     |     |      |
|     | Học sinh |          | Điểm     |        | 15 Điểm |      | 1 tiết   |       | Điểm     | HK  |      |     |     |      |
|     | Ghí chú: |          |          |        |         |      |          |       |          |     |      |     |     |      |
|     | - Trường |          | có 9 môn |        | học …   |      |          |       |          |     |      |     |     |      |
|     | Điểm     | 15, điểm |          | 1 tiết | có thể  | có   | nhiều    | cột   |          |     |      |     |     |      |
|     | - Điểm   | số       | là số    | thực   | có giá  | trị  | từ 0 đến |       | 10       |     |      |     |     |      |
|     |          |          |          |        |         | Bảng |          | xếp   | loại học | lực |      |     |     |      |
|     |          |          |          |        |         | Lớp  | … Niên   |       | khóa     | …   |      |     |     |      |
|     | Học sinh |          |          | TBHK1  |         |      |          | TBHK2 |          |     | TBCN |     | Học | lực  |
TBHK1, TBHK2: trung bình cuối học kỳ được tính dựa trên quy tắc tính điểm trung
| bình | học kỳ |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TBCN: trung bình cuối năm được tính dựa trên quy tắc tính điểm trung bình cuối
năm
| Học | lực: được |     | tính | điểm | dựa | trên | quy | tắc | xếp loại | học | lực |     |     |     |
| --- | --------- | --- | ---- | ---- | --- | ---- | --- | --- | -------- | --- | --- | --- | --- | --- |
Software Engineering 80
tkhuong@dthu.edu.vn

|        | Đề        | BT1. Xếp   |        |        | loại | học | lực          | của         |                  | học     | sinh  |
| ------ | --------- | ---------- | ------ | ------ | ---- | --- | ------------ | ----------- | ---------------- | ------- | ----- |
| Quy    | tắc tính  | điểm trung | bình   | học    | kỳ   |     |              |             |                  |         |       |
|        |           |            |        |        |      |     | Quy tắc      | xếp         | loại             | học lực |       |
| TBHK   | = TTB/SMH |            |        |        |      |     |              |             |                  |         |       |
|        |           |            |        |        |      |     | TBCN         | < 5.0: Loại |                  | Yếu     |       |
|        |           |            |        |        |      |     | TBCN >= 5 và |             | TBCN < 6.5: Loại |         | Trung |
| SMH là | số môn    | học (hiện  | nay là | 9 môn) |      |     |              |             |                  |         |       |
bình
| TTB | là tổng trung | bình | các môn | (TBMH) |     |     |                 |     |                |      |     |
| --- | ------------- | ---- | ------- | ------ | --- | --- | --------------- | --- | -------------- | ---- | --- |
|     |               |      |         |        |     |     | TBCN >= 6.5 và  |     | TBCN < 8: Loại |      | Khá |
|     |               |      |         |        |     |     | TBCN >= 8: Loại |     |                | Giỏi |     |
TBMH = (TB15 + 2*TB1T + 3*DHK)/6
| TB15 là | trung | bình của             | các bài | kiểm  | tra        |     |     |     |     |     |     |
| ------- | ----- | -------------------- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
| thường  | xuyên |                      |         |       |            |     |     |     |     |     |     |
| TB1T là | trung | bình của             | các bài | kiểm  | tra 1 tiết |     |     |     |     |     |     |
| DHK là  | điểm  | thi cuối học         | kỳ      |       |            |     |     |     |     |     |     |
|         | Quy   | tắc tính             | điểm    | trung | bình cuối  | năm |     |     |     |     |     |
|         | TBCN  | = TBHK1 + 2*TBHK2)/3 |         |       |            |     |     |     |     |     |     |
Software Engineering 81
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C4_MoHinhHoaPM.md -->

---


<!-- BẮT ĐẦU FILE: C5_1ThietKePM_KN.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 5
THIẾT KẾ PHẦN MỀM
– KHÁI NIỆM
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
CÁC KHÁI NIỆM THIẾT KẾ
THIẾT KẾ
NỘI DUNG THIẾT KẾ
PHẦN
MỀM
CHẤT LƯỢNG THIẾT KẾ
Software Engineering 2
tkhuong@dthu.edu.vn

1. CÁC KHÁI NIỆM THIẾT KẾ
| ❖ Thiết | kế là      | gì? |
| ------- | ---------- | --- |
| ❖ Vai   | trò thiết  | kế  |
| ❖ Cấu   | trúc thiết | kế  |
Software Engineering 3
tkhuong@dthu.edu.vn

|         | Khái | niệm  |     | về  | thiết |      | kế       |     |     |
| ------- | ---- | ----- | --- | --- | ----- | ---- | -------- | --- | --- |
| ❖ Thiết | kế   | là mô | tả  | các | thành | phần | của phần | mềm | dựa |
trên?
| ▪   | Hồ sơ | phân | tích | yêu  | cầu |     |     |     |     |
| --- | ----- | ---- | ---- | ---- | --- | --- | --- | --- | --- |
| ▪   | Công  | nghệ | được | chọn |     |     |     |     |     |
Software Engineering 4
tkhuong@dthu.edu.vn

| Khái           | niệm | về thiết | kế  |
| -------------- | ---- | -------- | --- |
| Phân tích viên |      |          |     |
Hồ sơ
phân tích
Hồ sơ
thiết kế
Phụ trách thiết kế
Software Engineering 5
tkhuong@dthu.edu.vn

|     |     | Vai |     | trò  |     | của |     | thiết |     | kế  |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| ❖   | Tạo |     | mô  | hình | cài | đặt | của | phần  |     | mềm |     |     |     |     |
❖ Ý tưởng, sự sáng tạo và việc lựa chọn công nghệ trong thiết
|     | kế  | sẽ  | quyết |     | định | chất |     | lượng |     | của phần |     | mềm |     |     |
| --- | --- | --- | ----- | --- | ---- | ---- | --- | ----- | --- | -------- | --- | --- | --- | --- |
❖ Là công cụ giao tiếp giữa những người tham gia phát triển, cơ
|     | sở   | đảm |         | bảo | chất     | lượng          |          | hệ      | thống |         |      |        |       |     |
| --- | ---- | --- | ------- | --- | -------- | -------------- | -------- | ------- | ----- | ------- | ---- | ------ | ----- | --- |
|     | ▪    | Dễ  | đọc, dễ |     | hiểu, dễ |                |          | sửa     | đổi   | hơn mã  |      | chương | trình |     |
|     | ▪    | Có  | nhiều   |     | mức      | chi tiết; cung |          |         |       | cấp cái | nhìn | tổng   | thể   |     |
|     | ▪    | Làm | cơ      | sở  | để       | trao           | đổi, cải |         | tiến  |         |      |        |       |     |
| ❖   | Cung |     | cấp     | đầy |          | đủ thông       |          | tin cho |       | việc    | bảo  | trì    | sau   | này |
Software Engineering 6
tkhuong@dthu.edu.vn

|     |      | Cấu      | trúc     |       | thiết    |       | kế        |       |
| --- | ---- | -------- | -------- | ----- | -------- | ----- | --------- | ----- |
| ❖   | Quá  | trình    | thiết    | kế    | gồm      |       | có 2 bước |       |
| ❖   | Bước | 1: thiết |          | kế    | tổng     | thể   | (kiến     | trúc) |
|     | ▪ Mô | tả       | thành    | phần  | mức      |       | tổng thể  |       |
|     |      | • Sự     | tồn      | tại   |          |       |           |       |
|     |      | • Sự     | phụ      | thuộc |          |       |           |       |
| ❖   | Bước | 2: thiết |          | kế    | chi tiết |       |           |       |
|     | ▪ Mô | tả       | chi tiết | từng  |          | thành | phần      |       |
Software Engineering 7
tkhuong@dthu.edu.vn

NỘI DUNG
CÁC KHÁI NIỆM THIẾT KẾ
THIẾT KẾ
NỘI DUNG THIẾT KẾ
PHẦN
MỀM
CHẤT LƯỢNG THIẾT KẾ
Software Engineering 8
tkhuong@dthu.edu.vn

2. NỘI DUNG THIẾT KẾ
| ❖ Thiết |     | kế kiến |       | trúc |       |      |      |      |     |      |      |       |
| ------- | --- | ------- | ----- | ---- | ----- | ---- | ---- | ---- | --- | ---- | ---- | ----- |
| ▪       | Mô  | tả      | một   | cách | tổng  | thể  | phần | mềm  |     |      |      |       |
|         | •   | Gồm     | những |      | thành | phần | nào  | cùng | với | công | nghệ | tương |
ứng
|         | •    | Cách        | liên | kết   | giữa | các | thành   | phần |      |     |     |      |
| ------- | ---- | ----------- | ---- | ----- | ---- | --- | ------- | ---- | ---- | --- | --- | ---- |
| ❖ Thiết |      | kế dữ       | liệu |       |      |     |         |      |      |     |     |      |
| ▪       | Mô   | tả chi tiết |      | thành | phần |     | lưu trữ | của  | phần | mềm | dựa | trên |
|         | công | nghệ        |      | được  | chọn |     |         |      |      |     |     |      |
Software Engineering 9
tkhuong@dthu.edu.vn

2. NỘI DUNG THIẾT KẾ
| ❖ Thiết | kế giao | diện |
| ------- | ------- | ---- |
| ❖ Thiết | kế xử   | lý   |
Software Engineering 10
tkhuong@dthu.edu.vn

NỘI DUNG
CÁC KHÁI NIỆM THIẾT KẾ
THIẾT KẾ
NỘI DUNG THIẾT KẾ
PHẦN
MỀM
CHẤT LƯỢNG THIẾT KẾ
Software Engineering 11
tkhuong@dthu.edu.vn

3. CHẤT LƯỢNG THIẾT KẾ
| ❖ Hồ | sơ thiết | kế tốt | là phải | như | thế nào???? |     |
| ---- | -------- | ------ | ------- | --- | ----------- | --- |
▪ Thiết kế phải triển khai được tất cả yêu cầu trong mô hình phân
|     | tích & yêu | cầu tiềm | ẩn mà | khách | hàng | đòi hỏi. |
| --- | ---------- | -------- | ----- | ----- | ---- | -------- |
▪ Thiết kế cần là bản hướng dẫn dễ đọc, dễ hiểu cho người viết
|     | chương | trình, người | kiểm | thử và | người | bảo trì. |
| --- | ------ | ------------ | ---- | ------ | ----- | -------- |
▪ Thiết kế phải hướng đến các yêu cầu chất lượng của phần mềm
Software Engineering 12
tkhuong@dthu.edu.vn

3. CHẤT LƯỢNG THIẾT KẾ
| ❖   | Độ  | đo  | chất   | lượng | thiết            | kế?     |           |      |           |       |           |
| --- | --- | --- | ------ | ----- | ---------------- | ------- | --------- | ---- | --------- | ----- | --------- |
|     | ▪   | Phụ | thuộc  |       | bài toán, không  |         | có phương |      | pháp      |       | chung     |
|     | ▪   | Hai | nguyên |       | lý thiết         | kế phần | mềm       |      |           |       |           |
|     |     | •   | Nguyên |       | lý Coupling: độ  |         | liên kết  | giữa | các thành |       | phần      |
|     |     | •   | Nguyên |       | lý Cohension: độ |         | kết dính  | giữa | các       | thành | phần con  |
|     |     |     | trong  | một   | thành            | phần    |           |      |           |       |           |
Software Engineering 13
tkhuong@dthu.edu.vn

|         | Nguyên  |          |     | lý  | thiết |       | kế  | phần |       | mềm     |       |
| ------- | ------- | -------- | --- | --- | ----- | ----- | --- | ---- | ----- | ------- | ----- |
| Mục     | tiêu:   |          |     |     |       |       |     |      |       |         |       |
| ❖ Giới  | thiệu   | 2 nguyên |     |     | lý cơ | bản   | và  | nền  | tảng  | của quá | trình |
| thiết   | kế phần |          | mềm |     |       |       |     |      |       |         |       |
| → Trình | bày     | chi tiết |     | hơn | khi   | thiết | kế  | từng | thành | phần    |       |
| → Định  | hướng   |          | tư  | duy | thiết | kế    |     |      |       |         |       |
Software Engineering 14
tkhuong@dthu.edu.vn

| Nguyên |     | lý  | thiết   | kế  | phần | mềm |     |     |
| ------ | --- | --- | ------- | --- | ---- | --- | --- | --- |
|        |     |     | Yêu cầu | của |      |     |     |     |
sản phẩm
|     |     |     | Thiết | kế  |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
sản phẩm
| Các thành |        | phần | Các thành |      | phần | Các thành |        | phần |
| --------- | ------ | ---- | --------- | ---- | ---- | --------- | ------ | ---- |
| của sản   | phẩm   | theo |           |      |      | của sản   | phẩm   | theo |
|           |        |      | của sản   | phẩm | theo |           |        |      |
|           | cách 1 |      |           |      |      |           | cách 3 |      |
cách 2
|     |     |     | Software Engineering |     |     |     |     | 15  |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

| Nguyên    |        | lý      | thiết                | kế      | phần   | mềm   |          |      |
| --------- | ------ | ------- | -------------------- | ------- | ------ | ----- | -------- | ---- |
| ❖ Vấn đề: |        |         |                      |         |        |       |          |      |
| ▪ Cùng    | một    | yêu cầu | về sản               | phẩm    | có rất | nhiều | lựa chọn | khác |
| nhau      | về các | thành   | phần                 | của sản | phẩm   |       |          |      |
| →Chọn     | cách   | nào ??? |                      |         |        |       |          |      |
| →Tại      | sao??  |         |                      |         |        |       |          |      |
|           |        |         | Software Engineering |         |        |       |          | 16   |
tkhuong@dthu.edu.vn

|       | Nguyên |     |       | lý thiết |      | kế  | phần | mềm |     |     |
| ----- | ------ | --- | ----- | -------- | ---- | --- | ---- | --- | --- | --- |
| ❖ Vấn | đề     | với | thiết | kế dữ    | liệu |     |      |     |     |     |
▪ Cùng một yêu cầu về thông tin cần lưu trữ, có rất nhiều lựa
|       | chọn | khác    | nhau | về các | bảng | của | CSDL | (nếu | được | chọn) |
| ----- | ---- | ------- | ---- | ------ | ---- | --- | ---- | ---- | ---- | ----- |
| -     | Dùng | 1 bảng? |      |        |      |     |      |      |      |       |
| -     | Dùng | 2 bảng? |      |        |      |     |      |      |      |       |
| -     | …….  |         |      |        |      |     |      |      |      |       |
| →Chọn |      | cách    | nào  | ???    |      |     |      |      |      |       |
| →Tại  |      | sao??   |      |        |      |     |      |      |      |       |
Software Engineering 17
tkhuong@dthu.edu.vn

|     |       | Nguyên |        |       | lý  | thiết |       | kế    | phần      |      | mềm       |          |
| --- | ----- | ------ | ------ | ----- | --- | ----- | ----- | ----- | --------- | ---- | --------- | -------- |
| ❖   | Vấn   | đề     | với    | thiết | kế  | xử    | lý    |       |           |      |           |          |
|     | ▪     | Cùng   | một    | yêu   | cầu | về    | nhiệm | vụ    | xử lý, có |      | rất nhiều | lựa chọn |
|     |       | khác   | nhau   | về    | các | hàm   | xử    | lý sẽ | được      | dùng |           |          |
|     | -     | Dùng   | 1 hàm? |       |     |       |       |       |           |      |           |          |
|     | -     | Dùng   | 2 hàm? |       |     |       |       |       |           |      |           |          |
|     | -     | …….    |        |       |     |       |       |       |           |      |           |          |
|     | →Chọn |        | cách   | nào   | ??? |       |       |       |           |      |           |          |
|     | →Tại  |        | sao??  |       |     |       |       |       |           |      |           |          |
Software Engineering 18
tkhuong@dthu.edu.vn

|     |       | Nguyên |        |       |       | lý thiết  |       |      | kế      | phần |     |      | mềm    |     |
| --- | ----- | ------ | ------ | ----- | ----- | --------- | ----- | ---- | ------- | ---- | --- | ---- | ------ | --- |
| ❖   | Vấn   | đề     | với    | thiết |       | kế giao   |       | diện |         |      |     |      |        |     |
|     | ▪     | Cùng   | một    | yêu   |       | cầu về    | thông |      | tin cần |      | thể | hiện | trong  | một |
|     |       | nghiệp | vụ, có |       |       | rất nhiều |       | lựa  | chọn    | khác |     | nhau | về các | màn |
|     |       | hình   | giao   | diện  |       | sẽ được   |       | dùng |         |      |     |      |        |     |
|     | -     | Dùng   | 1 màn  |       | hình? |           |       |      |         |      |     |      |        |     |
|     | -     | Dùng   | 2 màn  |       | hình? |           |       |      |         |      |     |      |        |     |
|     | -     | …….    |        |       |       |           |       |      |         |      |     |      |        |     |
|     | →Chọn |        | cách   |       | nào   | ???       |       |      |         |      |     |      |        |     |
|     | →Tại  | sao??  |        |       |       |           |       |      |         |      |     |      |        |     |
Software Engineering 19
tkhuong@dthu.edu.vn

|      |        | Nguyên |          |         |          | lý     | thiết |       | kế   |        | phần |         | mềm      |         |
| ---- | ------ | ------ | -------- | ------- | -------- | ------ | ----- | ----- | ---- | ------ | ---- | ------- | -------- | ------- |
| Khái |        | niệm   |          | nguyên  |          | lý     | thiết | kế    | phần |        | mềm  |         |          |         |
| ❖    | Định   |        | hướng    |         | chung    |        | khi   | thiết |      | kế     | phần | mềm     | hướng    | đến các |
|      | yêu    |        | cầu      | chất    |          | lượng  |       |       |      |        |      |         |          |         |
|      |        |        |          |         |          |        |       |       |      | Trả    | lời  | câu hỏi | Tại sao? |         |
|      |        | ▪ Tính |          | tái     | sử       | dụng   |       |       |      |        |      |         |          |         |
|      |        |        |          |         |          |        |       |       |      | →Thiết |      | kế như  | vậy để…. |         |
|      |        | ▪ Tính |          | dễ      | bảo      | trì    |       |       |      |        |      |         |          |         |
|      |        | ▪ Tính |          | dễ      | mang     | chuyển |       |       |      |        |      |         |          |         |
|      | Trả    | lời    | câu      | hỏi     | Chọn     | cách   |       |       |      |        |      |         |          |         |
|      | nào    |        | để thiết |         | kế?      |        |       |       |      |        |      |         |          |         |
|      | →Dựa   |        |          | vào nội | dung của |        |       |       |      |        |      |         |          |         |
|      | nguyên |        |          | lý.     |          |        |       |       |      |        |      |         |          |         |
Software Engineering 20
tkhuong@dthu.edu.vn

Nguyên lý Coupling
| ❖ Vấn | đề: có    | quá nhiều |
| ----- | --------- | --------- |
| giao  | tiếp giữa | X, Y      |
Thành phần X
→ ???
→ ???
Thành phần Y
Software Engineering 21
tkhuong@dthu.edu.vn

| Khái |                 | niệm |     | về     | Coupling  |      |      | (độ       | móc   |      | nối/ liên |          | kết) |
| ---- | --------------- | ---- | --- | ------ | --------- | ---- | ---- | --------- | ----- | ---- | --------- | -------- | ---- |
| ▪    | Coupling giữa   |      |     | hai    | thành     | phần |      | X, Y được |       | biểu | thị       | qua giao |      |
|      | tiếp giữa       |      | hai | thành  | phần      | X, Y |      |           |       |      |           |          |      |
| ▪    | Ví dụ:          |      |     |        |           |      |      |           |       |      |           |          |      |
|      | • Coupling giữa |      |     | 2 bảng |           | dữ   | liệu |           |       |      |           |          |      |
|      | • Coupling giữa |      |     | 2 hàm  |           | xử   | lý   |           |       |      |           |          |      |
|      | • Coupling giữa |      |     | 2 màn  |           | hình | giao | diện      |       |      |           |          |      |
|      | • Coupling giữa |      |     | thành  |           | phần | xử   | lý và     | thành | phần | lưu       | trữ      | phần |
mềm
Software Engineering 22
tkhuong@dthu.edu.vn

|          | Nguyên |                 | lý Coupling |        |          |        |                   |     |
| -------- | ------ | --------------- | ----------- | ------ | -------- | ------ | ----------------- | --- |
| ❖ Nguyên |        | lý Coupling với |             | thành  | phần     | xử     | lý và lưu         | trữ |
|          |        |                 | Tối thiểu   | hóa    | Coupling |        |                   |     |
|          | Giữa   | thành           | phần        | xử lý  | và thành | phần   | lưu               | trữ |
| Thành    |        | phần X          |             |        |          |        |                   |     |
|          |        |                 |             | Cho ví | dụ về    | nguyên | lý Coupling?????? |     |
| Thành    | phần   | Y               |             |        |          |        |                   |     |
Software Engineering 23
tkhuong@dthu.edu.vn

Nguyên lý Cohension
|       |         |     | ❖ Vấn | đề: X | có quá | nhiều |
| ----- | ------- | --- | ----- | ----- | ------ | ----- |
| Thành | phần    | X   |       |       |        |       |
|       |         |     | thành | phần  | con    |       |
| bao   | gồm các |     |       |       |        |       |
→ ???
| thành | phần | con |       |     |     |     |
| ----- | ---- | --- | ----- | --- | --- | --- |
| X1,   |      |     | → ??? |     |     |     |
X2,
…..
Software Engineering 24
tkhuong@dthu.edu.vn

|     | Khái | niệm |     | về  | Cohension |     |     | (độ |     | kết | dính) |     |
| --- | ---- | ---- | --- | --- | --------- | --- | --- | --- | --- | --- | ----- | --- |
❖
| Cohension |     | của   |     | thành | phần    |     | X được | biểu | thị |     | qua liên | hệ  |
| --------- | --- | ----- | --- | ----- | ------- | --- | ------ | ---- | --- | --- | -------- | --- |
| giữa      | các | thành |     | phần  | con của |     | X      |      |     |     |          |     |
❖ Ví dụ:
| ▪   | Cohension |     | của | bảng | dữ                   | liệu | gồm   | nhiều | cột  |     |     |     |
| --- | --------- | --- | --- | ---- | -------------------- | ---- | ----- | ----- | ---- | --- | --- | --- |
| ▪   | Cohension |     | của | hàm  | xử lý                | gồm  | nhiều | lệnh  |      |     |     |     |
| ▪   | Cohension |     | của | màn  | hình                 | gồm  | nhiều | thể   | hiện |     |     |     |
| ▪   | Cohension |     | của | đơn  | thể gồm              |      | nhiều | hàm   | xử   | lý  |     |     |
|     |           |     |     |      | Software Engineering |      |       |       |      |     |     | 25  |
tkhuong@dthu.edu.vn

| Nguyên |     |     | lý Cohension |     |     |     |     |     |
| ------ | --- | --- | ------------ | --- | --- | --- | --- | --- |
❖
| Nguyên | lý      | Cohension |               |     |       |     |       |      |
| ------ | ------- | --------- | ------------- | --- | ----- | --- | ----- | ---- |
|        | Tối     | đa        | hóa Cohension |     | của   |     | thành | phần |
| Thành  | phần    |           | X             |     | Thành |     | phần  | X1   |
| bao    | gồm các |           |               |     |       |     | …..   |      |
| thành  | phần    | con       |               |     |       |     |       |      |
X1,
|     |     |     |     |     | Thành |     | phần | X2  |
| --- | --- | --- | --- | --- | ----- | --- | ---- | --- |
X2,
…..
…..
|     |     |     |     | Cho ví | dụ về | nguyên |     | lý Cohension?????? |
| --- | --- | --- | --- | ------ | ----- | ------ | --- | ------------------ |
Software Engineering 26
tkhuong@dthu.edu.vn

CÂU HỎI THI
| 1) Thiết | kế phần    | mềm là  | gì?         |                |              |
| -------- | ---------- | ------- | ----------- | -------------- | ------------ |
| 2) Nhà   | phát triển | phần    | mềm cần     | thiết kế những | nội dung gì? |
| 3) Nêu   | đặc trưng  | của bản | thiết kế    | tốt?           |              |
| 4) Trình | bày nguyên | lý      | Coupling và | Cohension, cho | ví dụ?       |
Software Engineering 28
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 30
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C5_1ThietKePM_KN.md -->

---


<!-- BẮT ĐẦU FILE: C5_2ThietKePM_KienTruc.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 5
THIẾT KẾ PHẦN MỀM
- KIẾN TRÚC
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM
KIẾN
TRÚC
CÁC MÔ HÌNH KIẾN TRÚC
PHẦN
MỀM
CÔNG NGHỆ PHÂN TÁN
Software Engineering 2
tkhuong@dthu.edu.vn

KHÁI NIỆM
❖ Thiết kế kiến trúc là mô tả một cách tổng thể các thành phần
| của phần | mềm, cụ |     | thể | hơn đó | là: |     |     |     |
| -------- | ------- | --- | --- | ------ | --- | --- | --- | --- |
▪ Quyết định về sự tồn tại của các thành phần cùng với công nghệ
| tương | ứng |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
▪ Quyết định về cách thức liên kết/ kết nối giữa các thành phần
| ❖ Ghi chú:  |      |      |          |                      |            |         |          |      |
| ----------- | ---- | ---- | -------- | -------------------- | ---------- | ------- | -------- | ---- |
| ▪ Không     | đi   | vào  | chi tiết | của                  | từng thành | phần    |          |      |
| ▪ Cần       | chọn | công | nghệ     | thích                | hợp theo   | yêu cầu | phi chức | năng |
|             |      |      |          | Software Engineering |            |         |          | 3    |
tkhuong@dthu.edu.vn

NỘI DUNG
CÁC KHÁI NIỆM CƠ BẢN
KIẾN
TRÚC
CÁC MÔ HÌNH KIẾN TRÚC
PHẦN
MỀM
CÔNG NGHỆ PHÂN TÁN
Software Engineering 6
tkhuong@dthu.edu.vn

2. CÁC MÔ HÌNH KIẾN TRÚC
| ❖ Xét        | 4 dạng | mô hình | kiến    | trúc |
| ------------ | ------ | ------- | ------- | ---- |
| ❖ DẠNG 1: mô |        | hình    | đơn lập |      |
A
Giao diện
|     |     |     | Dữ  | liệu |
| --- | --- | --- | --- | ---- |
và Xử lý
Software Engineering 8
tkhuong@dthu.edu.vn

2. CÁC MÔ HÌNH KIẾN TRÚC
❖ DẠNG 2: mô hình Client-Server
A B
Mạng
Giao diện Giao diện
cục bộ
và Xử lý và Xử lý
HQT
Dữ liệu
CSDL
Software Engineering 9
tkhuong@dthu.edu.vn

2. CÁC MÔ HÌNH KIẾN TRÚC
❖
| DẠNG 3: Mô |     | hình | trung | chuyển |     |     |
| ---------- | --- | ---- | ----- | ------ | --- | --- |
|            | A   |      |       |        | B   |     |
USB,
| Giao diện |     |     |     |     | Giao diện |     |
| --------- | --- | --- | --- | --- | --------- | --- |
CD,
| và Xử | lý  |     |     |     | và Xử | lý  |
| ----- | --- | --- | --- | --- | ----- | --- |
Email
| phân hệ | A   |     |     |     | phân hệ | B   |
| ------- | --- | --- | --- | --- | ------- | --- |
| Dữ liệu |     |     |     |     | Dữ liệu |     |
Software Engineering 10
tkhuong@dthu.edu.vn

2. CÁC MÔ HÌNH KIẾN TRÚC
❖
| DẠNG 4: Mô | hình | 3 tầng |
| ---------- | ---- | ------ |
A B
Internet
Giao diện Giao diện
Dữ liệu
|     |     | Xử lý |
| --- | --- | ----- |
Software Engineering 11
tkhuong@dthu.edu.vn

NỘI DUNG
CÁC KHÁI NIỆM CƠ BẢN
KIẾN
TRÚC
CÁC MÔ HÌNH KIẾN TRÚC
PHẦN
MỀM
CÔNG NGHỆ PHÂN TÁN
Software Engineering 12
tkhuong@dthu.edu.vn

3. CÔNG NGHỆ PHÂN TÁN
❖
Middleware
| ▪ Các | thành                                             | phần | trong | hệ phân   | tán giao | tiếp thế | nào? |
| ----- | ------------------------------------------------- | ---- | ----- | --------- | -------- | -------- | ---- |
| →Hệ   | thống                                             | đứng | giữa  | điều phối |          |          |      |
| ▪ Các | chuẩn                                             | phổ  | biến  |           |          |          |      |
| •     | CORBA (Common Object Request Broker Architecture) |      |       |           |          |          |      |
| •     | COM (Component Object Model)                      |      |       |           |          |          |      |
| •     | JavaBeans                                         |      |       |           |          |          |      |
Software Engineering 13
tkhuong@dthu.edu.vn

| Hệ  | thống |     | phân |     | tán |
| --- | ----- | --- | ---- | --- | --- |
❖ Web Service
| ▪ Thư  | viện                                               | lập trình    | dựng | sẵn |     |
| ------ | -------------------------------------------------- | ------------ | ---- | --- | --- |
| ▪ Cung | cấp                                                | dạng         | dịch | vụ  |     |
| ▪ Truy | xuất                                               | qua internet |      |     |     |
| ▪ Các  | dịch                                               | vụ phổ       | biến |     |     |
| •      | Math services                                      |              |      |     |     |
| •      | Google map                                         |              |      |     |     |
| •      | Amazon services                                    |              |      |     |     |
| ▪ Các  | chuẩn                                              | giao         | tiếp | XML |     |
| •      | SOA (Simple Access Protocol)                       |              |      |     |     |
| •      | WSDL (Web Service Description Language)            |              |      |     |     |
| •      | UDDI (Universal Description Discovery and Integran |              |      |     |     |
Software Engineering 14
tkhuong@dthu.edu.vn

VD minh họa
| ❖ Mục  | tiêu: minh họa |         | hồ   | sơ thiết | kế   | (thiết kế tổng | thể) cho |
| ------ | -------------- | ------- | ---- | -------- | ---- | -------------- | -------- |
| ứng    | dụng           | nhỏ với | công | nghệ     | được | chọn:          |          |
| ▪ Giao | diện           | Console |      |          |      |                |          |
| ▪ Xử   | lý với         | đơn thể |      |          |      |                |          |
Software Engineering 15
tkhuong@dthu.edu.vn

VD minh họa
Đề bài:
| ❖ Xét       | ứng  | dụng | rèn luyện | bài                  | tập     | về Giải  | phương     | trình | bậc |
| ----------- | ---- | ---- | --------- | -------------------- | ------- | -------- | ---------- | ----- | --- |
| 2(với       | phần | mềm  | đóng      | vai                  | trò của | Giáo     | viên). Hãy | phân  |     |
| tích, thiết |      | kế   | với công  | nghệ                 | Giao    | diện     | Console và | Xử    | lý  |
| dùng        | đơn  | thể  |           |                      |         |          |            |       |     |
|             | PHÂN | TÍCH |           |                      |         | THIẾT KẾ |            |       |     |
|             |      |      |           | Software Engineering |         |          |            |       | 16  |
tkhuong@dthu.edu.vn

VD minh họa
| ❖ Thiết kế |         |       |       |      |
| ---------- | ------- | ----- | ----- | ---- |
| ▪ Thiết    | kế tổng | thể   |       |      |
| ▪ Thiết    | kế giao | diện  | người | dùng |
| ▪ Thiết    | kế hệ   | thống | xử lý |      |
Học sinh
Giao diện
và Xử lý
Software Engineering 17
tkhuong@dthu.edu.vn

BÀI TẬP 1
| ❖ Đề | bài | 1   |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
▪
|     | Xét | phần | mềm Quản | lý nhân | sự với | yêu cầu | chính | là tra cứu | hồ  |
| --- | --- | ---- | -------- | ------- | ------ | ------- | ----- | ---------- | --- |
sơ nhân viên dựa trên họ tên. Hãy phân tích, thiết kế với công
|      | nghệ      | giao    | diện Console, xử |                | lý dùng | đơn thể                | và lưu | trữ dùng |     |
| ---- | --------- | ------- | ---------------- | -------------- | ------- | ---------------------- | ------ | -------- | --- |
|      | CSDL quan |         | hệ               |                |         |                        |        |          |     |
| Phân | tích:     |         |                  |                |         |                        |        |          |     |
| → Vẽ | sơ đồ     | UseCase | các              | chức năng, đặc |         | tả UseCase, Activity,  |        |          |     |
Sequence
| Thiết | kế: |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
→ ???
| → Thiết | kế  | tổng | thể??? |                      |     |     |     |     |     |
| ------- | --- | ---- | ------ | -------------------- | --- | --- | --- | --- | --- |
|         |     |      |        | Software Engineering |     |     |     |     | 18  |
tkhuong@dthu.edu.vn

BÀI TẬP 2
| ❖ Đề | bài | 2   |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
▪
|     | Xét | phần mềm | Quản lý | thu chi với | yêu cầu | chính | là thống | kê  |
| --- | --- | -------- | ------- | ----------- | ------- | ----- | -------- | --- |
doanh thu theo tháng. Hãy phân tích, thiết kế với công nghệ giao
diện Console, xử lý dùng đơn thể và lưu trữ dùng CSDL quan hệ
| Phân | tích:  |         |          |           |                        |     |     |     |
| ---- | ------ | ------- | -------- | --------- | ---------------------- | --- | --- | --- |
| → Vẽ | sơ đồ  | UseCase | các chức | năng, đặc | tả UseCase, Activity,  |     |     |     |
Sequence
| Thiết | kế: |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
→ ???
| → Thiết | kế  | tổng thể??? |     |     |     |     |     |     |
| ------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Software Engineering 19
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 22
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C5_2ThietKePM_KienTruc.md -->

---


<!-- BẮT ĐẦU FILE: C5_3ThietKePM_TKDuLieu_HDT.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 5
THIẾT KẾ PHẦN MỀM
– HƯỚNG ĐỐI TƯỢNG
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
KỸ THUẬT HƯỚNG ĐỐI TƯỢNG
THIẾT KẾ
THIẾT KẾ ĐỐI TƯỢNG
PHẦN
MỀM
HĐT
THIẾT KẾ DỮ LIỆU
Software Engineering 2
tkhuong@dthu.edu.vn

1. KỸ THUẬT HƯỚNG ĐỐI TƯỢNG
| ❖   | Hiện  |       | đang |       | trở nên   |      | phổ        | biến  |     |      |        |
| --- | ----- | ----- | ---- | ----- | --------- | ---- | ---------- | ----- | --- | ---- | ------ |
| ❖   | Là    | một   | cách |       | tiếp      | cận  | khác, nhìn |       |     | nhận | hệ     |
|     | thống |       | theo |       | các       | quan | điểm:      |       |     |      |        |
|     | ▪     | Tập   | các  |       | đối tượng |      | có         | tượng | tác | với  | nhau   |
|     | ▪     | Tương |      | tác   | giữa      | các  | đối        | tượng |     | bằng | truyền |
|     |       | thông |      | báo   |           |      |            |       |     |      |        |
|     | ▪     | Các   | đối  | tượng |           | có   | thể kế     | thừa  |     | nhau |        |
Software Engineering 3
tkhuong@dthu.edu.vn

1. KỸ THUẬT HƯỚNG ĐỐI TƯỢNG
| ❖ Đối | tượng         | phần   | mềm:  |
| ----- | ------------- | ------ | ----- |
| ▪     | Dữ liệu       | (thuộc | tính) |
| ▪     | Xử lý (phương |        | thức) |
Software Engineering 4
tkhuong@dthu.edu.vn

|     | Ưu       | điểm    |         | của       | OOD      |        |       |      |      |          |
| --- | -------- | ------- | ------- | --------- | -------- | ------ | ----- | ---- | ---- | -------- |
| ❖   | Dễ bảo   | trì:    | các     | đối tượng | được     | hiểu   | như   | các  | thực | thể hoạt |
|     | động     | độc     | lập     |           |          |        |       |      |      |          |
|     | ▪ Bao    | gói     | thông   | tin       |          |        |       |      |      |          |
|     | ▪ Liên   | kết     | lỏng    | lẻo (trao | đổi bằng | truyền | thông | báo) |      |          |
| ❖   | Dễ tái   | sử dụng |         |           |          |        |       |      |      |          |
|     | ▪ Độ     | độc     | lập cao |           |          |        |       |      |      |          |
|     | ▪ Có     | khả     | năng    | kế thừa   |          |        |       |      |      |          |
| ❖   | Dễ hiểu: |         |         |           |          |        |       |      |      |          |
▪ Một vài hệ thống có sự ánh xạ tường minh giữa thế giới thực và
|     | đối | tượng | hệ  | thống |     |     |     |     |     |     |
| --- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- |
Software Engineering 5
tkhuong@dthu.edu.vn

| Nội | dung của |     |     | OOD |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
❖ Xác định các tập đối tượng (gọi là lớp) và các đặc trưng của
chúng
| ❖ Phân  | định vai | trò   | và trách | nhiệm | của chúng | trong   | hệ thống  |
| ------- | -------- | ----- | -------- | ----- | --------- | ------- | --------- |
| ❖ Thiết | lập được | sự    | tương    | tác   | của chúng | để thực | hiện chức |
| năng    | của hệ   | thống | phần     | mềm   | đặt ra    |         |           |
Software Engineering 6
tkhuong@dthu.edu.vn

| ❖ Các | lớp đối  | tượng |           |        |
| ----- | -------- | ----- | --------- | ------ |
| ▪     | Bạn nhìn | thấy  | bao nhiêu | class? |
tkhuong@dthu.edu.vn

NỘI DUNG
KỸ THUẬT HƯỚNG ĐỐI TƯỢNG
THIẾT KẾ
THIẾT KẾ ĐỐI TƯỢNG
PHẦN
MỀM
HĐT
THIẾT KẾ DỮ LIỆU
Software Engineering 8
tkhuong@dthu.edu.vn

2. THIẾT KẾ ĐỐI TƯỢNG
|         |     | Quy trình | thiết kế | đối tượng |        |
| ------- | --- | --------- | -------- | --------- | ------ |
| Mô hình |     |           | 1.       |           | 2.     |
| hướng   | đối | Xác       | định đối | Vẽ sơ     | đồ lớp |
|         |     | tượng     |          | đối       | tượng  |
tượng!!!
Software Engineering 9
tkhuong@dthu.edu.vn

|       | Xác     | định | đối    | tượng |     |
| ----- | ------- | ---- | ------ | ----- | --- |
| ❖ Đối | với các | thực | thể sự | vật:  |     |
▪ Kiểm xem có nhu cầu quản lý thông tin về thực thể này trong hệ
|     | thống | không? |     |     |     |
| --- | ----- | ------ | --- | --- | --- |
▪ Nếu có, xác định một lớp trong sơ đồ phân tích biểu diễn cho
|     | thực thể | này.     |          |        |     |
| --- | -------- | -------- | -------- | ------ | --- |
|     | • Xác    | định tên | lớp: tên | của sự | vật |
• Thuôc tính: bổ sung các thuộc tính mô tả đầy đủ thông tin mà hệ
|     | thống | có nhu | cầu quản | lý về | đối tượng. |
| --- | ----- | ------ | -------- | ----- | ---------- |
tkhuong@dthu.edu.vn

| Xác | định | đối | tượng |
| --- | ---- | --- | ----- |
❖ Ví dụ:
tkhuong@dthu.edu.vn

|     | Xác |       | định  |        | đối    |       | tượng |        |            |          |      |         |      |       |      |
| --- | --- | ----- | ----- | ------ | ------ | ----- | ----- | ------ | ---------- | -------- | ---- | ------- | ---- | ----- | ---- |
| ❖   | Đối | với   | thực  | thể    | thông  |       | tin:  |        |            |          |      |         |      |       |      |
|     | ▪   | Nếu   | thực  | thể    | mô tả  | thông |       | tin về |            | một      | hoạt | động    | giao | dịch  | hệ   |
|     |     | thống | thì   | chuyển | thành  |       | một   |        | lớp        | trong    | mô   | hình    | phân | tích. |      |
|     | ▪   | Nếu   | thực  | thể    | là một | dạng  |       | thông  |            | tin tổng |      | hợp     | → có | thể   | tách |
|     |     | thành | nhiều | lớp    | mới    |       | hoặc  | bổ     | sung thông |          |      | tin cho | các  | lớp   | đang |
|     |     | tồn   | tại.  |        |        |       |       |        |            |          |      |         |      |       |      |
| ❖   | Ví  | dụ:   |       |        |        |       |       |        |            |          |      |         |      |       |      |
tkhuong@dthu.edu.vn

| Xác   | định     | đối       | tượng |
| ----- | -------- | --------- | ----- |
| ❖ Đối | với thực | thể thông | tin:  |
| ▪     | Ví dụ:   |           |       |
tkhuong@dthu.edu.vn

| Xác     |     | định | đối      | tượng |            |          |     |
| ------- | --- | ---- | -------- | ----- | ---------- | -------- | --- |
| ❖ Đối   | với | thừa | tác viên | và    | tác nhân:  |          |     |
| NV quan | ly  | Thủ  | kho      |       | Khách hàng | Nhà cung | cấp |
|         |     |      |          | Khách | hàng       | Nhà cung | cấp |
Nhân Viên
tkhuong@dthu.edu.vn

2. THIẾT KẾ ĐỐI TƯỢNG
|         |     | Quy trình | thiết kế | đối tượng |        |
| ------- | --- | --------- | -------- | --------- | ------ |
| Mô hình |     |           | 1.       |           | 2.     |
| hướng   | đối | Xác       | định đối | Vẽ sơ     | đồ lớp |
|         |     | tượng     |          | đối       | tượng  |
tượng!!!
Software Engineering 15
tkhuong@dthu.edu.vn

|     | Lớp |     | đối   |     | tượng |     |      | (Class) |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ----- | --- | ---- | ------- | --- | --- | --- | --- | --- |
| ❖   | Lớp | đối | tượng |     | (nhắc |     | lại) |         |     |     |     |     |     |
▪
|     |     | Tập  | hợp  | các  | đối   | tượng |      | chia        |          | sẻ chung   | cấu trúc  | (các | thuộc  |
| --- | --- | ---- | ---- | ---- | ----- | ----- | ---- | ----------- | -------- | ---------- | --------- | ---- | ------ |
|     |     | tính | và   | mối  | quan  | hệ)   | và   | hành        |          | vi.        |           |      |        |
|     | ▪   | Lớp  | là   | trừu | tượng |       | hóa  | các         |          | đối tượng, | đối tượng |      | là thể |
|     |     | hiện | của  | lớp  |       |       |      |             |          |            |           |      |        |
|     | ▪   | Biểu | diễn | một  | lớp   |       | đối  | tượng:      |          |            |           |      |        |
|     |     | •    | Tên  | lớp  |       |       |      |             |          |            |           |      |        |
|     |     | •    | Danh | sách | thuộc |       | tính | (attribute) |          |            |           |      |        |
|     |     | •    | Danh | sách | các   | hoạt  |      | động        | (method) |            |           |      |        |
tkhuong@dthu.edu.vn

|     | Sơ  | đồ  | lớp | đối | tượng |     | (class diagram) |
| --- | --- | --- | --- | --- | ----- | --- | --------------- |
❖ Là một hình thức biểu diễn lớp đối tượng (tên, thuộc tính, hành vi)
| và     | quan   | hệ   | giữa chúng | một       | cách | trực      | quan. |
| ------ | ------ | ---- | ---------- | --------- | ---- | --------- | ----- |
| ❖ Biểu | diễn   | sơ   | đồ lớp     | đối tượng |      | bằng UML: |       |
|        | ▪ Biểu | diễn | lớp        |           |      |           |       |
tkhuong@dthu.edu.vn

|     | Sơ   |      | đồ  |     | lớp  |     | đối |      | tượng          |     |       | (class diagram) |       |            |     |
| --- | ---- | ---- | --- | --- | ---- | --- | --- | ---- | -------------- | --- | ----- | --------------- | ----- | ---------- | --- |
| ❖   | Biểu | diễn |     | sơ  | đồ   | lớp | đối |      | tượng          |     | bằng  | UML(tt):        |       |            |     |
|     | ▪    | Mối  | kết | hợp | giữa |     | các | lớp  | (Association): |     |       |                 |       |            |     |
|     |      | •    | Mối | kết | hợp  | có  | thể | giữa | các            | đối | tượng | của             | 2 lớp | đối tượng. |     |
• Nếu 2 đối tượng của 2 lớp có mối kết hợp thì giữa 2 lớp có mối kết
hợp.
|     | ▪   | Một  | sơ  | đồ  | lớp | đối | tượng |     | sẽ  | bao | gồm | các | lớp | và các quan | hệ  |
| --- | --- | ---- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | ----------- | --- |
|     |     | giữa |     | các | lớp |     |       |     |     |     |     |     |     |             |     |
|     | ▪   | Bản  | số  | của | mối |     | kết   | hợp |     |     |     |     |     |             |     |
tkhuong@dthu.edu.vn

|     | Sơ  | đồ   | lớp    | đối | tượng |         | (class diagram) |     |
| --- | --- | ---- | ------ | --- | ----- | ------- | --------------- | --- |
| ❖   | Xác | định | bản số | cho | mối   | kết hợp | (min,max):      |     |
▪ 1; 0..1
▪ 1..*
▪ 0..*
|     | ▪   | a..* : a là | hằng | số  |     |     |     |     |
| --- | --- | ----------- | ---- | --- | --- | --- | --- | --- |
▪ 1 = 1..1
| Diễn  | giải: |     |          |     |     |     |                  |     |
| ----- | ----- | --- | -------- | --- | --- | --- | ---------------- | --- |
| ✓ Một | bản   | yêu | cầu được | gửi | tới | cho | duy nhất 1 phòng | ban |
✓ Một phòng ban có thể có từ 0 → nhiều (0..*) bản yêu cầu gửi tới
tkhuong@dthu.edu.vn

| Ví    | dụ      |          |          |
| ----- | ------- | -------- | -------- |
| Sơ đồ | lớp của | hệ thống | bán hàng |
Software Engineering 20
tkhuong@dthu.edu.vn

NỘI DUNG
KỸ THUẬT HƯỚNG ĐỐI TƯỢNG
THIẾT KẾ
THIẾT KẾ ĐỐI TƯỢNG
PHẦN
MỀM
HĐT
THIẾT KẾ DỮ LIỆU
Software Engineering 22
tkhuong@dthu.edu.vn

3. THIẾT KẾ DỮ LIỆU
| ❖   | Kiến        | thức: các |      |       | công |      | nghệ | lưu trữ |
| --- | ----------- | --------- | ---- | ----- | ---- | ---- | ---- | ------- |
| ❖   | Kỹ năng: tổ |           |      | chức  |      | lưu  | trữ  | dữ liệu |
| ❖   | Nội         | dung:     |      |       |      |      |      |         |
|     | ▪ Thành     |           | phần |       | lưu  | trữ  |      |         |
|     | ▪ Thiết     |           | kế   | thành |      | phần | lưu  | trữ     |
|     | ▪ Thiết     |           | kế   | xử    | lý   | lưu  | trữ  |         |
Software Engineering 23
tkhuong@dthu.edu.vn

| 3.1 Thành |     |     | phần | lưu | trữ | - Khái | niệm |     |
| --------- | --- | --- | ---- | --- | --- | ------ | ---- | --- |
❖ Khái niệm:
| ▪ Thành | phần          | chịu | trách | nhiệm    | lưu trữ   | tất cả | các dữ | liệu cần |
| ------- | ------------- | ---- | ----- | -------- | --------- | ------ | ------ | -------- |
| thiết   | cho sự        | hoạt | động  | của phần | mềm       |        |        |          |
| • Dữ    | liệu do người |      | dùng  | cung     | cấp       |        |        |          |
| • Dữ    | liệu do người |      | dùng  | tính     | toán phát | sinh   |        |          |
| • Dữ    | liệu nội      | bộ   |       |          |           |        |        |          |
Software Engineering 24
tkhuong@dthu.edu.vn

|     | 3.1 Thành |     |     | phần |     | lưu | trữ |     | - Tổ | chức |     |     |
| --- | --------- | --- | --- | ---- | --- | --- | --- | --- | ---- | ---- | --- | --- |
❖ Tổ chức:
| ▪   | Thành | phần    | lưu | trữ | bao   | gồm | các  | đơn | vị lưu  | trữ | dữ   | liệu   |
| --- | ----- | ------- | --- | --- | ----- | --- | ---- | --- | ------- | --- | ---- | ------ |
| ▪   | Mỗi   | đơn vị  | lưu | trữ | tương | ứng | vùng | nhớ | trên    | bộ  | nhớ  | phụ và |
|     | có    | thể bao | gồm | bên | trong | các | đơn  | vị  | lưu trữ | dữ  | liệu | thành  |
phần
|     | Thông | tin  |     |     |     |     |     |     |     |        |     |     |
| --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
|     |       |      |     |     |     |     |     |     | Đơn | vị lưu | trữ | dữ  |
Chọn
| trong | thực   | tế và |     |     |     |     |     |     | liệu    | với các | “đơn | vị   |
| ----- | ------ | ----- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | ---- |
| các   | “thông | tin   |     |     |     |     |     |     | lưu trữ | dữ      | liệu | con” |
con”
Software Engineering 25
tkhuong@dthu.edu.vn

|     | 3.1 Thành |     |      |      | phần    |     | lưu |     | trữ | - Công |     | nghệ |
| --- | --------- | --- | ---- | ---- | ------- | --- | --- | --- | --- | ------ | --- | ---- |
| ❖   | Công      |     | nghệ | lưu  | trữ:    |     |     |     |     |        |     |      |
| Có  | 2 loại    |     | công | nghệ | chính   |     |     |     |     |        |     |      |
|     | ▪         | Lưu | trữ  | với  | tập tin |     |     |     |     |        |     |      |
.txt
|     |     | •   | Tập | tin nhị | phân |     | .html |     |     |      |           |     |
| --- | --- | --- | --- | ------- | ---- | --- | ----- | --- | --- | ---- | --------- | --- |
|     |     |     |     |         |      |     |       |     |     | Khác | nhau????? |     |
.xml
.xls
|     |     | •   | Tập | tin văn | bản |     |     |     | .doc |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |
.jpg
|     | ▪   | Lưu | trữ        | với | Cơ sở | dữ    | liệu |     |           |     |      |         |
| --- | --- | --- | ---------- | --- | ----- | ----- | ---- | --- | --------- | --- | ---- | ------- |
|     |     | •   | CSDL quan  |     | hệ    |       |      | Có  | bao nhiêu | mô  | hình | CSDL??? |
|     |     | •   | CSDL hướng |     | đối   | tượng |      |     |           |     |      |         |
Software Engineering 26
tkhuong@dthu.edu.vn

| 3.1 Thành |     | phần |     | lưu | trữ | -   | Công |     | nghệ |     |
| --------- | --- | ---- | --- | --- | --- | --- | ---- | --- | ---- | --- |
❖ Tập tin XML
| ▪ Bao      | gồm bên | trong  | các  | thẻ | (tag), mỗi |     | thẻ có  | thể | có  | nhiều |
| ---------- | ------- | ------ | ---- | --- | ---------- | --- | ------- | --- | --- | ----- |
| thuộc      | tính và | có thể | bao  | gồm | bên trong  |     | nhiều   | thẻ |     | con   |
| Thông      | tin     |        |      |     |            |     |         |     |     |       |
|            |         |        |      |     |            |     | Các thẻ | của | tập | tin   |
| trong thực | tế      |        | Chọn |     |            |     |         |     |     |       |
XML
Software Engineering 27
tkhuong@dthu.edu.vn

|     |       | 3.1 Thành |      |           | phần  |      | lưu  | trữ     | - Công       | nghệ     |     |
| --- | ----- | --------- | ---- | --------- | ----- | ---- | ---- | ------- | ------------ | -------- | --- |
| ❖   | Lưu   | trữ       | với  | CSDL quan |       |      | hệ   |         |              |          |     |
|     | ▪     | Bao       | gồm  | bên       | trong | các  | bảng | dữ liệu | (table). Mỗi | bảng     | có  |
|     |       | nhiều     | cột  | và        | nhiều | dòng |      |         |              |          |     |
|     | Thông |           | tin  |           |       |      |      |         |              |          |     |
|     |       |           |      |           |       |      |      |         | Các dòng     | của bảng |     |
Chọn
|     | trong | thực | tế  |     |     |     |     |     | trong CSDL quan |     | hệ  |
| --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- |
Software Engineering 28
tkhuong@dthu.edu.vn

| 3.2 Thiết |                 |       |       | kế     | thành    |       |      | phần |      |       |      | lưu     |      | trữ       |
| --------- | --------------- | ----- | ----- | ------ | -------- | ----- | ---- | ---- | ---- | ----- | ---- | ------- | ---- | --------- |
| ❖ Khái    | niệm            |       |       |        |          |       |      |      |      |       |      |         |      |           |
| ▪ Mô      | tả các          | đơn   |       | vị lưu | trữ      | theo  | công |      | nghệ |       | được |         | chọn |           |
| ▪ Lưu     | ý: chọn         |       | công  | nghệ   |          | thích | hợp  |      | loại | thông |      | tin cần |      | dùng      |
| về        | dung lượng, bảo |       |       |        | mật, tốc |       | độ,… |      |      |       |      |         |      |           |
|           | Phụ             | trách | thiết | kế     |          |       |      |      |      |       |      | Hồ      | sơ   |           |
|           |                 | Dữ    | liệu  |        |          |       |      |      |      |       |      | phân    |      | tích      |
|           |                 |       |       |        |          |       |      |      |      |       |      | Các     | công |           |
| Hồ sơ     | thiết           |       |       |        |          |       |      |      |      |       |      | nghệ    | lưu  | trữ       |
| kế dữ     | liệu            |       |       |        |          |       |      |      |      |       |      |         |      |           |
|           |                 |       |       |        |          | Có    | thể  | chọn | và   | kết   | hợp  | nhiều   | loại | công nghệ |
Software Engineering 29
tkhuong@dthu.edu.vn

|            | 3.2 Thiết |           | kế          | thành          |         | phần  |      | lưu | trữ      |     |
| ---------- | --------- | --------- | ----------- | -------------- | ------- | ----- | ---- | --- | -------- | --- |
| Các        | bước      | tiến hành | thiết       | kế             | dữ liệu |       |      |     |          |     |
| ❖ B1. Lập  |           | các sơ    | đồ logic dữ |                | liệu    | thành | phần | cho | từng     | yêu |
| cầu        | nhập      | liệu      |             |                |         |       |      |     |          |     |
| ❖ B2. Tích |           | hợp các   | sơ          | đồ logic thành |         |       | phần | để  | có sơ đồ |     |
logic chung
| ❖ B3. Cải |     | tiến sơ | đồ logic của |     | B2. theo |     | các | yêu | cầu chất |     |
| --------- | --- | ------- | ------------ | --- | -------- | --- | --- | --- | -------- | --- |
lượng
|     |     |     |     | Software Engineering |     |     |     |     |     | 30  |
| --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
tkhuong@dthu.edu.vn

|         | 3.2 Thiết |            |          |     | kế  |      | thành |     |      | phần  | lưu   |     | trữ  |       |
| ------- | --------- | ---------- | -------- | --- | --- | ---- | ----- | --- | ---- | ----- | ----- | --- | ---- | ----- |
| ❖ Lập   |           | sơ đồ      | logic dữ |     |     | liệu | thành |     | phần |       |       |     |      |       |
|         |           |            |          |     |     |      |       |     |      | Sơ đồ | logic | dữ  | liệu | thành |
| Yêu cầu |           | nhập liệu: |          |     |     |      |       |     |      |       |       |     |      |       |
phần:
| Thông    | tin | về đối     | tượng | X    |     |     |     |     |     |        |        |     |     |       |
| -------- | --- | ---------- | ----- | ---- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | ----- |
|          |     |            |       |      |     |     |     |     |     | - Bảng | X với  | các | cột | khóa  |
| cần nhập |     | liệu trong |       | thực |     |     |     |     |     |        |        |     |     |       |
|          |     |            |       |      |     |     |     |     |     | chính  | và các | cột | dữ  | liệu, |
tế
|         |      |           |      |       |      | Phụ   | trách     | thiết | kế       | các | cột liên kết |     |     |     |
| ------- | ---- | --------- | ---- | ----- | ---- | ----- | --------- | ----- | -------- | --- | ------------ | --- | --- | --- |
| TH1.    | X là | đối tượng |      | đơn   | giản |       |           |       |          |     |              |     |     |     |
| X không |      | chứa bên  |      | trong | đối  | tượng | con khác  |       |          |     |              |     |     |     |
| TH2.    | X là | đối tượng |      | phức  | hợp  |       |           |       |          |     |              |     |     |     |
| X chứa  |      | bên trong | danh | sách  |      | các   | đối tượng |       | con khác |     |              |     |     |     |
Vd.
| Hồ sơ | đối  | tác      |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hồ sơ | nhân | viên     |     |     |     |     |     |     |     |     |     |     |     |     |
| Phiếu | thu  |          |     |     |     |     |     |     |     |     |     |     |     |     |
| Hóa   | đơn  | bán hàng |     |     |     |     |     |     |     |     |     |     |     |     |
Software Engineering 31
tkhuong@dthu.edu.vn

|     | VD. Tiếp |     |     | nhận |     | đối | tác |     |     |     |     |
| --- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
❖ Dựa vào hồ sơ phân tích, hãy thiết kế dữ liệu phần mềm quản
| lý   | bán | hàng | khi chỉ | xem | xét | chức | năng | Tiếp | nhận | đối tác |     |
| ---- | --- | ---- | ------- | --- | --- | ---- | ---- | ---- | ---- | ------- | --- |
| ❖ Mô | tả: |      |         |     |     |      |      |      |      |         |     |
Chức năng cho phép nhân viên của cửa hàng ghi nhận thông tin
| về đối      | tác | qua 2 bước |         | như  | sau: |       |        |     |       |         |     |
| ----------- | --- | ---------- | ------- | ---- | ---- | ----- | ------ | --- | ----- | ------- | --- |
| B1. NV cung |     |            | cấp cho | phần | mềm  | thông | tin về |     | hồ sơ | của đối | tác |
B2. Phần mềm tiến hành kiểm tra tính hợp lệ và sau đó ghi nhận
| thông | tin tương |     | ứng | vào bộ | nhớ                  | phụ | (nếu | hợp | lệ) |     |     |
| ----- | --------- | --- | --- | ------ | -------------------- | --- | ---- | --- | --- | --- | --- |
|       |           |     |     |        | Software Engineering |     |      |     |     |     | 32  |
tkhuong@dthu.edu.vn

| VD. Tiếp |     | nhận | đối | tác |     |
| -------- | --- | ---- | --- | --- | --- |
❖ Cấu trúc:
|            |              |                              | Hồ sơ        | đối tác     |     |
| ---------- | ------------ | ---------------------------- | ------------ | ----------- | --- |
|            | Tên:………….... |                              | Điện         | thoại:…………. |     |
|            | Địa          | chỉ: …….....            Ngày |              | tiếp nhận:  | ……  |
|            | Quy          | tắc kiểm                     | tra tính     | hợp lệ      |     |
| Tên: không | được trống…  | Điện                         | thoại: không | được trống  |     |
Địa chỉ: không được trống.. Ngày tiếp nhận: <= ngày hiện hành
Software Engineering 33
tkhuong@dthu.edu.vn

|         | VD. Tiếp |         |     | nhận | đối | tác |     |     |
| ------- | -------- | ------- | --- | ---- | --- | --- | --- | --- |
| ❖ Thiết | kế       | dữ liệu |     |      |     |     |     |     |
Doi_Tac
MaDT: Auto
|     | ▪ Cấu | trúc |     |     |      |        |     |     |
| --- | ----- | ---- | --- | --- | ---- | ------ | --- | --- |
|     |       |      |     |     | Ten: | String |     |     |
|     | ▪ Nội | dung |     |     |      |        |     |     |
DienThoai: String
DiaChi: String
|     |      |      |      |               | NgayTiepNhan: |        |      | Date         |
| --- | ---- | ---- | ---- | ------------- | ------------- | ------ | ---- | ------------ |
|     | MaDT | Ten  |      | DienThoai     |               | DiaChi |      | NgayTiepNhan |
|     | 1    | Công | ty A | 0673. 112 335 | CL,           | Đồng   | Tháp | 17/11/2016   |
|     | 2    | …    |      | ….            | …             |        |      | ….           |
Software Engineering 34
tkhuong@dthu.edu.vn

|      | VD2. Xếp |     |     |       | loại |        | học    | lực | của | học | sinh |
| ---- | -------- | --- | --- | ----- | ---- | ------ | ------ | --- | --- | --- | ---- |
| Phân | tích     | yêu | cầu | (Ngôn |      | ngữ tự | nhiên) |     |     |     |      |
❖ Với yêu cầu lập bảng xếp loại học lực, phần mềm bao gồm các
|     | người | sử   | dụng | và    | chức | năng        | như | sau: |        |      |     |
| --- | ----- | ---- | ---- | ----- | ---- | ----------- | --- | ---- | ------ | ---- | --- |
| ❖   | Nhân  | viên | văn  | phòng |      | giáo vụ: sử |     | dụng | 2 chức | năng |     |
|     | ▪ Ghi | nhận |      | bảng  | điểm |             |     |      |        |      |     |
|     | ▪ Lập | bảng |      | xếp   | loại | học lực     |     |      |        |      |     |
❖ Ban giám hiệu: chỉ sử dụng 1 chức năng là cập nhật quy tắc xếp loại
|     | học | lực |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ghi chú: Chi tiết các chức năng sẽ mô tả sau, chưa xem xét hết tất cả các chức
năng
Software Engineering 35
tkhuong@dthu.edu.vn

|     | VD2. Xếp |          |          |        | loại    |      | học      |          | lực  |     | của  | học | sinh    |
| --- | -------- | -------- | -------- | ------ | ------- | ---- | -------- | -------- | ---- | --- | ---- | --- | ------- |
|     |          |          |          | Bảng   | điểm    | môn  | ….       |          |      |     |      |     |         |
|     |          |          | Lớp      | … Niên |         | khóa | …        |          |      |     |      |     |         |
|     | Học sinh |          | Điểm     |        | 15 Điểm |      | 1 tiết   | Điểm     |      | HK  |      |     |         |
|     | Ghí chú: |          |          |        |         |      |          |          |      |     |      |     |         |
|     | - Trường |          | có 9 môn |        | học …   |      |          |          |      |     |      |     |         |
|     | Điểm     | 15, điểm |          | 1 tiết | có thể  | có   | nhiều    | cột      |      |     |      |     |         |
|     | - Điểm   | số       | là số    | thực   | có giá  | trị  | từ 0 đến | 10       |      |     |      |     |         |
|     |          |          |          |        |         | Bảng |          | xếp loại | học  | lực |      |     |         |
|     |          |          |          |        |         | Lớp  | … Niên   |          | khóa | …   |      |     |         |
|     | Học sinh |          |          | TBHK1  |         |      |          | TBHK2    |      |     | TBCN |     | Học lực |
TBHK1, TBHK2: trung bình cuối học kỳ được tính dựa trên quy tắc tính điểm trung
| bình | học kỳ |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TBCN: trung bình cuối năm được tính dựa trên quy tắc tính điểm trung bình cuối
năm
| Học | lực: được |     | tính | điểm | dựa | trên | quy | tắc xếp | loại | học | lực |     |     |
| --- | --------- | --- | ---- | ---- | --- | ---- | --- | ------- | ---- | --- | --- | --- | --- |
Software Engineering 36
tkhuong@dthu.edu.vn

|          | BÀI TẬP thiết |          |      | kế dữ |      | liệu  |         |      |
| -------- | ------------- | -------- | ---- | ----- | ---- | ----- | ------- | ---- |
| 1) Thiết | kế dữ         | liệu cho | chức | năng  | Lập  | phiếu | thu     |      |
| 2) Thiết | kế dữ         | liệu cho | chức | năng  | Tiếp | nhận  | nhân    | viên |
| 3) Thiết | kế dữ         | liệu cho | chức | năng  | Lập  | hóa   | đơn bán | hàng |
Software Engineering 37
tkhuong@dthu.edu.vn

|     | Đề  |     | bài | tập |     | 1   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Dựa vào hồ sơ phân tích, hãy thiết kế dữ liệu phần mềm quản
| lý   | bán | hàng | khi | chỉ | xem | xét | chức | năng | Lập | phiếu | thu |
| ---- | --- | ---- | --- | --- | --- | --- | ---- | ---- | --- | ----- | --- |
| ❖ Mô | tả: |      |     |     |     |     |      |      |     |       |     |
Chức năng cho phép nhân viên của cửa hàng ghi nhận thông tin
| về phiếu    |     | thu | qua 2 bước |     |      | như | sau:  |        |     |       |     |
| ----------- | --- | --- | ---------- | --- | ---- | --- | ----- | ------ | --- | ----- | --- |
| B1. NV cung |     |     | cấp        | cho | phần | mềm | thông | tin về |     | phiếu | thu |
B2. Phần mềm tiến hành kiểm tra tính hợp lệ và sau đó ghi nhận
| thông | tin tương |     | ứng |     | vào | bộ nhớ | phụ | (nếu | hợp | lệ) |     |
| ----- | --------- | --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- |
Software Engineering 38
tkhuong@dthu.edu.vn

| Đề  | bài |     | tập | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Cấu trúc:
|     |     |     |                                     |     | Phiếu | thu | tiền       |            |
| --- | --- | --- | ----------------------------------- | --- | ----- | --- | ---------- | ---------- |
|     |     | Họ  | và Tên:…………....                     |     |       |     | CMND:…………. |            |
|     |     | Địa | chỉ: ……..............          Ngày |     |       |     |            | thu: ……... |
Số tiền: ………………
|         |       |      | Quy    | tắc | kiểm tra   | tính | hợp   | lệ  |
| ------- | ----- | ---- | ------ | --- | ---------- | ---- | ----- | --- |
| Họ Tên: | không | được | trống… |     | CMND: được |      | trống |     |
Địa chỉ: được trống..                Ngày thu: <=ngày hiện hành
| Số tiền: không |     | được | rỗng |     |     |     |     |     |
| -------------- | --- | ---- | ---- | --- | --- | --- | --- | --- |
Software Engineering 39
tkhuong@dthu.edu.vn

|         | Giải |     | bài  |     | tập |     | 1   |     |     |     |     |     |     |
| ------- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ❖ Thiết | kế   | dữ  | liệu |     |     |     |     |     |     |     |     |     |     |
KhachHang
|     |     |      |     |            |             | Phiếu |      | thu        |           |     |          |                |        |
| --- | --- | ---- | --- | ---------- | ----------- | ----- | ---- | ---------- | --------- | --- | -------- | -------------- | ------ |
|     |     |      |     |            | MaPT: Auto  |       |      |            |           |     |          | MaKH: Auto     |        |
| ▪   | Cấu | trúc |     |            |             |       |      |            |           |     |          |                |        |
|     |     |      |     |            | Ngaylap:    |       | Date |            |           |     |          | HoTen:         | String |
| ▪   | Nội | dung |     |            |             |       |      |            |           |     |          |                |        |
|     |     |      |     |            | SoTien: Int |       |      |            |           |     |          | CMND: String   |        |
|     |     |      |     |            | MaKH: Int   |       |      |            |           |     |          | DiaChi: String |        |
|     |     | MaPT |     |            | Ngaylap     |       |      |            | SoTien    |     | MaKH     |                |        |
|     |     | 1    |     | 17/11/2016 |             |       |      | 20.000.000 |           | 2   |          |                |        |
|     |     | MaKH |     |            |             | HoTen |      |            | CMND      |     | DiaChi   |                |        |
|     |     | 1    |     | Nguyễn     |             | Văn   | An   |            | 112345678 |     | CL, Đồng | Tháp           |        |
|     |     | 2    |     | …          |             |       |      |            | ….        |     | …        |                |        |
Software Engineering 40
tkhuong@dthu.edu.vn

|     | Đề  | bài |     | tập |     | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Dựa vào hồ sơ phân tích, hãy thiết kế dữ liệu phần mềm quản
| lý           | bán   | hàng   | khi | chỉ  | xem  |      | xét chức   | năng     |            | Tiếp | nhận  |      | Nhân   | viên   |
| ------------ | ----- | ------ | --- | ---- | ---- | ---- | ---------- | -------- | ---------- | ---- | ----- | ---- | ------ | ------ |
| ❖ Mô         | tả:   |        |     |      |      |      |            |          |            |      |       |      |        |        |
| Chức         | năng  | cho    |     | phép | nhân |      | viên phòng |          | tổ         | chức | của   | công |        | ty ghi |
| nhận         | thông | tin về |     | hồ   | sơ   | của  | nhân       | viên     | qua 2 bước |      |       | như  | sau:   |        |
| B1. NV phòng |       |        | tổ  | chức |      | cung | cấp        | cho phần |            | mềm  | thông |      | tin về | hồ     |
| sơ nhân      |       | viên   |     |      |      |      |            |          |            |      |       |      |        |        |
B2. Phần mềm tiến hành kiểm tra tính hợp lệ và sau đó ghi thông
| tin tương |     | ứng | vào | bộ  | nhớ |     | phụ (nếu | hợp |     | lệ) |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 42
tkhuong@dthu.edu.vn

| Đề  | bài | tập | 2   |       |      |      |     |
| --- | --- | --- | --- | ----- | ---- | ---- | --- |
|     |     |     |     | Hồ sơ | Nhân | viên |     |
❖ Cấu trúc:
|     |     | Họ                                   | và Tên:………….... |     |     | Giới | tính:………….  |
| --- | --- | ------------------------------------ | --------------- | --- | --- | ---- | ----------- |
|     |     | CMND: ……..............          Ngày |                 |     |     |      | sinh: ……... |
Địa chỉ: ………………
|         |       | Trinh độ: …………….         Đơn |         |                       |      |     | vị:………….. |
| ------- | ----- | ---------------------------- | ------- | --------------------- | ---- | --- | --------- |
|         |       |                              | Quy tắc | kiểm tra              | tính | hợp | lệ        |
| Họ Tên: | không | được                         | trống…  | Giới tính: Nam hay Nữ |      |     |           |
CMND: không được trống..       Ngày sinh: tương ứng độ tuổi từ 20-50
| Địa chỉ: không |     | được | rỗng………….. |     |     |     |     |
| -------------- | --- | ---- | ---------- | --- | --- | --- | --- |
Trình độ: 1 trong 3 trình độ Cao đẳng, Đại học và Sau đại học
| Đơn vị: 1 trong |     | các | đơn vị hiện | nay của | công | ty  |     |
| --------------- | --- | --- | ----------- | ------- | ---- | --- | --- |
Software Engineering 43
tkhuong@dthu.edu.vn

|     | Đề  |     | bài | tập |     | 3   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
❖ Dựa vào hồ sơ phân tích, hãy thiết kế dữ liệu phần mềm quản
| lý   | bán | hàng | khi | chỉ | xem | xét | chức | năng | Lập | hóa | đơn |
| ---- | --- | ---- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- |
| ❖ Mô | tả: |      |     |     |     |     |      |      |     |     |     |
Chức năng cho phép nhân viên của cửa hàng ghi nhận thông tin
| lập hóa     |     | đơn | qua 2 bước |     |      | như | sau:  |     |        |      |             |
| ----------- | --- | --- | ---------- | --- | ---- | --- | ----- | --- | ------ | ---- | ----------- |
| B1. NV cung |     |     | cấp        | cho | phần | mềm | thông |     | tin về | việc | lập hóa đơn |
B2. Phần mềm tiến hành kiểm tra tính hợp lệ và sau đó ghi thông
| tin tương |     | ứng | vào | bộ  | nhớ | phụ | (nếu | hợp | lệ) |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Software Engineering 47
tkhuong@dthu.edu.vn

|       |      | Đề  |       | bài   |       | tập             |                    | 3    |          |          |      |       |          |     |
| ----- | ---- | --- | ----- | ----- | ----- | --------------- | ------------------ | ---- | -------- | -------- | ---- | ----- | -------- | --- |
|       |      |     |       |       |       |                 |                    | Hóa  | đơn      | bán hàng |      |       |          |     |
| ❖     | Cấu  |     | trúc: |       |       |                 |                    |      |          |          |      |       |          |     |
|       |      |     |       |       |       | Khách           | hàng:…………....……... |      |          |          |      |       |          |     |
|       |      |     |       |       |       | Địa chỉ: ……………… |                    |      |          |          |      |       |          |     |
|       |      |     |       |       |       | Ngày            | lập:…………….         |      |          |          |      |       |          |     |
|       |      |     |       |       |       | STT             | Mặt                | hàng | Số lượng | Đơn      | giá  | Thành | tiền     |     |
|       |      |     |       |       |       | 1               | …..                |      | …..      | ….       |      | ……    |          |     |
|       |      |     |       |       |       |                 |                    |      |          |          | Tổng |       | tiền: …. |     |
|       | Quy  | tắc | kiểm  | tra   | tính  | hợp             | lệ                 |      |          |          |      |       |          |     |
| Khách | hàng |     | (Họ   | Tên): | không | được            |                    |      |          |          |      |       |          |     |
|       |      |     |       |       |       |                 |                    |      |          |          | Quy  | tắc   | xử lý    |     |
trống…
|     |               |     |        |     |     |      |      |     | Đơn giá   | =  theo    | quy   | định     | của công  | ty (k nhập) |
| --- | ------------- | --- | ------ | --- | --- | ---- | ---- | --- | --------- | ---------- | ----- | -------- | --------- | ----------- |
| Địa | chỉ: được     |     | trống… |     |     |      |      |     |           |            |       |          |           |             |
|     |               |     |        |     |     |      |      |     | Thành     | tiền =  số | lượng |          | * Đơn giá |             |
| Mặt | hàng: 1 trong |     |        | các | mặt | hàng | hiện | có  |           |            |       |          |           |             |
|     |               |     |        |     |     |      |      |     | Tổng tiền | =   tổng   |       | tiền của | từng mặt  | hàng        |
| của | công          | ty  |        |     |     |      |      |     |           |            |       |          |           |             |
Số lượng: >0
Software Engineering 48
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 52
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C5_3ThietKePM_TKDuLieu_HDT.md -->

---


<!-- BẮT ĐẦU FILE: C5_4ThietKePM_TKGiaoDien.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 5
THIẾT KẾ PHẦN MỀM
– GIAO DIỆN
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG CHI TIẾT
GIAO DIỆN NGƯỜI DÙNG (UI)
THIẾT KẾ
PHẦN
THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
MỀM -
GIAO
XỬ LÝ GIAO DIỆN NGƯỜI DÙNG
DIỆN
THIẾT KẾ XỬ LÝ GIAO DIỆN NGƯỜI DÙNG
Software Engineering 2
tkhuong@dthu.edu.vn

1. GIAO DIỆN NGƯỜI DÙNG
❖ VAI TRÒ CỦA GIAO DIỆN
❖ GIAO DIỆN NGƯỜI DÙNG (UI)
Software Engineering 4
tkhuong@dthu.edu.vn

1.1 VAI TRÒ CỦA GIAO DIỆN
❖ Phần mềm không hoạt động độc lập
❖ Phần mềm giao tiếp với
▪ Người sử dụng
▪ Các hệ thống liên quan
❖ Cần thành phần phụ trách giao tiếp?
→ Giao diện
▪ Nơi diễn ra tương tác
▪ Định nghĩa cách thức giao tiếp
▪ Tiếp nhận và phản hồi thông tin
Software Engineering 5
tkhuong@dthu.edu.vn

|           | 1.2 Giao |      | diện | người | dùng | (UI) |
| --------- | -------- | ---- | ---- | ----- | ---- | ---- |
| ❖ Ý nghĩa | sử       | dụng |      |       |      |      |
| ❖ Cấu     | trúc tổ  | chức |      |       |      |      |
| ❖ Công    | nghệ     | giao | diện |       |      |      |
Software Engineering 7
tkhuong@dthu.edu.vn

| 1.2 Giao |               | diện | người | dùng             | (UI) |
| -------- | ------------- | ---- | ----- | ---------------- | ---- |
| HỆ       | THỐNG THỰC TẾ |      |       | HỆ THỐNG TIN HỌC |      |
| X thực   | hiện nghiệp   | vụ   |       | X                | Y    |
f1, f2, …
|        |             |     |     | Thành | phần |
| ------ | ----------- | --- | --- | ----- | ---- |
| Y thực | hiện nghiệp | vụ  |     |       |      |
giao diện
g1, g2, ….
Software Engineering 8
tkhuong@dthu.edu.vn

|         |       | 1.2 UI –  |      |        |       | Ý nghĩa |         |      |      | sử       |      | dụng  |       |     | (1)     |
| ------- | ----- | --------- | ---- | ------ | ----- | ------- | ------- | ---- | ---- | -------- | ---- | ----- | ----- | --- | ------- |
| ❖       | Thành |           | phần |        | của   |         | phần    |      | mềm  | cho      | phép |       | người |     | sử dụng |
|         | thực  | hiện      |      | nghiệp |       |         | vụ      | với  | phần | mềm      |      | thông |       | qua |         |
|         | ▪     | Cung      |      | cấp    | thông |         | tin/ dữ |      | liệu | cho      | phần |       | mềm   |     |         |
|         | ▪     | Nhận/ xem |      |        |       | các     | kết     | quả  | xử   | lý tượng |      | ứng   |       |     |         |
| ==> Xem |       |           | xét  |        | tính  | tiện    |         | dụng |      |          |      |       |       |     |         |
Software Engineering 9
tkhuong@dthu.edu.vn

|     |     | 1.2 UI – |     |     |     |     | Cấu |     | trúc |     | tổ  | chức |     |     | (2) |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
❖
|          | Màn |      | hình  |        | giao |      | diện:   |       |       |     |            |      |      |      |            |     |
| -------- | --- | ---- | ----- | ------ | ---- | ---- | ------- | ----- | ----- | --- | ---------- | ---- | ---- | ---- | ---------- | --- |
| Thành    |     |      | phần  |        | giao |      | diện    | trong |       | hệ  | thống      | bao  |      | gồm  | các màn    |     |
| hình     |     | giao |       | diện   |      | cho  | phép    |       | người |     | dùng       | thực |      | hiện | các nghiệp |     |
| vụ       | với |      | phần  |        | mềm  |      |         |       |       |     |            |      |      |      |            |     |
| ==> Mỗi  |     |      |       | màn    |      | hình | giao    |       | diện  | cho | phép       | thực |      | hiện | đúng       | 1   |
| nghiệp   |     |      | vụ??? |        |      |      |         |       |       |     |            |      |      |      |            |     |
| == > Mỗi |     |      |       | nghiệp |      |      | vụ thực |       | hiện  |     | trên 1 màn |      | hình |      | duy nhất   | ??? |
Software Engineering 10
tkhuong@dthu.edu.vn

| VD1. UI – |     | Cấu | trúc |     | tổ chức |     |     |
| --------- | --- | --- | ---- | --- | ------- | --- | --- |
❖
| VD minh họa | màn | hình | giao | diện | pm Quản | lý nhân | sự  |
| ----------- | --- | ---- | ---- | ---- | ------- | ------- | --- |
MH_DANG_KY
MH_QLNS MH_BGĐ
MH_TNHS MH_CNCT
MH_CN_XHS
MH_TCHS
Software Engineering 11
tkhuong@dthu.edu.vn

|        |       |      | 1.2 UI – |       |         |      | Cấu   |      | trúc |       | tổ    | chức    |      | (2)     |       |       |
| ------ | ----- | ---- | -------- | ----- | ------- | ---- | ----- | ---- | ---- | ----- | ----- | ------- | ---- | ------- | ----- | ----- |
| ❖      | Đối   |      | tượng    |       | giao    |      | diện: |      |      |       |       |         |      |         |       |       |
| Màn    |       | hình |          | giao  |         | diện | bao   |      | gồm  | bên   | trong |         | các  | đối     | tượng | giao  |
| diện   |       | cho  |          | phép  |         | thể  | hiện  | các  |      | thông |       | tin/ dữ | liệu | tương   |       | ứng   |
| nghiệp |       |      | vụ       | đang  |         | xét  |       |      |      |       |       |         |      |         |       |       |
| →      | Mỗi   |      | đối      | tượng |         | giao |       | diện | thể  | hiện  |       | với     | đúng | 1 thông |       | tin/  |
|        | dữ    |      | liệu???  |       |         |      |       |      |      |       |       |         |      |         |       |       |
| →      |       | Mỗi  | thông    |       | tin/ dữ |      |       | liệu | được | thể   |       | hiện    | với  | đúng    | 1 đối |       |
|        | tượng |      |          | giao  | diện    |      | ???   |      |      |       |       |         |      |         |       |       |
Software Engineering 12
tkhuong@dthu.edu.vn

|      | VD2. UI –   |                  |           | Cấu  |       | trúc |      | tổ chức |          |      |
| ---- | ----------- | ---------------- | --------- | ---- | ----- | ---- | ---- | ------- | -------- | ---- |
| ❖ Ví | dụ minh họa |                  | các       | đối  | tượng |      | giao | diện    | trên màn | hình |
| Tiếp | nhận        | hồ sơ            |           | nhân | viên  |      |      |         |          |      |
|      |             |                  |           | Tiếp | nhận  | hồ   | sơ   | mới     |          |      |
|      |             | Mã số: ********* |           |      |       |      |      | Nam     | Nữ       |      |
|      |             | Họ và            | tên: ………. |      |       |      |      |         |          |      |
|      |             | Ngày             | sinh: ……… |      |       |      |      |         |          |      |
Địa chỉ: …………..
…………………….
|     |     |     |     | Ghi |     |     |     | Kết thúc |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
Software Engineering 13
tkhuong@dthu.edu.vn

1.2 UI – Công nghệ giao diện (3)
GIAO DIỆN
CONSOLE
GIAO DIỆN ĐIỆN
THOẠI DI ĐỘNG
GIAO DIỆN
WINDOW
GIAO DIỆN
……
GIAO DIỆN
WEB
Software Engineering 14
tkhuong@dthu.edu.vn

GIAO DIỆN CONSOLE
| ❖ Cấu |      | trúc    |       |      |           |        |       |       |       |      |       |      |          |     |
| ----- | ---- | ------- | ----- | ---- | --------- | ------ | ----- | ----- | ----- | ---- | ----- | ---- | -------- | --- |
| ▪     | Màn  |         | hình  | giao | diện: chỉ |        | gồm   | một   | màn   |      | hình  | giao | diện     | duy |
|       | nhất |         | chung | cho  | mọi       | nghiệp |       | vụ    |       |      |       |      |          |     |
| ▪     | Đối  | tượng   |       | giao | diện: gồm |        |       | 2 đối | tượng |      | giao  | diện | cơ       | bản |
|       | •    | Đối     | tượng |      | tiếp nhận |        | thông | tin   |       |      |       |      |          |     |
|       | •    | Đối     | tượng |      | kết xuất  | thông  |       | tin   |       |      |       |      |          |     |
| ❖ Đặc | điểm |         |       |      |           |        |       |       |       |      |       |      |          |     |
| ▪     | Dễ   | học, dễ |       | sử   | dụng      | nhưng  |       | khó   | thể   | hiện | thông |      | tin dạng | tự  |
nhiên
| →   | thiếu |     | tính | tiện | dụng |                      |     |     |     |     |     |     |     |     |
| --- | ----- | --- | ---- | ---- | ---- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |       |     |      |      |      | Software Engineering |     |     |     |     |     |     |     | 15  |
tkhuong@dthu.edu.vn

GIAO DIỆN WINDOWS
❖ Cấu trúc
▪ Màn hình giao diện: cho phép sử dụng nhiều màn hình giao diện với
| số  | lượng | tùy theo | người | thiết | kế  |     |     |     |
| --- | ----- | -------- | ----- | ----- | --- | --- | --- | --- |
▪ Đối tượng giao diện: gồm nhiều và đa dạng các đối tượng giao diện
• Đối tượng giao diện thư viện do môi trường lập trình cung cấp
• Đối tượng giao diện tự định nghĩa do các chuyên viên tin học thiết kế và
|     | thực | hiện dựa | trên | các đối | tượng | giao diện | đã có |     |
| --- | ---- | -------- | ---- | ------- | ----- | --------- | ----- | --- |
❖ Đặc điểm
| ▪ Cho phép |     | thể | hiện | thông tin dạng |     | tự nhiên | nhất có | thể |
| ---------- | --- | --- | ---- | -------------- | --- | -------- | ------- | --- |
▪ Cần nhiều thời gian để học và tận dụng các khả năng của đối tượng
| giao | diện | người | dùng |     |     |     |     |     |
| ---- | ---- | ----- | ---- | --- | --- | --- | --- | --- |
Software Engineering 16
tkhuong@dthu.edu.vn

GIAO DIỆN WEB
❖ Cấu trúc
▪ Màn hình giao diện: cho phép sử dụng nhiều màn hình giao diện với
| số  | lượng | tùy theo | người | thiết kế |     |     |     |
| --- | ----- | -------- | ----- | -------- | --- | --- | --- |
▪ Đối tượng giao diện: gồm nhiều và đa dạng các đối tượng giao diện
• Đối tượng giao diện thư viện do môi trường lập trình cung cấp
• Đối tượng giao diện tự định nghĩa do các chuyên viên tin học thiết kế và
|     | thực | hiện dựa | trên các | đối tượng | giao diện | đã có |     |
| --- | ---- | -------- | -------- | --------- | --------- | ----- | --- |
❖ Đặc điểm
| ▪ Cho phép |     | thể hiện | thông | tin dạng | tự nhiên | nhất có | thể |
| ---------- | --- | -------- | ----- | -------- | -------- | ------- | --- |
▪ Chuẩn hóa: HTML/ XHTML là ngôn ngữ thống nhất chung mô tả các
| đối    | tượng | giao diện | người | dùng |     |     |     |
| ------ | ----- | --------- | ----- | ---- | --- | --- | --- |
| → Tính | mang  | chuyển    |       |      |     |     |     |
Software Engineering 17
tkhuong@dthu.edu.vn

NỘI DUNG CHI TIẾT
GIAO DIỆN NGƯỜI DÙNG (UI)
THIẾT KẾ
PHẦN
THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
MỀM -
GIAO
XỬ LÝ GIAO DIỆN NGƯỜI DÙNG
DIỆN
THIẾT KẾ XỬ LÝ GIAO DIỆN NGƯỜI DÙNG
Software Engineering 18
tkhuong@dthu.edu.vn

2. THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ KHÁI NIỆM
❖ NGUYÊN TẮC THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ CÁC KIỂU TƯƠNG TÁC
❖ QUY TRÌNH THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ KỸ THUẬT THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
Software Engineering 19
tkhuong@dthu.edu.vn

| Phân | tích |     |
| ---- | ---- | --- |
Hồ sơ
viên
phân tích
| Phụ | trách |     |
| --- | ----- | --- |
Kiến trúc về
| thiết kế | giao diện | công nghệ |
| -------- | --------- | --------- |
| Hồ       | sơ thiết  |           |
Lập trình
| kế  | giao diện |     |
| --- | --------- | --- |
viên
Software Engineering 20
tkhuong@dthu.edu.vn

2.1 KHÁI NIỆM THIẾT KẾ UI
| ❖   | Thiết | kế  | giao  | diện  |     | người | dùng |      |      |     |          |      |     |     |
| --- | ----- | --- | ----- | ----- | --- | ----- | ---- | ---- | ---- | --- | -------- | ---- | --- | --- |
|     | ▪     | Mô  | tả hệ | thống |     | các   | màn  | hình | giao |     | diện của | phần | mềm | dựa |
trên
|     |     | •   | Hồ sơ | phân |     | tích | yêu | cầu | (đặc | biệt | các | dòng | dữ liệu |     |
| --- | --- | --- | ----- | ---- | --- | ---- | --- | --- | ---- | ---- | --- | ---- | ------- | --- |
nhập/ xuất)
|     |       | •   | Công  | nghệ |      | giao | diện                 | được | chọn |     |      |     |      |     |
| --- | ----- | --- | ----- | ---- | ---- | ---- | -------------------- | ---- | ---- | --- | ---- | --- | ---- | --- |
|     | →Lưu  |     | ý xem |      | xét  | tính | tiện                 | dụng |      |     |      |     |      |     |
|     | →Hiểu |     | rõ    | khả  | năng |      | của                  | công | nghệ |     | đang | sử  | dụng |     |
|     |       |     |       |      |      |      | Software Engineering |      |      |     |      |     |      | 21  |
tkhuong@dthu.edu.vn

2.1 KHÁI NIỆM THIẾT KẾ UI
| ❖   | Hồ    | sơ  | thiết  | kế   | giao |      | diện  | người |      | dùng |      |      |      |     |      |
| --- | ----- | --- | ------ | ---- | ---- | ---- | ----- | ----- | ---- | ---- | ---- | ---- | ---- | --- | ---- |
|     | ▪     | Tài | liệu   | mô   | tả   | hệ   | thống |       | các  | màn  | hình | giao | diện | của | phần |
|     |       | mềm | theo   |      | công |      | nghệ  |       | giao | diện | được | chọn |      |     |      |
| ➢   | Thiết |     | kế với | công |      | nghệ |       | cụ    | thể  |      |      |      |      |     |      |
o
Sử dụng các khái niệm từ khóa đặc thù của công nghệ giao diện
|     |       | được | chọn   |     |      |      |      |       |     |     |     |           |     |      |      |
| --- | ----- | ---- | ------ | --- | ---- | ---- | ---- | ----- | --- | --- | --- | --------- | --- | ---- | ---- |
| ➢   | Thiết |      | kế độc |     | lập  | công |      | nghệ  |     |     |     |           |     |      |      |
|     | o     | Sử   | dụng   | các | khái |      | niệm | chung |     | cho | các | công nghệ |     | giao | diện |
Software Engineering 22
tkhuong@dthu.edu.vn

2.2 NGUYÊN TẮC THIẾT KẾ UI
❖ Khi thiết kế UI phải tính đến kinh nghiệm, năng lực, nhu cầu của
| người   |     | dùng:      |          |     |             |     |           |     |       |     |     |
| ------- | --- | ---------- | -------- | --- | ----------- | --- | --------- | --- | ----- | --- | --- |
| ▪       | Khả | năng dùng  |          | bàn | phím, chuột |     |           |     |       |     |     |
| ▪       | Tốc | độ phản    | ứng, khả |     | năng        | nhớ | thao      | tác |       |     |     |
| ▪       | Sở  | thích, văn | hóa, lứa |     | tuổi: màu   |     | sắc, ngôn |     | ngữ,… |     |     |
| ❖ Người |     | thiết kế   | nên      |     |             |     |           |     |       |     |     |
▪ Nhận thức được các hạn chế về vật lý và tinh thần của người dùng
|     | •    | Ví dụ: khả | năng | nhớ     | ngắn | hạn | bị hạn | chế   |      |      |     |
| --- | ---- | ---------- | ---- | ------- | ---- | --- | ------ | ----- | ---- | ---- | --- |
|     | •    | Nên thừa   | nhận | ai cũng | có   | thể | nhầm   | lẫn   |      |      |     |
| ▪   | Luôn | bao gồm    | việc | làm     | bản  | mẫu | để     | người | dùng | đánh | giá |
Software Engineering 23
tkhuong@dthu.edu.vn

2.2 NGUYÊN TẮC THIẾT KẾ UI
| ❖ Các |     | nguyên | tắc | thiết |     | kế: |     |     |     |     |     |
| ----- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
▪
|     | Thân | thiện |     | với người |     | dùng |     |     |     |     |     |
| --- | ---- | ----- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
• Giao diện nên dựa vào các thuật ngữ và khái niệm hướng người
|     |     | dùng | hơn | là các |     | khái niệm | máy | tính. |     |     |     |
| --- | --- | ---- | --- | ------ | --- | --------- | --- | ----- | --- | --- | --- |
• Ví dụ, một hệ thống văn phòng nên dùng các khái niệm như thư từ,
|     |      | tài liệu, |     | thư mục,... |     | hơn | là đường | dẫn, | tên | file,... |     |
| --- | ---- | --------- | --- | ----------- | --- | --- | -------- | ---- | --- | -------- | --- |
| ▪   | Nhất | quán      |     |             |     |     |          |      |     |          |     |
• Hệ thống nên hiển thị một cách nhất quán. Các lệnh và menu nên
|     |     | có cùng |     | định | dạng, | các | dấu chấm | lệnh | nên | tương | tự nhau... |
| --- | --- | ------- | --- | ---- | ----- | --- | -------- | ---- | --- | ----- | ---------- |
| ▪   | Ít  | bất ngờ |     |      |       |     |          |      |     |       |            |
• Nếu một lệnh được thực hiện theo cách thông thường, người dùng
|     |     | có thể | dự  | đoán | được | thao | tác của | các | lệnh | tương | tự. |
| --- | --- | ------ | --- | ---- | ---- | ---- | ------- | --- | ---- | ----- | --- |
Software Engineering 24
tkhuong@dthu.edu.vn

2.2 NGUYÊN TẮC THIẾT KẾ UI
| ❖ Các | nguyên |      | lý thiết | kế (tt): |     |     |     |     |     |
| ----- | ------ | ---- | -------- | -------- | --- | --- | --- | --- | --- |
| ▪     | Có thể | khôi | phục     | được     |     |     |     |     |     |
• Hệ thống nên cung cấp một số cơ chế phục hồi lại tình trạng hoạt
|     | động  | bình | thường | sau khi  | gặp lỗi. | Cơ chế | này có    | thể bao | gồm |
| --- | ----- | ---- | ------ | -------- | -------- | ------ | --------- | ------- | --- |
|     | chức  | năng | undo,  | xác nhận | một hành | động   | hủy, xóa, | ...     |     |
| ▪   | Hướng | dẫn  | người  | dùng     |          |        |           |         |     |
• Một số hướng dẫn người dùng như hệ thống giúp đỡ, tài liệu trực
|     | tuyến   | ...   | nên được | cung cấp. |     |     |     |     |     |
| --- | ------- | ----- | -------- | --------- | --- | --- | --- | --- | --- |
| ▪   | Đa dạng | người | dùng     |           |     |     |     |     |     |
• Nên cung cấp các tiện ích tương tác cho các loại người dùng khác
nhau.
• Ví dụ, một số người dùng có khả năng nhìn hạn chế thì nên để cỡ
|     | chữ | to  | hơn. |                      |     |     |     |     |     |
| --- | --- | --- | ---- | -------------------- | --- | --- | --- | --- | --- |
|     |     |     |      | Software Engineering |     |     |     |     | 25  |
tkhuong@dthu.edu.vn

|     |       | Vấn   | đề   |     | thiết |     | kế   | trong |     |       | các |          | UI  |      |       |
| --- | ----- | ----- | ---- | --- | ----- | --- | ---- | ----- | --- | ----- | --- | -------- | --- | ---- | ----- |
| ❖   | Hai   | vấn   | đề   | cần | được  |     | quan |       | tâm | trong |     | thiết    | kế  | hệ   | thống |
|     | tương | tác   |      |     |       |     |      |       |     |       |     |          |     |      |       |
|     | ▪     | Người | dùng |     | cung  | cấp |      | thông | tin | cho   |     | hệ thống |     | bằng | cách  |
nào?
|     | ▪   | Hệ thống |     | biểu | diễn | thông |                      | tin | đến | người |     | dùng | như | thế | nào? |
| --- | --- | -------- | --- | ---- | ---- | ----- | -------------------- | --- | --- | ----- | --- | ---- | --- | --- | ---- |
|     |     |          |     |      |      |       | Software Engineering |     |     |       |     |      |     |     | 26   |
tkhuong@dthu.edu.vn

2.3 CÁC KIỂU TƯƠNG TÁC
| ❖ Thao | tác trực                 | tiếp                | (direct manipulation)  |
| ------ | ------------------------ | ------------------- | ---------------------- |
| ❖ Chọn | menu (menu selection)    |                     |                        |
| ❖ Điền | vào form (form fill-in)  |                     |                        |
| ❖ Ngôn | ngữ lệnh                 | (command language)  |                        |
| ❖ Ngôn | ngữ tự                   | nhiên               | (natural language)     |
Software Engineering 27
tkhuong@dthu.edu.vn

2.3 CÁC KIỂU TƯƠNG TÁC
Software Engineering 28
tkhuong@dthu.edu.vn

| Một      | số   | vấn  |     | đề   | trong |       | thiết    | kế giao | diện |
| -------- | ---- | ---- | --- | ---- | ----- | ----- | -------- | ------- | ---- |
| ❖ Phương |      | pháp |     | hiển | thị   | thông | tin, màu |         |      |
| ❖ Thời   | gian | phản |     | hồi  | của   | hệ    | thống    |         |      |
| ❖ Cách   | thức |      | xây | dựng | thông |       | báo      |         |      |
| ❖ Các    | tiện | ích  | trợ | giúp |       |       |          |         |      |
Software Engineering 29
tkhuong@dthu.edu.vn

|      | Một      | số vấn  | đề trong | thiết | kế giao | diện |
| ---- | -------- | ------- | -------- | ----- | ------- | ---- |
| ❖ Ví | dụ thông | báo lỗi |          |       |         |      |
Software Engineering 30
tkhuong@dthu.edu.vn

2.4 QUY TRÌNH THIẾT KẾ UI
❖ Thiết kế UI là một quy trình có tính lặp lại với mối liên hệ
| chặt | chẽ    | giữa | người  | dùng | và người | thiết kế. |     |     |
| ---- | ------ | ---- | ------ | ---- | -------- | --------- | --- | --- |
| ❖ Có | 3 hoạt | động | chính: |      |          |           |     |     |
▪ Phân tích người dùng: Hiểu người dùng sẽ làm gì với hệ thống;
▪ Xây dựng prototype: Xây dựng một chuỗi các prototype để thử
nghiệm;
| ▪   | Đánh  | giá   | giao diện: | Thử                  | nghiệm | các prototype | này cùng | với |
| --- | ----- | ----- | ---------- | -------------------- | ------ | ------------- | -------- | --- |
|     | người | dùng. |            |                      |        |               |          |     |
|     |       |       |            | Software Engineering |        |               |          | 35  |
tkhuong@dthu.edu.vn

2.4 QUY TRÌNH THIẾT KẾ UI
Software Engineering 37
tkhuong@dthu.edu.vn

2. THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ KHÁI NIỆM
❖ NGUYÊN TẮC THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ CÁC KIỂU TƯƠNG TÁC
❖ QUY TRÌNH THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
❖ KỸ THUẬT THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG
Software Engineering 38
tkhuong@dthu.edu.vn

2.5 KỸ THUẬT THIẾT KẾ UI
| ❖ Các | bước  | thiết | kế UI |     |
| ----- | ----- | ----- | ----- | --- |
| ❖ Một | số kỹ | thuật | thiết | kế  |
Software Engineering 39
tkhuong@dthu.edu.vn

|     | Các |     | bước |     | thiết |     | kế  | UI  |
| --- | --- | --- | ---- | --- | ----- | --- | --- | --- |
❖
|     | Bước   | 1: Thiết |          | kế tổng     | thể   | giao  |     | diện      |
| --- | ------ | -------- | -------- | ----------- | ----- | ----- | --- | --------- |
|     | ▪ Mô   | tả       | tổng     | thể các     | màn   | hình  |     | giao diện |
|     | ▪ Sự   | tồn      | tại      |             |       |       |     |           |
|     | ▪ Liên | kết      |          |             |       |       |     |           |
| ❖   | Bước   | 2: Thiết |          | kế chi tiết |       | giao  |     | diện      |
|     | ▪ Mô   | tả       | chi tiết | từng        | màn   | hình  |     | giao diện |
|     | ▪ Sắp  | xếp/ bố  |          | trí các     | đối   | tượng |     | giao diện |
|     | ▪ Các  | biến     |          | cố cần      | xử lý |       |     |           |
Software Engineering 40
tkhuong@dthu.edu.vn

|       | Các      | bước | thiết |       | kế UI   |      |      |     |
| ----- | -------- | ---- | ----- | ----- | ------- | ---- | ---- | --- |
|       |          |      | Mô tả | tổng  | thể các | chức | năng |     |
|       |          |      |       | Thiết | kế      |      |      |     |
|       |          |      |       | tổng  | thể     |      |      |     |
| Mô tả | chi tiết | chức |       |       |         |      |      |     |
năng
|     |       |     | Sơ  | đồ  | màn hình | giao | diện |           |
| --- | ----- | --- | --- | --- | -------- | ---- | ---- | --------- |
|     | Thiết | kế  |     |     | Chi tiết | màn  | hình | giao diện |
chi tiết
Software Engineering 41
tkhuong@dthu.edu.vn

|     |       | Sơ    | đồ    |      | màn  | hình |          | giao |     | diện         |          |
| --- | ----- | ----- | ----- | ---- | ---- | ---- | -------- | ---- | --- | ------------ | -------- |
| ❖   | Khái  | niệm  |       |      |      |      |          |      |     |              |          |
|     | ▪ Một |       | trong | các  | công | cụ   | cho phép |      | mô  | tả trực quan | hệ thống |
|     | các   | màn   |       | hình | giao | diện |          |      |     |              |          |
| ❖   | Ký    | hiệu: |       |      |      |      |          |      |     |              |          |
|     |       |       |       |      |      |      |          |      | Tên | màn hình     |          |
| ✓   | Màn   | hình  |       | giao | diện |      |          |      |     |              |          |
| ✓   | Liên  | kết   | 2 màn |      | hình | giao | diện     |      |     |              |          |
Software Engineering 42
tkhuong@dthu.edu.vn

| VD. Sơ | đồ  | màn | hình | giao | diện |
| ------ | --- | --- | ---- | ---- | ---- |
MH_DANG_KY
MH_QLNS MH_BGĐ
| MH_TNHS |     |     |     | MH_CNCT |     |
| ------- | --- | --- | --- | ------- | --- |
MH_CN_XHS
MH_TCHS
Software Engineering 43
tkhuong@dthu.edu.vn

|     | Chi tiết |     |     | màn |     | hình |     | giao | diện |
| --- | -------- | --- | --- | --- | --- | ---- | --- | ---- | ---- |
KÝ HIỆU TRÊN MÀN HÌNH GIAO DIỆN
❖
|     | Dữ liệu | cần | nhập              | mới  |     |     |      |      |     |
| --- | ------- | --- | ----------------- | ---- | --- | --- | ---- | ---- | --- |
|     |         |     | Hay ……. Hay ký    |      |     |     | hiệu | khác |     |
| ❖   | Dữ liệu | kết | xuất              |      |     |     |      |      |     |
|     |         |     | Hay ****** Hay ký |      |     |     | hiệu | khác |     |
| ❖   | Dữ liệu | cập | nhật              |      |     |     |      |      |     |
|     | #####   |     | Hay ##### Hay ký  |      |     |     | hiệu | khác |     |
| ❖   | Dữ liệu | với | giá trị           | định | sẵn |     |      |      |     |
(giá trị)
|     |         |     | Hay (giá |     | trị) Hay ký |     | hiệu | khác |     |
| --- | ------- | --- | -------- | --- | ----------- | --- | ---- | ---- | --- |
| ❖   | Biến cố | cần | xử       | lý  |             |     |      |      |     |
Software Engineering 46
tkhuong@dthu.edu.vn

|            | VD. Chi tiết |     |      | màn        | hình  | giao | diện |
| ---------- | ------------ | --- | ---- | ---------- | ----- | ---- | ---- |
| ❖ Minh họa |              | màn | hình | tiếp nhận  | hồ sơ | nhân | sự   |
|            |              |     | Tiếp | nhận hồ sơ | mới   |      |      |
Mã số: *********
|     |     |     |     |     | Nam | Nữ  |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Họ và tên: ……….
Ngày sinh: ………
Địa chỉ: …………..
…………………….
|     |     |     | Ghi |     | Kết thúc |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- |
Software Engineering 47
tkhuong@dthu.edu.vn

| Một     | số          | kỹ  | thuật | thiết |      | kế   | UI  |
| ------- | ----------- | --- | ----- | ----- | ---- | ---- | --- |
| ❖ Lập   | sơ đồ       | màn | hình  | giao  | diện |      |     |
| ❖ Thiết | kế chi tiết |     | màn   | hình  | giao | diện |     |
Software Engineering 49
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | lập | sơ  | đồ  | màn | hình        | GD        |     |
| ----- | -------- | --- | --- | --- | --- | ----------- | --------- | --- |
| Mô tả | tổng thể |     |     |     | Mô  | tả tổng     | thể màn   |     |
| chức  | năng     |     |     |     |     | hình giao   | diện      |     |
|       |          |     |     |     | Sơ  | đồ màn hình | theo cách | 1   |
|       |          |     |     |     | Sơ  | đồ màn hình | theo cách | 2   |
f1
|     |     |     |     |     | Sơ  | đồ màn hình | theo cách | 3   |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- |
f3
|     |     |     |     |     | Sơ  | đồ màn hình | theo cách | 4   |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | --- |
f2
|     |     |     |                      |     | Sơ  | đồ màn hình | theo cách | 5   |
| --- | --- | --- | -------------------- | --- | --- | ----------- | --------- | --- |
|     |     |     | Software Engineering |     |     |             |           | 50  |
tkhuong@dthu.edu.vn

❖ Cách 1:
MH_CHÍNH
MH_F1 MH_F3
MH_F2
Software Engineering 51
tkhuong@dthu.edu.vn

❖ Cách 2:
MH_F2
MH_F1 MH_F3
Software Engineering 52
tkhuong@dthu.edu.vn

❖ Cách 3:
MH_F2
MH_F1 MH_F3
MH_G
Software Engineering 53
tkhuong@dthu.edu.vn

❖ Cách 4:
MH_F12
MH_F3
MH_G
Software Engineering 54
tkhuong@dthu.edu.vn

❖ Cách 5:
MH_F123
MH_G2
MH_G1
Software Engineering 55
tkhuong@dthu.edu.vn

| Một     | số    | kỹ       | thuật | thiết |      | kế   | UI  |
| ------- | ----- | -------- | ----- | ----- | ---- | ---- | --- |
| ❖ Lập   | sơ đồ | màn      | hình  | giao  | diện |      |     |
| ❖ Thiết | kế    | chi tiết | màn   | hình  | giao | diện |     |
Software Engineering 56
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | thiết | kế       | chi tiết |     | màn    | hình      |     |
| ----- | -------- | ----- | -------- | -------- | --- | ------ | --------- | --- |
| Mô tả | tổng thể |       |          |          | Mô  | tả     | tổng thể  | màn |
|       |          |       | Kỹ thuật | 1        |     |        |           |     |
| chức  | năng     |       |          |          |     | hình   | giao diện |     |
|       | X        |       |          |          |     | Nghiệp | vụ f      |     |
D1 D2
|     |      |     |     | Thể hiện | dạng | nhập | liệu của | D1   |
| --- | ---- | --- | --- | -------- | ---- | ---- | -------- | ---- |
| Xử  | lý f |     |     |          |      |      |          |      |
|     |      |     |     | Thể hiện | dạng | kết  | xuất của | D2   |
|     |      |     |     | Thực     | hiện |      | Kết      | thúc |
Software Engineering 57
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | thiết | kế       | chi tiết |     | màn    |      | hình |      |     |
| ----- | -------- | ----- | -------- | -------- | --- | ------ | ---- | ---- | ---- | --- |
| Mô tả | tổng thể |       |          |          |     | Mô     | tả   | tổng | thể  | màn |
|       |          |       | Kỹ thuật | 2        |     |        |      |      |      |     |
| chức  | năng     |       |          |          |     |        | hình | giao | diện |     |
|       | X        |       |          |          |     | Nghiệp |      | vụ   | f    |     |
D1 D2
|     |      |     |     | Thể hiện | dạng |      | nhập | liệu | của | D1 với |
| --- | ---- | --- | --- | -------- | ---- | ---- | ---- | ---- | --- | ------ |
|     |      |     |     | các giá  | trị  | định | sẵn  |      |     |        |
| Xử  | lý f |     |     |          |      |      |      |      |     |        |
|     |      |     |     | Thể hiện | dạng |      | kết  | xuất | của | D2     |
|     |      |     |     | Thực     | hiện |      |      |      | Kết | thúc   |
Software Engineering 58
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | thiết | kế       | chi tiết |     | màn    | hình |         |
| ----- | -------- | ----- | -------- | -------- | --- | ------ | ---- | ------- |
| Mô tả | tổng thể |       |          |          |     | Mô tả  | tổng | thể màn |
|       |          |       | Kỹ thuật | 3        |     |        |      |         |
| chức  | năng     |       |          |          |     | hình   | giao | diện    |
|       | X        |       |          |          |     | Nghiệp | vụ   | f       |
D1 D2
|     |      |     |     | Thể hiện | dạng  | nhập     | liệu | của D1 với |
| --- | ---- | --- | --- | -------- | ----- | -------- | ---- | ---------- |
|     |      |     |     | các giá  | trị   | định sẵn |      |            |
| Xử  | lý f |     |     |          |       |          |      |            |
|     |      |     |     | Thể hiện | dạng  | kết      | xuất | của D2 với |
|     |      |     |     | dạng     | chuỗi |          |      |            |
|     |      |     |     | Thực     | hiện  |          |      | Kết thúc   |
Software Engineering 59
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | thiết | kế       | chi tiết |     | màn    | hình |         |
| ----- | -------- | ----- | -------- | -------- | --- | ------ | ---- | ------- |
| Mô tả | tổng thể |       |          |          | Mô  | tả     | tổng | thể màn |
|       |          |       | Kỹ thuật | 4        |     |        |      |         |
| chức  | năng     |       |          |          |     | hình   | giao | diện    |
|       | X        |       |          |          |     | Nghiệp | vụ   | f       |
D1 D2
|     |      |     |     | Thể hiện   | dạng | nhập | liệu | của D1 với |
| --- | ---- | --- | --- | ---------- | ---- | ---- | ---- | ---------- |
|     |      |     |     | dạng chuỗi |      |      |      |            |
| Xử  | lý f |     |     |            |      |      |      |            |
|     |      |     |     | Thể hiện   | dạng | kết  | xuất | của D2 với |
|     |      |     |     | biểu tượng |      |      |      |            |
|     |      |     |     | Thực       | hiện |      |      | Kết thúc   |
Software Engineering 60
tkhuong@dthu.edu.vn

| Kỹ    | thuật    | thiết | kế       | chi tiết |     | màn    | hình |         |
| ----- | -------- | ----- | -------- | -------- | --- | ------ | ---- | ------- |
| Mô tả | tổng thể |       |          |          | Mô  | tả     | tổng | thể màn |
|       |          |       | Kỹ thuật | 5        |     |        |      |         |
| chức  | năng     |       |          |          |     | hình   | giao | diện    |
|       | X        |       |          |          |     | Nghiệp | vụ   | f       |
D1 D2
|     |      |     |     | Thể hiện  | dạng  | nhập | liệu | của D1 với |
| --- | ---- | --- | --- | --------- | ----- | ---- | ---- | ---------- |
|     |      |     |     | dạng biểu | tượng |      |      |            |
| Xử  | lý f |     |     |           |       |      |      |            |
|     |      |     |     | Thể hiện  | dạng  | kết  | xuất | của D2 với |
biểu tượng
|     |     |     |     | Thực | hiện |     |     | Kết thúc |
| --- | --- | --- | --- | ---- | ---- | --- | --- | -------- |
Software Engineering 61
tkhuong@dthu.edu.vn

| Kỹ  | thuật       | thiết | kế chi tiết |     |     | màn | hình |         |     |
| --- | ----------- | ----- | ----------- | --- | --- | --- | ---- | ------- | --- |
| Mô  | tả tổng thể |       |             |     | Mô  | tả  | tổng | thể màn |     |
|     |             |       | Kỹ thuật    | 6   |     |     |      |         |     |
(TAB)
|     | chức năng |     |     |     |        | hình | giao      | diện |     |
| --- | --------- | --- | --- | --- | ------ | ---- | --------- | ---- | --- |
|     | X         |     |     |     | Nghiệp |      | vụ f1, f2 |      |     |
D11 D12
| Xử  | lý f1 |     |     | Nghiệp | vụ  | f1  | Nghiệp |     | vụ f2 |
| --- | ----- | --- | --- | ------ | --- | --- | ------ | --- | ----- |
X
D21 D22
|     |       |     |     | Thực | hiện |     |     | Kết thúc |     |
| --- | ----- | --- | --- | ---- | ---- | --- | --- | -------- | --- |
| Xử  | lý f2 |     |     |      |      |     |     |          |     |
Software Engineering 62
tkhuong@dthu.edu.vn

| Kỹ  | thuật       | thiết | kế chi tiết |     |     | màn |         | hình |         |     |
| --- | ----------- | ----- | ----------- | --- | --- | --- | ------- | ---- | ------- | --- |
| Mô  | tả tổng thể |       |             |     | Mô  |     | tả tổng |      | thể màn |     |
|     |             |       | Kỹ thuật    | 6   |     |     |         |      |         |     |
(tab1)
|     | chức năng |     |     |     |        | hình |     | giao   | diện |     |
| --- | --------- | --- | --- | --- | ------ | ---- | --- | ------ | ---- | --- |
|     | X         |     |     |     | Nghiệp |      | vụ  | f1, f2 |      |     |
D11 D12
|     |       |     |     | Nghiệp   | vụ   | f1   |      | Nghiệp |      | vụ f2 |
| --- | ----- | --- | --- | -------- | ---- | ---- | ---- | ------ | ---- | ----- |
| Xử  | lý f1 |     |     |          |      |      |      |        |      |       |
|     |       |     |     | Thể hiện | dạng | nhập |      | của    | D11  |       |
|     | X     |     |     | Thể hiện | dạng | kết  | xuất | của    | D12  |       |
D21 D22
|     |       |     |     | Thực | hiện |     |     |     | Kết thúc |     |
| --- | ----- | --- | --- | ---- | ---- | --- | --- | --- | -------- | --- |
| Xử  | lý f2 |     |     |      |      |     |     |     |          |     |
Software Engineering 63
tkhuong@dthu.edu.vn

| Kỹ  | thuật       | thiết | kế chi tiết |     |     |     | màn |      | hình |         |     |
| --- | ----------- | ----- | ----------- | --- | --- | --- | --- | ---- | ---- | ------- | --- |
| Mô  | tả tổng thể |       |             |     |     | Mô  | tả  | tổng |      | thể màn |     |
|     |             |       | Kỹ thuật    | 6   |     |     |     |      |      |         |     |
(tab2)
|     | chức năng |     |     |     |     |        | hình |     | giao   | diện |     |
| --- | --------- | --- | --- | --- | --- | ------ | ---- | --- | ------ | ---- | --- |
|     | X         |     |     |     |     | Nghiệp |      | vụ  | f1, f2 |      |     |
D11 D12
|     |       |     |     | Nghiệp |     | vụ   | f1   |     | Nghiệp |      | vụ f2    |
| --- | ----- | --- | --- | ------ | --- | ---- | ---- | --- | ------ | ---- | -------- |
| Xử  | lý f1 |     |     |        |     |      |      |     |        |      |          |
|     |       |     |     |        | Thể | hiện | dạng |     | nhập   | của  | D21      |
|     | X     |     |     |        | Thể | hiện | dạng |     | kết    | xuất | của D22  |
D21 D22
|     |       |     |     | Thực |     | hiện |     |     |     | Kết thúc |     |
| --- | ----- | --- | --- | ---- | --- | ---- | --- | --- | --- | -------- | --- |
| Xử  | lý f2 |     |     |      |     |      |     |     |     |          |     |
Software Engineering 64
tkhuong@dthu.edu.vn

| VD. Thiết | kế  | GD Giải | PT bậc | 2   |
| --------- | --- | ------- | ------ | --- |
❖ Cách 1
❖ SƠ ĐỒ MÀN HÌNH
MH_CHINH
| MH_GIAI_PT |     | MH_TU_REN_LUYEN |     |     |
| ---------- | --- | --------------- | --- | --- |
Software Engineering 65
tkhuong@dthu.edu.vn

❖ Cách 1:
❖ MH_CHINH
| Phần mềm    | tự rèn | luyện | bài |
| ----------- | ------ | ----- | --- |
| tập phương  | trình  | bậc   | 2   |
| Giải phương |        | trình |     |
Tự rèn luyện
Software Engineering 66
tkhuong@dthu.edu.vn

❖ Cách 1:
❖ MH_GIAI_PT
|     | Giải phương | trình bậc | 2   |
| --- | ----------- | --------- | --- |
Phương trình:
…..X2
|     | – ….X + …. | = 0 |     |
| --- | ---------- | --- | --- |
Nghiệm:
| Phương | trình ***x2 | – ***x + *** = 0 có | *** |
| ------ | ----------- | ------------------- | --- |
nghiệm
| phân | biệt x1=*** và | x2=*** |     |
| ---- | -------------- | ------ | --- |
Đồng ý
Software Engineering 67
tkhuong@dthu.edu.vn

❖ Cách 1:
❖ MH_TU_REN_LUYEN
|             | Tự rèn | luyện | giải  |
| ----------- | ------ | ----- | ----- |
|             | phương | trình | bậc 2 |
| Giải phương | trình: |       |       |
***X2
|     | + ***X - | *** = 0 |     |
| --- | -------- | ------- | --- |
Nghiệm: …….
Kết quả:
| Sai rồi | !!! Phương       | trình | có 2 nghiệm |
| ------- | ---------------- | ----- | ----------- |
|         | x1=*** và x2=*** |       |             |
Đồng ý
Software Engineering 68
tkhuong@dthu.edu.vn

| VD. Thiết |     | kế  | GD Giải |     | PT bậc |     | 2   |
| --------- | --- | --- | ------- | --- | ------ | --- | --- |
❖ Cách 2
❖ SƠ ĐỒ MÀN HÌNH
|     | Phần mềm    | bài | tập phương |        | trình bậc | 2   |     |
| --- | ----------- | --- | ---------- | ------ | --------- | --- | --- |
|     | Giải phương |     | trình      | Tự rèn | luyện     |     |     |
Kết thúc
Software Engineering 69
tkhuong@dthu.edu.vn

|        | VD. Thiết |        |        |        | kế   | GD Giải    |        |      |       | PT bậc |     |       | 2   |
| ------ | --------- | ------ | ------ | ------ | ---- | ---------- | ------ | ---- | ----- | ------ | --- | ----- | --- |
| ❖ Cách | 2         |        |        |        |      |            |        |      |       |        |     |       |     |
| ❖ Giao | diện      | khi    | chọn   |        | chức |            | năng   | Giải |       | phương |     | trình |     |
|        |           | Phần   |        | mềm    | bài  | tập        | phương |      | trình | bậc    | 2   |       |     |
|        |           | Giải   | phương |        |      | trình      |        | Tự   | rèn   | luyện  |     |       |     |
|        |           | Phương |        | trình: |      |            |        |      |       |        |     |       |     |
|        |           |        |        | …..X2  |      | – ….X + …. |        | = 0  |       |        |     |       |     |
Nghiệm:
|     |     |     | Phương |     | trình | 2x2 | –   | 5x + 7 = 0 có |     | 2   |     |     |     |
| --- | --- | --- | ------ | --- | ----- | --- | --- | ------------- | --- | --- | --- | --- | --- |
nghiệm
|     |     |     | phân | biệt |     | x1=-1 và |      | x2=-3.5 |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --- | -------- | ---- | ------- | --- | --- | --- | --- | --- |
|     |     |     |      |      |     | Kết      | thúc |         |     |     |     |     |     |
Software Engineering 70
tkhuong@dthu.edu.vn

|        | VD. Thiết |      |        | kế   |        | GD Giải |        |       | PT bậc |       | 2   |
| ------ | --------- | ---- | ------ | ---- | ------ | ------- | ------ | ----- | ------ | ----- | --- |
| ❖ Cách | 2         |      |        |      |        |         |        |       |        |       |     |
| ❖ Giao | diện      | khi  | chọn   | chức |        | năng    | Giải   |       | phương | trình |     |
|        |           | Phần | mềm    |      | bài    | tập     | phương | trình | bậc    | 2     |     |
|        |           | Giải | phương |      | trình  |         | Tự     | rèn   | luyện  |       |     |
|        |           | Giải | phương |      | trình: |         |        |       |        |       |     |
|        |           |      |        | 3X2  | + 7X - | 10 = 0  |        |       |        |       |     |
Nghiệm: …….
|     |     | Kết | quả:  |                |     |          |       |             |     |     |     |
| --- | --- | --- | ----- | -------------- | --- | -------- | ----- | ----------- | --- | --- | --- |
|     |     |     | Sai   | rồi !!! Phương |     |          | trình | có 2 nghiệm |     |     |     |
|     |     |     |       | x1=1 và        |     | x2=-3.33 |       |             |     |     |     |
|     |     |     |       |                |     | Kết      | thúc  |             |     |     |     |
Software Engineering 71
tkhuong@dthu.edu.vn

Bài tập
| BT1. Thiết | kế giao | diện    | cho pm Quản | lý nhân  | sự      |     |
| ---------- | ------- | ------- | ----------- | -------- | ------- | --- |
| ▪ Sơ       | đồ tổng | thể màn | hình        |          |         |     |
| ▪ Chi tiết | từng    | màn     | hình        |          |         |     |
| BT2. Thiết | kế giao | diện    | cho pm xếp  | loại học | lực của | học |
sinh
| BT3. Thiết | kế giao | diện | cho pm Quản | lý thu | chi |     |
| ---------- | ------- | ---- | ----------- | ------ | --- | --- |
Software Engineering 72
tkhuong@dthu.edu.vn

| Đề  | bài | BT1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
❖ Xét phần mềm Quản lý nhân sự với yêu cầu chính là tra cứu hồ sơ
nhân viên dựa trên họ tên. Hãy phân tích thiết kế với công nghệ
Windows, xử lý dùng đơn thể và lưu trữ dùng CSDL quan hệ (chỉ xét
| các thuộc | tính Họ | tên, giới | tính, ngày | sinh, địa | chỉ) |       |     |
| --------- | ------- | --------- | ---------- | --------- | ---- | ----- | --- |
| PHÂN      | TÍCH    |           |            |           |      | THIẾT | KẾ  |
Software Engineering 73
tkhuong@dthu.edu.vn

|      | BT1. Quản |     |     |       |     | lý nhân |        | viên |     |     |
| ---- | --------- | --- | --- | ----- | --- | ------- | ------ | ---- | --- | --- |
| Phân | tích      | yêu | cầu | (Ngôn |     | ngữ tự  | nhiên) |      |     |     |
❖ Người dùng muốn phần mềm quản lý nhân viên cho phép thực hiện
| các    |     | chức | năng | như |     | sau: |     |     |     |     |
| ------ | --- | ---- | ---- | --- | --- | ---- | --- | --- | --- | --- |
| ❖ Nhân |     | viên |      |     |     |      |     |     |     |     |
▪
Quản lý hồ sơ nhân viên (Thêm mới, cập nhật, xóa) dựa theo BM1
▪ Tra cứu hồ sơ nhân viên: cho phép nhập vào tên hoặc địa chỉ, hoặc trình
độ của nhân viên và sau đó phần mềm sẽ xuất ra danh sách các nhân
|     |     | viên | (thông | tin hồ |     | sơ nhân | viên khi | tra | cứu theo | BM1) |
| --- | --- | ---- | ------ | ------ | --- | ------- | -------- | --- | -------- | ---- |
▪ Lập báo cáo thống kê: yêu cầu lập báo cáo thông kê theo BM2
❖ Ban giám đốc: chỉ sử dụng 1 chức năng là cập nhật quy định tiếp
| nhận |           | nhận | nhân |     | viên | mới        |      |      |     |     |
| ---- | --------- | ---- | ---- | --- | ---- | ---------- | ---- | ---- | --- | --- |
| Ghi  | chú: chưa |      | xem  | xét | hết  | tất cả các | chức | năng |     |     |
Software Engineering 74
tkhuong@dthu.edu.vn

|                     | BT1. Quản        |     |      |      |            | lý   | nhân |                                       | viên  |     |     |       |       |     |       |
| ------------------- | ---------------- | --- | ---- | ---- | ---------- | ---- | ---- | ------------------------------------- | ----- | --- | --- | ----- | ----- | --- | ----- |
| BM1      Hồ         |                  | sơ  | nhân | viên |            |      |      |                                       |       |     |     |       |       |     |       |
|                     |                  |     |      |      |            |      |      | BM2                             Thống |       |     |     | kê    | trình | độ  |       |
| Họ và               | tên: ………… Giới   |     |      |      | tính: ………  |      |      |                                       |       |     |     |       |       |     |       |
|                     |                  |     |      |      |            |      |      |                                       | Trình | độ  | Số  | lượng |       |     | Tỷ lệ |
| Ngày                | sinh: ………... Địa |     |      |      | chỉ: ……….. |      |      |                                       |       |     |     |       |       |     |       |
|                     |                  |     |      |      |            |      |      | Trung                                 | cấp   |     |     |       |       |     |       |
| Đơn vị: …………… Trình |                  |     |      |      | độ: ……….   |      |      |                                       |       |     |     |       |       |     |       |
| Ghi chú:            |                  |     |      |      |            |      |      | Cao đẳng                              |       |     |     |       |       |     |       |
| - Tuổi              | nhân             |     | viên | theo | quy        | định |      |                                       |       |     |     |       |       |     |       |
Đại học
| Nam từ |     | 18 đến |       | 60, Nữ | từ     | 18 đến | 55  |     |     |     |     |     |     |     |     |
| ------ | --- | ------ | ----- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |     |        |       |        |        |        |     | Sau | đại | học |     |     |     |     |     |
| - Công | ty  | có     | 5 đơn | vị     | và chỉ | chấp   |     |     |     |     |     |     |     |     |     |
Ghi chú:
| nhận      | 4 trình          |     | độ: Trung |       | cấp, Cao             |           |                      |     |           |             |      |         |      |     |     |
| --------- | ---------------- | --- | --------- | ----- | -------------------- | --------- | -------------------- | --- | --------- | ----------- | ---- | ------- | ---- | --- | --- |
|           |                  |     |           |       |                      |           |                      | Số  | lượng: Số | lượng       | nhân | viên    |      |     |     |
| đẳng, Đại |                  |     | học, Sau  | đại   | học                  |           |                      |     |           |             |      |         |      |     |     |
|           |                  |     |           |       |                      |           |                      | Tỷ  | lệ = Số   | lượng/ Tổng |      | số nhân | viên |     |     |
|           |                  |     | QUY TẮC   |       | KIỂM TRA TÍNH HỢP LỆ |           |                      |     |           |             |      |         |      |     |     |
| Họ và     | tên: không       |     |           | được  | rỗng                 |           |                      |     |           |             |      |         |      |     |     |
| Giới      | tính: Nam hay Nữ |     |           |       |                      |           |                      |     |           |             |      |         |      |     |     |
| Ngày      | sinh: tương      |     |           | ứng   | tuổi                 | từ 20 đến | 40                   |     |           |             |      |         |      |     |     |
| Địa       | chỉ: không       |     | được      | trống |                      |           |                      |     |           |             |      |         |      |     |     |
|           |                  |     |           |       |                      |           | Software Engineering |     |           |             |      |         |      |     | 75  |
tkhuong@dthu.edu.vn

TRA CỨU HỒ SƠ NHÂN VIÊN
| Tên | nhân viên | :…………....… |     |     |
| --- | --------- | ---------- | --- | --- |
(2)
(1)
DANH SÁCH NHÂN VIÊN
| STT            | Họ tên | Giới tính | Địa chỉ | Tuổi   |
| -------------- | ------ | --------- | ------- | ------ |
| 1              | ****** | ******    | ******  | ****** |
| 2              | ****** | ******    | ******  | ****** |
| Mô tả sự kiện: |        |           |         |        |
(1) Load form: phần mềm hiển thị textbox cho phép người dùng nhập
| chuỗi và | danh sách | nhân viên | rỗng |     |
| -------- | --------- | --------- | ---- | --- |
(2) Textbox: Người dùng nhập chuỗi tên cần tìm và phần mềm tìm gần
đúng theo chuỗi nhập, hiển thị thông tin nhân viên vào danh sách
| nhân viên |     |     |     |     |
| --------- | --- | --- | --- | --- |
Software Engineering 76
tkhuong@dthu.edu.vn

|      | Đề   |     | BT2. Xếp |       |     | loại   |        | học | lực | của | học | sinh |
| ---- | ---- | --- | -------- | ----- | --- | ------ | ------ | --- | --- | --- | --- | ---- |
| Phân | tích | yêu | cầu      | (Ngôn |     | ngữ tự | nhiên) |     |     |     |     |      |
❖ Với yêu cầu lập bảng xếp loại học lực, phần mềm bao gồm các
|     | người | sử   | dụng | và    | chức | năng        | như | sau: |        |      |     |     |
| --- | ----- | ---- | ---- | ----- | ---- | ----------- | --- | ---- | ------ | ---- | --- | --- |
| ❖   | Nhân  | viên | văn  | phòng |      | giáo vụ: sử |     | dụng | 2 chức | năng |     |     |
|     | ▪ Ghi | nhận |      | bảng  | điểm |             |     |      |        |      |     |     |
|     | ▪ Lập | bảng |      | xếp   | loại | học lực     |     |      |        |      |     |     |
❖ Ban giám hiệu: chỉ sử dụng 1 chức năng là cập nhật quy tắc xếp loại
|     | học | lực |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ghi chú: Chi tiết các chức năng sẽ mô tả sau, chưa xem xét hết tất cả các chức
năng
Software Engineering 77
tkhuong@dthu.edu.vn

|     | Đề       | BT2. Xếp |          |        |         |      | loại     |       | học      | lực |      | của | học | sinh |
| --- | -------- | -------- | -------- | ------ | ------- | ---- | -------- | ----- | -------- | --- | ---- | --- | --- | ---- |
|     |          |          |          | Bảng   | điểm    | môn  | ….       |       |          |     |      |     |     |      |
|     |          |          | Lớp      | … Niên |         | khóa | …        |       |          |     |      |     |     |      |
|     | Học sinh |          | Điểm     |        | 15 Điểm |      | 1 tiết   |       | Điểm     | HK  |      |     |     |      |
|     | Ghí chú: |          |          |        |         |      |          |       |          |     |      |     |     |      |
|     | - Trường |          | có 9 môn |        | học …   |      |          |       |          |     |      |     |     |      |
|     | Điểm     | 15, điểm |          | 1 tiết | có thể  | có   | nhiều    | cột   |          |     |      |     |     |      |
|     | - Điểm   | số       | là số    | thực   | có giá  | trị  | từ 0 đến |       | 10       |     |      |     |     |      |
|     |          |          |          |        |         | Bảng |          | xếp   | loại học | lực |      |     |     |      |
|     |          |          |          |        |         | Lớp  | … Niên   |       | khóa     | …   |      |     |     |      |
|     | Học sinh |          |          | TBHK1  |         |      |          | TBHK2 |          |     | TBCN |     | Học | lực  |
TBHK1, TBHK2: trung bình cuối học kỳ được tính dựa trên quy tắc tính điểm trung
| bình | học kỳ |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TBCN: trung bình cuối năm được tính dựa trên quy tắc tính điểm trung bình cuối
năm
| Học | lực: được |     | tính | điểm | dựa | trên | quy | tắc | xếp loại | học | lực |     |     |     |
| --- | --------- | --- | ---- | ---- | --- | ---- | --- | --- | -------- | --- | --- | --- | --- | --- |
Software Engineering 78
tkhuong@dthu.edu.vn

|        | Đề        | BT2. Xếp   |        |        | loại | học | lực          | của         |                  | học     | sinh  |
| ------ | --------- | ---------- | ------ | ------ | ---- | --- | ------------ | ----------- | ---------------- | ------- | ----- |
| Quy    | tắc tính  | điểm trung | bình   | học    | kỳ   |     |              |             |                  |         |       |
|        |           |            |        |        |      |     | Quy tắc      | xếp         | loại             | học lực |       |
| TBHK   | = TTB/SMH |            |        |        |      |     |              |             |                  |         |       |
|        |           |            |        |        |      |     | TBCN         | < 5.0: Loại |                  | Yếu     |       |
|        |           |            |        |        |      |     | TBCN >= 5 và |             | TBCN < 6.5: Loại |         | Trung |
| SMH là | số môn    | học (hiện  | nay là | 9 môn) |      |     |              |             |                  |         |       |
bình
| TTB | là tổng trung | bình | các môn | (TBMH) |     |     |                 |     |                |      |     |
| --- | ------------- | ---- | ------- | ------ | --- | --- | --------------- | --- | -------------- | ---- | --- |
|     |               |      |         |        |     |     | TBCN >= 6.5 và  |     | TBCN < 8: Loại |      | Khá |
|     |               |      |         |        |     |     | TBCN >= 8: Loại |     |                | Giỏi |     |
TBMH = (TB15 + 2*TB1T + 3*DHK)/6
| TB15 là | trung | bình của             | các bài | kiểm  | tra        |     |     |     |     |     |     |
| ------- | ----- | -------------------- | ------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
| thường  | xuyên |                      |         |       |            |     |     |     |     |     |     |
| TB1T là | trung | bình của             | các bài | kiểm  | tra 1 tiết |     |     |     |     |     |     |
| DHK là  | điểm  | thi cuối học         | kỳ      |       |            |     |     |     |     |     |     |
|         | Quy   | tắc tính             | điểm    | trung | bình cuối  | năm |     |     |     |     |     |
|         | TBCN  | = TBHK1 + 2*TBHK2)/3 |         |       |            |     |     |     |     |     |     |
Software Engineering 79
tkhuong@dthu.edu.vn

| Đề  | bài | BT3 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
❖ Xét phần mềm Quản lý thu chi với yêu cầu chính là Thống kê doanh
thu tháng. Hãy phân tích thiết kế với công nghệ Windows, xử lý dùng
| đơn thể | và lưu | trữ dùng | CSDL quan | hệ  |       |     |
| ------- | ------ | -------- | --------- | --- | ----- | --- |
| PHÂN    | TÍCH   |          |           |     | THIẾT | KẾ  |
Software Engineering 80
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 90
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C5_4ThietKePM_TKGiaoDien.md -->

---


<!-- BẮT ĐẦU FILE: C5_5ThietKePM_Gioithieu_tpXuLy.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 5
GIỚI THIỆU THÀNH
PHẦN XỬ LÝ
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

THÀNH PHẦN XỬ LÝ
❖
| Thành | phần      | phần | xử lý | là hệ | thống | các xử | lý  |
| ----- | --------- | ---- | ----- | ----- | ----- | ------ | --- |
| ▪ Xử  | lý giao   | diện |       |       |       |        |     |
| ▪ Xử  | lý nghiệp | vụ   |       |       |       |        |     |
| ▪ Xử  | lý lưu    | trữ  |       |       |       |        |     |
Software Engineering 2
tkhuong@dthu.edu.vn

THÀNH PHẦN XỬ LÝ
|       | Người dùng |      |
| ----- | ---------- | ---- |
| Thành | phần Giao  | diện |
Xử lý
|     | Biến cố |     |
| --- | ------- | --- |
Xử lý
Xử lý
Nhập liệu Kết xuất
Xử lý
Nghiệp vụ
Xử lý
Xử lý
Đọc
Ghi
| Thành | phần Lưu | trữ |
| ----- | -------- | --- |
Software Engineering 3
tkhuong@dthu.edu.vn

THÀNH PHẦN XỬ LÝ
| ❖   | Xử  | lý biến | cố  |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
▪ Xử lý thực hiện theo các biến cố phát sinh từ người sử dụng
| ❖   | Xử  | lý nhập, xuất |      |       |           |      |        |      |      |            |
| --- | --- | ------------- | ---- | ----- | --------- | ---- | ------ | ---- | ---- | ---------- |
|     | ▪   | Xử lý         | thực | hiện: |           |      |        |      |      |            |
|     |     | • Tiếp        | nhận | dữ    | liệu      | nhập | → biến | bộ   | nhớ  |            |
|     |     | • Kết         | xuất | nội   | dung biến |      | bộ nhớ | → dữ | liệu | “xem được” |
| ❖   | Xử  | lý nghiệp     |      | vụ    |           |      |        |      |      |            |
▪ Xử lý thực hiện tính toán/ kiểm tra/ … theo quy tắc xử lý nghiệp vụ trong
|     |     | thực tế     |      |           |       |     |       |        |        |     |
| --- | --- | ----------- | ---- | --------- | ----- | --- | ----- | ------ | ------ | --- |
| ❖   | Xử  | lý đọc, ghi |      |           |       |     |       |        |        |     |
|     | ▪   | Xử lý       | thực | hiện:     |       |     |       |        |        |     |
|     |     | • Đọc       | dữ   | liệu      | từ bộ | nhớ | phụ → | biến   | bộ nhớ |     |
|     |     | • Ghi       | nội  | dung biến |       | bộ  | nhớ → | bộ nhớ | phụ    |     |
Software Engineering 4
tkhuong@dthu.edu.vn

THÀNH PHẦN XỬ LÝ
| ❖ Thiết | kế    | xử lý    |     |           |     |
| ------- | ----- | -------- | --- | --------- | --- |
| ▪       | Mô tả | hệ thống | các | hàm xử lý | gồm |
• Tên
|     | • Tham       | số       |      |         |     |
| --- | ------------ | -------- | ---- | ------- | --- |
|     | • Kết        | quả trả  | về   |         |     |
|     | • Thuật      | giải     |      |         |     |
| ▪   | Cùng         | với cách | thức | tổ chức |     |
|     | • Theo đơn   |          | thể  |         |     |
|     | • Theo hướng |          | đối  | tượng   |     |
Software Engineering 5
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 6
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C5_5ThietKePM_Gioithieu_tpXuLy.md -->

---


<!-- BẮT ĐẦU FILE: C6_LapTrinh.md -->
LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 6
KỸ THUẬT
LẬP TRÌNH
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM KỸ THUẬT LẬP TRÌNH
PHƯƠNG PHÁP LẬP TRÌNH
KỸ THUẬT
LẬP NGÔN NGỮ LẬP TRÌNH
TRÌNH
PHONG CÁCH LẬP TRÌNH
KỸ THUẬT LẬP TRÌNH
Software Engineering 2
tkhuong@dthu.edu.vn

1. KHÁI NIỆM LẬP TRÌNH HIỆU QUẢ
| ❖ Sản | phẩm   | phần      | mềm   | tốt khi? |        |
| ----- | ------ | --------- | ----- | -------- | ------ |
| ▪     | Phân   | tích tốt  |       |          |        |
| ▪     | Thiết  | kế tốt    |       |          |        |
| ▪     | Lập    | trình tốt |       |          |        |
| ▪     | Kiểm   | thử chặt  | chẽ   |          |        |
| ❖ Kỹ  | thuật  | lập trình | tốt?  |          |        |
| ▪     | Chuyên | nghiệp    | (tuân | theo các | chuẩn) |
| ▪     | Ổn     | định      |       |          |        |
| ▪     | Hiệu   | quả       |       |          |        |
Software Engineering 3
tkhuong@dthu.edu.vn

1. KHÁI NIỆM LẬP TRÌNH HIỆU QUẢ
| ❖   | Lập    | trình |       | hiệu     |       | quả: |            |         |      |     |
| --- | ------ | ----- | ----- | -------- | ----- | ---- | ---------- | ------- | ---- | --- |
|     | ▪      | Tốc   | độ    | phát     | triển |      | cao        | hơn     |      |     |
|     |        | •     | Năng  | lực      | biểu  | diễn | cao        |         | hơn  |     |
|     |        | •     | Khả   | năng     | sử    | dụng | lại        | cao     | hơn  |     |
|     | ▪      | Dễ    | bảo   | trì      | hơn   |      |            |         |      |     |
|     |        | •     | Dễ    | hiểu, dễ |       | sửa  | lỗi, thích |         | nghi |     |
|     | ▪      | Chất  | lượng |          | cao   | hơn  |            |         |      |     |
|     |        | •     | Sử    | dụng     | các   | cấu  | trúc       | an toàn |      | hơn |
| →   | Chương |       |       | trình    | cần   | dễ   | hiểu       |         |      |     |
Software Engineering 4
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM KỸ THUẬT LẬP TRÌNH
PHƯƠNG PHÁP LẬP TRÌNH
KỸ THUẬT
LẬP NGÔN NGỮ LẬP TRÌNH
TRÌNH
PHONG CÁCH LẬP TRÌNH
KỸ THUẬT LẬP TRÌNH
Software Engineering 5
tkhuong@dthu.edu.vn

2. PHƯƠNG PHÁP LẬP TRÌNH
| ❖ Lập | trình | tuần tự   | (tuyến | tính)     |        |
| ----- | ----- | --------- | ------ | --------- | ------ |
| ❖ Lập | trình | có cấu    | trúc   | (thủ tục) |        |
| ❖ Lập | trình | hướng     | chức   | năng      |        |
| ❖ Lập | trình | hướng     | đối    | tượng     |        |
| ❖ Lập | trình | logic (kỹ | thuật  | thế hệ    | thứ 4) |
Software Engineering 6
tkhuong@dthu.edu.vn

|     | 2.1 Lập |     |     | trình |     | tuần |     | tự  |     |
| --- | ------- | --- | --- | ----- | --- | ---- | --- | --- | --- |
❖ Không có/ thiếu các lệnh có cấu trúc (for, while, do while)
| ❖   | Lạm     | dụng | các   | lệnh | GOTO      |                           |         |     |          |
| --- | ------- | ---- | ----- | ---- | --------- | ------------------------- | ------- | --- | -------- |
| ❖   | Thiếu   | khả  | năng  | khai | báo       | biến                      | cục     |     | bộ       |
|     | →độ     | ghép | nối   | cao  |           |                           |         |     |          |
|     | →Chương |      | trình | khó  | hiểu, khó |                           | sửa, dễ |     | sinh lỗi |
|     | →Dùng   |      | ngôn  | ngữ  | thế hệ    | 1, 2 (assembly, bacsic,…) |         |     |          |
Software Engineering 7
tkhuong@dthu.edu.vn

| 2.2 Lập |          |              | trình |       |      | có                         | cấu                         |     | trúc |
| ------- | -------- | ------------ | ----- | ----- | ---- | -------------------------- | --------------------------- | --- | ---- |
| ❖ Sử    | dụng     | các          | lệnh  |       | có   | cấu                        | trúc (for, while, do while) |     |      |
| ❖ Hạn   | chế/ cấm |              |       | dùng  | GOTO |                            |                             |     |      |
| ❖ Sử    | dụng     | chương       |       | trình |      | con, biến                  |                             | cục | bộ   |
| → Dễ    | hiểu     | hơn, an toàn |       |       |      | hơn                        |                             |     |      |
| → Ngôn  | ngữ      | dùng         |       | thế   | hệ   | 2, 3: Fortran, pascal, C,… |                             |     |      |
Software Engineering 8
tkhuong@dthu.edu.vn

|     | 2.3 Lập      |      |     |        | trình |      | hướng   |      |       |       | chức    |               | năng |
| --- | ------------ | ---- | --- | ------ | ----- | ---- | ------- | ---- | ----- | ----- | ------- | ------------- | ---- |
| ❖   | Dựa          | trên |     | nguyên |       | tắc  | ghép    | nối  | dữ    | liệu  |         |               |      |
|     | ▪            | Trao | đổi | dữ     | liệu  | bằng | tham    |      | số và | giá   | trị trả | lại           |      |
|     | ▪            | Loại | bỏ  | hoàn   |       | toàn | dữ liệu | dùng |       | chung |         |               |      |
| ❖   | Loại         | bỏ   | các | hiệu   |       | ứng  | phụ     | khi  | sửa   | đổi   | các     | module chương |      |
|     | trình; nâng  |      |     | cao    |       | tính | tái sử  | dụng |       |       |         |               |      |
| ❖   | Ví dụ: LISP  |      |     |        |       |      |         |      |       |       |         |               |      |
Software Engineering 9
tkhuong@dthu.edu.vn

|     | 2.4 Lập |      |       | trình |      |         | hướng |           | đối | tượng |
| --- | ------- | ---- | ----- | ----- | ---- | ------- | ----- | --------- | --- | ----- |
| ❖   | Che     | giấu | thông |       | tin  |         |       |           |     |       |
| ❖   | Thao    | tác  | với   | dữ    | liệu | qua các |       | giao diện | xác | định  |
| ❖   | Kế      | thừa |       |       |      |         |       |           |     |       |
|     | →Cục    | bộ   | hơn   |       |      |         |       |           |     |       |
|     | →Dễ     | tái  | sử    | dụng  | hơn  |         |       |           |     |       |
→Thuận
|     |      |     | tiện | cho   | các | ứng   | dụng | lớn                    |     |     |
| --- | ---- | --- | ---- | ----- | --- | ----- | ---- | ---------------------- | --- | --- |
| →   | Ngôn | ngữ | lập  | trình |     | hướng | đối  | tượng: C++, Java, C#,… |     |     |
Software Engineering 10
tkhuong@dthu.edu.vn

| 2.5 Lập |            |          | trình  |      | logic |          |           |
| ------- | ---------- | -------- | ------ | ---- | ----- | -------- | --------- |
| ❖ Tách  |            | tri thức | về bài | toán | khỏi  | kỹ thuật | lập trình |
| ❖ Mô    | tả         | tri thức |        |      |       |          |           |
| ▪       | Các        | quy      | tắc    |      |       |          |           |
| ▪       | Các        | sự kiện  |        |      |       |          |           |
| ▪       | Mục        | tiêu     |        |      |       |          |           |
| ❖ Hệ    | thống      | tự       | chứng  | minh |       |          |           |
| ▪       | Tìm        | đường    | đi đến | mục  | tiêu  |          |           |
| ❖ Ví    | dụ: Prolog |          |        |      |       |          |           |
Software Engineering 11
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM KỸ THUẬT LẬP TRÌNH
KỸ PHƯƠNG PHÁP LẬP TRÌNH
THUẬT
NGÔN NGỮ LẬP TRÌNH
LẬP
TRÌNH
PHONG CÁCH LẬP TRÌNH
KỸ THUẬT LẬP TRÌNH
Software Engineering 12
tkhuong@dthu.edu.vn

3. NGÔN NGỮ LẬP TRÌNH
| ❖   | Lựa | chọn |        |           | ngôn      | ngữ    | dựa       |     | vào:      |            |
| --- | --- | ---- | ------ | --------- | --------- | ------ | --------- | --- | --------- | ---------- |
|     | ▪   | Đặc  | trưng  |           | của       | ngôn   | ngữ       |     |           |            |
|     |     | •    | Năng   |           | lực (kiểu |        | biến, các |     | cấu trúc) |            |
|     |     | •    | Tính   | khả       | chuyển    |        |           |     |           |            |
|     |     | •    | Mức    | độ        | hỗ        | trợ    | của các   |     | ngôn ngữ  |            |
|     | ▪   | Miền |        | ứng       | dụng      | của    | ngôn      |     | ngữ       |            |
|     |     | •    | Lập    | trình     | hệ        | thống  |           |     |           |            |
|     |     | •    | Nghiệp |           | vụ, kinh  |        | doanh     |     |           |            |
|     |     | •    | Khoa   |           | học kỹ    | thuật  |           |     |           |            |
|     |     | •    | Trí    | tuệ       | nhân      | tạo    |           |     |           |            |
|     | ▪   | Năng |        | lực, kinh |           | nghiệm |           | của | nhóm      | phát triển |
|     | ▪   | Yêu  | cầu    |           | của       | khách  | hàng      |     |           |            |
Software Engineering 13
tkhuong@dthu.edu.vn

|     | 3.1 Đặc |      |        | trưng       |      |           | của     | ngôn | ngữ |
| --- | ------- | ---- | ------ | ----------- | ---- | --------- | ------- | ---- | --- |
| ❖   | Năng    | lực  | của    | ngôn        |      | ngữ       |         |      |     |
|     | ▪       | Ngôn | ngữ    | bậc         | cao: |           |         |      |     |
|     |         | •    | Có cấu | trúc, câu   |      | lệnh      | phong   | phú  |     |
|     |         | •    | Hỗ trợ | nhiều       | kiểu | dữ        | liệu    |      |     |
|     |         | •    | Hỗ trợ | con trỏ, đệ |      | quy       |         |      |     |
|     |         | •    | Hỗ trợ | hướng       |      | đối tượng |         |      |     |
|     |         | •    | Thư    | viện phong  |      | phú       |         |      |     |
|     | →       | Nên  | dùng   | ngôn        |      | ngữ       | bậc cao |      |     |
Software Engineering 14
tkhuong@dthu.edu.vn

| 3.1 Đặc |      |      |        | trưng |        |      | của      |      | ngôn |        | ngữ |
| ------- | ---- | ---- | ------ | ----- | ------ | ---- | -------- | ---- | ---- | ------ | --- |
| ❖ Tính  | khả  |      | chuyển |       |        |      |          |      |      |        |     |
| ▪       | Là   | yếu  | tố     | quan  | trọng  | của  | ngôn     | ngữ, | cần  | khi    |     |
|         | •    | Thay | đổi    | phần  | cứng   |      |          |      |      |        |     |
|         | •    | Thay | đổi    | OS    |        |      |          |      |      |        |     |
| ▪       | Java | khả  | chuyển |       |        |      |          |      |      |        |     |
| ▪       | Các  | ngôn |        | ngữ   | thông  | dịch | (script) |      | khả  | chuyển |     |
| →sử     |      | dụng | các    | tính  | năng   |      | chuẩn    | của  | ngôn | ngữ    |     |
| →Sử     |      | dụng | script |       | khi có | thể  |          |      |      |        |     |
Software Engineering 15
tkhuong@dthu.edu.vn

|     | 3.1 Đặc |       |                                      |           |     | trưng       |            | của   | ngôn |      | ngữ |
| --- | ------- | ----- | ------------------------------------ | --------- | --- | ----------- | ---------- | ----- | ---- | ---- | --- |
| ❖   | Công    |       | cụ                                   | hỗ trợ    | của | ngôn        |            | ngữ   |      |      |     |
|     | ▪       | Trình |                                      | biên dịch |     | hiệu        | quả        |       |      |      |     |
|     |         | •     | Biên                                 | dịch      | tốc | độ cao      |            |       |      |      |     |
|     |         | •     | Khả                                  | năng      | tối | ưu cao      |            |       |      |      |     |
|     |         | •     | Khai                                 | thác      | các | tập         | lệnh, kiến | trúc  | phần | cứng | mới |
|     | ▪       | Các   | công                                 | cụ        | trợ | giúp        | hiệu       | quả   |      |      |     |
|     |         | •     | Editor, debugger,…                   |           |     |             |            |       |      |      |     |
|     |         | •     | IDE (Integrated Develop Environment) |           |     |             |            |       |      |      |     |
|     |         | •     | Môi                                  | trường    |     | UNIX thường |            | không | dùng | IDE  |     |
Software Engineering 16
tkhuong@dthu.edu.vn

|     | 3.2 Miền |         |     | ứng     | dụng | và  | ngôn | ngữ |     |
| --- | -------- | ------- | --- | ------- | ---- | --- | ---- | --- | --- |
| ❖   | Phần     | mềm     | hệ  | thống   |      |     |      |     |     |
|     | ▪ Hiệu   | quả, dễ |     | mở rộng |      |     |      |     |     |
▪
C, C++
| ❖   | Hệ thời | gian | thực: C, C++, Ada, Assembly |     |     |     |     |     |     |
| --- | ------- | ---- | --------------------------- | --- | --- | --- | --- | --- | --- |
❖
|     | Phần          | mềm  | nhúng: C++, Java |          |           |     |          |      |       |
| --- | ------------- | ---- | ---------------- | -------- | --------- | --- | -------- | ---- | ----- |
| ❖   | Phần          | mềm  | khoa             | học kỹ   | thuật:    |     |          |      |       |
|     | ▪ Tính        | toán | chính            | xác, thư | viện toán | học | mạnh, dễ | dàng | song  |
|     | song          | hóa  |                  |          |           |     |          |      |       |
|     | ▪ FORTRAN vẫn |      |                  | phổ biến |           |     |          |      |       |
Software Engineering 17
tkhuong@dthu.edu.vn

|        | 3.2 Miền                               |                                     | ứng | dụng | và  | ngôn | ngữ |
| ------ | -------------------------------------- | ----------------------------------- | --- | ---- | --- | ---- | --- |
| ❖ Phần | mềm                                    | nghiệp                              | vụ: |      |     |      |     |
| ▪      | CSDL: Oracle, DB2, SQL Server, MySQL,… |                                     |     |      |     |      |     |
| ▪      | Ngôn                                   | ngữ: Foxpro, COBOL, VB.NET, VC++, … |     |      |     |      |     |
| ❖ Trí  | tuệ nhân                               | tạo                                 |     |      |     |      |     |
| ▪      | Lisp, Prolog, OPS5,…                   |                                     |     |      |     |      |     |
| ❖ Lập  | trình                                  | Web/ CGI:                           |     |      |     |      |     |
| ▪      | Perl, ASP, PHP, Java, JavaScript, …    |                                     |     |      |     |      |     |
Software Engineering 18
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM KỸ THUẬT LẬP TRÌNH
KỸ PHƯƠNG PHÁP LẬP TRÌNH
THUẬT
NGÔN NGỮ LẬP TRÌNH
LẬP
TRÌNH
PHONG CÁCH LẬP TRÌNH
KỸ THUẬT LẬP TRÌNH
Software Engineering 19
tkhuong@dthu.edu.vn

4. PHONG CÁCH LẬP TRÌNH
| ❖   | Gồm    | các | yếu | tố:     |     |      |     |     |     |
| --- | ------ | --- | --- | ------- | --- | ---- | --- | --- | --- |
|     | ▪ Cách |     | đặt | tên hàm | và  | biến |     |     |     |
▪
|     | Cách     |     | xây      | dựng  | câu    | lệnh, cấu | trúc      | chương   | trình       |
| --- | -------- | --- | -------- | ----- | ------ | --------- | --------- | -------- | ----------- |
|     | ▪ Cách   |     | viết     | chú   | thích  |           |           |          |             |
| →   | Hướng    |     | đến      | phong | cách   | làm       | cho       | mã nguồn |             |
|     | →Dễ      |     | hiểu, dễ | sửa   | đổi    |           |           |          |             |
|     | →An toàn |     | (ít      | lỗi)  |        |           |           |          |             |
|     | Người    |     | khác     |       | có thể | hiểu      | được, bảo |          | trì được!!! |
Software Engineering 20
tkhuong@dthu.edu.vn

|     | Chú |      |       | thích  |        |        |         |       |       |        |        |       |
| --- | --- | ---- | ----- | ------ | ------ | ------ | ------- | ----- | ----- | ------ | ------ | ----- |
| ❖   | Mọi | điều |       | được   |        | chú    | thích   |       | trong |        | chương | trình |
|     | ▪   | Mục  | đích  |        | sử     | dụng   |         | của   | các   | biến   |        |       |
|     | ▪   | Chức |       | năng   | của    |        | khối    | lệnh, |       | câu    | lệnh   |       |
|     |     | •    | Các   | lệnh   | điều   |        | khiển   |       |       |        |        |       |
|     |     | •    | Các   | lệnh   | phức   |        | tạp     |       |       |        |        |       |
|     | ▪   | Chú  | thích |        | các    | module |         |       |       |        |        |       |
|     |     | •    | Mục   | đích,  |        | chức   | năng    |       | của   | module |        |       |
|     |     | •    | Tham  | số,    | giá    |        | trị trả | lại   | (giao |        | diện)  |       |
|     |     | •    | Các   | module |        | thuộc  |         | cấp   |       |        |        |       |
|     |     | •    | Cấu   | trúc,  | thuật  |        | toán    |       |       |        |        |       |
|     |     | •    | Nhiệm |        | vụ của |        | các     | biến  | cục   |        | bộ     |       |
|     |     | •    | Tác   | giả,   | người  |        | kiểm    |       | tra,  | thời   | gian   |       |
Software Engineering 22
tkhuong@dthu.edu.vn

|     | Đặt |       | tên       |             |             |            |               |       |
| --- | --- | ----- | --------- | ----------- | ----------- | ---------- | ------------- | ----- |
| ❖   | Đặt | tên   | biến,     | tên         | hàm         | có nghĩa,  | gợi           | nhớ   |
|     | ▪   | Sử    | dụng      | các ký      | hiệu,       | từ tiếng   | Anh có        | nghĩa |
|     | ▪   | Làm   | cho       | dễ đọc      |             |            |               |       |
|     |     | •     | Vd: dùng  | DateOfBirth |             | hoặc       | date_of_birth |       |
|     |     |       | → Không   | viết        | dateofbirth |            |               |       |
|     | ▪   | Tránh | đặt       | tên quá     | dài         |            |               |       |
|     | ▪   | Thống | nhất      | cách        | dùng        |            |               |       |
|     |     | •     | Vd: i cho | vòng        | lặp,        | tm cho các | giá trị       | tạm…  |
Software Engineering 23
tkhuong@dthu.edu.vn

|     | Câu |        | lệnh |        |      |             |      |      |        |             |           |      |
| --- | --- | ------ | ---- | ------ | ---- | ----------- | ---- | ---- | ------ | ----------- | --------- | ---- |
| ❖   | Các | câu    |      | lệnh   | phải |             | mô   | tả   | cấu    | trúc        |           |      |
|     | ▪   | Tụt    | lề,  | dễ     | đọc, | dễ          | hiểu |      |        |             |           |      |
| ❖   | Làm | đơn    |      | giản   |      | các         | lệnh |      |        |             |           |      |
|     | ▪   | Mỗi    | lệnh | trên   |      | một         | dòng |      |        |             |           |      |
|     | ▪   | Triển  |      | khai   | các  | biểu        |      | thức | phức   | tạp         |           |      |
|     | ▪   | Hạn    | chế  | truyền |      |             | tham | số   | là     | kết quả của | hàm, biểu | thức |
|     | Vd: | printf |      | (“%s”, |      | strcpy(des, |      |      | src)); |             |           |      |
|     | ▪   | Tránh  |      | các    | cấu  | trúc        |      | phức | tạp    |             |           |      |
|     |     | •      | Các  | lệnh   | if   | lồng        | nhau |      |        |             |           |      |
|     |     | •      | Điều | khiển  |      | phủ         | định | if   | not    |             |           |      |
Software Engineering 24
tkhuong@dthu.edu.vn

|     | Hàm     | và    |      | biến  |      | cục      | bộ    |       |           |       |
| --- | ------- | ----- | ---- | ----- | ---- | -------- | ----- | ----- | --------- | ----- |
| ❖   | Chương  | trình | cần  | được  |      | chia     | thành | nhiều | module    | (hàm) |
| ❖   | Không   | viết  | hàm  | quá   | dài  |          |       |       |           |       |
|     | ▪ Không | quá   | 2    | trang | màn  | hình     |       |       |           |       |
| ❖   | Không   | dùng  | quá  | nhiều |      | biến cục | bộ    |       |           |       |
|     | ▪ Không | thể   | theo | dõi   | đồng | thời     | hoạt  | động  | của nhiều | biến  |
Software Engineering 25
tkhuong@dthu.edu.vn

|      | Xử  | lý lỗi |          |       |          |      |     |     |     |
| ---- | --- | ------ | -------- | ----- | -------- | ---- | --- | --- | --- |
| ❖ Có | thể | phát   | hiện lỗi | trong | khi thực | hiện |     |     |     |
| ▪    | Lỗi | chia 0 |          |       |          |      |     |     |     |
▪
|      | Lỗi    | input/ | outut  |                      |      |           |       |           |      |
| ---- | ------ | ------ | ------ | -------------------- | ---- | --------- | ----- | --------- | ---- |
| ❖ Xử | lý lỗi |        |        |                      |      |           |       |           |      |
| ▪    | Nhất   | quán   | trong  | xử lý:               | phân | loại lỗi, | thống | nhất định | dạng |
|      | thông  | báo    |        |                      |      |           |       |           |      |
| ▪    | Phân   | biệt   | output | và thông             | báo  | lỗi       |       |           |      |
|      |        |        |        | Software Engineering |      |           |       |           | 26   |
tkhuong@dthu.edu.vn

|     | Phong  |      |      | cách |       |      | lập   |       | trình |             | tốt     |          |
| --- | ------ | ---- | ---- | ---- | ----- | ---- | ----- | ----- | ----- | ----------- | ------- | -------- |
| ❖   | Tuân   | theo |      | các  | chuẩn |      | thông |       | dụng  |             |         |          |
| ❖   | Chuẩn  |      | được | chấp |       | nhận |       | rộng  |       | rãi hơn, dễ |         | hiểu hơn |
| ❖   | Chú    | giải | đầy  | đủ   | mỗi   |      | khi   | không |       | tuân        | theo    | chuẩn    |
|     | “Người |      | khác |      | có    |      | thể   | hiểu  |       | được        | không?” |          |
Software Engineering 27
tkhuong@dthu.edu.vn

NỘI DUNG
KHÁI NIỆM KỸ THUẬT LẬP TRÌNH
KỸ PHƯƠNG PHÁP LẬP TRÌNH
THUẬT
NGÔN NGỮ LẬP TRÌNH
LẬP
TRÌNH
PHONG CÁCH LẬP TRÌNH
KỸ THUẬT LẬP TRÌNH
Software Engineering 28
tkhuong@dthu.edu.vn

5. KỸ THUẬT LẬP TRÌNH
| ❖   | kỹ  | thuật        | lập      | trình |      | tốt dựa    | trên       | các   | yếu tố: |
| --- | --- | ------------ | -------- | ----- | ---- | ---------- | ---------- | ----- | ------- |
|     | ▪   | Lập          | trình    | có    | cấu  | trúc       |            |       |         |
|     |     | • Dùng       |          | các   | lệnh | có cấu     | trúc       |       |         |
|     |     | • Module hóa |          |       |      |            |            |       |         |
|     |     | • Hạn        |          | chế   | dùng | các cấu    | trúc nguy  |       | hiểm    |
|     | ▪   | Đóng         | gói/ che |       |      | giấu thông | tin        |       |         |
|     |     | • Xây        |          | dựng  | kiểu | dữ liệu    | trừu tượng |       |         |
|     |     | • Hạn        |          | chế   | thao | tác trực   | tiếp lên   | thuộc | tính    |
Software Engineering 29
tkhuong@dthu.edu.vn

| Tránh |     | các |     | cấu | trúc |     | nguy |     | hiểm |     |
| ----- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- | --- |
❖ Số thực:
| ▪ Các | phép | toán | làm | tròn, kết |     | quả | không | chính | xác tuyệt | đối |
| ----- | ---- | ---- | --- | --------- | --- | --- | ----- | ----- | --------- | --- |
▪
| So sánh |     | (=) hai |     | số thực | là  | không | khả | thi |     |     |
| ------- | --- | ------- | --- | ------- | --- | ----- | --- | --- | --- | --- |
❖ Con trỏ
| ▪ Có | khả  | năng | gây | lỗi nghiêm |     | trọng |     |     |     |     |
| ---- | ---- | ---- | --- | ---------- | --- | ----- | --- | --- | --- | --- |
| ▪ Dễ | nhầm |      |     |            |     |       |     |     |     |     |
Vd: double r;
int* n = &r;
Software Engineering 30
tkhuong@dthu.edu.vn

| Tránh |          | các    | cấu  | trúc | nguy | hiểm |
| ----- | -------- | ------ | ---- | ---- | ---- | ---- |
| ❖ Cấp | phát     | bộ nhớ | động |      |      |      |
| ▪     | Quên cấp | phát   |      |      |      |      |
▪
|      | Quên giải | phóng |           |     |     |     |
| ---- | --------- | ----- | --------- | --- | --- | --- |
| ❖ Đệ | quy       |       |           |     |     |     |
| ▪    | Khó hiểu  |       |           |     |     |     |
| ▪    | Dễ nhầm   | điều  | kiện dừng |     |     |     |
Software Engineering 31
tkhuong@dthu.edu.vn

Lập trình phòng thủ
❖ Nhiều lệnh có khả năng sinh lỗi
▪ Lệnh vào/ ra
▪ Các phép toán
▪ Thao tác với bộ nhớ
▪ Truyền tham số sai kiểu
❖ Dự đoán khả năng xuất hiện lỗi
❖ Khắc phục lỗi
▪ Lưu trạng thái an toàn
▪ Quay lại trạng thái an toàn gần nhất
Software Engineering 32
tkhuong@dthu.edu.vn

|     | Lập  |         | trình |       | phòng |        | thủ |     |
| --- | ---- | ------- | ----- | ----- | ----- | ------ | --- | --- |
| ❖   | Lệnh | vào/ ra |       |       |       |        |     |     |
|     | ▪    | Dữ liệu | vào   | không |       | hợp lệ |     |     |
▪
|     |     | Tràn       | bộ nhớ | (kiểu     |       | ký tự)    |      |       |
| --- | --- | ---------- | ------ | --------- | ----- | --------- | ---- | ----- |
|     | ▪   | Lỗi thao   | tác    | file (sai |       | tên, chưa | được | mở,…) |
| ❖   | Các | phép       | toán   |           |       |           |      |       |
|     | ▪   | Lỗi chia 0 |        |           |       |           |      |       |
|     | ▪   | Tràn       | số     |           |       |           |      |       |
|     | ▪   | So sánh    | số     | thực      | (bằng | nhau)     |      |       |
Software Engineering 33
tkhuong@dthu.edu.vn

Lập trình phòng thủ
❖ Ví dụ:
FILE* fp;
fp = fopen (“data”,”r”);
FILE* fp;
If (NULL == (fp=fopen(“data”, “r”)) {
fprintf (stderr, “can not open file…”);
…..
}
Software Engineering 34
tkhuong@dthu.edu.vn

|     | Hướng |          |     |      | hiệu |      |     | quả  | thực    |      | hiện |
| --- | ----- | -------- | --- | ---- | ---- | ---- | --- | ---- | ------- | ---- | ---- |
| ❖   | Phần  | mềm      |     | ngày |      | càng |     | phức | tạp, đa | dạng |      |
|     | ▪     | Mô phỏng |     |      |      |      |     |      |         |      |      |
▪
|     |      | Ứng      | dụng |      | thời  | gian  | thực |     |      |     |     |
| --- | ---- | -------- | ---- | ---- | ----- | ----- | ---- | --- | ---- | --- | --- |
|     | ▪    | Phần     | mềm  |      | nhúng |       |      |     |      |     |     |
|     | ▪    | Trò      | chơi |      |       |       |      |     |      |     |     |
| ❖   | Hiệu | quả      |      | thực | hiện  |       | luôn | cần | được | xem | xét |
|     | ▪    | Thuật    | toán |      | hiệu  | quả   |      |     |      |     |     |
|     | ▪    | Kỹ thuật |      | lập  | trình | hiệu  |      | quả |      |     |     |
|     | ▪    | Ngôn     | ngữ  |      | lập   | trình | hiệu | quả |      |     |     |
Software Engineering 35
tkhuong@dthu.edu.vn

|     | Câu  |        | hỏi    |       |      |      |           |     |           |     |       |         |
| --- | ---- | ------ | ------ | ----- | ---- | ---- | --------- | --- | --------- | --- | ----- | ------- |
| 1.  | Kỹ   | thuật  | lập    | trình | tốt  | thể  | hiện ở    | chỗ | nào?      | Hệ  | quả   | của nó? |
| 2.  | Nêu  | các    | phương |       | pháp |      | lập trình | đã  | có?       | Đặc | trưng | của mỗi |
|     | loại | là gì? |        |       |      |      |           |     |           |     |       |         |
| 3.  | Tiêu | chuẩn  |        | lựa   | chọn | ngôn | ngữ       | lập | trình?    |     |       |         |
| 4.  | Thế  | nào    | là     | ngôn  | ngữ  | khả  | chuyển?   |     | Cho       | ví  | dụ?   |         |
| 5.  | Nêu  | các    | miền   | ứng   | dụng |      | và ngôn   |     | ngữ thích |     | hợp   | với nó? |
6. Các yếu tố tạo ra phong cách lập trình là gì? Nó hướng tới
|     | phần | mềm |     | có đặc | trưng |     | gì? |     |     |     |     |     |
| --- | ---- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 36
tkhuong@dthu.edu.vn

| Câu     |       | hỏi  |          |            |           |           |             |
| ------- | ----- | ---- | -------- | ---------- | --------- | --------- | ----------- |
| 7. Giải | thích | cách | làm: chú | thích? Đặt |           | tên? Viết | câu lệnh?.. |
| 8. Tiêu | chuẩn | cho  | phong    | cách       | lập trình | tốt?      |             |
Software Engineering 37
tkhuong@dthu.edu.vn

| Câu | hỏi | thảo | luận |
| --- | --- | ---- | ---- |
Questions
Software Engineering 39
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C6_LapTrinh.md -->

---


<!-- BẮT ĐẦU FILE: C7_KiemThuPM.md -->
LOGO
Chương 7
KIỂM THỬ
PHẦN MỀM
TRẦN KIM HƯƠNG – KHOA SƯ PHẠM TOÁN TIN
tkhuong@dthu.edu.vn

LOGO
KHOA KỸ THUẬT – CÔNG NGHỆ
Chương 7
KIỂM THỬ
PHẦN MỀM
GV biên soạn: Trần Kim Hương
tkhuong@dthu.edu.vn
Software Engineering
tkhuong@dthu.edu.vn

NỘI DUNG
XÁC MINH & THẨM ĐỊNH
KIỂM
THỬ
RÀ SOÁT PHẦN MỀM
PHẦN
MỀM
KIỂM THỬ PHẦN MỀM
Software Engineering 4
tkhuong@dthu.edu.vn

KIỂM THỬ PHẦN MỀM
| ❖ Kiểm | thử  | là   | nhằm | đánh | giá  |      | chất | lượng    | hoặc | tính   | chấp | nhận  |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- | ------ | ---- | ----- |
| được   | của  | sản  | phẩm |      |      |      |      |          |      |        |      |       |
| ❖ Kiểm | thử  | cũng |      | nhằm | phát | hiện |      | lỗi hoặc | bất  | cứ vấn | đề   | gì về |
| sản    | phẩm |      |      |      |      |      |      |          |      |        |      |       |
❖ Kiểm thử thực hiện mục đích xác minh (Verification) và thẩm
| định | (Validation) |      |     | (V&V) | nhằm                 |     | đảm | bảo | chất | lượng | và  | độ tin |
| ---- | ------------ | ---- | --- | ----- | -------------------- | --- | --- | --- | ---- | ----- | --- | ------ |
| cậy  | của          | phần | mềm |       |                      |     |     |     |      |       |     |        |
|      |              |      |     |       | Software Engineering |     |     |     |      |       |     | 5      |
tkhuong@dthu.edu.vn

KIỂM THỬ PHẦN MỀM
Validation
testing
| Để  | chỉ ra cho | người   | phát    | triển | và khách | hàng | rằng | phần |
| --- | ---------- | ------- | ------- | ----- | -------- | ---- | ---- | ---- |
| mềm | thỏa       | mãn các | yêu cầu | đưa   | ra.      |      |      |      |
Verification
testing
| Để    | chỉ ra các | tình    | huống | trong | đó các | hành | vi của | phần  |
| ----- | ---------- | ------- | ----- | ----- | ------ | ---- | ------ | ----- |
| mềm   | không      | đúng,   | không | như   | mong   | đợi  | hoặc   | không |
| tương | thích      | với đặc | tả    |       |        |      |        |       |
Software Engineering 7
tkhuong@dthu.edu.vn

1. XÁC MINH & THẨM ĐỊNH
❖ Xác minh (Verification)
▪ Kiểm tra xem phần mềm làm ra có đúng đặc tả (yêu cầu, thiết kế)
hay không
| ❖ Thẩm | định (Validation) |      |      |          |            |          |            |            |
| ------ | ----------------- | ---- | ---- | -------- | ---------- | -------- | ---------- | ---------- |
| ▪ Kiểm | tra xem           |      | phần | mềm có   | đáp ứng    | yêu cầu  | người      | dùng không |
| Đây    | là 2              | hoạt | động | cốt yếu  | để đảm     | bảo      | chất lượng |            |
| phần   | mềm,              | diễn | ra   | suốt quá | trình phát | triển!!! |            |            |
Software Engineering 8
tkhuong@dthu.edu.vn

1. XÁC MINH & THẨM ĐỊNH
Software Engineering 9
tkhuong@dthu.edu.vn

|     | Các  |      | hoạt  |        | động     |             | xác  | minh   |       |
| --- | ---- | ---- | ----- | ------ | -------- | ----------- | ---- | ------ | ----- |
| ❖   | Cơ   | sở   | cho   | hoạt   | động     | xác         | minh |        |       |
|     | ▪    | Bản  | đặc   | tả yêu | cầu      |             |      |        |       |
|     | ▪    | Các  | bản   | thiết  | kế       |             |      |        |       |
|     | ▪    | Mã   | nguồn |        |          |             |      |        |       |
| ❖   | Hoạt |      | động  | xác    | minh     |             |      |        |       |
|     | ▪    | Rà   | soát  | (thanh | tra, xét | duyệt, kiểm |      |        | toán) |
|     | ▪    | Kiểm | thử   | (đơn   | vị, tích | hợp, hệ     |      | thống) |       |
Software Engineering 10
tkhuong@dthu.edu.vn

|     | Các  |      | hoạt  |        |       | động     |       |        | thẩm  | định        |        |
| --- | ---- | ---- | ----- | ------ | ----- | -------- | ----- | ------ | ----- | ----------- | ------ |
| ❖   | Cơ   | sở   | cho   | hoạt   |       | động     | thẩm  |        | định  |             |        |
|     | ▪    | Bản  | đặc   | tả     | yêu   |          | cầu   |        |       |             |        |
|     | ▪    | Mã   | nguồn |        |       |          |       |        |       |             |        |
| ❖   | Hoạt |      | động  | thẩm   |       | định     |       |        |       |             |        |
|     | ▪    | Rà   | soát  | (thanh |       | tra, xét |       | duyệt) |       |             |        |
|     | ▪    | Kiểm | toán  |        |       |          |       |        |       |             |        |
|     | ▪    | Kiểm | thử   |        | thẩm  | định     | (chấp |        | nhận) |             |        |
|     | Hai  | hoạt | động  |        | chính |          | của   | thẩm   | định  | và xác minh | là: rà |
|     | soát | và   | kiểm  |        | thử.  |          |       |        |       |             |        |
Software Engineering 11
tkhuong@dthu.edu.vn

| Phân | loại | Xác | minh & Thẩm | định |
| ---- | ---- | --- | ----------- | ---- |
Xác minh (Verification)
Thẩm định (Validation)
| Kiểm | tra (động) |     |     |     |
| ---- | ---------- | --- | --- | --- |
Nghiệm thu Alpha
(Testing)
(Alpha Testing)
| Kiểm | tra (tĩnh) |     |     |     |
| ---- | ---------- | --- | --- | --- |
Nghiệm thu Beta
(Static Verification)
(Beta Testing)
Software Engineering 12
tkhuong@dthu.edu.vn

|     |      | Phân |     | loại |                        | Xác |     | minh (Verification) |     |     |     |     |     |
| --- | ---- | ---- | --- | ---- | ---------------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
| ❖   | Kiểm |      | tra | động | (dynamic verification) |     |     |                     |     |     |     |     |     |
▪
|     |       | Kiểm     | tra  | bằng     | vận  | hành, chạy |                    |          | thử sản  | phẩm   |       | phần    | mềm |
| --- | ----- | -------- | ---- | -------- | ---- | ---------- | ------------------ | -------- | -------- | ------ | ----- | ------- | --- |
|     | →kiểm |          | thử  | phần     |      | mềm        | (software testing) |          |          |        |       |         |     |
|     | ▪     | Dựa      | trên | đầu      | vào  | và         | đầu                | ra       |          |        |       |         |     |
|     | ▪     | Ưu điểm: |      |          |      |            |                    |          |          |        |       |         |     |
|     |       | •        | Đơn  | giản, ít | tốn  | chi phí    |                    | (đối     | với phần | mềm    | thông | thường) |     |
|     |       | •        | Kiểm | tra      | được | yêu        | cầu                | phi chức | năng.    |        |       |         |     |
|     | ▪     | Nhược    |      | điểm:    |      |            |                    |          |          |        |       |         |     |
|     |       | •        | Phức | tạp, tốn |      | kém        | (đối               | với phần | mềm      | chuyên |       | dụng)   |     |
|     |       | •        | Phần | mềm      | phải | hoàn       |                    | thành    |          |        |       |         |     |
|     |       | •        | Có   | thể bỏ   | sót  | lỗi.       |                    |          |          |        |       |         |     |
Software Engineering 13
tkhuong@dthu.edu.vn

|     | Phân |       |       | loại  |                       | Xác  |              | minh (Verification) |       |       |          |      |     |
| --- | ---- | ----- | ----- | ----- | --------------------- | ---- | ------------ | ------------------- | ----- | ----- | -------- | ---- | --- |
| ❖   | Kiểm |       | tra   | tĩnh  | (static verification) |      |              |                     |       |       |          |      |     |
|     | ▪    | Kiểm  | tra   | bằng  |                       | xét  | duyệt, rà    |                     | soát  | các   | tài liệu | phần | mềm |
|     | →    | kiểm  | chứng |       | phần                  |      | mềm          |                     |       |       |          |      |     |
|     | ▪    | Dựa   | trên  | xem   |                       | xét  | nội dung bên |                     |       | trong |          |      |     |
|     | ▪    | Ưu    | điểm: |       |                       |      |              |                     |       |       |          |      |     |
|     |      | •     | Phần  | mềm   | không                 |      | cần          | hoàn                | thành |       |          |      |     |
|     |      | •     | Không | cần   | vận                   | hành |              |                     |       |       |          |      |     |
|     |      | •     | Phát  | hiện  | được                  |      | lỗi tiềm     | ẩn                  |       |       |          |      |     |
|     | ▪    | Nhược |       | điểm: |                       |      |              |                     |       |       |          |      |     |
|     |      | •     | Phức  | tạp   |                       |      |              |                     |       |       |          |      |     |
|     |      | •     | Cần   | đội   | ngũ                   | kinh | nghiệm       |                     |       |       |          |      |     |
|     |      | •     | Tốn   | thời  | gian, công            |      | sức.         |                     |       |       |          |      |     |
Software Engineering 14
tkhuong@dthu.edu.vn

| Phân     |        | loại  |                       | thẩm  |      |       | định | (Validation) |
| -------- | ------ | ----- | --------------------- | ----- | ---- | ----- | ---- | ------------ |
| ❖ Nghiệm |        | thu   | Alpha (Alpha Testing) |       |      |       |      |              |
| ▪        | Nghiệm |       | thu                   | có    | giới | hạn   |      |              |
|          | →      | Triển | khai                  | thí   | điểm |       |      |              |
| ▪        | Chọn   | lọc   | đối                   | tượng |      | tham  | gia  |              |
| ▪        | Vận    | hành  | có                    | kiểm  |      | soát. |      |              |
| ❖ Nghiệm |        | thu   | Beta (Beta Testing)   |       |      |       |      |              |
| ▪        | Nghiệm |       | thu                   | không |      | giới  | hạn  |              |
|          | →Triển |       | khai                  | đại   | trà  |       |      |              |
| ▪        | Không  |       | hạn                   | chế   | đối  | tượng | tham | gia          |
| ▪        | Vận    | hành  | tự                    | do.   |      |       |      |              |
Software Engineering 15
tkhuong@dthu.edu.vn

NỘI DUNG
XÁC MINH & THẨM ĐỊNH
KIỂM
THỬ
RÀ SOÁT PHẦN MỀM
PHẦN
MỀM
KIỂM THỬ PHẦN MỀM
Software Engineering 16
tkhuong@dthu.edu.vn

2. RÀ SOÁT PHẦN MỀM
| ❖   | Rà soát   |     | là xem    | xét, | đánh | giá   | sản | phẩm  |     | được   | tiến hành | mỗi   |
| --- | --------- | --- | --------- | ---- | ---- | ----- | --- | ----- | --- | ------ | --------- | ----- |
|     | giai đoạn |     | để phát   | hiện | ra   | những |     | khiếm |     | khuyết | cần sửa   | trước |
|     | khi sang  |     | giai đoạn |      | sau  |       |     |       |     |        |           |       |
❖
|     | Mục     | tiêu: |            |     |        |      |      |     |       |     |     |     |
| --- | ------- | ----- | ---------- | --- | ------ | ---- | ---- | --- | ----- | --- | --- | --- |
|     | ▪ Chỉ   | ra    | các khiếm  |     | khuyết | cần  | phải | cải | thiện |     |     |     |
|     | ▪ Khẳng |       | định những |     | sản    | phẩm | đạt  | yêu | cầu   |     |     |     |
▪ Kiểm soát việc đạt chất lượng kỹ thuật tối thiểu của sản phẩm
❖ Áp dụng tại các thời điểm khác nhau trong quá trình phát triển
|     | phần | mềm. |     |     |     |                      |     |     |     |     |     |     |
| --- | ---- | ---- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
|     |      |      |     |     |     | Software Engineering |     |     |     |     |     | 17  |
tkhuong@dthu.edu.vn

2. RÀ SOÁT PHẦN MỀM
| ❖ Các | kiểu  | rà soát   |       |       |      |     |     |     |
| ----- | ----- | --------- | ----- | ----- | ---- | --- | --- | --- |
| ▪     | Thanh | tra       |       |       |      |     |     |     |
| ▪     | Họp   | xét duyệt | không | chính | thức |     |     |     |
▪ Họp chính thức với các thành viên: khách hàng, nhà quản lý,
|     | nhân      | viên kỹ | thuật | (rà soát | kỹ thuật | chính | thức | – formal |
| --- | --------- | ------- | ----- | -------- | -------- | ----- | ---- | -------- |
|     | technical | review: | FTR)  |          |          |       |      |          |
Software Engineering 18
tkhuong@dthu.edu.vn

2. RÀ SOÁT PHẦN MỀM
| ❖ Rà | soát    | kỹ thuật | chính   | thức       | (FTR) |      |              |       |
| ---- | ------- | -------- | ------- | ---------- | ----- | ---- | ------------ | ----- |
| ▪    | Là hoạt | động     | đảm bảo | chất       | lượng | phần | mềm do những | người |
|      | đang    | tham gia | phát    | triển thực | hiện  |      |              |       |
Software Engineering 19
tkhuong@dthu.edu.vn

2. RÀ SOÁT PHẦN MỀM
| ▪   | Mục | tiêu | của  | FTR |       |      |      |         |     |        |          |      |
| --- | --- | ---- | ---- | --- | ----- | ---- | ---- | ------- | --- | ------ | -------- | ---- |
|     | •   | Phát | hiện | lỗi | trong | chức | năng | (chương |     | trình) | và triển | khai |
(implementation)
|     | •   | Kiểm  | thử  | sự phù | hợp     | của phần   | mềm   | với | yêu    | cầu       |      |     |
| --- | --- | ----- | ---- | ------ | ------- | ---------- | ----- | --- | ------ | --------- | ---- | --- |
|     | •   | Khẳng | định | phần   | đã      | đạt yêu    | cầu   |     |        |           |      |     |
|     | •   | Đảm   | bảo  | PM     | phù hợp | với các    | chuẩn | đã  | đặt ra |           |      |     |
|     | •   | Đảm   | bảo  | PM     | được    | phát triển | theo  | một | cách   | thức nhất | quán |     |
|     | •   | Làm   | cho  | dự án  | dễ quản | lý hơn     |       |     |        |           |      |     |
• Ngoài ra làm cơ sở huấn luyện các kỹ sư trẻ và có ích ngay cả cho
|     |     | những | kỹ  | sư đã | có kinh | nghiệm               |     |     |     |     |     |     |
| --- | --- | ----- | --- | ----- | ------- | -------------------- | --- | --- | --- | --- | --- | --- |
|     |     |       |     |       |         | Software Engineering |     |     |     |     |     | 20  |
tkhuong@dthu.edu.vn

| Tiến | trình | hoạt | động | rà soát |
| ---- | ----- | ---- | ---- | ------- |
Software Engineering 21
tkhuong@dthu.edu.vn

|     | Cuộc  |      |       | họp  |      |         | rà  | soát     |     |         |       |         |          |
| --- | ----- | ---- | ----- | ---- | ---- | ------- | --- | -------- | --- | ------- | ----- | ------- | -------- |
| ❖   | Thành |      | phần: |      | lãnh |         | đạo | rà soát, |     | các cá  | nhân  | rà soát | và người |
|     | tạo   | ra   | sản   | phẩm |      | được    |     | rà soát  |     | (+khách | hàng) |         |          |
| ❖   | Kết   | luận |       | đưa  | ra   | 1 trong |     | 3 quyết  |     | định    | sau:  |         |          |
|     | ▪     | Chấp |       | nhận | sản  | phẩm    |     | không    | cần | chỉnh   | sửa   |         |          |
|     | ▪     | Từ   | chối  | sản  | phẩm |         | vì  | những    | lỗi | nghiêm  | trọng |         |          |
▪ Chấp nhận cho chỉnh sửa sản phẩm, sau khi chỉnh sửa phải rà
|     |     | soát  | lại |      |     |      |     |          |     |          |     |           |      |
| --- | --- | ----- | --- | ---- | --- | ---- | --- | -------- | --- | -------- | --- | --------- | ---- |
| ❖   | Mọi | thành |     | viên |     | tham |     | gia cuộc |     | họp phải | ký  | vào quyết | định |
Software Engineering 22
tkhuong@dthu.edu.vn

|     | Sản |       | phẩm |      |     | rà      | soát    |          |       |      |         |        |
| --- | --- | ----- | ---- | ---- | --- | ------- | ------- | -------- | ----- | ---- | ------- | ------ |
| ❖   | Sản | phẩm  |      | cuộc | họp |         | rà soát |          |       |      |         |        |
|     | ▪   | Một   | báo  | cáo  | các | vấn     | đề nảy  | sinh     | do cá | nhân | rà soát | nêu ra |
|     | ▪   | Một   | danh | sách |     | các     | vấn đề  | cần giải | quyết |      |         |        |
|     | ▪   | Một   | bản  | tổng | kết | cuộc    | họp     |          |       |      |         |        |
| ❖   | Bản | tổng  | kết  | họp  |     | rà soát | phải    | chỉ      | rõ:   |      |         |        |
|     | ▪   | Đã rà | soát | cái  | gì  |         |         |          |       |      |         |        |
|     | ▪   | Ai rà | soát |      |     |         |         |          |       |      |         |        |
|     | ▪   | Tìm   | thấy | cái  | gì  | và kết  | luận    | ra sao   |       |      |         |        |
Software Engineering 23
tkhuong@dthu.edu.vn

|     | Sản     |      | phẩm |     |      | rà    | soát                 |     |       | (tt) |     |       |      |         |       |
| --- | ------- | ---- | ---- | --- | ---- | ----- | -------------------- | --- | ----- | ---- | --- | ----- | ---- | ------- | ----- |
| ❖   | Danh    | sách |      | các | vấn  | đề    | tồn                  | tại | phục  |      | vụ  |       |      |         |       |
|     | ▪ Nhận  |      | ra   | các | vùng | có    | vấn                  | đề  | trong | sản  |     | phẩm  | được | rà soát |       |
|     | ▪ Dùng  |      | như  |     | một  | danh  | sách                 | các | khoản |      | mục | để    | chỉ  | cho các | người |
|     | làm     |      | ra   | sản | phảm | cần   | chỉnh                |     | sửa   |      |     |       |      |         |       |
|     | ▪ Thiết |      | lập  | thủ | tục  | để    | đảm                  | bảo | rằng  |      | các | khoản | mục  | trong   | danh  |
|     | sách    |      | đó   | sẽ  | được | chỉnh | sửa                  |     | thực  | sự   |     |       |      |         |       |
|     |         |      |      |     |      |       | Software Engineering |     |       |      |     |       |      |         | 24    |
tkhuong@dthu.edu.vn

|     | Tiến   |       |       | hành    |       |        | rà  | soát   |       |      |       |          |      |        |      |         |
| --- | ------ | ----- | ----- | ------- | ----- | ------ | --- | ------ | ----- | ---- | ----- | -------- | ---- | ------ | ---- | ------- |
| ❖   | Mọi    | sản   |       | phẩm    |       | được   |     | tạo    | ra    | ở    | mỗi   | bước     | đều  | được   |      | rà soát |
|     | (không |       | chỉ   | sản     |       | phẩm   |     | cuối   | cùng) |      |       |          |      |        |      |         |
| ❖   | Tiến   | trình |       | phát    |       | triển  |     | chung  |       | nhất | gồm   | các      | giai | đoạn:  |      |         |
|     | ▪      | Công  |       | nghệ    | hệ    | thống  |     | (kế    | hoạch |      | triển | khai)    |      |        |      |         |
|     | ▪      | Phân  |       | tích,   | xác   | định   |     | yêu    | cầu   | phần |       | mềm (đặc |      | tả yêu | cầu) |         |
|     | ▪      | Thiết |       | kế phần |       | mềm    |     | (thiết | kế)   |      |       |          |      |        |      |         |
|     | ▪      | Lập   | trình |         | (mã   | nguồn) |     |        |       |      |       |          |      |        |      |         |
|     | ▪      | Kiểm  |       | thử     | phần  | mềm    |     | (kế    | hoạch |      | kiểm  | thử)     |      |        |      |         |
|     | ▪      | Bảo   | trì   | (kế     | hoạch |        | bảo |        | trì)  |      |       |          |      |        |      |         |
|     | →      | Rà    | soát  | bám     |       | theo   |     | sản    | phẩm  | của  | các   | giai     | đoạn | này    |      |         |
Software Engineering 25
tkhuong@dthu.edu.vn

| Các    | danh   | mục        | sản      | phẩm         | cần | rà soát |
| ------ | ------ | ---------- | -------- | ------------ | --- | ------- |
| ❖ Danh | mục rà | soát công  | nghệ     | hệ thống     |     |         |
| ❖ Danh | mục rà | soát lập   | kế hoạch | dự án        |     |         |
| ❖ Danh | mục rà | soát phân  | tích     | yêu cầu phần | mềm |         |
| ❖ Danh | mục rà | soát thiết | kế phần  | mềm          |     |         |
| ❖ Danh | mục rà | soát khâu  | lập      | trình        |     |         |
| ❖ Danh | mục rà | soát kiểm  | thử      | phần mềm     |     |         |
| ❖ Danh | mục rà | soát bảo   | trì phần | mềm          |     |         |
Software Engineering 26
tkhuong@dthu.edu.vn

NỘI DUNG
XÁC MINH & THẨM ĐỊNH
KIỂM
THỬ
RÀ SOÁT PHẦN MỀM
PHẦN
MỀM
KIỂM THỬ PHẦN MỀM
Software Engineering 27
tkhuong@dthu.edu.vn

3. KIỂM THỬ PHẦN MỀM
❖
| Mô      | hình  | chữ  |      | V – các | pha | kiểm | thử |
| ------- | ----- | ---- | ---- | ------- | --- | ---- | --- |
| ❖ Các   | hình  | thức |      | kiểm    | thử |      |     |
| ❖ Quy   | trình | kiểm |      | thử     |     |      |     |
| ❖ Thiết | kế    | dữ   | liệu | kiểm    | thử |      |     |
| ❖ Lập   | tài   | liệu | kiểm | thử     |     |      |     |
Software Engineering 28
tkhuong@dthu.edu.vn

| 3.1 Mô | hình | chữ | V – | các | pha | kiểm | thử |
| ------ | ---- | --- | --- | --- | --- | ---- | --- |
Software Engineering 29
tkhuong@dthu.edu.vn

|     | 3.1 Mô            |       | hình       |                   | chữ    | V –   | các | pha | kiểm | thử |
| --- | ----------------- | ----- | ---------- | ----------------- | ------ | ----- | --- | --- | ---- | --- |
| ❖   | Kiểm              | thử   | đơn        | vị (Unit Testing) |        |       |     |     |      |     |
|     | ▪ Kiểm            |       | tra từng   | đơn               | vị lập | trình |     |     |      |     |
|     |                   | →Các  | phương     | thức              |        |       |     |     |      |     |
|     | ▪ Thực            |       | hiện trong | môi               | trường | cô    | lập |     |      |     |
|     | ▪ Lập             | trình | viên       | thực              | hiện   |       |     |     |      |     |
|     | ▪ Unit Test Case: |       |            |                   |        |       |     |     |      |     |
Software Engineering 30
tkhuong@dthu.edu.vn

| 3.1 Mô |          | hình     | chữ                   |        | V –       | các | pha | kiểm | thử |
| ------ | -------- | -------- | --------------------- | ------ | --------- | --- | --- | ---- | --- |
| ❖ Kiểm | thử tích | hợp      | (Integration Testing) |        |           |     |     |      |     |
| ▪ Kiểm | tra      | một nhóm |                       | đơn vị | lập trình |     |     |      |     |
| ▪ Kiểm | tra      | sự phối  | hợp                   | hoạt   | động      |     |     |      |     |
| ▪ Thực | hiện     | trong    | môi                   | trường | tích      | hợp |     |      |     |
Software Engineering 31
tkhuong@dthu.edu.vn

|     | 3.1 Mô |                          | hình     |      | chữ              | V –     | các | pha | kiểm | thử |
| --- | ------ | ------------------------ | -------- | ---- | ---------------- | ------- | --- | --- | ---- | --- |
| ❖   | Kiểm   | thử                      | hệ thống |      | (System Testing) |         |     |     |      |     |
|     | ▪ Kiểm | tra                      | toàn     | bộ   | hệ thống         |         |     |     |      |     |
|     | ▪ Hệ   | thống                    | hoạt     | động | như              | đặc tả? |     |     |      |     |
|     | ▪ Thực | hiện                     | trong    | môi  | trường           | giả     | lập |     |      |     |
|     | ▪ Phân | loại:                    |          |      |                  |         |     |     |      |     |
|     |        | • Functional Testing     |          |      |                  |         |     |     |      |     |
|     |        | • Non-Functional Testing |          |      |                  |         |     |     |      |     |
Software Engineering 32
tkhuong@dthu.edu.vn

| 3.1 Mô   |          | hình  | chữ        | V –                  | các  | pha     | kiểm | thử |
| -------- | -------- | ----- | ---------- | -------------------- | ---- | ------- | ---- | --- |
| ❖ Nghiệm | thu      | phần  | mềm        | (Acceptance Testing) |      |         |      |     |
| ▪ Khách  | hàng     | dùng  | thử        |                      |      |         |      |     |
| ▪ Hệ     | thống    | thỏa  | mãn nhu    | cầu?                 |      |         |      |     |
| ▪ Thực   | hiện     | trong | môi trường | vận                  | hành | thật sự |      |     |
| ▪ Phân   | loại:    |       |            |                      |      |         |      |     |
|          | • Nghiệm | thu   | Alpha      |                      |      |         |      |     |
|          | • Nghiệm | thu   | Beta       |                      |      |         |      |     |
Software Engineering 33
tkhuong@dthu.edu.vn

|     | 3.2 Các |                |           | hình |        | thức                |                       | kiểm                 | thử |
| --- | ------- | -------------- | --------- | ---- | ------ | ------------------- | --------------------- | -------------------- | --- |
| ❖   | Kỹ      | thuật          | kiểm      | thử  | tĩnh   | (static testing)    |                       |                      |     |
|     | ▪       | Thanh          | tra       | phần | mềm    |                     | (Software Inspection) |                      |     |
|     | ▪       | Model Checking |           |      |        |                     |                       |                      |     |
|     | ▪       | Không          | thực      | thi  | chương |                     | trình                 |                      |     |
| ❖   | Kỹ      | thuật          | kiểm      | thử  | động   |                     | (dynamic testing)     |                      |     |
|     | ▪       | Kiểm           | thử       | hộp  | đen    | (black-box testing) |                       |                      |     |
|     |         | •              | Kỹ thuật  | kiểm | thử    | chức                | năng                  | (functional testing) |     |
|     |         | •              | Test Case |      |        |                     |                       |                      |     |
|     | ▪       | Kiểm           | thử       | hộp  | trắng  | (white-box testing) |                       |                      |     |
|     |         | •              | Kỹ thuật  | kiểm | thử    | cấu                 | trúc                  | (structural testing) |     |
Software Engineering 34
tkhuong@dthu.edu.vn

|     | 3.2 Các |       |      |     | hình |     |      | thức | kiểm | thử |
| --- | ------- | ----- | ---- | --- | ---- | --- | ---- | ---- | ---- | --- |
| ❖   | Kỹ      | thuật | kiểm |     | thử  |     | tĩnh | - 1  |      |     |
▪
|     |     | Thanh |         | tra   | phần  | mềm   |         | (Software  | Inspection) |     |
| --- | --- | ----- | ------- | ----- | ----- | ----- | ------- | ---------- | ----------- | --- |
|     |     | •     | Micheal |       | Fagan |       | đề xuất | 1979       |             |     |
|     |     | •     | Kiểm    | tra   | bằng  |       | cách    | đọc nội    | dung        |     |
|     |     | •     | Đội     | ngũ   | thanh |       | tra độc | lập        |             |     |
|     |     | •     | Ưu      | điểm: |       |       |         |            |             |     |
|     |     |       | –       | Có    | thể   | thực  | hiện    | ở mỗi pha  |             |     |
|     |     |       | –       | Rất   | hiệu  | quả   | để      | tìm lỗi    |             |     |
|     |     | •     | Khuyết  |       | điểm: |       |         |            |             |     |
|     |     |       | –       | Đội   | ngũ   | nhiều | kinh    | nghiệm     |             |     |
|     |     |       | –       | Tốn   | kém   | thời  | gian    | và chi phí |             |     |
Software Engineering 35
tkhuong@dthu.edu.vn

|     | 3.2 Các |       |        |          | hình  |       | thức |           |       | kiểm     | thử |
| --- | ------- | ----- | ------ | -------- | ----- | ----- | ---- | --------- | ----- | -------- | --- |
| ❖   | Kỹ      | thuật | kiểm   |          | thử   | tĩnh  |      | - 2       |       |          |     |
|     | ▪       | Model |        | Checking |       |       |      |           |       |          |     |
|     |         | •     | Kiểm   | tra      | bằng  | cách  |      | chứng     | minh  |          |     |
|     |         |       | –      | Mô       | hình  | toán  | học  | sản phẩm  |       | kiểm tra |     |
|     |         |       | –      | Chứng    |       | minh  | mô   | hình đúng |       | đắn      |     |
|     |         | •     | Thực   | hiện     |       | ở pha | phân | tích      | thiết | kế       |     |
|     |         | •     | Ưu     | điểm:    |       |       |      |           |       |          |     |
|     |         |       | –      | Có       | khả   | năng  | đúng | đắn       | hoàn  | toàn     |     |
|     |         |       | –      | Có       | thể   | thực  | hiện | tự động   |       |          |     |
|     |         | •     | Khuyết |          | điểm: |       |      |           |       |          |     |
|     |         |       | –      | Phức     | tạp   | để    | mô   | hình hóa  |       |          |     |
|     |         |       | –      | Chưa     | có    | công  | cụ   | tự động   | hiệu  | quả      |     |
Software Engineering 36
tkhuong@dthu.edu.vn

|     |     | 3.2 Các   |      |      | hình |      | thức    | kiểm              | thử |
| --- | --- | --------- | ---- | ---- | ---- | ---- | ------- | ----------------- | --- |
| ❖   | Kỹ  | thuật     | kiểm |      | thử  | động | - 1     |                   |     |
|     | ▪   | Kiểm      | thử  | hộp  | đen  |      |         |                   |     |
|     |     | • Chỉ     | cần  | dựa  | vào  | đặc  | tả phần | mềm               |     |
|     |     | • Thường  |      | phát | hiện | các  | lỗi đặc | tả yêu cầu, thiết | kế  |
|     |     | • Dễ      | dàng | thực | hiện |      |         |                   |     |
|     |     | • Chi phí |      | thấp |      |      |         |                   |     |
• Xây dựng các test case  (dữ liệu) để kiểm tra các chức năng
Software Engineering 37
tkhuong@dthu.edu.vn

|     |     | 3.2 Các |          | hình    |      | thức | kiểm | thử |
| --- | --- | ------- | -------- | ------- | ---- | ---- | ---- | --- |
| ❖   | Kỹ  | thuật   | kiểm     | thử     | động | - 2  |      |     |
|     | ▪   | Kiểm    | thử      | hộp đen |      |      |      |     |
|     |     | •       | Xây dựng | dữ liệu | kiểm | thử  |      |     |
– Kỹ thuật phân tích giá trị biên – BVA (boundary value analysis)
– Kỹ thuật phân vùng tương đương - EP(equivalence Partitioning)
|     |     |     | – Kiểm | thử ngẫu     | nhiên        | (random testing) |        |     |
| --- | --- | --- | ------ | ------------ | ------------ | ---------------- | ------ | --- |
|     |     |     | – Đồ   | thị nhân-quả | (cause-efect |                  | graph) |     |
|     |     |     | – Kiểm | thử cú       | pháp         |                  |        |     |
Software Engineering 38
tkhuong@dthu.edu.vn

|      | 3.2 Các     |      |                |       | hình     |          | thức  | kiểm | thử |
| ---- | ----------- | ---- | -------------- | ----- | -------- | -------- | ----- | ---- | --- |
| ❖ Kỹ | thuật       | kiểm |                | thử   | động     |          | - 3   |      |     |
|      | ▪ Test Case |      |                |       |          |          |       |      |     |
|      | •           | Kiểm | tra            | đầu   | vào, đầu |          | ra    |      |     |
|      | •           | Dùng | kịch           | bản   | kiểm     |          | thử   |      |     |
|      | •           | Các  | đối            | tượng | kiểm     |          | tra:  |      |     |
|      |             | –    | Một            | đoạn  | mã       | nguồn    |       |      |     |
|      |             | –    | Một            | kịch  | bản      | Use Case |       |      |     |
|      |             | –    | Một            | chức  | năng     | hoàn     | chỉnh |      |     |
|      | •           | Nội  | dung Test Case |       |          |          |       |      |     |
|      |             | –    | Ngữ            | cảnh  | kiểm     | tra      |       |      |     |
|      |             | –    | Dữ             | liệu  | đầu vào  |          |       |      |     |
|      |             | –    | Kết            | quả   | đầu ra   | mong     | đợi   |      |     |
|      |             | –    | Các            | bước  | thực     | hiện     |       |      |     |
Software Engineering 39
tkhuong@dthu.edu.vn

|                 | 3.2 Các | hình   | thức      | kiểm | thử       |
| --------------- | ------- | ------ | --------- | ---- | --------- |
| ❖ Test Case của |         | trường | hợp “Nhập | sách | thất bại” |
Software Engineering 40
tkhuong@dthu.edu.vn

|     |     | 3.2 Các |           |      |      | hình       |                    | thức  |       | kiểm    |       | thử |
| --- | --- | ------- | --------- | ---- | ---- | ---------- | ------------------ | ----- | ----- | ------- | ----- | --- |
| ❖   | Kỹ  | thuật   |           | kiểm |      | thử        | động               |       |       |         |       |     |
|     | ▪   | Kiểm    |           | thử  | hộp  | trắng      |                    |       |       |         |       |     |
|     |     |         | • Dựa     | vào  | mã   | nguồn/ cấu |                    |       | trúc  | chương  | trình |     |
|     |     |         | • Thường  |      | phát | hiện       | các                | lỗi   | lập   | trình   |       |     |
|     |     |         | • Khó     | thực |      | hiện       |                    |       |       |         |       |     |
|     |     |         | • Chi phí |      | cao  |            |                    |       |       |         |       |     |
|     | ▪   | Kỹ      | thuật     | kiểm |      | thử        | hộp                | trắng |       |         |       |     |
|     |     |         | • Kiểm    | thử  |      | dựa trên   | đồ                 | thị   | điều  | khiển   |       |     |
|     |     |         | • Kiểm    | thử  |      | dựa trên   | đồ                 | thị   | luồng | dữ liệu |       |     |
|     |     |         | • Kiểm    | thử  |      | đột biến   | (mutation testing) |       |       |         |       |     |
Software Engineering 41
tkhuong@dthu.edu.vn

3. KIỂM THỬ PHẦN MỀM
| ❖ Mô    | hình     | chữ  | V –  | các  | pha kiểm | thử |
| ------- | -------- | ---- | ---- | ---- | -------- | --- |
| ❖ Các   | hình     | thức | kiểm |      | thử      |     |
| ❖ Quy   | trình    | kiểm |      | thử  |          |     |
| ❖ Thiết | kế       | dữ   | liệu | kiểm | thử      |     |
| ❖ Lập   | tài liệu |      | kiểm | thử  |          |     |
Software Engineering 48
tkhuong@dthu.edu.vn

|     | 3.3 Quy | trình |     | kiểm    | thử |     |     |     |     |
| --- | ------- | ----- | --- | ------- | --- | --- | --- | --- | --- |
|     |         |       |     | Dữ liệu | KT  |     |     |     |     |
(Test data)
| Đặc | tả YC | Kế hoạch | KT  | Ca kiểm | thử | Kết quả | KT  | Báo cáo | KT  |
| --- | ----- | -------- | --- | ------- | --- | ------- | --- | ------- | --- |
(Requirement spec) (Test plan) (Test cases) (Test result) (Test report)
|     |          | Thiết | kế kiểm |                      | Thực | hiện |     | Đánh giá |     |
| --- | -------- | ----- | ------- | -------------------- | ---- | ---- | --- | -------- | --- |
| Lập | kế hoạch |       |         |                      |      |      |     |          |     |
|     |          |       | thử     |                      | kiểm | thử  |     | kết quả  |     |
|     |          |       |         | Software Engineering |      |      |     |          | 49  |
tkhuong@dthu.edu.vn

|     | 3.3 Quy |       |         |        | trình |      |       | kiểm  |      |      | thử |              |          |
| --- | ------- | ----- | ------- | ------ | ----- | ---- | ----- | ----- | ---- | ---- | --- | ------------ | -------- |
| ❖   | Kiểm    |       | thử     | thường |       | gồm  |       | các   | bước |      |     |              |          |
|     | ▪       | Lập   | kế      | hoạch  |       |      |       |       |      |      |     |              |          |
|     | ▪       | Thiết | kế      | các    | ca    | kiểm |       | thử   |      |      |     |              |          |
|     | ▪       | Tạo   | dữ      | liệu   | kiểm  |      | thử   |       |      |      |     |              |          |
|     |         | •     | Kiểm    | thử    | với   | tất  | cả    | các   | dữ   | liệu | vào | là cần thiết |          |
|     |         |       | –       | Không  | thể   |      | kiểm  | thử   | “vét | cạn” |     |              |          |
|     |         | •     | Chọn    | tập    | các   | dữ   | liệu  | thử   | đại  | diện |     | từ miền dữ   | liệu vào |
|     |         |       | –       | Dựa    | trên  | các  | tiêu  | chuẩn |      | chọn | dữ  | liệu thử     |          |
|     | ▪       | Thực  | thi     | chương |       |      | trình | dựa   |      | trên | dữ  | liệu kiểm    | thử      |
|     |         | •     | Cung    | cấp    | dữ    | liêu | thử   |       |      |      |     |              |          |
|     |         | •     | Thực    | thi    |       |      |       |       |      |      |     |              |          |
|     |         | •     | Ghi     | nhận   | kết   | quả  |       |       |      |      |     |              |          |
|     | ▪       | Quan  | sát     |        | kết   | quả  | kiểm  | thử   |      |      |     |              |          |
|     |         | •     | So sánh |        | kết   | quả  | nhận  | được  |      | với  | kết | quả mong     | đợi      |
Software Engineering 50
tkhuong@dthu.edu.vn

|     | 3.4 Thiết |     |     | kế  |     | dữ  | liệu |     | kiểm |     | thử |     |
| --- | --------- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
❖
|     | Ví  | dụ: một | textbox chỉ |     |     | cho | phép |     | nhập | số nguyên |     | từ 1 đến |
| --- | --- | ------- | ----------- | --- | --- | --- | ---- | --- | ---- | --------- | --- | -------- |
100
| →   | Ta không |          | thể nhập |      | tất | cả    | các   | giá  | trị   | từ 1 đến | 100??? |     |
| --- | -------- | -------- | -------- | ---- | --- | ----- | ----- | ---- | ----- | -------- | ------ | --- |
| ❖   | 2 kỹ     | thuật    | để thiết |      | kế  | dữ    | liệu  | kiểm | thử   |          |        |     |
|     | ▪        | Kỹ thuật | phân     | tích | giá | trị   | giới  | hạn  | – BVA |          |        |     |
|     | ▪        | Kỹ thuật | phân     | vùng |     | tương | đương |      | –     | EP       |        |     |
Software Engineering 51
tkhuong@dthu.edu.vn

|         | 3.4 Thiết |       |      | kế   | dữ   | liệu | kiểm                   | thử |     |
| ------- | --------- | ----- | ---- | ---- | ---- | ---- | ---------------------- | --- | --- |
| PP1: Kỹ |           | thuật | phân | tích | giới | hạn  | – BVA (Boundary Value  |     |     |
Analysis)
| o Kỹ | thuật | BVA sẽ         |       | chọn    | các | giá trị        | nằm tại | các điểm    | giới hạn |
| ---- | ----- | -------------- | ----- | ------- | --- | -------------- | ------- | ----------- | -------- |
| của  | phần  | vùng           |       |         |     |                |         |             |          |
| o Áp | dụng  | kỹ             | thuật | BVA cần |     | 4 test case để |         | test trường | hợp vd   |
| trên |       | là 0,1,100,101 |       |         |     |                |         |             |          |
Software Engineering 54
tkhuong@dthu.edu.vn

|         | 3.4 Thiết |       |     |      |     | kế   |     | dữ    | liệu |       | kiểm |     | thử              |     |     |
| ------- | --------- | ----- | --- | ---- | --- | ---- | --- | ----- | ---- | ----- | ---- | --- | ---------------- | --- | --- |
| PP2: Kỹ |           | thuật |     | phân |     | vùng |     | tương |      | đương |      | –   | EP (Equivalence  |     |     |
Partitioning)
| ❖   | Phân | chia dữ |      |     | liệu | đầu |         | vào  | thành |     | các lớp | tương |     | đương | nhau |
| --- | ---- | ------- | ---- | --- | ---- | --- | ------- | ---- | ----- | --- | ------- | ----- | --- | ----- | ---- |
| ❖   | Tạo  | ca      | kiểm | thử |      | cho | mỗi     | lớp  | tương |     | đương   |       |     |       |      |
|     | ▪    | Kiểm    | thử  | một | giá  |     | trị đại | diện | của   |     | lớp     |       |     |       |      |
▪ Nếu giá trị đại diện bị lỗi → các giá trị trong lớp đó cũng sẽ bị lỗi
|     |      | như | vậy   |     |     |      |     |           |     |     |        |     |     |     |     |
| --- | ---- | --- | ----- | --- | --- | ---- | --- | --------- | --- | --- | ------ | --- | --- | --- | --- |
| →   | Giảm | số  | lượng |     | ca  | kiểm |     | thử, tăng |     |     | độ phủ |     |     |     |     |
Software Engineering 58
tkhuong@dthu.edu.vn

|         | 3.4 Thiết |       |      | kế   | dữ    | liệu | kiểm  |     | thử              |     |
| ------- | --------- | ----- | ---- | ---- | ----- | ---- | ----- | --- | ---------------- | --- |
| PP2: Kỹ |           | thuật | phân | vùng | tương |      | đương | –   | EP (Equivalence  |     |
Partitioning)
o
| Trong |     | ví dụ | trên | dùng | kỹ thuật |     | này sẽ | chia làm | 3 phân | vùng |
| ----- | --- | ----- | ---- | ---- | -------- | --- | ------ | -------- | ------ | ---- |
o
Như vậy chỉ cần chọn 3 test case để test trường hợp này: -5,
| 55, 102 hoặc |     |     | 0, 10, 1000,…. |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Software Engineering 59
tkhuong@dthu.edu.vn

|         | 3.4 Thiết |     |       |     |      | kế  |      | dữ    | liệu |       | kiểm |     | thử              |     |     |
| ------- | --------- | --- | ----- | --- | ---- | --- | ---- | ----- | ---- | ----- | ---- | --- | ---------------- | --- | --- |
| PP2: Kỹ |           |     | thuật |     | phân |     | vùng | tương |      | đương |      | –   | EP (Equivalence  |     |     |
Partitioning)
| o   | Tuy  | nhiên |         | nếu | nhập |     | số  | thập | phân |     | (55.5) hay một |     |     | ký  | tự không |
| --- | ---- | ----- | ------- | --- | ---- | --- | --- | ---- | ---- | --- | -------------- | --- | --- | --- | -------- |
|     | phải | số    | (abc)?? |     |      |     |     |      |      |     |                |     |     |     |          |
o
|     | Trong |     | trường |     | hợp |     | trên | có  | thể | chia thành |     | 5 phân |     | vùng | như |
| --- | ----- | --- | ------ | --- | --- | --- | ---- | --- | --- | ---------- | --- | ------ | --- | ---- | --- |
sau:
|     | o   | Các   | số   | nguyên |     | từ  | 1 đến | 100   |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | ------ | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
|     | o   | Các   | số   | nguyên |     | nhỏ |       | hơn 1 |     |     |     |     |     |     |     |
|     | o   | Các   | số   | nguyên |     | lớn | hơn   | 100   |     |     |     |     |     |     |     |
|     | o   | Không |      | phải   | số  |     |       |       |     |     |     |     |     |     |     |
|     | o   | Số    | thập | phân   |     |     |       |       |     |     |     |     |     |     |     |
Software Engineering 60
tkhuong@dthu.edu.vn

| 3.4 Thiết |     | kế dữ | liệu | kiểm | thử |
| --------- | --- | ----- | ---- | ---- | --- |
Có 2 bước:
| ▪ Xác | định | các lớp | tương | đương |     |
| ----- | ---- | ------- | ----- | ----- | --- |
| ▪ Xác | định | các ca  | kiểm  | thử   |     |
Software Engineering 61
tkhuong@dthu.edu.vn

|     |       | Xác   | định       |       |           | lớp                      |         | tương |        | đương |           |         |       |         |
| --- | ----- | ----- | ---------- | ----- | --------- | ------------------------ | ------- | ----- | ------ | ----- | --------- | ------- | ----- | ------- |
| ❖   | Dựa   | vào   | điều       |       | kiện      | đầu                      | vào/đầu |       | ra     |       |           |         |       |         |
| ❖   | Lớp   | tương |            | đương |           | (equivalence class) biểu |         |       |        |       |           | diễn    | một   | tập hợp |
|     | trạng | thái  |            |       |           |                          |         |       |        |       |           |         |       |         |
|     | ▪     | hợp   | lệ (valid) |       |           |                          |         |       |        |       |           |         |       |         |
|     | ▪     | không | hợp        | lệ    | (invalid) |                          |         |       |        |       |           |         |       |         |
|     | Điều  | kiện  | bên        | ngoài |           |                          | Các     | lớp   | tương  | đương |           | Các lớp | tương | đương   |
|     |       |       |            |       |           |                          |         |       | hợp lệ |       |           | không   |       | hợp lệ  |
| ❖   | Phân  | hoạch |            | tương |           | đương                    |         | là    | 1 quá  | trình | heuristic |         |       |         |
Software Engineering 62
tkhuong@dthu.edu.vn

| Dựa    | vào      | điều                  | kiện | đầu | vào |
| ------ | -------- | --------------------- | ---- | --- | --- |
| ❖ Điều | kiện đầu | vào (input condition) |      |     |     |
▪
Giá trị: A
| ▪     | Dãy giá trị: [1..100] |                       |     |     |     |
| ----- | --------------------- | --------------------- | --- | --- | --- |
| ▪     | Tập giá trị: {A,B,C}  |                       |     |     |     |
| ▪     | Boolean: là           | số nguyên             |     |     |     |
| ❖ Một | số nguyên             | tắc                   |     |     |     |
| ▪     | A → A, not A          |                       |     |     |     |
| ▪     | [1..100] →            | x<1, 1<=x<=100, x>100 |     |     |     |
| ▪     | {A,B,C} →             | A, B, C, not{A,B,C}   |     |     |     |
| ▪     | Là số nguyên          | → true, false         |     |     |     |
Software Engineering 69
tkhuong@dthu.edu.vn

|      | Dựa                | vào            | điều      | kiện  | đầu | vào     |
| ---- | ------------------ | -------------- | --------- | ----- | --- | ------- |
| ❖ Ví | dụ: nhập           | vào            | số nguyên | dương | nhỏ | hơn 100 |
|      | ▪ Chuỗi            | ký tự, invalid |           |       |     |         |
|      | ▪ Số thực, invalid |                |           |       |     |         |
|      | ▪ x<=0, invalid    |                |           |       |     |         |
|      | ▪ 1<=x<100, valid  |                |           |       |     |         |
|      | ▪ x>=100, invalid  |                |           |       |     |         |
Software Engineering 70
tkhuong@dthu.edu.vn

|     | Dựa                   | vào        |                          | điều |            | kiện         |          | đầu | vào       |        |
| --- | --------------------- | ---------- | ------------------------ | ---- | ---------- | ------------ | -------- | --- | --------- | ------ |
| ❖   | Ví dụ: chuỗi          |            | có                       | 7 ký | tự         | (chữ         | cái), ký | tự  | đầu là ký | tự hoa |
|     | ▪ Length < 7, invalid |            |                          |      |            |              |          |     |           |        |
|     | ▪ Length > 7, invalid |            |                          |      |            |              |          |     |           |        |
|     | ▪ 7 ký                | tự, ký     | tự                       | đầu  | hoa, valid |              |          |     |           |        |
|     | ▪ 7 ký                | tự, ký     | tự                       | đầu  | không      | hoa, invalid |          |     |           |        |
|     | ▪ Ký                  | tự đặc     | biệt: #, *, &,.., invaid |      |            |              |          |     |           |        |
|     | ▪ Chuỗi               | số, invaid |                          |      |            |              |          |     |           |        |
Software Engineering 71
tkhuong@dthu.edu.vn

|      | Dựa              | vào     | điều             | kiện | đầu | vào |
| ---- | ---------------- | ------- | ---------------- | ---- | --- | --- |
| ❖ Ví | dụ: tọa          | độ điểm | 3<=x<=7, 5<=y<=9 |      |     |     |
|      | ▪ x<3, invalid   |         |                  |      |     |     |
|      | ▪ 3<=x<=7, valid |         |                  |      |     |     |
|      | ▪ x>7, invalid   |         |                  |      |     |     |
|      | ▪ y<5, invalid   |         |                  |      |     |     |
|      | ▪ 5<=y<=9, valid |         |                  |      |     |     |
|      | ▪ y>9, invalid   |         |                  |      |     |     |
|      | ▪ x, y khác      | ký      | tự số, invalid   |      |     |     |
Software Engineering 72
tkhuong@dthu.edu.vn

|        | Dựa          | vào   | điều  | kiện  | đầu     | ra        |        |
| ------ | ------------ | ----- | ----- | ----- | ------- | --------- | ------ |
| ❖ Phân | lớp          | tương | đương | tương | ứng với | điều kiện | đầu ra |
| ❖ Ví   | dụ: xếp      | loại  |       |       |         |           |        |
|        | ▪ 0<=x<3 →   | D     |       |       |         |           |        |
|        | ▪ 3<=x<5 →   | C     |       |       |         |           |        |
|        | ▪ 5<=x<7 →   | B     |       |       |         |           |        |
|        | ▪ 7<=x<=10 → |       | A     |       |         |           |        |
Software Engineering 75
tkhuong@dthu.edu.vn

|     | Xác      | định          | các    | ca kiểm   |         | thử     |           |      |
| --- | -------- | ------------- | ------ | --------- | ------- | ------- | --------- | ---- |
| ❖   | Gán Mã   | ID cho        | mỗi    | lớp tương | đương   |         |           |      |
| ❖   | Viết các | test case phủ |        | nhiều     | nhất có | thể các | lớp hợp   | lệ → |
|     | phủ toàn | bộ các        | lớp    | hợp lệ    |         |         |           |      |
| ❖   | Viết các | test case phủ |        | nhiều     | nhất có | thể các | lớp không | hợp  |
|     | lệ → phủ | toàn          | bộ các | lớp không | hợp     | lệ      |           |      |
Software Engineering 76
tkhuong@dthu.edu.vn

| Lập | tài liệu | kiểm | thử |
| --- | -------- | ---- | --- |
❖ Test cases
❖ Bug report
Software Engineering 81
tkhuong@dthu.edu.vn

Test cases
❖ Là một tình huống kiểm tra, được thiết kế để kiểm tra một đối
|     | tượng |      | có  | thỏa | mãn    | yêu  | cầu  | đặt | ra  | hay không. |      |      |      |     |
| --- | ----- | ---- | --- | ---- | ------ | ---- | ---- | --- | --- | ---------- | ---- | ---- | ---- | --- |
| ❖   | 3     | bước | cơ  | bản  |        |      |      |     |     |            |      |      |      |     |
|     | ▪     | Mô   | tả: | đặc  | tả các | điều | kiện | cần | cố  | để tiến    | hành | kiểm | tra. |     |
▪ Nhập: đặc tả đối tượng hoặc dữ liệu cần thiết, được sử dụng làm
|     |      | đầu  | vào      | để   | thực   | hiện | kiểm    | tra. |      |        |        |      |      |     |
| --- | ---- | ---- | -------- | ---- | ------ | ---- | ------- | ---- | ---- | ------ | ------ | ---- | ---- | --- |
|     | ▪    | Kết  | quả      | mong |        | chờ: | kết quả | trả  | về   | từ đối | tượng  | kiểm | tra. |     |
| ❖   | Test |      | scenario |      | → test | case | →       | Test |      | Step   |        |      |      |     |
|     | ▪    | Test | Step:    |      | một    | hành | động    | để   | thực | hiện   | và đáp | ứng  | mong | đợi |
|     | ▪    | Test | Case:    |      | danh   | sách | các     | test | step |        |        |      |      |     |
▪ Test Scenario: danh sách các test case và phối hợp của chúng.
Software Engineering 82
tkhuong@dthu.edu.vn

|                         | Test cases – |      |                  |          | Nội  |            | dung    |      |      |      |
| ----------------------- | ------------ | ---- | ---------------- | -------- | ---- | ---------- | ------- | ---- | ---- | ---- |
| 1. ID: định             |              | danh | phân             | biệt     | các  | test cases |         |      |      |      |
| 2. Test case name: mô   |              |      |                  | tả       | ngắn |            | gọn mục | tiêu | của  | test |
| 3. Precondition: điều   |              |      |                  | kiện     | tiên | quyết      | để      | thực | hiện | test |
| 4. Test step: các       |              |      | bước             | thực     |      | hiện       | cùng dữ | liệu | test |      |
| 5. Expected result: kết |              |      |                  | quả      | mong |            | đợi     |      |      |      |
| 6. Actual result: kết   |              |      |                  | quả thực |      | tế         |         |      |      |      |
| 7. Status: kết          |              | quả  | test (Pass/Fail) |          |      |            |         |      |      |      |
| 8. Tester: người        |              |      | thực             | hiện     | test |            |         |      |      |      |
| 9. Date: ngày           |              | test |                  |          |      |            |         |      |      |      |
| 10. Remark: ghi         |              |      | chú              |          |      |            |         |      |      |      |
Software Engineering 83
tkhuong@dthu.edu.vn

Ví dụ
| ❖ Test Case của | trường | hợp “Nhập | sách | thất bại” |
| --------------- | ------ | --------- | ---- | --------- |
Software Engineering 84
tkhuong@dthu.edu.vn

Bug Report
❖ Cung cấp thông tin chi tiết về sự cố hoặc lỗi cho những bên
liên quan
| ▪ Người | phát triển: | sửa   | lỗi      |         |           |         |
| ------- | ----------- | ----- | -------- | ------- | --------- | ------- |
| ▪ Người | quản lý:    | quyết | định tài | nguyên, | cấp phát, | ưu tiên |
▪ Nhân viên hỗ trợ kỹ thuật: nắm bắt thông tin thực hiện, chuẩn bị
| ▪ Kiểm | thử viên: | cần | biết trạng | thái của | hệ thống | hiện tại |
| ------ | --------- | --- | ---------- | -------- | -------- | -------- |
Software Engineering 85
tkhuong@dthu.edu.vn

| Bug report –                |       | Nội                     | dung   |        |     |
| --------------------------- | ----- | ----------------------- | ------ | ------ | --- |
| 1. ID: định danh            | lỗi   |                         |        |        |     |
| 2. Function name: chức      |       | năng                    | bị     | lỗi    |     |
| 3. Problem summary: mô      |       |                         | tả lỗi |        |     |
| 4. How to reproduce it: các |       |                         | bước   | tạo ra | lỗi |
| 5. Reported by: người       |       | báo                     | cáo    |        |     |
| 6. Date: ngày               | báo   | cáo                     |        |        |     |
| 7. Assigned to: giao        |       | ai sửa                  | lỗi    |        |     |
| 8. Status: tình             | trạng | lỗi (open/fixed/closed) |        |        |     |
| 9. Comment: ghi             | chú   |                         |        |        |     |
Software Engineering 86
tkhuong@dthu.edu.vn

|      |      | VD1. Giải |     |       |     |     | phương |        |     | trình | bậc | 2   |
| ---- | ---- | --------- | --- | ----- | --- | --- | ------ | ------ | --- | ----- | --- | --- |
| Phân | tích | yêu       | cầu | (ngôn |     | ngữ | tự     | nhiên) |     |       |     |     |
❖ Giáo viên muốn có phần mềm hỗ trợ học sinh tự rèn luyện bài tập Giải phương trình bậc
|     | 2 với | các | thông    |        | tin như | sau:  |     |       |     |     |     |     |
| --- | ----- | --- | -------- | ------ | ------- | ----- | --- | ----- | --- | --- | --- | --- |
|     | ▪     | Hỗ  | trợ giải | phương |         | trình |     | bậc 2 |     |     |     |     |
Học sinh nhập vào các hệ số a,b,c (a khác 0), phần mềm cho ra kết quả nghiệm của
|     | phương |     | trình     | với | 2 ký | số  | thập | phân |     |     |     |     |
| --- | ------ | --- | --------- | --- | ---- | --- | ---- | ---- | --- | --- | --- | --- |
|     | ▪      | Tự  | rèn luyện |     |      |     |      |      |     |     |     |     |
Học sinh nhập vào các hệ số a,b,c (a khác 0) và nghiệm của phương trình vừa nhập
Phần mềm cho kết quả đánh giá nghiệm đúng sai, nếu sai thì hiển thị nghiệm đúng
|     | Quy | tắc giải | phương |     | trình | bậc |     | 2:  |     |     |     |     |
| --- | --- | -------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2: ax2+bx+c=0 (với
|     | Cho phương |      | trình          |                | bậc        |       |     |            | a,b,c | là 3 số thực, a khác |     | 0)  |
| --- | ---------- | ---- | -------------- | -------------- | ---------- | ----- | --- | ---------- | ----- | -------------------- | --- | --- |
|     | Các        | bước | giải           | phương         |            | trình | như | sau:       |       |                      |     |     |
|     | B1. Tính   |      | delta = b2-4ac |                |            |       |     |            |       |                      |     |     |
|     | B2. Xác    | đinh | nghiệm         |                | theo       | delta |     |            |       |                      |     |     |
|     |            |      | + Nếu          | delta<0: PT vô |            |       |     | nghiệm     |       |                      |     |     |
|     |            |      | + Nếu          | delta=0: PT có |            |       |     | nghiệm     | kép x | =x =-b/2a            |     |     |
|     |            |      |                |                |            |       |     |            | 1     | 2                    |     |     |
|     |            |      | + Nếu          | delta>0: PT có |            |       |     | 2 nghiệm   | phân  | biệt                 |     |     |
|     |            |      |                |                | x =(-b-căn |       |     | delta)/ 2a |       |                      |     |     |
1
|     |     |     |     |     | x =(-b+căn |     |     | delta)/ 2a |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- |
2
Software Engineering 87
tkhuong@dthu.edu.vn

| Giải        | VD 1      |     |        |           |        |          |
| ----------- | --------- | --- | ------ | --------- | ------ | -------- |
| ❖ Điều kiện | TestCase  |     |        |           |        |          |
| Điều kiện   | Lớp hợp   | lệ  | Mã     | Lớp không | hợp lệ | Mã không |
|             |           |     | hợp lệ |           |        | hợp lệ   |
| a           | a số thực |     | v1     | a = 0     |        | x1       |
|             | a <>0     |     | v2     | a ký tự   |        | x2       |
|             |           |     |        | a null    |        | x3       |
| b           | b số thực |     | v3     | b ký tự   |        | x4       |
|             |           |     |        | b null    |        | x5       |
| c           | c số thực |     | v4     | c ký tự   |        | x6       |
|             |           |     |        | c null    |        | x7       |
Software Engineering 88
tkhuong@dthu.edu.vn

| Giải VD 1 |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- |
❖ Thiết kế TestCase
| TestCase | Mô tả | Đầu    | ra mong  | muốn   | Mã kiểm        | tra |
| -------- | ----- | ------ | -------- | ------ | -------------- | --- |
| 1        | a = 2 | Phương | trình vô | nghiệm | v1, v2, v3, v4 |     |
b = -5
c = 7
| 2   | ………… | ……….. |     |     | ………….  |     |
| --- | ---- | ----- | --- | --- | ------ | --- |
| 3   | ………. | …………. |     |     | ……………. |     |
Software Engineering 89
tkhuong@dthu.edu.vn

BÀI TẬP 1
| ❖ Kiểm     | thử chức | năng           | đăng | nhập  | hệ thống |
| ---------- | -------- | -------------- | ---- | ----- | -------- |
| ▪ Username |          |                |      |       |          |
| ▪ Password |          |                |      |       |          |
| 1) Xác     | định các | lớp tương      |      | đương |          |
| 2) Thiết   | kế các   | test case kiểm |      | thử   |          |
Software Engineering 90
tkhuong@dthu.edu.vn

BÀI TẬP 2
| ❖ Thiết | kế test cases cho |               |      | chức            | năng | sau đây |
| ------- | ----------------- | ------------- | ---- | --------------- | ---- | ------- |
| ▪       | Input:            |               |      |                 |      |         |
|         | • Điểm            | lý thuyết: là | số   | thực, >=0 và    |      | <=7     |
|         | • Điểm            | thực hành: là |      | số thực, >=0 và |      | <=3     |
| ▪       | Output: xếp       | loại          | nếu  | LT+TH           |      |         |
|         | • >=0 và          | <5 → loại     | C    |                 |      |         |
|         | • >=5 và          | <8 → loại     | B    |                 |      |         |
|         | • >=8 và          | <=10 →        | loại | A               |      |         |
91
tkhuong@dthu.edu.vn

Thảo luận
Software Engineering 92
tkhuong@dthu.edu.vn
<!-- KẾT THÚC FILE: C7_KiemThuPM.md -->

---
