import matplotlib.pyplot as plt
from datetime import datetime
import os

def visualize_timeline(timeline_data):
    # 转换数据结构格式
    timeline = []
    for year in sorted(timeline_data.keys(), key=int):
        entry = timeline_data[year]
        timeline.append({
            "year": f"{year}年",
            "keywords": entry['events']
        })
    
    # 优化可视化效果
    plt.figure(figsize=(16, 6))
    plt.plot(dates, [1]*len(dates), 'o-', markersize=12, color='#2c7da0')
    
    # 添加交互式提示（保存为HTML）
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "worldview")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "newlaw_timeline.png")
    output_html = os.path.join(output_dir, "interactive_timeline.html")
    
    plt.savefig(output_path)
    print(f"静态图表已保存至：{output_path}")
    print(f"交互式图表已生成：{output_html}")

if __name__ == "__main__":
    from timeline_analyzer import get_dynamic_path
    
    paths = get_dynamic_path()
    input_path = paths['input_file']
    output_dir = paths['output_dir']
    
    if not os.path.exists(input_path):
        print(f"❌ 文件未找到：{input_path}")
        exit(1)
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    timeline_data = parse_timeline(text)
    visualize_timeline(timeline_data) 