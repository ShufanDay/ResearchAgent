from app.prompt import SYSTEM_PROMPT
from app.llm import chat
from app.parser import parse_action
from app.registry import TOOLS

class ResearchAgent:

    def run(self, question):

        messages = [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": question
            }

        ]

        while True:

            response = chat(messages)
            
            if "Final Answer:" in response:

                return response

            result = parse_action(response)

            if result is None:

                return response

            tool_name, tool_input = result # 得到工具名和文件路径

            observation = TOOLS[tool_name](tool_input)

            messages.append(

                {

                    "role": "assistant",

                    "content": response

                }

            )

            messages.append(

                {

                    "role": "user",

                    "content": f"Observation:\n{observation}"

                }

            )