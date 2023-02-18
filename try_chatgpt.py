from os import environ, getenv
from textwrap import dedent

import openai
import rich.console
from dotenv import load_dotenv


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

            prompt_string = dedent(f"""
            Q: {input_string}


            A:
            """).strip()

            print()

            pred_string = ""
            ans_prefix = "🤖 :"
            console = rich.console.Console()
            with console.status(ans_prefix) as status:
                stream = openai.Completion.create(
                    prompt=prompt_string,
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
