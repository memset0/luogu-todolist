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

# config.yml 配置指南

按照如下方法，您就可以获取您的账户下所有题目的 AC 状态：

* `userid`请更改为您账户的 uid
* `clientid`可以按如下方式获取（以Chrome浏览器为例）：
  1. 点击地址栏左边的锁，然后点击cookie，在正在使用的cookie中找到`__client_id`，双击其内容后复制即可。
  2. 或者按F12进入开发者模式，点击开发者模式上方Network一栏，按F5刷新页面，在加载项中找到www.luogu.org，点击后选择Header一栏，在其中显示的cookie信息中找到`__client_id`后复制即可。

# Demo

![](https://i.loli.net/2019/01/25/5c4adb75c188f.png)
