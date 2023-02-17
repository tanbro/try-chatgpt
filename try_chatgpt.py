from os import environ, getenv
from textwrap import dedent

import openai
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
            print("🤖💬 : ", end="", flush=True)

            stream = openai.Completion.create(
                prompt=prompt_string,
                **kdargs
            )

            is_empty = True
            for x in stream:
                s = x["choices"][0]["text"]  # type: ignore
                if is_empty and s.strip():
                    is_empty = False
                    s = s.lstrip()
                if not is_empty:
                    print(s, end="", flush=True)

            print()
            print('━'*30)
            print()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
