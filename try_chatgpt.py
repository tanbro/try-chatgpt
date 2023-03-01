from os import environ, getenv
from string import Template
from textwrap import dedent

try:
    import readline
except ImportError:
    pass

import openai
import rich.console
import rich.markdown
from dotenv import load_dotenv

DEFAULT_MODEL = "text-davinci-003"

PROMPT_TPL = Template(dedent("""
    Q: ${input}


    A:
""").lstrip())


def show_readme(console):
    for fname in ("README.md", "NOTICE.md", "AUTHORS.md"):
        try:
            with open(fname, encoding="utf8") as f:
                md = rich.markdown.Markdown(f.read())
                print()
                console.print(md)
                print()
            console.input("[green]按[bold]『Enter』[/]键继续 ...[/]")
            console.clear()
        except FileNotFoundError:
            pass


def main():
    load_dotenv()
    openai.api_key = environ["OPENAI_API_KEY"]
    #
    kdargs = dict(
        model=getenv("OPENAI_COMPLETION_MODEL") or DEFAULT_MODEL,
        stream=True,
    )
    max_tokens = getenv("OPENAI_COMPLETION_MAX_TOKENS")
    if max_tokens:
        kdargs.update(max_tokens=int(max_tokens))  # type: ignore
    #
    console = rich.console.Console()
    #
    try:
        show_readme(console)
    except KeyboardInterrupt:
        return
    print()
    console.print("[green]现在开始 GPT QA 吧! (Ctrl+C 退出)[/]")
    print()
    console.rule("")
    print()
    #
    try:
        while True:
            input_string = console.input("🧑💬 : ").strip()
            if not input_string:
                continue

            pred_string = ""
            ans_prefix = "🤖 :"
            with console.status(ans_prefix) as status:
                stream = openai.Completion.create(
                    prompt=PROMPT_TPL.safe_substitute(input=input_string),
                    **kdargs
                )
                for x in stream:
                    pred_string += x["choices"][0]["text"]  # type: ignore
                    status.update(f"{ans_prefix} {pred_string}")
            console.print(f"🤖💬 : {pred_string}")

            print()
            console.rule("")
            print()

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
