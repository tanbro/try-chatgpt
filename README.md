# 我们的 ChatGPT 体验例子

## Summary

它包好了几个了在命令行中(CLI)试用 [OpenAI][] LM 的简单小例子，供体验和评估用。

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
  python <例子文件名>.py
  ```

- MacOS: 懒得写了
- 其它: 懒得写了

[OpenAI]: https://openai.com/ "OpenAI is an AI research and deployment company."
[Python]: https://www.python.org/ "Python is a programming language that lets you work quickly and integrate systems more effectively"
