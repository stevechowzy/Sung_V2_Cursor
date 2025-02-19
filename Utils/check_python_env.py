import sys
import subprocess

print("=== Python环境诊断 ===")
print(f"当前Python路径: {sys.executable}")
print(f"Python版本: {sys.version}")

try:
    import fitz
    print("✅ PyMuPDF已正确安装")
except ImportError:
    print("❌ PyMuPDF未安装")
    print("\n修复建议：")
    print(f"请运行：{sys.executable} -m pip install PyMuPDF")

print("\n=== 系统依赖检查 ===")
result = subprocess.run(['brew', 'list', 'mupdf'], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ mupdf已通过Homebrew安装")
else:
    print("❌ mupdf未安装，请运行：brew install mupdf") 