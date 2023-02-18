from os import environ, getenv
from textwrap import dedent

import openai
from dotenv import load_dotenv
from rich import print
from rich.console import Console


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

            console = Console()
            ans_prefix = "🤖 : "
            with console.status(ans_prefix) as status:
                ans_string = ""
                stream = openai.Completion.create(
                    prompt=prompt_string,
                    **kdargs
                )
                for x in stream:
                    s = x["choices"][0]["text"]  # type: ignore
                    if ans_string:
                        ans_string += s
                    else:
                        ans_string += s.lstrip()
                    status.update(f"{ans_prefix}{ans_string}")
            print(f"🤖💬 : {ans_string}")

            print()
            print('━'*30)
            print()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
