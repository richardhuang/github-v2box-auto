#!/usr/bin/env python3
"""
Claude Code Hook: PreToolUse
在工具调用前自动检测是否需要使用 github-v2box-auto 技能

功能：
- 检测 git clone/push/pull/fetch 命令
- 自动连接 V2Box
- 工具调用完成后自动断开 V2Box
"""

import json
import os
import subprocess
import sys
import time

# 配置
SCRIPTS_DIR = "/Users/rhuang/workspace/github-v2box-auto/scripts"
V2BOX_APP = "/Applications/V2Box.app"


def check_v2box_running():
    """检查 V2Box 是否正在运行"""
    script = '''
    tell application "System Events"
        return (name of processes) contains "V2Box"
    end tell
    '''
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip() == "true"


def start_v2box():
    """启动 V2Box"""
    if not check_v2box_running():
        subprocess.run(['open', V2BOX_APP], timeout=5)
        time.sleep(2)


def click_button(button_name):
    """点击 V2Box 窗口上的按钮"""
    button_offsets = {
        "连接": (129, 540),
        "断开": (129, 540),
    }

    if button_name not in button_offsets:
        return False

    x_offset, y_offset = button_offsets[button_name]

    script = '''
    tell application "System Events"
        tell application process "V2Box"
            try
                set win to window 1
                set winPos to position of win
                return (item 1 of winPos as string) & "," & (item 2 of winPos as string)
            on error
                return "error"
            end try
        end tell
    end tell
    '''
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, timeout=10)
    win_info = result.stdout.strip()

    if win_info == "error" or not win_info:
        return False

    parts = win_info.split(",")
    x, y = map(int, map(float, parts))

    click_x = x + x_offset
    click_y = y + y_offset

    click_script = f'''
    tell application "System Events"
        click at {{{click_x}, {click_y}}}
    end tell
    '''
    subprocess.run(['osascript', '-e', click_script], capture_output=True, timeout=5)
    return True


def connect_v2box():
    """连接 V2Box"""
    start_v2box()
    subprocess.run(['osascript', '-e', 'tell application "V2Box" to activate'], timeout=5)
    time.sleep(1)
    if click_button("连接"):
        time.sleep(2)  # 等待连接生效
        return True
    return False


def disconnect_v2box():
    """断开 V2Box"""
    if not check_v2box_running():
        return True
    subprocess.run(['osascript', '-e', 'tell application "V2Box" to activate'], timeout=5)
    time.sleep(1)
    return click_button("断开")


def is_git_command(tool_input):
    """检查输入是否包含 git 命令"""
    if isinstance(tool_input, str):
        git_commands = ['git clone', 'git push', 'git pull', 'git fetch', 'git remote']
        return any(cmd in tool_input.lower() for cmd in git_commands)
    elif isinstance(tool_input, dict):
        # 检查 bash 工具的 command 字段
        command = tool_input.get('command', '')
        git_commands = ['git clone', 'git push', 'git pull', 'git fetch', 'git remote']
        return any(cmd in command.lower() for cmd in git_commands)
    return False


def main():
    """主函数：读取 hook 数据并处理"""
    # 读取 hook 数据（从 stdin）
    try:
        raw_input = sys.stdin.read()
        data = json.loads(raw_input)
    except json.JSONDecodeError:
        sys.exit(0)  # 允许工具执行

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', '')

    # 检测 git 命令
    if tool_name == 'bash' and is_git_command(tool_input):
        connect_v2box()

        # 注册退出处理，在工具调用完成后断开 V2Box
        import atexit
        atexit.register(disconnect_v2box)

    # 允许工具执行
    sys.exit(0)


if __name__ == "__main__":
    main()
