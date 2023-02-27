# 我们的 ChatGPT 体验例子

## Summary

这是一个在命令行中运行(CLI)的很小的体验性质的程序。

他调使用 [OpenAI][] 的 `text-davinci-003` 模型（未作任何 finetune），根据用户输入进行续写。

由于 [OpenAI][] 尚未开放 Chat 接口,且本例没有针对多轮次对话做任何特殊处理,所以本例实际上是 `GPT` 续写,而**不是** `ChatGPT` 对话!
使用者可以简单的将它视作一个 QA 对答 AI,而不是对话 AI.

## How to use

这个例子在需要 Laptop/Desktop/Workstation/Server 设备上运行，它没有任何针对移动设备/智能设备/IoT设备的设计。

### 安装 Python

它用 [Python][] 编程语言编写，所以使用之前必须安装 [Python][] 运行环境。

- Windows (Windows 10 及以上)

  1. 在开始菜单找到并打开微软的软件商店 `Microsoft Store`
  1. 在软件商店的搜索栏输入 `python` ，按回车或点搜索按钮
  1. 在搜索结果中选择 `Python3.7`，`Python3.8`，`Python3.9`，`Python3.10`，`Python3.11` 中的任一个安装

  1. 打开命令提示符或 Windows 终端，输入:

     ```powershell
     python --version     
     ```

     如果输出类似

     ```powershell-interactive
     C:\> python --version
     Python 3.10.8
     ```

     这样的结果，说明安装成功。

- MacOS: 懒得写了
- 其它: 懒得写了

### 复制程序源码

在本地磁盘上找个工作目录，把这个程序的整个目录复制过去

### 安装 OpenAI SDK

- Windows

  在这个程序源码目录打开命令提示符或 Windows 终端，输入以下命令:

  ```powershell
  python -m pip install --user requirements.txt
  ```

- MacOS: 懒得写了
- 其它: 懒得写了

### 运行

- Windows

  在这个程序源码目录打开命令提示符或 Windows 终端，输入以下命令:

  ```powershell
  python try_chatgpt.py
  ```

- MacOS: 懒得写了
- 其它: 懒得写了

[OpenAI]: https://openai.com/ "OpenAI is an AI research and deployment company."
[Python]: https://www.python.org/ "Python is a programming language that lets you work quickly and integrate systems more effectively"
