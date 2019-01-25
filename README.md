# Luogu Todolist

第三方轻量级本地 TODO 列表 for 洛谷

如果你有大量的题目需要存储在 Todo List 中，或者需要对 Todo List 进行本地管理，可以考虑使用这个小脚本

# 功能

* 无限量添加题目
* 查看题目 AC 状态
* GUI 界面，好看直观
* 点击跳转到记录列表 / 题目列表
* 方便的 Todo List 管理（支持注释）
* 本地缓存，减少 GET 请求

![](https://i.loli.net/2019/01/25/5c4adb75c188f.png)

# 安装

* 需要 Python 3 ，第三方库：requests，pyyaml
* 复制 `config.example.yml` 到 `config.yml` ， `todo.example.list` 到 `todo.list`
* 运行 `python3 host.py`
* 在浏览器打开 `http://localhost:2333`