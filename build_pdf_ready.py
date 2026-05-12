# Script tạo file HTML chứa toàn bộ nội dung Markdown embedded trực tiếp
# Không cần XHR/fetch - hoạt động mọi nơi kể cả file://
import json
import os

MD_FILE = 'Tong_Hop_Tai_Lieu_KNPM_Toan_Dien_Full.md'
OUTPUT_HTML = 'KNPM_PDF_Ready.html'

# Đọc file Markdown
with open(MD_FILE, 'r', encoding='utf-8-sig') as f:
    md_content = f.read()

# Escape nội dung để nhúng an toàn vào JavaScript
md_json = json.dumps(md_content)

html_template = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tổng Hợp Tài Liệu KNPM Toàn Diện - PDF Ready</title>
    <script src="https://cdn.jsdelivr.net/npm/markdown-it@14.1.0/dist/markdown-it.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        /* === RESET & BASE === */
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', 'Noto Sans', Arial, sans-serif;
            font-size: 12.5px;
            line-height: 1.55;
            color: #1a1a2e;
            background: #fff;
            padding: 15px 22px;
            max-width: 210mm;
            margin: 0 auto;
        }}

        /* === HEADINGS === */
        h1 {{
            font-size: 19px; color: #0d1b2a;
            text-align: center;
            border-bottom: 3px solid #1b4965;
            padding-bottom: 6px;
            margin-bottom: 8px;
            margin-top: 10px;
            page-break-after: avoid;
        }}
        h2 {{
            font-size: 15px; color: #1b4965;
            border-bottom: 2px solid #62b6cb;
            padding-bottom: 3px;
            margin-top: 14px; margin-bottom: 6px;
            page-break-after: avoid;
        }}
        h3 {{
            font-size: 13.5px; color: #274c77;
            margin-top: 10px; margin-bottom: 4px;
            page-break-after: avoid;
        }}
        h4 {{
            font-size: 12.5px; color: #3a6ea5;
            margin-top: 8px; margin-bottom: 3px;
            page-break-after: avoid;
        }}

        /* === TEXT === */
        p {{ margin-bottom: 4px; text-align: justify; }}
        em {{ color: #555; }}
        strong {{ color: #0d1b2a; }}
        ul, ol {{ margin-left: 18px; margin-bottom: 4px; }}
        li {{ margin-bottom: 2px; }}
        li > ul, li > ol {{ margin-top: 1px; margin-bottom: 1px; }}

        /* === TABLE === */
        table {{
            width: 100%; border-collapse: collapse;
            margin: 6px 0; font-size: 11px;
            page-break-inside: avoid;
        }}
        th {{
            background: #1b4965; color: #fff;
            padding: 4px 6px; text-align: left;
            font-weight: 600; font-size: 10.5px;
        }}
        td {{
            padding: 3px 6px; border: 1px solid #ccc;
            vertical-align: top;
        }}
        tr:nth-child(even) td {{ background: #f0f4f8; }}

        /* === CODE === */
        code {{
            background: #e8eef3; padding: 1px 3px;
            border-radius: 2px;
            font-family: Consolas, 'Courier New', monospace;
            font-size: 11px; color: #c7254e;
        }}
        pre {{
            background: #f5f7fa;
            border: 1px solid #d0d7de;
            border-left: 3px solid #1b4965;
            padding: 6px 10px;
            margin: 5px 0;
            overflow-x: auto;
            border-radius: 3px;
            page-break-inside: avoid;
            font-size: 10.5px; line-height: 1.45;
        }}
        pre code {{
            background: none; padding: 0;
            color: #24292f; font-size: 10.5px;
        }}

        /* === MERMAID === */
        .mermaid {{
            text-align: center;
            margin: 6px 0;
            page-break-inside: avoid;
        }}
        .mermaid svg {{ max-width: 100%; height: auto; }}
        .mermaid-error {{
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 4px;
            padding: 8px 12px;
            margin: 5px 0;
            font-size: 11px;
            color: #856404;
            page-break-inside: avoid;
        }}
        .mermaid-error strong {{ color: #856404; }}

        /* === MISC === */
        hr {{ border: none; border-top: 1.5px solid #bee3f8; margin: 12px 0; }}
        blockquote {{
            border-left: 3px solid #62b6cb;
            padding: 4px 10px;
            margin: 5px 0;
            background: #f0f9ff;
            color: #333;
            font-size: 11.5px;
        }}

        /* === PRINT === */
        @media print {{
            body {{
                padding: 0; margin: 0;
                font-size: 10.5px; line-height: 1.45;
                max-width: none;
            }}
            h1 {{ font-size: 15px; margin-top: 0; }}
            h2 {{ font-size: 13px; margin-top: 10px; }}
            h3 {{ font-size: 11.5px; margin-top: 8px; }}
            h4 {{ font-size: 10.5px; }}
            p {{ margin-bottom: 3px; }}
            ul, ol {{ margin-left: 15px; margin-bottom: 3px; }}
            li {{ margin-bottom: 1px; }}
            pre {{ font-size: 9px; padding: 4px 6px; line-height: 1.35; }}
            table {{ font-size: 9px; }}
            th {{ padding: 2px 4px; font-size: 9px; }}
            td {{ padding: 2px 4px; }}
            .mermaid svg {{ max-height: 200px; }}
            h1, h2, h3, h4 {{ page-break-after: avoid; }}
            table, pre, .mermaid {{ page-break-inside: avoid; }}
            p {{ orphans: 3; widows: 3; }}
            .no-print {{ display: none !important; }}
            @page {{ size: A4; margin: 8mm 10mm; }}
            hr {{ margin: 8px 0; }}
        }}

        /* === TOOLBAR === */
        .toolbar {{
            position: fixed; top: 0; left: 0; right: 0;
            background: linear-gradient(135deg, #1b4965, #3a6ea5);
            color: #fff;
            padding: 8px 20px;
            display: flex; align-items: center; justify-content: space-between;
            z-index: 9999;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }}
        .toolbar span {{ font-size: 13px; font-weight: 600; }}
        .toolbar button {{
            background: #fff; color: #1b4965;
            border: none; padding: 6px 20px;
            font-size: 13px; font-weight: 700;
            border-radius: 5px; cursor: pointer;
            margin-left: 8px;
        }}
        .toolbar button:hover {{ background: #bee3f8; }}
        #content {{ margin-top: 45px; }}

        /* === LOADING === */
        #loading {{
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: #fff;
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            z-index: 99999;
            font-size: 16px; color: #1b4965;
        }}
        .spinner {{
            width: 40px; height: 40px;
            border: 3px solid #e0e0e0;
            border-top: 3px solid #1b4965;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-bottom: 12px;
        }}
        @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <div id="loading"><div class="spinner"></div><p>Đang render tài liệu & sơ đồ Mermaid...</p></div>
    <div class="toolbar no-print">
        <span>📄 Tổng Hợp Tài Liệu KNPM Toàn Diện</span>
        <div>
            <button onclick="window.print()">🖨️ In PDF (Ctrl+P)</button>
        </div>
    </div>
    <div id="content"></div>

    <script>
    // Nội dung Markdown được nhúng trực tiếp (không cần XHR/fetch)
    var RAW_MD = {md_json};

    (function() {{
        // Tách mermaid blocks trước khi render markdown
        var mermaidBlocks = [];
        var processed = RAW_MD.replace(/```mermaid\\s*\\n([\\s\\S]*?)```/g, function(match, code) {{
            var id = 'mermaid-block-' + mermaidBlocks.length;
            mermaidBlocks.push({{ id: id, code: code.trim() }});
            return '\\n<div class="mermaid" id="' + id + '">' + code.trim() + '</div>\\n';
        }});

        // Render Markdown
        var md = window.markdownit({{ html: true, breaks: true, typographer: true }});
        document.getElementById('content').innerHTML = md.render(processed);

        // Khởi tạo Mermaid
        mermaid.initialize({{
            startOnLoad: false,
            theme: 'default',
            securityLevel: 'loose',
            fontSize: 11,
            flowchart: {{ useMaxWidth: true, htmlLabels: true }},
            sequence: {{ useMaxWidth: true }},
            er: {{ useMaxWidth: true }}
        }});

        // Render Mermaid với xử lý lỗi cho từng block
        setTimeout(function() {{
            var mermaidDivs = document.querySelectorAll('.mermaid');
            var total = mermaidDivs.length;
            var done = 0;

            if (total === 0) {{
                document.getElementById('loading').style.display = 'none';
                return;
            }}

            // Thử render từng block riêng lẻ
            mermaidDivs.forEach(function(div, index) {{
                try {{
                    var code = div.textContent.trim();
                    // Kiểm tra xem mermaid có hỗ trợ loại diagram này không
                    // usecaseDiagram không được mermaid hỗ trợ, chuyển thành mô tả text
                    if (code.startsWith('usecaseDiagram')) {{
                        div.className = 'mermaid-error';
                        div.innerHTML = '<strong>📊 Sơ đồ Use-case</strong><br><em>(Mermaid không hỗ trợ usecaseDiagram - Vẽ tay trên giấy thi)</em><br><pre style="text-align:left;font-size:10px;margin-top:4px;background:#fff8e1;border:none;border-left:3px solid #ffc107;padding:4px 8px;">' + code.replace(/</g,'&lt;') + '</pre>';
                        done++;
                        if (done >= total) document.getElementById('loading').style.display = 'none';
                        return;
                    }}
                }} catch(e) {{}}

                // Thử render bằng mermaid
                try {{
                    mermaid.render('mermaid-svg-' + index, div.textContent.trim()).then(function(result) {{
                        div.innerHTML = result.svg;
                        done++;
                        if (done >= total) document.getElementById('loading').style.display = 'none';
                    }}).catch(function(err) {{
                        console.warn('Mermaid render error for block ' + index + ':', err);
                        var origCode = div.textContent.trim();
                        div.className = 'mermaid-error';
                        div.innerHTML = '<strong>📊 Sơ đồ</strong> <em>(Render lỗi - xem code bên dưới)</em><br><pre style="text-align:left;font-size:10px;margin-top:4px;background:#fff8e1;border:none;border-left:3px solid #ffc107;padding:4px 8px;">' + origCode.replace(/</g,'&lt;') + '</pre>';
                        done++;
                        if (done >= total) document.getElementById('loading').style.display = 'none';
                    }});
                }} catch(e) {{
                    console.warn('Mermaid error:', e);
                    var origCode = div.textContent.trim();
                    div.className = 'mermaid-error';
                    div.innerHTML = '<strong>📊 Sơ đồ</strong> <em>(Render lỗi)</em><br><pre style="text-align:left;font-size:10px;margin-top:4px;">' + origCode.replace(/</g,'&lt;') + '</pre>';
                    done++;
                    if (done >= total) document.getElementById('loading').style.display = 'none';
                }}
            }});

            // Fallback timeout - đảm bảo loading biến mất
            setTimeout(function() {{
                document.getElementById('loading').style.display = 'none';
            }}, 15000);
        }}, 800);
    }})();
    </script>
</body>
</html>'''

# Ghi file output
with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f'Da tao: {OUTPUT_HTML}')
print(f'Kich thuoc MD: {len(md_content):,} bytes')
print(f'Kich thuoc HTML: {os.path.getsize(OUTPUT_HTML):,} bytes')
print(f'So mermaid blocks: {md_content.count("```mermaid")}')
