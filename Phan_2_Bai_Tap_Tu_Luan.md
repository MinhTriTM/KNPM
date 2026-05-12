# TỔNG HỢP ÔN THI KỸ NGHỆ PHẦN MỀM - PHẦN 2
**GIẢI CHI TIẾT BÀI TẬP THIẾT KẾ HỆ THỐNG (Phong cách tự luận sinh viên)**

*Lưu ý: Dưới đây là lời giải chi tiết cho 3 đề thi bài tập thực hành (Câu II - 5 điểm) xuất hiện trong ảnh đề thi gốc. Lời giải được trình bày rõ ràng từng bước, mô tả cách vẽ sơ đồ để sinh viên có thể chép lại chính xác vào giấy thi.*

---

## BÀI 1: HỆ THỐNG QUẢN LÝ KÝ TÚC XÁ

**Đề bài tóm tắt:** Phần mềm "Quản lý ký túc xá". Nhân viên: Quản lý phòng, Lập hợp đồng, Thanh toán, Báo cáo doanh thu. Ban giám đốc: Cập nhật quy định. Thông tin phòng gồm: Mã phòng, Tầng, Số giường, Dãy phòng (A,B,C).

### 1. Vẽ Sơ đồ Usecase (1.5 điểm)
**Bài làm:**
*(Trên giấy thi, sinh viên vẽ hình người đại diện cho Actor và hình oval đại diện cho Usecase)*
- **Tác nhân (Actor):**
  - **Nhân viên:** Đứng bên trái hệ thống.
  - **Ban giám đốc:** Đứng bên phải hệ thống.
- **Các Use case (Hình oval bên trong khung chữ nhật hệ thống):**
  - Actor **Nhân viên** nối bằng các nét liền tới 4 Use case: `(Quản lý thông tin phòng)`, `(Lập hợp đồng thuê phòng)`, `(Thanh toán tiền phòng)`, `(Lập báo cáo doanh thu)`.
  - Actor **Ban giám đốc** nối nét liền tới Use case: `(Cập nhật quy định thuê phòng)`.
  - *Mở rộng (điểm cộng):* Từ UC `(Quản lý thông tin phòng)`, vẽ các đường đứt nét có mũi tên `<<include>>` trỏ tới 3 UC con: `(Thêm phòng)`, `(Cập nhật phòng)`, `(Xóa phòng)`.

### 2. Vẽ Sơ đồ màn hình giao diện (1.0 điểm)
**Bài làm:**
*(Mô tả bản vẽ trên giấy)*
- Vẽ một khung hình chữ nhật lớn tượng trưng cho màn hình máy tính.
- **Tiêu đề (Header):** Trên cùng ghi "HỆ THỐNG QUẢN LÝ KÝ TÚC XÁ - NHÂN VIÊN". Góc phải có "Tài khoản: Nguyễn Văn A | Đăng xuất".
- **Thanh menu (Sidebar bên trái):** Gồm các nút dọc: [Trang chủ], [Quản lý phòng], [Lập hợp đồng], [Thanh toán], [Báo cáo]. (Nút "Quản lý phòng" đang được bôi đậm vì đang chọn).
- **Vùng làm việc chính (Content bên phải):**
  - Nút [ + Thêm phòng mới ] ở góc trên bên phải vùng content.
  - **Bảng dữ liệu (Data Table):** Vẽ một bảng gồm các cột: `STT | Mã phòng | Dãy phòng | Tầng | Số giường | Thao tác (Sửa/Xóa)`. Vẽ vài dòng dữ liệu giả vào bảng.

### 3. Thực hiện chức năng "Quản lý Thông tin phòng" (2.5 điểm)

#### a. Vẽ sơ đồ lớp hướng đối tượng (1.0 điểm)
**Bài làm:**
*(Vẽ 2 hình chữ nhật chia làm 3 ngăn)*
- **Lớp `DayPhong` (Dãy phòng):**
  - Ngăn 1: Tên lớp `DayPhong`
  - Ngăn 2: Thuộc tính: `- maDay: String`, `- tenDay: String` (A, B, C), `- viTri: String`, `- mauSac: String`, `- moTa: String`
  - Ngăn 3: Phương thức: `+ getDayPhong()`, `+ updateDayPhong()`
- **Lớp `Phong` (Phòng):**
  - Ngăn 1: Tên lớp `Phong`
  - Ngăn 2: Thuộc tính: `- maPhong: String`, `- tang: int`, `- soGiuong: int`
  - Ngăn 3: Phương thức: `+ themPhong()`, `+ capNhatPhong()`, `+ xoaPhong()`
- **Mối quan hệ:** Vẽ đường thẳng nối từ `DayPhong` sang `Phong`. Ghi quan hệ `1 - n` (Một dãy phòng có nhiều phòng). Ký hiệu hình thoi rỗng ở đầu DayPhong (Quan hệ Aggregation).

#### b. Thiết kế dữ liệu lưu trữ (0.5 điểm)
**Bài làm:**
Thiết kế CSDL quan hệ gồm 2 bảng:
- **Bảng `DAY_PHONG`**:
  - `MaDay` (NVARCHAR, PK): Khóa chính.
  - `TenDay` (NVARCHAR, NOT NULL).
  - `ViTri` (NVARCHAR), `MauSac` (NVARCHAR), `MoTa` (NVARCHAR).
- **Bảng `PHONG`**:
  - `MaPhong` (NVARCHAR, PK): Khóa chính.
  - `MaDay` (NVARCHAR, FK): Khóa ngoại trỏ đến bảng `DAY_PHONG`.
  - `Tang` (INT, NOT NULL, CHECK > 0).
  - `SoGiuong` (INT, NOT NULL, CHECK > 0).

#### c. Thiết kế Màn hình giao diện chức năng này (0.5 điểm)
**Bài làm:**
*(Vẽ một Popup/Form nhập liệu)*
- Tiêu đề Form: "THÊM PHÒNG MỚI"
- Các trường nhập liệu (Label bên trái, Textbox bên phải):
  - Mã phòng: [__________] (*)
  - Dãy phòng: [ Combobox xổ xuống chọn A, B hoặc C v] (*)
  - Tầng: [__________] (Chỉ nhập số) (*)
  - Số giường: [__________] (Chỉ nhập số) (*)
- Bên dưới góc phải có 2 nút: `[ LƯU ]` và `[ HỦY ]`.
- Ghi chú: Dấu (*) là bắt buộc nhập.

#### d. Thiết kế Test Case thêm thành công (0.5 điểm)
**Bài làm:**
| Mã TC | Tên Test Case | Điều kiện tiên quyết | Dữ liệu đầu vào | Kết quả mong đợi |
|---|---|---|---|---|
| TC_PH_01 | Thêm phòng thành công | Người dùng đang ở màn hình Thêm phòng | - Mã phòng: P101<br>- Dãy phòng: A<br>- Tầng: 1<br>- Số giường: 4 | Hệ thống lưu dữ liệu vào CSDL, hiển thị thông báo "Thêm phòng thành công" và cập nhật phòng P101 lên bảng danh sách. |

---

## BÀI 2: HỆ THỐNG QUẢN LÝ HỌC TẬP SINH VIÊN

**Đề bài tóm tắt:** Phần mềm "Quản lý học tập sinh viên". Cán bộ đào tạo: QL sinh viên, QL điểm, QL lịch học, Lập báo cáo. Ban giám hiệu: Cập nhật quy định đánh giá. Form điểm: Mã SV, Họ tên, Môn học, Học kỳ, Điểm (số thực 0-10). Môn học thuộc danh mục.

### 1. Vẽ Sơ đồ Usecase (1.0 điểm)
**Bài làm:**
- **Tác nhân (Actor):**
  - **Cán bộ đào tạo** (bên trái).
  - **Ban giám hiệu** (bên phải).
- **Các Use case:**
  - Actor **Cán bộ đào tạo** nối đến: `(Quản lý thông tin sinh viên)`, `(Quản lý điểm học tập)`, `(Quản lý lịch học và lớp học)`, `(Lập báo cáo kết quả)`.
  - Actor **Ban giám hiệu** nối đến: `(Cập nhật quy định đánh giá)`.
  - Từ UC `(Quản lý điểm học tập)` dùng mũi tên `<<include>>` trỏ đến `(Thêm điểm)`, `(Cập nhật điểm)`, `(Xóa điểm)`.

### 2. Vẽ Sơ đồ màn hình giao diện (1.0 điểm)
**Bài làm:**
- Vẽ khung hình chữ nhật lớn (Form chính).
- Trái: Thanh điều hướng (Menu): Thông tin SV, Quản lý Điểm (đang tô đậm), Lịch học, Báo cáo.
- Phải (Vùng chính):
  - Khung tìm kiếm: Ô nhập [Mã sinh viên], Combobox [Chọn học kỳ], Nút `[Tìm kiếm]`.
  - Dưới là Bảng kết quả gồm: `STT | Mã SV | Họ Tên | Môn học | Học kỳ | Điểm thi | Thao tác`.
  - Nút `[ + Nhập điểm mới ]` nằm phía trên bảng.

### 3. Thực hiện chức năng "Quản lý điểm học tập" (3.0 điểm)

#### a. Vẽ sơ đồ lớp hướng đối tượng (1.0 điểm)
**Bài làm:**
Gồm 3 lớp chính:
- **Lớp `SinhVien`:**
  - Thuộc tính: `- maSV: String`, `- hoTen: String`
  - Hàm: `+ getInfo()`
- **Lớp `MonHoc`:**
  - Thuộc tính: `- maMon: String`, `- tenMon: String`, `- thuocKhoa: String`
- **Lớp `KetQuaHocTap` (Lớp liên kết giữa SV và Môn học):**
  - Thuộc tính: `- maSV: String`, `- maMon: String`, `- hocKy: String`, `- diem: float`
  - Hàm: `+ themDiem()`, `+ capNhatDiem()`, `+ xoaDiem()`
- **Quan hệ:** `SinhVien` (1) --- (n) `KetQuaHocTap` (n) --- (1) `MonHoc`. (Sinh viên có nhiều kết quả, Môn học có nhiều sinh viên thi).

#### b. Thiết kế dữ liệu lưu trữ (1.0 điểm)
**Bài làm:**
Cần 3 bảng để đảm bảo chuẩn hóa:
1. Bảng `SINH_VIEN` (MaSV PK, HoTen NOT NULL).
2. Bảng `MON_HOC` (MaMon PK, TenMon NOT NULL, KhoaQuanLy).
3. Bảng `DIEM_HOC_TAP` (Bảng trung gian lưu điểm):
   - `MaSV` (NVARCHAR, FK trỏ SINH_VIEN, PK part 1)
   - `MaMon` (NVARCHAR, FK trỏ MON_HOC, PK part 2)
   - `HocKy` (NVARCHAR, PK part 3)
   - `Diem` (FLOAT, CHECK: Diem >= 0 AND Diem <= 10, NOT NULL)
*(Khóa chính của bảng Điểm là cụm 3 cột: MaSV, MaMon, HocKy)*

#### c. Thiết kế Màn hình giao diện chức năng này (0.5 điểm)
**Bài làm:**
Vẽ Form popup "NHẬP ĐIỂM SINH VIÊN":
- Ô nhập: Mã sinh viên: [_____] (Khi gõ xong tự động hiển thị mờ Họ tên bên cạnh).
- Combobox: Chọn Môn học [ v ] (Chỉ lấy môn thuộc danh mục khoa).
- Ô nhập: Học kỳ: [_____].
- Ô nhập: Điểm: [_____] (Giới hạn 0 - 10).
- Nút bấm dưới cùng: `[ Lưu điểm ]` và `[ Đóng ]`.

#### d. Thiết kế Test Case thêm thành công (0.5 điểm)
**Bài làm:**
| ID | Tên | Tiền điều kiện | Input | Expected Output |
|---|---|---|---|---|
| TC_DIEM_01 | Thêm điểm hợp lệ | Mã SV 'SV001' tồn tại. Mã Môn 'CS101' tồn tại | Mã SV: SV001, Môn: CS101, Học kỳ: HK1, Điểm: 8.5 | Lưu CSDL thành công. Form đóng lại, bảng dữ liệu hiện dòng điểm 8.5 của SV001. |

---

## BÀI 3: HỆ THỐNG QUẢN LÝ ĐỒ ÁN MÔN HỌC

**Đề bài tóm tắt:** Trưởng bộ môn: Duyệt đề tài, Triển khai đề tài. Giảng viên: QL thông tin đề tài, Theo dõi tiến độ. Sinh viên: Chọn đề tài, Báo cáo tiến độ. Thông tin Đề tài: STT (khác rỗng), Tên (khác rỗng), Ngày ra (<= hiện tại), Loại (ĐA1, ĐA2), GV ra đề (trỏ về bảng GV).

### 1. Vẽ Sơ đồ Usecase (1.5 điểm)
**Bài làm:**
- **3 Tác nhân (Actor):** Trưởng bộ môn, Giảng viên, Sinh viên.
- **Use case theo Tác nhân:**
  - **Trưởng bộ môn** nối đến: `(Duyệt đề tài)`, `(Triển khai đề tài cho SV)`.
  - **Giảng viên** nối đến: `(Quản lý thông tin đề tài)`, `(Theo dõi tiến độ thực hiện)`.
  - **Sinh viên** nối đến: `(Chọn đề tài đồ án)`, `(Báo cáo tiến độ thực hiện)`.
- Use case `(Quản lý thông tin đề tài)` include 3 UC: `(Thêm đề tài)`, `(Sửa đề tài)`, `(Xóa đề tài)`.

### 2. Vẽ Sơ đồ màn hình giao diện (1.0 điểm)
**Bài làm:**
Vẽ layout chuẩn gồm Menu dọc bên trái và Bảng nội dung bên phải (Giao diện dành cho Giảng viên):
- Menu: Quản lý đề tài (Active), Theo dõi tiến độ.
- Thanh công cụ trên bảng: Nút `[Thêm Đề Tài Mới]`, Ô `[Tìm kiếm đề tài...]`.
- Bảng Grid (Lưới dữ liệu): Các cột `STT | Tên đề tài | Loại ĐA | Ngày ra | Trạng thái (Chờ duyệt/Đã duyệt) | Hành động`.

### 3. Thực hiện chức năng "Quản lý thông tin đề tài" (2.5 điểm)

#### a. Vẽ sơ đồ lớp (1.0 điểm)
**Bài làm:**
- **Lớp `GiangVien`:**
  - Thuộc tính: `- maGV`, `- hoTen`, `- ngaySinh`, `- queQuan`
- **Lớp `LoaiDoAn`:**
  - Thuộc tính: `- maLoai`, `- tenLoai` (ĐA1 hoặc ĐA2)
- **Lớp `DeTai`:**
  - Thuộc tính: `- sttDeTai`, `- tenDeTai`, `- yeuCau`, `- ngayRa`
  - Hàm: `+ them()`, `+ sua()`, `+ xoa()`
- **Quan hệ:**
  - `GiangVien` (1) --- (n) `DeTai`: 1 Giảng viên ra nhiều Đề tài.
  - `LoaiDoAn` (1) --- (n) `DeTai`: 1 Loại có nhiều Đề tài.

#### b. Thiết kế dữ liệu lưu trữ (0.5 điểm)
**Bài làm:**
- Bảng `GIANG_VIEN` (MaGV PK, HoTen, NgaySinh, QueQuan).
- Bảng `LOAI_DO_AN` (MaLoai PK, TenLoai). *Chỉ chứa 2 dòng: DA1 và DA2.*
- Bảng `DE_TAI`:
  - `SttDeTai` (INT, PK, NOT NULL)
  - `TenDeTai` (NVARCHAR, NOT NULL)
  - `YeuCau` (NVARCHAR)
  - `NgayRa` (DATE, CHECK <= GETDATE())
  - `MaGV` (FK trỏ bảng GIANG_VIEN)
  - `MaLoai` (FK trỏ bảng LOAI_DO_AN)

#### c. Thiết kế Màn hình giao diện chức năng (0.5 điểm)
**Bài làm:**
Vẽ Form "THÊM ĐỀ TÀI ĐỒ ÁN":
- Textbox: Số thứ tự Đề tài (*)
- Textbox: Tên đề tài (*)
- Textarea (Ô rộng): Yêu cầu đề tài
- DatePicker: Ngày ra đề tài [ Lịch ] (Tự động set ngày hôm nay, không cho chọn ngày tương lai) (*)
- Combobox: Loại đề tài [Đồ án 1 / Đồ án 2]
- Combobox: Giảng viên ra đề (Danh sách load từ DB)
- Nút `LƯU LẠI` và `ĐÓNG`.

#### d. Thiết kế Test Case (0.5 điểm)
**Bài làm:**
| ID | Tên | Tiền kiện | Input | Kết quả mong đợi |
|---|---|---|---|---|
| TC_DA_01 | Thêm đề tài ĐA1 thành công | Đang ở form thêm Đề tài | STT: 1, Tên: "Web bán hàng", Ngày ra: 12/05/2026, Loại: ĐA 1, GV: Nguyễn Văn A | Lưu thành công. Báo "Thành công", data lưu CSDL bảng DE_TAI, gridview được làm mới. |