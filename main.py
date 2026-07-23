from app.core.agent import ResearchAgent

agent = ResearchAgent()

while True:

    question = input(">>> ")
    if question == 'quit':
        break
    print(agent.run(question))

# 你可以帮我总结一下pdf中的内容吗?文件路径是./data/zhaoshuai.pdf
