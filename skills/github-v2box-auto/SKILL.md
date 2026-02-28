---
name: github-v2box-auto
description: 使用此技能当用户提到"GitHub"、"克隆仓库"、"推送代码"、"拉取代码"、"访问github.com"等关键词时。技能会自动控制 V2Box 连接或断开以确保 GitHub 访问正常。
version: 1.0.0
---

# GitHub V2Box 自动化 Skill

当用户需要访问 GitHub 时，Claude 会自动调用此技能来控制 V2Box 连接/断开。

## 功能说明

1. **连接**: 在执行 GitHub 操作前自动连接 V2Box
2. **操作**: 执行用户的 GitHub 操作（clone、push、pull 等）
3. **断开**: 操作完成后断开 V2Box 连接

## 触发条件

当用户请求涉及以下任何关键词时使用此技能：
- GitHub
- github.com
- 克隆仓库
- 推送代码
- 拉取代码
- git clone
- git push
- git pull
- download from GitHub

## 执行流程

1. 首先调用 `python3 /Users/rhuang/workspace/v2box-auto.py connect` 连接 V2Box
2. 等待 2 秒让连接生效
3. 执行用户的 GitHub 操作
4. 完成后调用 `python3 /Users/rhuang/workspace/v2box-auto.py disconnect` 断开 V2Box

## 注意事项

- V2Box 应用路径: `/Applications/V2Box.app`
- 点击位置固定: 屏幕坐标 (482, 678)
- 脚本路径: `/Users/rhuang/workspace/v2box-auto.py`
