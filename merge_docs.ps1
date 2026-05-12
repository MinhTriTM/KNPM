$files = @(
    "D:\Download\Thi\KNPM\Bo_De_Thi_KNPM_Toan_Dien.md",
    "D:\Download\Thi\KNPM\Phan_1_Ly_Thuyet_Tu_Luan.md",
    "D:\Download\Thi\KNPM\Phan_2_Bai_Tap_Tu_Luan.md",
    "D:\Download\Thi\KNPM\Ngan_Hang_Chi_Tiet_Phan_1_Cau_1_50.md",
    "D:\Download\Thi\KNPM\Ngan_Hang_Chi_Tiet_Phan_1_Cau_1_80.md",
    "D:\Download\Thi\KNPM\Ngan_Hang_Chi_Tiet_Phan_1_Va_2_Cau_1_100.md",
    "D:\Download\Thi\KNPM\Danh_Sach_De_Thi_KNPM.md",
    "D:\Download\Thi\KNPM\Ngan_Hang_Cau_Hoi_Phan_2.md",
    "D:\Download\Thi\KNPM\Ngan_Hang_100_Cau_Hoi_KNPM.md"
)
$output = "D:\Download\Thi\KNPM\Tai_Lieu_On_Thi_KNPM_Tong_Hop.md"
Clear-Content $output -ErrorAction SilentlyContinue
foreach ($f in $files) {
    if (Test-Path $f) {
        $name = Split-Path $f -Leaf
        Add-Content $output "# =========================================" -Encoding UTF8
        Add-Content $output "# NỘI DUNG TỪ: $name" -Encoding UTF8
        Add-Content $output "# =========================================`n" -Encoding UTF8
        Get-Content $f -Encoding UTF8 | Add-Content $output -Encoding UTF8
        Add-Content $output "`n`n" -Encoding UTF8
    }
}
