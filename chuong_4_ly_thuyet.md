# CHƯƠNG 4: MÔ HÌNH HÓA PHẦN MỀM (UML & ERD)

Tài liệu phục vụ giải bài tập tự luận với các quy ước, ký hiệu và luật vẽ chuẩn mực 100%.

## PHẦN 1: MÔ HÌNH HÓA DỮ LIỆU & TIẾN TRÌNH NGHIỆP VỤ

### 1. SƠ ĐỒ THỰC THỂ LIÊN KẾT (ERD - Entity Relationship Diagram)
- **Định nghĩa:** Mô hình hóa cấu trúc dữ liệu ở mức khái niệm.
- **Thực thể (Entity):** Đối tượng tồn tại độc lập. **Ký hiệu:** Hình chữ nhật.
- **Mối quan hệ (Relationship):** Liên kết ngữ nghĩa (1-1, 1-N, N-N). **Ký hiệu:** Hình thoi.
- **Thuộc tính (Attribute):** **Ký hiệu:** Hình Oval (Elip). Gồm 3 loại đặc biệt:
  - **Thuộc tính Khóa (Key):** Định danh duy nhất. Hình Oval, tên **gạch chân**.
  - **Thuộc tính Đa trị (Multi-valued):** Chứa nhiều giá trị (VD: Bằng cấp). Hình Oval **nét đôi**.
  - **Thuộc tính Dẫn xuất (Derived):** Tính toán từ thuộc tính khác (VD: Tuổi). Hình Oval **nét đứt**.

**Chuẩn hóa dữ liệu CSDL (Normalization):**
- **Dạng chuẩn 1 (1NF):** Các thuộc tính phải mang giá trị nguyên tố (đơn trị). Tuyệt đối KHÔNG chứa thuộc tính đa trị.
- **Dạng chuẩn 2 (2NF):** Đạt 1NF và mọi thuộc tính không khóa phải **phụ thuộc hàm hoàn toàn** vào khóa chính.
- **Dạng chuẩn 3 (3NF):** Đạt 2NF và **không có phụ thuộc bắc cầu** giữa các thuộc tính không khóa.

### 2. SƠ ĐỒ PHÂN CẤP CHỨC NĂNG (BFD - Business Function Diagram)
- **Khái niệm & Vai trò:** Rã các chức năng nghiệp vụ từ mức cao nhất xuống mức chi tiết theo dạng cây. Trả lời câu hỏi "Hệ thống làm những công việc gì?". (Không thể hiện trình tự thời gian, không có luồng dữ liệu).

### 3. SƠ ĐỒ LUỒNG DỮ LIỆU (DFD - Data Flow Diagram)
**4 thành phần cơ bản:**
1. **Thực thể ngoài (External Entity):** Tác nhân giao tiếp hệ thống. Hình chữ nhật.
2. **Tiến trình (Process):** Xử lý, biến đổi dữ liệu. Hình tròn hoặc Oval (chứa động từ).
3. **Kho dữ liệu (Data Store):** Nơi lưu trữ tĩnh. Hai đường thẳng song song hoặc hình chữ nhật khuyết 1 cạnh.
4. **Luồng dữ liệu (Data Flow):** Dòng chảy dữ liệu. Mũi tên có gắn tên dữ liệu.

**Quy tắc vẽ DFD:**
- MỌI luồng dữ liệu đều phải đi qua ít nhất 1 Tiến trình.
- CẤM: Thực thể ngoài <-> Thực thể ngoài; Thực thể ngoài <-> Kho dữ liệu; Kho dữ liệu <-> Kho dữ liệu.

**Phân biệt các mức DFD:**
- **Mức ngữ cảnh (Level 0):** Cả hệ thống là 1 Tiến trình duy nhất. Bao quanh là các Thực thể ngoài. Tuyệt đối KHÔNG vẽ Kho dữ liệu.
- **Mức đỉnh (Level 1):** Rã tiến trình hệ thống thành các phân hệ chính. Bắt đầu xuất hiện Kho dữ liệu.
- **Mức dưới đỉnh (Level 2):** Rã chi tiết. Đầu vào/Đầu ra của tiến trình bị phân rã phải khớp hoàn toàn với tổng Đầu vào/Đầu ra của các tiến trình con (luật bảo toàn).

---

## PHẦN 2: MÔ HÌNH HÓA VỚI UML

**Định nghĩa UML:** Unified Modeling Language, ngôn ngữ mô hình hóa thống nhất để thiết kế phần mềm hướng đối tượng.
**Phân loại:**
1. **Biểu đồ Cấu trúc (Structural):** Mô tả tĩnh (VD: Class).
2. **Biểu đồ Hành vi (Behavioral):** Mô tả động theo thời gian (VD: Use-case, Activity, Sequence, State Machine).

### 4. BIỂU ĐỒ USE-CASE
- **Actor:** Người dùng/hệ thống bên ngoài. Hình người (Stickman).
- **Use-case:** Chức năng do hệ thống cung cấp. Hình Oval.
- **Quan hệ Include (Bắt buộc):** Use-case gốc bắt buộc gọi Use-case include. Mũi tên **nét đứt**, trỏ TỪ Gốc -> VỀ Bao gồm (`<<include>>`).
- **Quan hệ Extend (Tùy chọn):** Bổ sung chức năng dưới điều kiện. Mũi tên **nét đứt**, trỏ TỪ Mở rộng -> VỀ Gốc (`<<extend>>`).
- **Generalization (Kế thừa):** Mũi tên **nét liền**, **tam giác rỗng** trỏ về đối tượng Cha.

### 5. BIỂU ĐỒ LỚP (Class Diagram)
- **Cấu trúc:** Hình chữ nhật chia 3 phần (Tên lớp, Thuộc tính, Phương thức).
- **Access Modifiers:** `+` (Public), `-` (Private), `#` (Protected).
- **Mối quan hệ:**
  - **Dependency (Phụ thuộc):** Dùng tạm thời (vd: tham số). Nét đứt, mũi tên hở.
  - **Association (Kết hợp):** Tham chiếu ngữ nghĩa. Nét liền ngang hàng.
  - **Aggregation (Tụ hợp):** "Toàn thể - Bộ phận" lỏng lẻo (Bộ phận không chết theo). Nét liền, **Hình thoi rỗng** ở Lớp Toàn thể.
  - **Composition (Cấu thành):** "Toàn thể - Bộ phận" chặt chẽ (Phụ thuộc vòng đời). Nét liền, **Hình thoi đặc** ở Lớp Toàn thể.
  - **Inheritance (Kế thừa):** Nét liền, **mũi tên tam giác rỗng** trỏ về Lớp Cha.

### 6. BIỂU ĐỒ TUẦN TỰ (Sequence Diagram)
- **Lifeline:** Đường nét đứt dọc biểu thị thời gian sống.
- **Message:**
  - **Đồng bộ:** Gửi và đợi kết quả. Mũi tên nét liền, **đầu đặc**.
  - **Bất đồng bộ:** Gửi và không đợi. Mũi tên nét liền, **đầu hở**.
  - **Phản hồi:** Trả dữ liệu. Mũi tên **nét đứt**, đầu hở.
- **Các Fragment:** `alt` (rẽ nhánh if-else), `opt` (tùy chọn if), `loop` (vòng lặp).

### 7. BIỂU ĐỒ HOẠT ĐỘNG (Activity Diagram)
- **Node:** Bắt đầu (Tròn đặc), Kết thúc (Tròn đặc có viền khuyên ngoài).
- **Fork / Join:** Vạch đen dày. (Fork: rẽ nhánh song song, Join: gộp nhánh đồng bộ).
- **Decision:** Hình thoi, rẽ nhánh theo điều kiện `[condition]`.
- **Swimlanes:** Các cột/làn dọc để xác định tác nhân thực hiện.

### 8. BIỂU ĐỒ TRẠNG THÁI (State Machine Diagram)
- Mô tả vòng đời của **một đối tượng duy nhất**.
- **Trạng thái (State):** Hình chữ nhật bo góc.
- **Transition (Chuyển đổi):** Mũi tên nét liền.
- **Event (Sự kiện):** Viết trên mũi tên. Cú pháp: `Event [Guard Condition] / Action`.
