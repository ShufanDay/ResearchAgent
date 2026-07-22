import re

def parse_action(text: str):

    action = re.search(
        r"Action:\s*(.*)",
        text
    )

    input_data = re.search(
        r"Input:\s*(.*)",
        text
    )

    if action and input_data:

        # 返回 action 和 input中的内容
        return action.group(1).strip(), input_data.group(1).strip()

    return None