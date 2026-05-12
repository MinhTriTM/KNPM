$files = "Bo_De_Thi_KNPM_Toan_Dien.md", "Phan_1_Ly_Thuyet_Tu_Luan.md", "Phan_2_Bai_Tap_Tu_Luan.md", "Ngan_Hang_Chi_Tiet_Phan_1_Cau_1_50.md", "Ngan_Hang_Chi_Tiet_Phan_1_Cau_1_80.md", "Ngan_Hang_Chi_Tiet_Phan_1_Va_2_Cau_1_100.md", "Danh_Sach_De_Thi_KNPM.md", "Ngan_Hang_Cau_Hoi_Phan_2.md", "Ngan_Hang_100_Cau_Hoi_KNPM.md"
Clear-Content "Tong_Hop_Tai_Lieu_KNPM_Full.md" -ErrorAction SilentlyContinue
foreach ($file in $files) {
    if (Test-Path $file) {
        Add-Content -Path "Tong_Hop_Tai_Lieu_KNPM_Full.md" -Value "`n# --- Nội dung file: $file ---`n" -Encoding UTF8
        Get-Content $file -Raw -Encoding UTF8 | Add-Content -Path "Tong_Hop_Tai_Lieu_KNPM_Full.md" -Encoding UTF8
    } else {
        Write-Host "File $file not found!"
    }
}