# Python 简易计算器

包含命令行版本 `calculator.py` 和 tkinter 图形界面版本 `gui_calculator.py`。

## 直接运行 GUI

Windows 电脑安装 Python（包含 tkinter）后，在本目录运行：

```powershell
py -3 gui_calculator.py
```

支持加减乘除、小数、百分比、正负数切换、清除和退格。可使用鼠标或数字键盘；Esc 清除，Backspace 退格，Enter 计算。

## Windows 打包为 EXE（推荐）

> **必须在 Windows 上构建 Windows EXE。** PyInstaller 不是跨平台编译器。以下操作需要 Windows 10/11、Python 3（建议使用 3.11 或 3.12）和网络连接（首次安装依赖）。

1. 安装 [Python for Windows](https://www.python.org/downloads/)，确保 `py -3 --version` 可以正常运行。
2. 下载或克隆仓库：`git clone https://github.com/sairui-bot/Codex.git`。
3. 打开 `Codex\python-calculator` 文件夹。
4. **双击 `build_windows.bat`**；脚本会创建独立虚拟环境、安装 PyInstaller，再使用 `calculator.spec` 打包。
5. 成功后在 `dist\Calculator.exe` 找到可执行程序，双击即可启动。

首次打包会下载依赖，耗时取决于网络和电脑性能。已生成的 EXE 正常情况下无需目标机器安装 Python。

## 手动打包

打开 PowerShell，进入 `python-calculator` 目录：

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-build.txt
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean calculator.spec
```

输出位置：`dist\Calculator.exe`。

配置文件 `calculator.spec` 使用 **onefile**（单文件）和 **windowed**（不显示命令行窗口）。构建过程生成的 `build\`、`dist\`、`.venv\` 不应提交到 Git。

## 常见问题

- **提示找不到 py**：重新安装 Windows 版 Python 并启用 Python Launcher，或从 PowerShell 使用可用的 Python 执行等效命令。
- **提示没有 tkinter**：检查 Python 安装中的 Tcl/Tk 支持；官方 Windows Python 安装通常自带。
- **安全软件警告**：新生成、未签名的单文件 EXE 可能被 Windows 或安全软件提示；只在可信机器上构建，分发时考虑代码签名，不建议直接关闭安全防护。
- **运行不出现窗口**：先直接运行 `py -3 gui_calculator.py` 检查 GUI 能否正常启动。
- **想换图标**：准备 `.ico` 文件，并在 `calculator.spec` 的 `EXE(...)` 添加 `icon='your-icon.ico'`，然后重新打包。

参考文档：[PyInstaller 官方手册](https://pyinstaller.org/en/stable/usage.html)。
