# CHƯƠNG 6: LẬP TRÌNH & XÂY DỰNG PHẦN MỀM

## 1. 4 Tính chất cơ bản của Lập trình hướng đối tượng (OOP)
*   **Trừu tượng (Abstraction):**
    *   *Định nghĩa:* Ẩn đi các chi tiết thực thi phức tạp bên trong, chỉ bộc lộ các tính năng, giao diện cốt lõi cần thiết ra bên ngoài.
    *   *Ý nghĩa:* Giúp giảm thiểu độ phức tạp của hệ thống, người lập trình chỉ cần biết đối tượng làm gì mà không cần quan tâm nó làm điều đó như thế nào.
*   **Đóng gói (Encapsulation):**
    *   *Định nghĩa:* Nhóm các thuộc tính (dữ liệu) và phương thức (hành vi) liên quan vào chung một lớp (class). Che giấu trạng thái bên trong của đối tượng và chỉ cho phép truy cập qua các phương thức công khai (getter/setter).
    *   *Ý nghĩa:* Bảo vệ dữ liệu khỏi các tác động hoặc thay đổi không mong muốn từ bên ngoài, đảm bảo tính toàn vẹn của đối tượng.
*   **Kế thừa (Inheritance):**
    *   *Định nghĩa:* Cho phép một lớp mới (lớp con) thừa hưởng và sử dụng lại các thuộc tính, phương thức của một lớp đã có (lớp cha).
    *   *Ý nghĩa:* Tăng khả năng tái sử dụng mã nguồn, loại bỏ code dư thừa, dễ dàng mở rộng và bảo trì hệ thống.
*   **Đa hình (Polymorphism):**
    *   *Định nghĩa:* Khả năng của một hành động hoặc phương thức có thể thực hiện theo nhiều cách khác nhau tùy thuộc vào đối tượng đang gọi nó (thường thông qua Nạp chồng - Overloading và Ghi đè - Overriding).
    *   *Ý nghĩa:* Tăng tính linh hoạt và mở rộng của chương trình, cho phép một giao diện xử lý được nhiều kiểu dữ liệu hoặc đối tượng khác nhau.

## 2. Chuẩn lập trình (Coding Convention)
*   **Định nghĩa:** Là tập hợp các quy tắc và tiêu chuẩn chung về cách viết mã nguồn (cách đặt tên biến, tên hàm, cấu trúc thụt lề, comment...) mà toàn bộ đội ngũ phát triển phải tuân thủ.
*   **Lợi ích:**
    *   Giúp mã nguồn đồng nhất như thể chỉ do một người viết.
    *   Tăng tính dễ đọc, dễ hiểu, giúp người mới nhanh chóng nắm bắt dự án.
    *   Hỗ trợ quá trình Code Review nhanh chóng, giảm thiểu lỗi tiềm ẩn và dễ dàng bảo trì sau này.

## 3. Clean Code (Mã nguồn sạch)
*   **Định nghĩa:** Là mã nguồn được tổ chức và viết một cách mạch lạc, rõ ràng, dễ đọc, dễ hiểu và dễ bảo trì đối với con người (lập trình viên), chứ không chỉ dành cho máy tính.
*   **Nguyên tắc viết:**
    *   Tên biến, hàm, lớp phải có ý nghĩa và tự giải thích được chức năng.
    *   **Nguyên lý Trách nhiệm đơn lẻ:** Mỗi hàm/lớp chỉ làm một việc duy nhất và làm thật tốt việc đó. Hàm phải giữ kích thước nhỏ gọn.
    *   **Hạn chế tham số:** Một hàm nên có càng ít tham số càng tốt (lý tưởng là không có, hoặc 1-2 tham số).
    *   **DRY (Don't Repeat Yourself):** Không lặp lại code. Nếu có logic trùng lặp, hãy tách thành hàm dùng chung.
    *   Chỉ dùng Comment để giải thích ngữ cảnh "tại sao lại code như vậy", không dùng Comment để giải thích "đoạn code này làm gì" (vì code tốt phải tự giải thích được nó làm gì).

## 4. Refactoring (Tái cấu trúc mã nguồn)
*   **Khái niệm:** Là quá trình tinh chỉnh, cải thiện cấu trúc bên trong của mã nguồn để code sạch hơn, tối ưu hơn mà không thay đổi chức năng.
*   **Quy tắc vàng:** TUYỆT ĐỐI không làm thay đổi chức năng hay hành vi đầu ra/đầu vào của hệ thống hiện tại. Nếu sau khi Refactoring mà app chạy sai kết quả cũ thì đó là làm hỏng code.
*   **Khi nào cần làm:**
    *   Khi phát hiện code có vấn đề, lộn xộn, lặp lại nhiều (Code Smell).
    *   Thực hiện trước khi thêm một tính năng mới để việc thêm mới dễ dàng hơn.
    *   Thực hiện sau khi sửa lỗi (bug) để dọn dẹp lại cấu trúc.

## 5. Nguyên lý SOLID
Bộ 5 nguyên lý thiết kế phần mềm linh hoạt, dễ bảo trì:
*   **S - Single Responsibility Principle (Trách nhiệm đơn lẻ):** Mỗi lớp chỉ nên đảm nhận một trách nhiệm duy nhất (chỉ có một lý do để thay đổi).
*   **O - Open/Closed Principle (Đóng/Mở):** Mã nguồn phải *mở* để dễ dàng mở rộng thêm tính năng, nhưng *đóng* đối với việc sửa đổi trực tiếp vào code cũ đã chạy ổn định.
*   **L - Liskov Substitution Principle (Thay thế Liskov):** Các đối tượng của lớp con phải có khả năng thay thế hoàn toàn các đối tượng của lớp cha mà không làm sai lệch tính đúng đắn của chương trình.
*   **I - Interface Segregation Principle (Phân tách Interface):** Không nên ép một lớp phải thực thi các phương thức/interface mà nó không cần dùng đến. Nên chia nhỏ interface lớn thành nhiều interface nhỏ đặc thù.
*   **D - Dependency Inversion Principle (Đảo ngược phụ thuộc):** Các module cấp cao không được phụ thuộc trực tiếp vào các module cấp thấp. Cả hai phải phụ thuộc vào những sự trừu tượng (Interface/Abstract Class).

## 6. Quản lý phiên bản (Version Control System) - Git
Git giúp theo dõi, lưu trữ các phiên bản của mã nguồn và phối hợp làm việc nhóm.
*   **Commit:** Lưu lại một cột mốc (điểm xét duyệt) ghi nhận các thay đổi hiện tại của mã nguồn trên máy cá nhân (Local Repository).
*   **Push:** Đẩy các thay đổi (commit) từ máy tính cá nhân lên máy chủ chung (Remote Repository, vd: GitHub/GitLab).
*   **Pull:** Lấy và cập nhật mã nguồn mới nhất từ máy chủ chung về máy tính cá nhân.
*   **Merge:** Gộp (trộn) các thay đổi từ một nhánh này sang một nhánh khác.
*   **Branching (Phân nhánh):** Tạo ra một luồng làm việc độc lập song song với luồng chính (main). Thường dùng để phát triển tính năng mới hoặc sửa lỗi mà không làm ảnh hưởng đến nhánh chính.
*   **Tránh xung đột code (Conflict):**
    *   Luôn `Pull` code mới nhất về trước khi bắt đầu code.
    *   Mỗi người làm việc trên một nhánh (Branch) riêng biệt.
    *   Giao tiếp tốt trong nhóm, tránh nhiều người cùng sửa chung một file tại cùng một thời điểm.

## 7. CI/CD (Continuous Integration / Continuous Deployment)
*   **CI (Tích hợp liên tục - Continuous Integration):** Là quy trình tự động hóa việc gộp mã nguồn của các lập trình viên vào kho lưu trữ chung một cách thường xuyên. Mỗi lần gộp sẽ tự động chạy quy trình Build và Test để phát hiện lỗi ngay lập tức, đảm bảo code luôn chạy đúng.
*   **CD (Triển khai liên tục - Continuous Deployment / Delivery):** Là bước tiếp theo của CI. Sau khi mã nguồn vượt qua tất cả các khâu kiểm thử tự động (Test), nó sẽ được tự động triển khai (Deploy) đưa lên môi trường thực tế (Production/Staging) một cách nhanh chóng và an toàn.
