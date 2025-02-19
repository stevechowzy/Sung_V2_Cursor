import os
from termcolor import cprint  # 需要 pip install termcolor
from fuzzywuzzy import fuzz  # 需要 pip install fuzzywuzzy

def debug_paths():
    # 获取当前脚本路径
    script_path = os.path.abspath(__file__)
    print(f"📁 脚本路径：{script_path}")
    
    # 计算项目根目录
    calculated_root = os.path.dirname(os.path.dirname(script_path))
    print(f"📂 计算的项目根目录：{calculated_root}")
    
    # 在函数开头初始化target_file
    target_file = os.path.join(calculated_root, "librarySong", "newlaw_WangAS_Song.txt")

    # Mac路径适配（修正后覆盖默认路径）
    mac_path = '/Users/zyong202009/Sung_V2_Cursor'
    if calculated_root != mac_path and os.path.exists(mac_path):
        cprint(f"⚠️  检测到Mac特殊路径，自动修正为：{mac_path}", 'yellow')
        calculated_root = mac_path
        target_file = os.path.join(calculated_root, "librarySong", "newlaw_WangAS_Song.txt")  # 覆盖默认路径

    # 检查目标文件
    print(f"🔍 目标文件路径：{target_file}")
    
    # 新增项目结构检查
    def print_tree(startpath):
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f'{indent}├── {os.path.basename(root)}/')
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print(f'{subindent}├── {f}')

    # 在文件检查后添加结构展示
    if os.path.exists(target_file):
        cprint("✅ 文件存在验证通过", 'green')
    else:
        cprint("❌ 文件未找到，请检查：", 'red')
        print(f"当前项目结构：")
        print_tree(calculated_root)  # 展示目录树帮助定位

    # 增强版路径自动修正
    def find_similar_path(base_path, target_file):
        """
        智能查找相似路径：
        1. 忽略大小写
        2. 允许部分字符差异
        3. 支持模糊匹配
        """
        best_match = None
        best_score = 0
        
        # 遍历所有可能目录
        for root, dirs, files in os.walk(base_path):
            for name in dirs + files:
                current_path = os.path.join(root, name)
                # 计算相似度
                score = fuzz.token_sort_ratio(target_file.lower(), current_path.lower())
                
                if score > best_score and score > 70:  # 相似度阈值
                    best_score = score
                    best_match = current_path
        
        return best_match

    # 在路径检查失败时调用
    if not os.path.exists(target_file):
        suggested_path = find_similar_path(calculated_root, "newlaw_WangAS_Song.txt")
        if suggested_path:
            cprint(f"🔍 发现相似文件：{suggested_path}", 'yellow')
            cprint("💡 是否要使用此路径？(y/n)", 'cyan')
            if input().lower() == 'y':
                target_file = suggested_path

if __name__ == "__main__":
    debug_paths() 