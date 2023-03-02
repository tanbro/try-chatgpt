from collections import deque
from os import environ, getenv, linesep
from pathlib import Path

try:
    import readline
except ImportError:
    pass

import openai
import rich.console
import rich.markdown
from dotenv import load_dotenv

DEFAULT_MODEL = "gpt-3.5-turbo"


def show_readme(console):
    s = ""
    for fname in ("README.md", "NOTICE.md", "AUTHORS.md"):
        try:
            if s:
                s += linesep
            s += Path(fname, encoding="utf8").read_text()
        except FileNotFoundError:
            pass
    if s:
        md = rich.markdown.Markdown(s)
        print()
        with console.pager(styles=True):
            console.print(md)
        print()


def run_chat(console, kdargs):
    messages = deque(maxlen=3)
    while True:
        input_string = console.input("🧑💬 : ").strip()
        if not input_string:
            continue

        ans_prefix = "🤖 :"
        messages.append({
            "role": "user",
            "content": input_string,
        })
        with console.status(ans_prefix) as status:
            stream = openai.ChatCompletion.create(
                messages=list(messages),
                **kdargs
            )
            message = {"role": "", "content": ""}
            for i, res in enumerate(stream):
                delta = res["choices"][0]["delta"]  # type: ignore
                if not delta:
                    break
                if i == 0:
                    role = delta["role"]
                    status.update(ans_prefix)
                    message["role"] = role
                else:
                    content = delta["content"]
                    message["content"] = message["content"] + content
                    status.update(f"{ans_prefix} {message['content']}")
            console.print(f"🤖💬 : {message['content']}")
        messages.append(message)

        print()
        console.rule("")
        print()


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

    #
    try:
        print()
        console.input("[green]按[bold]『Enter』[/]开始, [bold]『Ctrl+C』[/]退出 ...[/]")
        console.clear()
        print()
        console.rule("")
        print()

        run_chat(console, kdargs)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
