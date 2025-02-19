"""
📁 项目路径配置文件
版本：1.1
更新说明：支持动态路径配置
"""
PATHS = {
    # 允许使用通配符
    'source_dir': 'library*',    # 匹配 librarySomg, LibrarySong 等
    'source_file': 'newlaw_*_Song.txt'  # 匹配不同版本
}

# 添加路径别名（可选）
ALIAS = {
    'main_text': '{source_dir}/newlaw_WangAS_Song.txt',
    'output_dir': 'worldview'
}

# 可添加多版本支持
VERSIONS = {
    'v1': {'year': 2023, 'suffix': '_v1'},
    'v2': {'year': 2024, 'suffix': '_v2'}
}

# 新增智能匹配规则
SMART_MATCH = {
    'possible_dirs': [
        'librarySong',  # 精确匹配正确名称
        'library*',     # 保留通配符匹配
        'archives*',
        'text_resources*'
    ],
    'file_patterns': [
        'newlaw_*_Song.txt',
        'wang_*_reforms.txt',
        'song_dynasty_*.txt'
    ]
}

# 添加备选路径方案
FALLBACK_PATHS = {
    'macOS': [
        '/Users/*/Documents/song_resources',
        '/usr/local/var/historical_data'
    ],
    'windows': [
        'C:\\HistoricalDocuments\\SongReforms'
    ]
} 