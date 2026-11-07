# MySQL 学习区

## 连接信息

| 项 | 值 |
|---|---|
| 主机 | `localhost` |
| 端口 | `3306` |
| 用户 | `root` |
| 密码 | `root`（本地学习用，以后可改） |
| 练习库 | `StudyDB` |

## 可视化工具（轻量，二选一）

**① VS Code 插件（已装）**：左侧栏出现数据库图标 → 新建连接（localhost / root / root）→ 图形化看表、写 SQL
**② 命令行**：`mysql -u root -proot` 进入交互模式，输入 SQL 回车执行（和之前 practice.py 一样的感觉，但这是真数据库）

## 练习步骤

1. 打开 `01_建库建表.sql` → VS Code 里 `Ctrl+Shift+E` 执行（或右键 Run MySQL Query）
2. 执行 `02_增删改查.sql`
3. 每天从 `03_练习题.sql` 选题做

## 启动/停止 MySQL

- 启动：运行 `%LOCALAPPDATA%\Programs\MySQL\start-mysql.bat`
- 停止：运行 `%LOCALAPPDATA%\Programs\MySQL\stop-mysql.bat`
- 开机不会自动启动（免安装版），需要用时先启动

## 学习路线

1. **SQL 基础**（现在）：增删改查 → JOIN → GROUP BY → 子查询 → LIMIT
2. **进阶**：索引、事务、视图、存储过程
3. **接 Java**：JDBC 连接 MySQL → web/backend 做全栈项目
