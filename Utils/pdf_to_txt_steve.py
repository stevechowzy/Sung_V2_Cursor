import pdfplumber
import os
from tqdm import tqdm

def convert_pdf_to_txt(pdf_path, txt_path):
    """PDF转TXT核心函数（增强版）"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            print(f"📄 总页数：{len(pdf.pages)}")
            
            # 带进度条的页面处理
            for page in tqdm(pdf.pages, desc="转换进度", unit="页"):
                # 增强文本提取逻辑
                text = page.extract_text(x_tolerance=1, y_tolerance=1)
                
                if text:
                    # 添加分页标记
                    full_text += f"\n\n=== 第 {page.page_number} 页 ===\n{text}"
            
            # 自动创建目标目录
            os.makedirs(os.path.dirname(txt_path), exist_ok=True)
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(full_text)
            print(f"\n✅ 转换成功！文件保存至：{os.path.abspath(txt_path)}")
            
    except Exception as e:
        print(f"\n❌ 转换失败：{str(e)}")
        print("🔼 可能原因：1.文件被加密 2.非文本型PDF 3.路径包含特殊字符")

if __name__ == "__main__":
    # 路径配置（适配项目结构）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pdf_path = os.path.join(project_root, "LibrarySong", "宋代中国的改革：王安石及其新政.pdf")
    txt_path = os.path.join(project_root, "LibrarySong", "newlaw_WangAS_Song.txt")
    
    # 自动安装依赖
    try:
        from tqdm import tqdm
    except ImportError:
        print("🔧 正在安装必要依赖...")
        os.system("pip install tqdm pdfplumber")
        from tqdm import tqdm
    
    convert_pdf_to_txt(pdf_path, txt_path) 