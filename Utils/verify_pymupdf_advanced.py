import sys

try:
    import fitz
    print("[Success] PyMuPDF 已正确安装")
    print(f"Python 版本: {sys.version}")
    print(f"PyMuPDF 版本: {fitz.__doc__.split()[1]}")
    print(f"库文件路径: {fitz.__file__}")
except ImportError:
    print("[Error] 安装异常，请检查：")
    print("1. 当前Python路径:", sys.executable)
    print("2. 环境变量PATH:", sys.path)
    print("\n修复建议：")
    print("使用完整路径安装 ->")
    print(f"{sys.executable} -m pip install PyMuPDF") 