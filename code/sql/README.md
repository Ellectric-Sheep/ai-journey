# SQL 数据库学习区

## 本目录文件

| 文件 | 内容 |
|---|---|
| `01_建库建表.sql` | 学生/课程/成绩三张表（含 MySQL 差异注释） |
| `02_增删改查.sql` | CRUD + JOIN + GROUP BY 完整示例 |
| `03_练习题.sql` | 5 道练习题（答案在注释里） |
| `demo.py` | 一键生成 SQLite 数据库并跑查询（零安装） |

## 立即开始（不需要装任何数据库）

```bash
cd code/sql
python demo.py          # 生成 demo.db 并打印查询结果
```

生成 `demo.db` 后，用 VS Code 的 **SQLite Viewer** 插件直接点开看表和数据。

## 学习路线

1. **SQL 基础**（现在）：增删改查 → JOIN 联表 → GROUP BY 聚合 → 子查询。用 SQLite 练，语法 90% 通用
2. **进阶**：索引、事务、三大范式、ER 图设计
3. **接 Java**：JDBC 连接数据库 → 后面 web/backend 换 Spring Boot + MySQL 时就是同一套 SQL 知识

## 关于 MySQL

- SQLite 是零安装的"练手库"，适合学语法
- **MySQL** 是 Java 后端的行业标准，等学 web/backend 时再装（到时候我帮你装并配好）
- 两者 SQL 大同小异，先练 SQLite 完全不影响
