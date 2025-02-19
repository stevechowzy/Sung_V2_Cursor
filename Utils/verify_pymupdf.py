try:
    import fitz
    print(f"✅ PyMuPDF {fitz.__doc__.split()[1]} 已正确安装")
    print(f"库文件路径：{fitz.__file__}")
except ImportError:
    print("❌ PyMuPDF未安装")
    print("解决方案：")
    print("1. 运行 pip install PyMuPDF")
    print("2. 检查Python环境路径") 