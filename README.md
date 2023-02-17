# 我们的 ChatGPT 体验例子

## Summary

这是一个在命令行中运行(CLI)的很小的体验性质的程序。

他调使用 [OpenAI][] 的 `text-davinci-003` 模型（未作任何 finetune），根据用户输入，输出最多 2048 个 token 长度的预测结果。

## How to use

这个例子在需要 Laptop/Desktop/Workstation/Server 设备上运行，它没有任何针对移动设备/智能设备/IoT设备的设计。

### 安装 Python

它用 [Python][] 编程语言编写，所以使用之前必须安装 [Python][] 运行环境。

- Windows (Windows 10 及以上)

  1. 在开始菜单找到微软的软件商店 Microsoft Store，并打开
  1. 在软件商店的搜索栏输入 python ，并回车或点击搜索按钮
  1. 在搜索结果中选择 `Python3.7`，`Python3.8`，`Python3.9`，`Python3.10`，`Python3.11` 中的任何一个，然后选择安装，并等待安装其完成。

  1. 打开命令提示符或 Windows 终端，输入以下命令:

     ```powershell
     python --version     
     ```

     如果输出 `Python 3.10.8` 这样的结果，说明安装成功。

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

在这个程序源码目录打开终端/命令提示符，输入以下命令:

- Windows

  在这个程序源码目录打开命令提示符或 Windows 终端，输入以下命令:

  ```powershell
  python try_chatgpt.py
  ```

- MacOS: 懒得写了
- 其它: 懒得写了

## NOTICE

收到程序包的人，你会在 `.env` 文件中找到我个人的 [OpenAI][] API KEY，每次调用都在扣除作者的账户费用。
所以请使用者尊重作者的隐私和权益，不传播，不滥用！

[OpenAI]: https://openai.com/ "OpenAI is an AI research and deployment company."
[Python]: https://www.python.org/ "Python is a programming language that lets you work quickly and integrate systems more effectively"