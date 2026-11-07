# SQL Server 学习区

## 连接信息（配置好后）

| 项 | 值 |
|---|---|
| 服务器 | `localhost` |
| 认证 | SQL Server 身份验证 |
| 用户 | `sa` |
| 密码 | （你安装时设置的） |
| 练习库 | `StudyDB` |

## 连接方式（二选一）

**方式 A：VS Code（已装 mssql 插件）**
1. `Ctrl+Shift+P` → 输入 `MS SQL: Connect` → 填连接信息
2. 打开 .sql 文件 → `Ctrl+Shift+E` 执行选中语句

**方式 B：SSMS**（安装时一起勾选了，图形界面最直观）

## 练习步骤

1. 连接成功后，先执行 `01_建库建表.sql`（创建 StudyDB 和三张表）
2. 再执行 `02_增删改查.sql`（插入数据 + 各类查询）
3. 每天从 `03_练习题.sql` 选题，在查询窗口写自己的 SQL

## 学习路线

1. **T-SQL 基础**（现在）：增删改查 → JOIN → GROUP BY → 子查询 → TOP/排序
2. **进阶**：索引、事务、视图、存储过程
3. **接 Java**：JDBC 连接 SQL Server → web/backend 做全栈项目
