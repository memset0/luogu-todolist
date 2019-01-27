# Luogu Todolist

**第三方**轻量级本地 Todo List for 洛谷

# 功能

* 无限量添加题目
* 查看题目 AC 状态
* GUI 界面，好看直观
* 点击跳转到记录列表 / 题目列表
* 方便的 Todo List 管理（支持注释和标签）
* pass 标签，展示时会按此题 AC 处理
* warn 标签，展示时会特别标注此题

# 应用场景

* 嘴巴选手 / 鸽子们 可以利用标签功能方便地管理 Todo List
* 有大量的题目需要存储在 Todo List 中
* 利用脚本等方式批量管理 Todo List
* 将自己的 Todo List 以文本的方式传给他人
* 对 Todo List 进行方便的备份
* 同机房同学共用 Todo List （可以把 `todo.list` 局域网共享然后改一下代码里的引用目录）

# 安装

* 需要 Python 3 ，第三方库：requests，pyyaml
* 复制 `config.example.yml` 到 `config.yml` ， `todo.example.list` 到 `todo.list`
* 运行 `python3 host.py`
* 在浏览器打开 `http://localhost:2333`

更多细节请参考 Wiki

# Demo

![](https://i.loli.net/2019/01/25/5c4adb75c188f.png)
