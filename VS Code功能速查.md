# VS Code 各语言完整功能速查

> 你的环境已配好：Python / Java / C++ / Web / Git 全套插件 + Code Runner + Error Lens。
> 快捷键说明：`Ctrl+Shift+P` = 命令面板（万能入口，记不住就搜它）。

---

## 0. 通用神器（所有语言都适用）

| 功能 | 操作 |
|---|---|
| 跳转到定义 | `F12`（或 Ctrl+点击） |
| 悬浮速览定义 | `Alt+F12` |
| 查看所有引用 | `Shift+F12` |
| **重命名符号（全局安全改名）** | `F2` |
| 代码大纲跳转 | `Ctrl+Shift+O` 后输入名字 |
| 多光标编辑 | `Alt+Click` 加光标；`Ctrl+D` 选中下一个相同词 |
| 整行移动/复制 | `Alt+↑/↓` / `Shift+Alt+↑/↓` |
| 快速打开文件 | `Ctrl+P` |
| 全局搜索（支持正则） | `Ctrl+Shift+F` |
| 折叠/展开代码块 | `Ctrl+Shift+[` / `Ctrl+Shift+]` |
| 命令面板 | `Ctrl+Shift+P` |
| 注释行 | `Ctrl+/` |

## 调试三件套（F9 断点 → F5 开始 → F10/F11 单步）

| 键 | 功能 |
|---|---|
| `F9` | 打断点 / 取消断点 |
| `F5` | 开始调试（先选语言配置） |
| `F10` | 单步跳过（不进入函数） |
| `F11` | 单步进入（进入函数内部） |
| `Shift+F11` | 跳出当前函数 |
| 左侧调试面板 | 看**变量**实时值、**监视**表达式、**调用堆栈** |
| 条件断点 | 断点上右键 → 编辑断点 → 输入条件表达式 |
| 日志断点 | 断点上右键 → 日志点（不中断，只打印） |

---

## 1. Python 专属

| 功能 | 操作 |
|---|---|
| 自动补全 + 类型检查 | 打字即出（Pylance）；错误由 Error Lens 红字显示在行内 |
| 快速运行 | 右上角 ▶ 按钮，或 `Ctrl+F5`，或 `Ctrl+Alt+N`（Code Runner） |
| 调试 | `F5` 选「Python: 调试当前文件」 |
| 重构 | `F2` 重命名；右键 → Refactor → Extract Method（抽方法） |
| 快速修复 | 波浪线处点灯泡，或 `Ctrl+.`（自动导入、修 import 等） |
| 自动格式化 | 保存即用 black 格式化 |
| Lint 修复 | `Ctrl+Shift+P` → `Ruff: Fix all auto-fixable problems` |
| 切换解释器 | `Ctrl+Shift+P` → `Python: Select Interpreter` |
| Jupyter 笔记本 | 新建 `.ipynb` 文件；单元格内 `Shift+Enter` 运行；左侧变量面板看数据 |
| 查看函数文档 | 悬停函数名 |

## 2. Java 专属（redhat.java）

| 功能 | 操作 |
|---|---|
| 运行 / 调试 | 编辑器上方 **Run \| Debug** 按钮，或右键 → Run Java / Debug Java |
| 自动导包 | 打类名 → 回车自动 import；报错处 `Ctrl+.` 快速修复 |
| 生成代码 | 右键 → **Source Action** → Generate Getters/Setters / Constructors / toString |
| 重写方法 | 右键 → Source Action → Override/Implement Methods |
| 重构 | 右键 → Refactor → Rename / Extract Method |
| 查看类结构 | 右侧大纲（Outline），或 `Ctrl+Shift+O` |
| 格式化 | `Shift+Alt+F` |
| 单文件模式 | 目前你就是单文件练习，直接用 Code Runner `Ctrl+Alt+N` |

## 3. C / C++ 专属（cpptools）

| 功能 | 操作 |
|---|---|
| IntelliSense 补全 | 打字自动提示；悬停看函数签名 |
| 跳转定义/声明 | 右键 → Go to Definition / Declaration |
| 调用层次 | 函数上右键 → **Show Call Hierarchy**（谁调它/它调谁） |
| 编译并运行 | `Ctrl+Alt+N`（Code Runner，gcc/g++ 已配） |
| 调试 | `F5` 选「C: gcc」或「C++: g++」配置；可看变量、断点、**调用堆栈** |
| 内存查看 | 调试时变量右键 → View Memory（学指针利器） |
| 编译报错定位 | 问题面板 / `Ctrl+Shift+M`，点击直接跳到出错行 |

## 4. Web 前端专属

| 功能 | 操作 |
|---|---|
| 实时预览 | 右键 `index.html` → **Open with Live Server**（改代码自动刷新） |
| 格式化 | `Shift+Alt+F`（HTML/CSS/JS 内置格式化） |
| 标签跳转 | Ctrl+点击 class/id，跳到对应 CSS/JS 定义 |

## 5. Git / GitHub 专属

| 功能 | 操作 |
|---|---|
| 源代码管理面板 | `Ctrl+Shift+G`：`+` 暂存 → 写备注 → ✓ 提交 → 同步推送 |
| 行历史（GitLens） | 每行代码末尾淡色小字 = 谁在哪个提交改的；悬停看详情 |
| 文件历史 | 文件右键 → Open File History |
| 分支切换/新建 | 左下角分支名点击 |
| PR 管理 | 左侧 GitHub 图标面板 |

---

## 学习使用顺序（建议）

1. 第一周练会：`Ctrl+P` / `F12` / `F2` / `Ctrl+Shift+O`（导航四件套）
2. 第二周练会：`F9/F5/F10/F11` 断点调试（每个语言都调一遍）
3. 之后按需翻本表，用熟一个划掉一个

> 心法：**记不住快捷键没关系，`Ctrl+Shift+P` 输入功能名即可**——它列了所有命令。
