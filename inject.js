const fs = require('fs');
const mdFile = 'D:\\Download\\Thi\\KNPM\\Ngan_Hang_100_Cau_Hoi_KNPM.md';
const htmlFile = 'D:\\Download\\Thi\\KNPM\\Giao_Trinh_KNPM_Toc_Hanh_36h.html';

const mdContent = fs.readFileSync(mdFile, 'utf8');
const lines = mdContent.split('\n');

let htmlContent = [
    '<div class="page-break"></div>',
    '<h2>CHƯƠNG 7: NGÂN HÀNG 100 CÂU HỎI LÝ THUYẾT TRỌNG TÂM</h2>',
    '<div class="tip-box"><h4>💡 Mục tiêu:</h4><p>Học thuộc lòng 100 câu hỏi này để đảm bảo ăn trọn điểm phần lý thuyết (thường là 5 điểm) trong bài thi tự luận hoặc trắc nghiệm.</p></div>'
];

for (let line of lines) {
    line = line.trim();
    if (!line) continue;
    
    if (line.startsWith('## ')) {
        htmlContent.push('<h3>' + line.substring(3) + '</h3>');
    } else if (line.startsWith('**') && line.endsWith('**') && line.match(/^\*\*\d+\./)) {
        htmlContent.push('<p class="kw" style="margin-top: 15px;">' + line.replace(/\*\*/g, '') + '</p>');
    } else if (line.startsWith('=>')) {
        htmlContent.push('<p style="margin-left: 20px; border-left: 3px solid var(--secondary); padding-left: 10px;"><strong>Đáp án:</strong> ' + line.substring(2).trim() + '</p>');
    }
}

const htmlToInject = htmlContent.join('\n');
let content = fs.readFileSync(htmlFile, 'utf8');

const insertMarker = '<div style="text-align: center; margin-top: 60px; font-size: 1.2em; border-top: 2px solid var(--primary); padding-top: 20px;">';
if (content.includes(insertMarker)) {
    content = content.replace(insertMarker, htmlToInject + '\n\n' + insertMarker);
    fs.writeFileSync(htmlFile, content, 'utf8');
    console.log('Injection successful.');
} else {
    console.log('Marker not found.');
}
