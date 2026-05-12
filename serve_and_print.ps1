# Script khởi chạy local server và mở trình duyệt để xem + in PDF
# Cách dùng: Click phải -> Run with PowerShell
# Hoặc mở PowerShell rồi chạy: .\serve_and_print.ps1

$port = 8080
$dir = $PSScriptRoot

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  KNPM Markdown -> PDF Converter" -ForegroundColor White
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Dang khoi chay web server tai cong $port..." -ForegroundColor Yellow
Write-Host "Thu muc: $dir" -ForegroundColor Gray
Write-Host ""

# Mở trình duyệt sau 2 giây
$job = Start-Job -ScriptBlock {
    Start-Sleep -Seconds 2
    Start-Process "http://localhost:$using:port/md_to_pdf.html"
}

Write-Host "Trinh duyet se tu dong mo sau 2 giay..." -ForegroundColor Green
Write-Host ""
Write-Host "HUONG DAN:" -ForegroundColor Cyan
Write-Host "  1. Doi trang web load xong (mermaid diagrams render)" -ForegroundColor White
Write-Host "  2. Nhan Ctrl+P (hoac nut 'In PDF' tren trang)" -ForegroundColor White
Write-Host "  3. Chon 'Save as PDF' -> Save" -ForegroundColor White
Write-Host ""
Write-Host "Nhan Ctrl+C de dung server khi xong." -ForegroundColor Red
Write-Host ""

# Chạy Python HTTP server
Set-Location $dir
python -m http.server $port
