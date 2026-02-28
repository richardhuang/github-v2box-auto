#!/usr/bin/env python3
"""
V2Box Auto Connect - 使用 Python 和 AppleScript
点击 V2Box 界面上的"点击连接"和"点击断开"按钮

使用方法:
    python3 v2box-auto.py connect    - 点击连接按钮
    python3 v2box-auto.py disconnect - 点击断开按钮

相对坐标（基于窗口左上角）:
    X 偏移: 129 像素
    Y 偏移: 540 像素
"""

import subprocess
import time
import sys

# ============ 配置区域 ============
# 相对于窗口左上角的偏移量
X_OFFSET = 129  # 距离窗口左边的像素
Y_OFFSET = 540  # 距离窗口顶部的像素
# ================================

def get_v2box_window_info():
    """获取 V2Box 窗口的位置和大小信息"""
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
    return result.stdout.strip()

def click_at(x, y):
    """用 AppleScript 点击屏幕坐标"""
    script = f'''
    tell application "System Events"
        click at {{{x}, {y}}}
    end tell
    '''
    subprocess.run(['osascript', '-e', script], capture_output=True, timeout=5)

def main():
    action = sys.argv[1] if len(sys.argv) > 1 else "connect"

    # 检查 V2Box 是否运行
    check_script = '''
    tell application "System Events"
        return (name of processes) contains "V2Box"
    end tell
    '''
    result = subprocess.run(['osascript', '-e', check_script], capture_output=True, text=True)
    is_running = result.stdout.strip() == "true"

    if not is_running:
        subprocess.run(['open', '/Applications/V2Box.app'], timeout=5)
        time.sleep(2)

    # 激活应用
    subprocess.run(['osascript', '-e', 'tell application "V2Box" to activate'], timeout=5)
    time.sleep(1)

    # 获取窗口位置
    win_info = get_v2box_window_info()
    if win_info == "error" or not win_info:
        print("无法获取窗口信息")
        sys.exit(1)

    parts = win_info.split(",")
    x, y = map(int, map(float, parts))

    # 计算实际点击位置（窗口左上角 + 相对偏移）
    click_x = x + X_OFFSET
    click_y = y + Y_OFFSET

    print(f"=== V2Box 窗口信息（动态获取） ===")
    print(f"窗口左上角: ({x}, {y})")
    print(f"按钮: {'连接' if action == 'connect' else '断开'}")
    print(f"相对偏移: X+{X_OFFSET}, Y+{Y_OFFSET}")
    print(f"点击位置: ({click_x}, {click_y})")

    click_at(click_x, click_y)

if __name__ == "__main__":
    main()
