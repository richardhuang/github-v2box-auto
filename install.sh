#!/bin/bash
# github-v2box-auto 安装脚本
# 用于在重装 Claude Code 后快速部署

echo "=== github-v2box-auto 安装脚本 ==="
echo ""

# 创建目标目录
mkdir -p ~/.claude/plugins/custom/github-v2box/.claude-plugin
mkdir -p ~/.claude/plugins/custom/github-v2box/skills/github-v2box-auto

# 复制配置文件
echo "复制 plugin.json..."
cp ./plugin.json ~/.claude/plugins/custom/github-v2box/.claude-plugin/plugin.json

# 复制技能文件
echo "复制 SKILL.md..."
cp ./skills/github-v2box-auto/SKILL.md ~/.claude/plugins/custom/github-v2box/skills/github-v2box-auto/SKILL.md

# 验证
echo ""
echo "=== 验证 ==="
if [ -f ~/.claude/plugins/custom/github-v2box/.claude-plugin/plugin.json ]; then
    echo "✓ plugin.json 已安装"
else
    echo "✗ plugin.json 安装失败"
    exit 1
fi

if [ -f ~/.claude/plugins/custom/github-v2box/skills/github-v2box-auto/SKILL.md ]; then
    echo "✓ SKILL.md 已安装"
else
    echo "✗ SKILL.md 安装失败"
    exit 1
fi

echo ""
echo "=== 安装完成 ==="
echo "请重启 Claude Code 以加载新插件"
echo ""
