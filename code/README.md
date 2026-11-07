# code 目录（多语言练习区，全部在 VS Code 完成）

## 一键运行（Code Runner，已配置）

打开任意代码文件 → 按 **`Ctrl+Alt+N`** 或点右上角 ▶ 运行按钮，自动编译并运行。

| 文件夹 | 语言 | 运行方式 |
|---|---|---|
| `c/` | C 语言 | `Ctrl+Alt+N`（gcc 编译运行）或 `F5` 调试 |
| `cpp/` | C++ | `Ctrl+Alt+N`（g++ 编译运行）或 `F5` 调试 |
| `java/` | Java | `Ctrl+Alt+N`（javac+java）或 `F5` 调试 |
| `python/` | Python | `Ctrl+Alt+N` 或 `Ctrl+F5` |
| `web/` | Web 全栈 | 前端：右键 index.html → Open with Live Server |

## 调试（F5，断点单步）

- Python：选中 Python 配置直接 F5
- Java / C / C++：F5 后选对应配置（首次选择一次，之后记住）

## 小贴士

- 保存即自动格式化（各语言默认格式化器已配）
- 编译产物（*.exe、*.class、bin、obj）已在资源管理器隐藏 + gitignore，眼不见心不烦
- 写错代码时 Error Lens 会在错误行直接显示红色提示，不用看终端
