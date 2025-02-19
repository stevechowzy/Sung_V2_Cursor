import os
import platform
import fnmatch
from .config import PATHS, ALIAS, SMART_MATCH, FALLBACK_PATHS

class PathFinder:
    @staticmethod
    def find_resource():
        """智能定位资源文件"""
        system = platform.system()
        search_paths = []
        
        # 添加备选路径
        search_paths += FALLBACK_PATHS.get(system.lower(), [])
        search_paths += [os.path.expanduser('~')]
        
        # 深度搜索
        for base in search_paths:
            for root, dirs, files in os.walk(base):
                for pattern in SMART_MATCH['file_patterns']:
                    for f in fnmatch.filter(files, pattern):
                        yield os.path.join(root, f)

    @staticmethod
    def get_latest_file():
        """获取最新版本文件"""
        files = list(PathFinder.find_resource())
        if not files:
            raise FileNotFoundError("未找到任何符合要求的文本文件")
        return max(files, key=os.path.getmtime)

    @staticmethod
    def validate_path(path):
        """深度验证路径有效性"""
        checks = [
            ('存在性', os.path.exists),
            ('可读性', os.access(path, os.R_OK)),
            ('文件类型', lambda p: os.path.isfile(p))
        ]
        
        for check_name, check_func in checks:
            if not check_func(path):
                raise PermissionError(f"验证失败：{check_name} ({path})")

    @staticmethod
    def spell_check(path):
        """拼写校验逻辑"""
        common_typos = {
            'somg': 'song',
            'Libary': 'Library',
            'newlaw': 'new_law'
        }
        
        corrected = path
        for wrong, right in common_typos.items():
            corrected = corrected.replace(wrong, right)
        
        if corrected != path and os.path.exists(corrected):
            print(f"⚠️  检测到常见拼写错误，建议修正为：{corrected}")
            return corrected
        return path 