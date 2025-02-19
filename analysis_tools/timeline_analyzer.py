import re
import jieba.analyse
from collections import defaultdict
import os
import fnmatch
from .config import PATHS, ALIAS
from .path_service import PathFinder

def parse_timeline(text):
    """解析时间线"""
    timeline = defaultdict(list)
    
    # 匹配年份和事件
    year_events = re.findall(r'(\d{4})年(.*?)(?=\d{4}年|$)', text, re.S)
    
    for year, content in year_events:
        # 提取人物（匹配2-4字中文名）
        people = re.findall(r'[王李吕司苏曾程韩][\u4e00-\u9fa5]{1,3}', content)
        
        # 提取关键政策
        policies = re.findall(r'(青苗法|市易法|均输法|保甲法|将兵法|方田法)', content)
        
        # 添加自定义词典提升分词准确性
        jieba.analyse.set_stop_words('analysis_tools/stop_words.txt')
        jieba.load_userdict('analysis_tools/history_terms.txt')
        
        # 添加异常处理
        try:
            events = jieba.analyse.textrank(content, topK=5, allowPOS=('n','vn'))
        except Exception as e:
            print(f"分词异常：{str(e)}")
            events = []
        
        timeline[year] = {
            'people': list(set(people)),
            'policies': policies,
            'events': events,
            'excerpt': content[:150] + '...'
        }
    
    return timeline

def generate_timeline_report(data, output_path):
    """生成可视化报告"""
    report = [
        "# 王安石新政核心时间线（1069-1085）",
        "‖ 年份 ‖ 关键人物 ‖ 推行政策 ‖ 重大事件 ‖",
        "|-------|-----------|-----------|---------|"
    ]
    
    for year in sorted(data.keys(), key=int):
        entry = data[year]
        report.append(
            f"| {year} | {', '.join(entry['people'][:3])} | "
            f"{'、'.join(entry['policies'])} | "
            f"{entry['events'][0]} |"
        )
    
    report.append("\n## 关键人物关系演变\n```mermaid\ngraph LR\n")
    
    # 生成人物关系图
    people_net = defaultdict(set)
    for year in data.values():
        for p in year['people']:
            people_net[p].update(year['people'])
    
    connections = set()
    for person, links in people_net.items():
        for link in links:
            if person != link and (link, person) not in connections:
                connections.add((person, link))
                report.append(f"    {person} --> {link}")
    
    report.append("```")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

def get_dynamic_path():
    return {
        'input_file': PathFinder.get_latest_file(),
        'output_dir': ALIAS['output_dir']
    }

if __name__ == "__main__":
    # 替换原有的路径获取方式
    input_file = os.path.join(project_root, "librarySong", "newlaw_WangAS_Song.txt")
    output_file = os.path.join(ALIAS['output_dir'], "新政核心时间线.md")
    
    # 添加路径存在性检查
    if not os.path.exists(input_file):
        print(f"❌ 关键错误：文件路径不存在 -> {input_file}")
        print("建议操作：")
        print("1. 确认已运行过pdf_to_txt_steve.py生成文本")
        print("2. 检查文件名是否包含特殊字符")
        exit(1)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    timeline_data = parse_timeline(text)
    generate_timeline_report(timeline_data, output_file)
    print(f"报告已生成：{output_file}") 