from email import message
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Qwen3-1.7B-4bit")

def chat(messages):
    if tokenizer.chat_template is not None:
        # messages = [{"role": "user", "content": messages}]
        # 关键：tokenize=False 返回原始文本字符串
        messages = tokenizer.apply_chat_template(
            messages, 
            add_generation_prompt=True,
            tokenize=False,
            enable_thinking=False
        )

    response = generate(model, tokenizer, prompt=messages, verbose=False, max_tokens=512)
    return response

if __name__ == '__main__':
    messages = input("请输入您的问题：")
    text = chat(messages=messages)
    print(text)