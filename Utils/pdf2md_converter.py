# 示例：使用PyMuPDF提取章节
import pdfplumber

# 添加版本检查
print("PyMuPDF版本:", pdfplumber.__doc__.split()[1])

def extract_sections(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join([page.extract_text() for page in pdf.pages])
    return text 