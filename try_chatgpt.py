from os import environ, getenv
from textwrap import dedent
from string import Template

try:
    import readline
except ImportError:
    pass

import openai
import rich.console
import rich.markdown
from dotenv import load_dotenv


PROMPT_TPL = Template(dedent("""
    Q: ${input}


    A:
""").lstrip())


def show_readme(console):
    for fname in ("README.md", "NOTICE.md", "AUTHORS.md"):
        try:
            with open(fname) as f:
                md = rich.markdown.Markdown(f.read())
                print()
                console.print(md)
                print()
            console.input("[green]按[bold]『Enter』[/]键继续 ...[/]")
        except FileNotFoundError:
            pass


def main():
    load_dotenv()
    openai.api_key = environ["OPENAI_API_KEY"]
    #
    kdargs = dict(
        model=getenv("OPENAI_COMPLETION_MODEL") or "text-davinci-003",
        stream=True,
    )
    max_tokens = getenv("OPENAI_COMPLETION_MAX_TOKENS")
    if max_tokens:
        kdargs.update(max_tokens=int(max_tokens))  # type: ignore
    #
    console = rich.console.Console()
    #
    show_readme(console)
    print()
    console.print("[green]现在开始 GPT QA 吧! (Ctrl+c 退出)[/]")
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
