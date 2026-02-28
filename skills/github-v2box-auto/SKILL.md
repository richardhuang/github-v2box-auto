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

当用户请求执行以下任何操作时，**务必先调用此技能**：

### 必须使用此技能的场景
- `git clone` 仓库
- `git push` 代码到远程仓库
- `git pull` 拉取远程仓库
- `git fetch` 获取远程仓库数据
- `git push` 或 `git pull` 使用 `origin` 远程
- 访问 `github.com` 相关操作

### 调用方式
使用以下命令控制 V2Box：
```bash
# 连接 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py connect

# 断开 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py disconnect
```

## 执行流程

1. 首先调用 `python3 /Users/rhuang/workspace/v2box-auto.py connect` 连接 V2Box
2. 等待 2 秒让连接生效
3. 执行用户的 GitHub 操作
4. 完成后调用 `python3 /Users/rhuang/workspace/v2box-auto.py disconnect` 断开 V2Box

## 注意事项

- V2Box 应用路径: `/Applications/V2Box.app`
- 点击位置: 脚本会动态获取窗口位置，基于 **相对偏移** X+129, Y+540 计算实际点击位置
- 脚本路径: `/Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py`
- 如需调整点击位置，可修改脚本中的 `X_OFFSET` 和 `Y_OFFSET` 参数
