"""SQLite 零安装演示：不用装任何数据库，直接运行本脚本练 SQL"""
import sqlite3
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'demo.db')

# 每次重跑都是全新数据库
if os.path.exists(DB):
    os.remove(DB)

conn = sqlite3.connect(DB)
cur = conn.cursor()

# 建表（内容和 01_建库建表.sql 一致）
with open(os.path.join(HERE, '01_建库建表.sql'), encoding='utf-8') as f:
    cur.executescript(f.read())

# 插入数据
cur.executescript("""
INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');
INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);
INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);
""")

print('=== 1. 所有学生 ===')
for r in cur.execute('SELECT * FROM students'):
    print(r)

print('=== 2. 联表查询：学生 - 课程 - 分数 ===')
for r in cur.execute('''
    SELECT s.name, c.name, sc.score
    FROM scores sc
    JOIN students s ON sc.student_id = s.id
    JOIN courses c ON sc.course_id = c.id
'''):
    print(r)

print('=== 3. 每门课平均分 ===')
for r in cur.execute('''
    SELECT c.name, AVG(sc.score)
    FROM scores sc JOIN courses c ON sc.course_id = c.id
    GROUP BY c.name
'''):
    print(r)

conn.commit()
conn.close()
print(f'\n数据库已生成: {DB}')
