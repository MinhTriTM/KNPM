# Script PowerShell: Build file HTML tự chứa V2
# KHÔNG dùng Mermaid render (tránh bị treo) - chuyển tất cả thành code block đẹp
# Đảm bảo 100% nội dung được hiển thị

$mdPath = Join-Path $PSScriptRoot "Tong_Hop_Tai_Lieu_KNPM_Toan_Dien_Full.md"
$outPath = Join-Path $PSScriptRoot "KNPM_PDF_Ready.html"

Write-Host "=== BUILD HTML TU CHUA V2 ===" -ForegroundColor Green
Write-Host "Dang doc file markdown..." -ForegroundColor Cyan
$mdContent = Get-Content $mdPath -Raw -Encoding UTF8

# Convert sang base64
$bytes = [System.Text.Encoding]::UTF8.GetBytes($mdContent)
$base64 = [Convert]::ToBase64String($bytes)
Write-Host "Markdown: $($mdContent.Length) bytes -> Base64: $($base64.Length) bytes" -ForegroundColor Yellow

$html = @"
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tổng Hợp Tài Liệu KNPM Toàn Diện - PDF Ready</title>
    <script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"><\/script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', 'Noto Sans', Arial, sans-serif;
            font-size: 13px; line-height: 1.6; color: #1a1a2e;
            background: #fff; padding: 18px 25px;
            max-width: 210mm; margin: 0 auto;
        }
        h1 { font-size: 20px; color: #0d1b2a; text-align: center; border-bottom: 3px solid #1b4965; padding-bottom: 8px; margin-bottom: 10px; margin-top: 12px; page-break-after: avoid; }
        h2 { font-size: 16px; color: #1b4965; border-bottom: 2px solid #62b6cb; padding-bottom: 4px; margin-top: 18px; margin-bottom: 8px; page-break-after: avoid; }
        h3 { font-size: 14px; color: #274c77; margin-top: 12px; margin-bottom: 5px; page-break-after: avoid; }
        h4 { font-size: 13px; color: #3a6ea5; margin-top: 9px; margin-bottom: 4px; page-break-after: avoid; }
        p { margin-bottom: 5px; text-align: justify; }
        em { color: #555; } strong { color: #0d1b2a; }
        ul, ol { margin-left: 20px; margin-bottom: 5px; }
        li { margin-bottom: 2px; }
        li > ul, li > ol { margin-top: 1px; margin-bottom: 1px; }
        table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 11.5px; page-break-inside: avoid; }
        th { background: #1b4965; color: #fff; padding: 5px 7px; text-align: left; font-weight: 600; }
        td { padding: 4px 7px; border: 1px solid #ccc; vertical-align: top; }
        tr:nth-child(even) td { background: #f0f4f8; }
        code { background: #e8eef3; padding: 1px 4px; border-radius: 3px; font-family: Consolas, monospace; font-size: 11.5px; color: #c7254e; }
        pre { background: #f5f7fa; border: 1px solid #d0d7de; border-left: 4px solid #1b4965; padding: 8px 12px; margin: 6px 0; overflow-x: auto; border-radius: 4px; page-break-inside: avoid; font-size: 11px; line-height: 1.45; }
        pre code { background: none; padding: 0; color: #24292f; font-size: 11px; }
        hr { border: none; border-top: 2px solid #bee3f8; margin: 15px 0; }
        blockquote { border-left: 4px solid #62b6cb; padding: 6px 14px; margin: 8px 0; background: #f0f9ff; color: #333; font-size: 12.5px; }

        /* Sơ đồ Mermaid fallback - hiển thị code đẹp */
        .diagram-box { background: #f8f9fa; border: 1px solid #dee2e6; border-left: 4px solid #3a6ea5; border-radius: 5px; padding: 10px 14px; margin: 8px 0; page-break-inside: avoid; }
        .diagram-box .diagram-title { font-weight: 700; color: #1b4965; font-size: 12px; margin-bottom: 5px; }
        .diagram-box .diagram-note { font-size: 10.5px; color: #6c757d; font-style: italic; margin-bottom: 5px; }
        .diagram-box pre { background: #fff; border: none; border-left: 2px solid #adb5bd; padding: 5px 10px; margin: 0; font-size: 10px; line-height: 1.35; white-space: pre-wrap; word-break: break-word; }

        /* In ấn */
        @media print {
            body { padding: 0; margin: 0; font-size: 11px; line-height: 1.5; max-width: none; }
            h1 { font-size: 16px; margin-top: 0; }
            h2 { font-size: 13.5px; margin-top: 12px; }
            h3 { font-size: 12px; margin-top: 8px; }
            h4 { font-size: 11px; }
            p { margin-bottom: 3px; }
            ul, ol { margin-left: 16px; margin-bottom: 3px; }
            li { margin-bottom: 1px; }
            pre { font-size: 9px; padding: 4px 8px; }
            pre code { font-size: 9px; }
            table { font-size: 9.5px; }
            th { padding: 3px 5px; font-size: 9.5px; }
            td { padding: 2px 5px; }
            .diagram-box { padding: 6px 10px; }
            .diagram-box pre { font-size: 8.5px; }
            .diagram-box .diagram-title { font-size: 10.5px; }
            h1, h2, h3, h4 { page-break-after: avoid; }
            table, pre, .diagram-box { page-break-inside: avoid; }
            p { orphans: 3; widows: 3; }
            .no-print { display: none !important; }
            @page { size: A4; margin: 10mm 12mm; }
            hr { margin: 10px 0; }
        }

        /* Thanh công cụ */
        .toolbar { position: fixed; top: 0; left: 0; right: 0; background: linear-gradient(135deg, #1b4965, #3a6ea5); color: #fff; padding: 10px 20px; display: flex; align-items: center; justify-content: space-between; z-index: 9999; box-shadow: 0 2px 10px rgba(0,0,0,0.3); }
        .toolbar span { font-size: 14px; font-weight: 600; }
        .toolbar .info { font-size: 11px; opacity: 0.8; margin-top: 2px; }
        .toolbar button { background: #fff; color: #1b4965; border: none; padding: 8px 24px; font-size: 14px; font-weight: 700; border-radius: 6px; cursor: pointer; }
        .toolbar button:hover { background: #bee3f8; }
        #content { margin-top: 55px; }
    </style>
</head>
<body>
    <div class="toolbar no-print">
        <div>
            <span>📄 Tổng Hợp Tài Liệu KNPM Toàn Diện</span>
            <div class="info" id="toolbar-info">Đang render...</div>
        </div>
        <div><button onclick="window.print()">🖨️ In PDF (Ctrl+P)</button></div>
    </div>
    <div id="content"></div>
    <script>
    // Nội dung Markdown nhúng trực tiếp dạng Base64 - KHÔNG cần fetch/XHR
    var MD_BASE64 = "$base64";

    function b64DecodeUnicode(str) {
        return decodeURIComponent(atob(str).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));
    }

    function getDiagramTitle(code) {
        var fl = code.split('\n')[0].trim();
        if (fl.startsWith('usecaseDiagram')) return '📊 Sơ đồ Use-case (Usecase Diagram)';
        if (fl.startsWith('classDiagram')) return '📐 Sơ đồ Lớp (Class Diagram)';
        if (fl.startsWith('erDiagram')) return '🗄️ Sơ đồ ER (Entity Relationship Diagram)';
        if (fl.startsWith('sequenceDiagram')) return '🔄 Sơ đồ Tuần tự (Sequence Diagram)';
        if (fl.startsWith('flowchart') || fl.startsWith('graph')) return '📋 Sơ đồ Luồng (Flowchart)';
        if (fl.startsWith('stateDiagram')) return '🔲 Sơ đồ Trạng thái (State Diagram)';
        return '📊 Sơ đồ';
    }

    (function() {
        // Giải mã Base64 -> Markdown text
        var raw = b64DecodeUnicode(MD_BASE64);

        // Thay thế tất cả ```mermaid blocks thành diagram-box HTML
        // KHÔNG dùng Mermaid.js render để tránh bị treo/lỗi
        var diagramCount = 0;
        var processed = raw.replace(/\`\`\`mermaid\s*\n([\s\S]*?)\`\`\`/g, function(match, code) {
            diagramCount++;
            var title = getDiagramTitle(code.trim());
            var escapedCode = code.trim()
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');
            return '\n<div class="diagram-box"><div class="diagram-title">' + title + '</div>' +
                '<div class="diagram-note">⚠️ Sơ đồ mô tả bằng code UML - Vẽ tay trên giấy thi</div>' +
                '<pre><code>' + escapedCode + '</code></pre></div>\n';
        });

        // Render Markdown bằng markdown-it
        var md = window.markdownit({ html: true, breaks: true, typographer: true });
        document.getElementById('content').innerHTML = md.render(processed);

        // Cập nhật thông tin toolbar
        document.getElementById('toolbar-info').textContent =
            (raw.length / 1024).toFixed(0) + 'KB | ' + diagramCount + ' sơ đồ | Sẵn sàng in PDF';
    })();
    <\/script>
</body>
</html>
"@

Write-Host "Dang ghi file HTML..." -ForegroundColor Cyan
[System.IO.File]::WriteAllText($outPath, $html, [System.Text.Encoding]::UTF8)

$size = (Get-Item $outPath).Length
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "HOAN TAT!" -ForegroundColor Green
Write-Host "File: $outPath" -ForegroundColor Yellow
Write-Host "Kich thuoc: $([math]::Round($size / 1024))KB" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Mo file bang trinh duyet -> Nhan Ctrl+P de in PDF" -ForegroundColor Cyan
Write-Host "QUAN TRONG: Doi 2-3 giay de trang load xong truoc khi in!" -ForegroundColor Yellow

# Mở file trong trình duyệt
Start-Process $outPath
