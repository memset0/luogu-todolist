# Luogu Todolist

**第三方**轻量级本地 Todo List for 洛谷

# 功能

* 无限量添加题目
* 查看题目 AC 状态
* GUI 界面，好看直观
* 点击跳转到记录列表 / 题目列表
* 方便的 Todo List 管理（支持注释）
* 本地缓存，减少 GET 请求

# 应用场景

* 有大量的题目需要存储在 Todo List 中
* 需要利用脚本等方式批量管理 Todo List
* 需要将自己的 Todo List 以文本的方式传给他人

# 安装

* 需要 Python 3 ，第三方库：requests，pyyaml
* 复制 `config.example.yml` 到 `config.yml` ， `todo.example.list` 到 `todo.list`
* 运行 `python3 host.py`
* 在浏览器打开 `http://localhost:2333`

# Demo

![](https://i.loli.net/2019/01/25/5c4adb75c188f.png)