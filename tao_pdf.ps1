# Script tạo file HTML tự chứa từ Markdown để in PDF
# Cách dùng: Click phải -> Run with PowerShell
# Hoặc mở PowerShell tại thư mục KNPM rồi chạy: .\tao_pdf.ps1

$mdFile = Join-Path $PSScriptRoot "Tong_Hop_Tai_Lieu_KNPM_Toan_Dien_Full.md"
$htmlFile = Join-Path $PSScriptRoot "KNPM_Print_PDF.html"

Write-Host "Dang doc file Markdown..." -ForegroundColor Cyan
$mdContent = Get-Content $mdFile -Raw -Encoding UTF8

# Escape cho JavaScript (thay \ thành \\, thay ` thành \`, thay $ thành \$, v.v.)
$escaped = $mdContent -replace '\\', '\\\\' 
$escaped = $escaped -replace '`', '\`'
$escaped = $escaped -replace '\$', '\$'

$html = @"
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tong Hop Tai Lieu KNPM - PDF Ready</title>
    <script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"><\/script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"><\/script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', 'Noto Sans', Arial, sans-serif;
            font-size: 13px; line-height: 1.6; color: #1a1a2e;
            background: #fff; padding: 20px 30px;
            max-width: 210mm; margin: 0 auto;
        }
        h1 { font-size: 22px; color: #0d1b2a; text-align: center; border-bottom: 3px solid #1b4965; padding-bottom: 8px; margin-bottom: 6px; page-break-after: avoid; }
        h2 { font-size: 17px; color: #1b4965; border-bottom: 2px solid #62b6cb; padding-bottom: 4px; margin-top: 18px; margin-bottom: 8px; page-break-after: avoid; }
        h3 { font-size: 15px; color: #274c77; margin-top: 14px; margin-bottom: 6px; page-break-after: avoid; }
        h4 { font-size: 13.5px; color: #3a6ea5; margin-top: 10px; margin-bottom: 4px; page-break-after: avoid; }
        p { margin-bottom: 6px; text-align: justify; }
        em { color: #555; } strong { color: #0d1b2a; }
        ul, ol { margin-left: 20px; margin-bottom: 6px; }
        li { margin-bottom: 3px; }
        table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 12px; page-break-inside: avoid; }
        th { background: #1b4965; color: #fff; padding: 6px 8px; text-align: left; font-weight: 600; }
        td { padding: 5px 8px; border: 1px solid #ccc; vertical-align: top; }
        tr:nth-child(even) td { background: #f0f4f8; }
        code { background: #e8eef3; padding: 1px 4px; border-radius: 3px; font-family: Consolas, monospace; font-size: 12px; color: #c7254e; }
        pre { background: #f5f7fa; border: 1px solid #d0d7de; border-left: 4px solid #1b4965; padding: 10px 14px; margin: 8px 0; overflow-x: auto; border-radius: 4px; page-break-inside: avoid; font-size: 11.5px; line-height: 1.5; }
        pre code { background: none; padding: 0; color: #24292f; }
        .mermaid { text-align: center; margin: 10px 0; page-break-inside: avoid; }
        .mermaid svg { max-width: 100%; height: auto; }
        hr { border: none; border-top: 2px solid #bee3f8; margin: 16px 0; }
        blockquote { border-left: 4px solid #62b6cb; padding: 6px 14px; margin: 8px 0; background: #f0f9ff; color: #333; }
        @media print {
            body { padding: 0; margin: 0; font-size: 11.5px; line-height: 1.55; max-width: none; }
            h1 { font-size: 18px; margin-top: 0; } h2 { font-size: 15px; margin-top: 14px; }
            h3 { font-size: 13px; } h4 { font-size: 12px; }
            pre { font-size: 10px; padding: 6px 10px; }
            table { font-size: 10.5px; } th { padding: 4px 6px; } td { padding: 3px 6px; }
            .mermaid svg { max-height: 280px; }
            h1, h2, h3, h4 { page-break-after: avoid; }
            table, pre, .mermaid { page-break-inside: avoid; }
            p { orphans: 3; widows: 3; }
            .no-print { display: none !important; }
            @page { size: A4; margin: 12mm 15mm; }
        }
        .print-btn { position: fixed; top: 20px; right: 20px; z-index: 9999; background: linear-gradient(135deg, #1b4965, #3a6ea5); color: #fff; border: none; padding: 12px 28px; font-size: 16px; font-weight: 700; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 15px rgba(27,73,101,0.4); }
        .print-btn:hover { background: linear-gradient(135deg, #3a6ea5, #62b6cb); transform: translateY(-2px); }
        #loading { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 99999; font-size: 18px; color: #1b4965; }
        .spinner { width: 50px; height: 50px; border: 4px solid #e0e0e0; border-top: 4px solid #1b4965; border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 16px; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div id="loading"><div class="spinner"></div><p>Dang render tai lieu & so do Mermaid...</p></div>
    <button class="print-btn no-print" onclick="window.print()">In PDF (Ctrl+P)</button>
    <div id="content"></div>
    <script>
    const mdRaw = document.getElementById('md-source').textContent;
    const md = window.markdownit({ html: true, breaks: true, typographer: true });
    
    // Tach mermaid blocks
    let mermaidIdx = 0;
    let processed = mdRaw.replace(/\x60\x60\x60mermaid\s*\n([\s\S]*?)\x60\x60\x60/g, function(m, code) {
        return '<div class="mermaid">' + code.trim() + '</div>';
    });
    
    document.getElementById('content').innerHTML = md.render(processed);
    
    mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose', fontSize: 12 });
    mermaid.run().then(function() {
        document.getElementById('loading').style.display = 'none';
    }).catch(function() {
        document.getElementById('loading').style.display = 'none';
    });
    <\/script>
    <script id="md-source" type="text/plain">
$($mdContent)
    <\/script>
</body>
</html>
"@

Write-Host "Dang ghi file HTML..." -ForegroundColor Cyan
[System.IO.File]::WriteAllText($htmlFile, $html, [System.Text.Encoding]::UTF8)

Write-Host ""
Write-Host "=== HOAN THANH ===" -ForegroundColor Green
Write-Host "File HTML da tao tai: $htmlFile" -ForegroundColor Yellow
Write-Host ""
Write-Host "HUONG DAN:" -ForegroundColor Cyan
Write-Host "1. Double-click mo file 'KNPM_Print_PDF.html' trong trinh duyet"
Write-Host "2. Doi Mermaid render xong (vai giay)"
Write-Host "3. Nhan Ctrl+P de in thanh PDF"
Write-Host "4. Chon 'Save as PDF' va nhan Save"
Write-Host ""

# Tự động mở file
Start-Process $htmlFile

Write-Host "Da tu dong mo file trong trinh duyet!" -ForegroundColor Green
