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
- git clone / git push / git pull
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

安装完成后请重启 Claude Code。

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
├── install.sh             # 安装脚本
└── plugin.json            # 插件配置
```

## 手动使用脚本

```bash
# 连接 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py connect

# 断开 V2Box
python3 /Users/rhuang/workspace/github-v2box-auto/scripts/v2box-auto.py disconnect
```
