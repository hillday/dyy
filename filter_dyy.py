import json

def filter_json(input_file, output_file):
    # 读取JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 过滤对象
    filtered_data = [
        item for item in data
        if all(key in item for key in ["instruction", "input", "output"])
    ]
    
    # 写入过滤后的数据到新的JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=2)

    print(f"过滤完成。原始对象数量: {len(data)}, 过滤后对象数量: {len(filtered_data)}")

# 使用示例
input_file = 'data/dyy_ft.json'  # 替换为你的输入文件名
output_file = 'data/dyy_final.json'  # 替换为你想要的输出文件名

filter_json(input_file, output_file)