# github-v2box-auto

自动控制 V2Box 连接/断开以访问 GitHub 的 Claude Code 插件。

## 功能说明

当需要访问 GitHub 时，该插件会自动：
1. 启动并连接 V2Box
2. 执行用户的 GitHub 操作（clone、push、pull 等）
3. 操作完成后自动断开 V2Box 连接

## 触发条件

当用户请求涉及以下关键词时自动触发：
- GitHub / github.com
- 克隆仓库 / 推送代码 / 拉取代码
- git clone / git push / git pull / git fetch
- download from GitHub

## 安装

```bash
# 克隆项目
cd /Users/rhuang/workspace
git clone https://github.com/your-username/github-v2box-auto.git

# 运行安装脚本
cd github-v2box-auto
chmod +x install.sh
./install.sh
```

安装完成后请**重启 Claude Code**。

## 配置要求

- **V2Box 应用路径**: `/Applications/V2Box.app`
- **系统**: macOS（依赖 AppleScript）
- **Python**: Python 3.x（系统自带）

## 原理

通过 Python 结合 AppleScript 控制 V2Box 应用的图形界面，动态获取窗口位置后点击对应按钮。

## 项目结构

```
.
├── scripts/
│   └── v2box-auto.py      # 核心脚本：控制 V2Box 连接/断开
├── skills/
│   └── github-v2box-auto/ # Claude Code 技能定义
├── hooks/
│   ├── hooks.json         # Hook 配置：定义何时自动触发
│   └── pre_tool_use.py    # PreToolUse Hook：检测 git 命令并自动连接 V2Box
├── install.sh             # 安装脚本
└── plugin.json            # 插件配置
```

## Hooks（自动触发机制）

插件使用 Claude Code 的 **PreToolUse Hook** 机制实现自动触发：

- **hooks/hooks.json** - 配置 hook 规则，匹配 bash 工具
- **hooks/pre_tool_use.py** - 检测 git 命令并自动控制 V2Box

当检测到以下 git 命令时会自动：
1. 启动 V2Box（如果未运行）
2. 连接 V2Box
3. 执行用户的 git 命令
4. 命令完成后自动断开 V2Box

支持的 git 命令：
- `git clone`
- `git push`
- `git pull`
- `git fetch`
- `git remote`

## 手动使用脚本

```bash
# 连接 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py connect

# 断开 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py disconnect
```

## 调试

如果需要查看 hook 执行日志，可以修改 `hooks/pre_tool_use.py` 添加日志输出：

```python
import logging
logging.basicConfig(filename='/tmp/v2box-hook.log', level=logging.DEBUG)
```
