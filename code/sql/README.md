# SQL 学习区（MySQL 版）

## 连接信息

| 项 | 值 |
|---|---|
| 主机 | localhost:3306 |
| 用户 | root |
| 密码 | root |
| 数据库 | StudyDB |

## 可视化窗口（双击即用）

**双击 `start-gui.bat`** → 弹出可视化窗口（连接 MySQL）：
- 左侧：数据表列表，点击浏览
- 上方：SQL 输入框（Ctrl+Enter 执行）
- 下方：结果表格 / 错误提示
- 「重置数据」按钮：一键还原

## 启动 / 停止 MySQL

- 启动：双击 `%LOCALAPPDATA%\Programs\MySQL\start-mysql.bat`
- 停止：双击 `stop-mysql.bat`
- 免安装版开机不自启，要用时先启动

## 命令行练习（可选）

```bash
mysql -u root -proot        # 进入 SQL 交互模式
```

## 文件说明

| 文件 | 内容 |
|---|---|
| `start-gui.bat` | 可视化练习窗口 |
| `01_建库建表.sql` | 建库建表 |
| `02_增删改查.sql` | CRUD 示例 |
| `03_练习题.sql` | 练习题（答案在注释） |
| `demo.py` | 命令行重置练习数据 |

## 学习路线

1. 双击可视化窗口 → 点左侧表熟悉结构
2. 敲 `SELECT * FROM students;` → Ctrl+Enter
3. 每天做 `03_练习题.sql` 的题
4. 进阶：JOIN → GROUP BY → 子查询 → 事务 → 索引
