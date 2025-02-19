from pdf2image import convert_from_path
import pytesseract
import os

def pdf_ocr(pdf_path, txt_path):
    """处理扫描版PDF"""
    try:
        images = convert_from_path(pdf_path)
        full_text = ""
        
        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img, lang='chi_sim')
            full_text += f"\n=== 第 {i+1} 页 ===\n{text}"
        
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"OCR转换完成：{txt_path}")
        
    except Exception as e:
        print(f"OCR失败：{str(e)}")

if __name__ == "__main__":
    pdf_path = "LibrarySong/扫描件.pdf"
    txt_path = "LibrarySong/扫描件文本.txt"
    pdf_ocr(pdf_path, txt_path) 