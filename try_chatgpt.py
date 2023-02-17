from os import getenv

import openai
from dotenv import load_dotenv


def main():
    load_dotenv()
    openai.api_key = getenv("OPENAI_API_KEY")
    #
    kdargs = dict(
        model=getenv("OPENAI_COMPLETION_MODEL") or "text-davinci-003",
        max_tokens=int(getenv("OPENAI_COMPLETION_MAX_TOKENS", 0)) or 1024,
        stream=True,
    )
    #
    try:
        while True:
            prompt_string = input("🧑💬 : ").strip()
            if not prompt_string:
                continue
            print()
            print("🤖💬 : ", end="", flush=True)

            stream = openai.Completion.create(
                prompt=prompt_string,
                **kdargs
            )

            for i, x in enumerate(stream):
                s = x["choices"][0]["text"]  # type: ignore
                s = s if i else s.lstrip()
                print(s, end="", flush=True)

            print()
            print('━'*30)
            print()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
