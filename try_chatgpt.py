from os import environ, getenv
from textwrap import dedent
from string import Template

import openai
import rich.console
from dotenv import load_dotenv


"以下是与人工智能助手的对话。这位助理乐于助人、富有创造力、聪明而且非常友好。"

PROMPT_TPL = Template(dedent("""
    Marvo 是一个聊天机器人，他不情愿地、充满讽刺意味的与用户交谈。

    
    用户: ${input}


    Marvo:
""").strip())


def main():
    load_dotenv()
    openai.api_key = environ["OPENAI_API_KEY"]
    #
    kdargs = dict(
        model=getenv("OPENAI_COMPLETION_MODEL") or "text-ada-001",
        stream=True,
    )
    max_tokens = getenv("OPENAI_COMPLETION_MAX_TOKENS")
    if max_tokens:
        kdargs.update(max_tokens=int(max_tokens))  # type: ignore
    #
    try:
        while True:
            input_string = input("🧑💬 : ").strip()
            if not input_string:
                continue

            print()

            pred_string = ""
            ans_prefix = "🤖 :"
            console = rich.console.Console()
            with console.status(ans_prefix) as status:
                stream = openai.Completion.create(
                    prompt=PROMPT_TPL.safe_substitute(input=input_string),
                    **kdargs
                )
                for x in stream:
                    pred_string += x["choices"][0]["text"]  # type: ignore
                    status.update(f"{ans_prefix} {pred_string}")
            print(f"🤖💬 : {pred_string}")

            print()
            print('━'*30)
            print()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
