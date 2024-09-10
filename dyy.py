from openai import OpenAI
import json

client = OpenAI()

def extract_dialogues(text):
    prompt = f"""
    -目标-
    给定一份文本文件，识别文本中的所有关于丁元英的对话记录，以及相关背景信息，输出相关的对话。

    -指令-
    1. 识别对话。对于给出的文本，提取以下对话信息：
    - 角色: 小说中的角色名称
    - 背景: 对话的背景

    2. 从第1步中识别的对话中，识别所有关于丁元英的对话。
    对于每对对话，提取以下信息：
    - 背景: 对话的背景
    - 对话角色: 和丁元英对话的角色
    - 输出: 丁元英说的内容

    3. 将结果输出为一个JSON数组，无需任何额外的解释或格式化。

    -示例-
    对于文本：“陈茹面有难色地说：“元英，你刚下飞机我就来找你，真不好意思。楚风说你撤完摊子就要离开北京，我想，我还是早点来找你。”丁元英说：“如果没有特别的事，我打算明天走。有什么事你先说。””

    输出应为：

    [{{
    "instruction": "陈茹遇到急事，想请丁元英帮忙",
    "input": "陈茹面有难色地说：“元英，你刚下飞机我就来找你，真不好意思。楚风说你撤完摊子就要离开北京，我想，我还是早点来找你。",
    "output": "如果没有特别的事，我打算明天走。有什么事你先说。"
    }}]  

    instruction为背景信息，input为对话角色说的内容，output为丁元英说的内容，json 使用英文输出，无需任何额外的解释或格式化，无需```json类似的 markdown 输出。
    -真实数据-
    ######################
    文本: {text}
    ######################
    输出:
    """
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        max_tokens=3000
    )

    return completion.choices[0].message.content

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size):
    # 根据指定的 chunk_size 分块
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def main():
    # 读取文本文件
    text = read_text_file('data/ddy.txt')
    
    # 设置 chunk_size
    chunk_size = 5000  # 可以根据需要调整

    # 分块文本
    text_segments = chunk_text(text, chunk_size)

    results = []

    for text in text_segments:
        if text.strip():  # 确保段落不是空的
            result = extract_dialogues(text)
            print(result)
            results.extend(json.loads(result))

    # 输出最终的 JSON 数组
    with open('data/dyy_ft.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
