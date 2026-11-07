"""交互式 SQL 练习器
用法: python practice.py
- 输入一句 SQL，回车执行看结果
- 输入 reset 重置数据；输入 exit 退出
"""
import sqlite3
import os
import sys

# 统一 UTF-8，避免中文乱码
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'demo.db')

SEED = """
INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');
INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);
INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);
"""


def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    with open(os.path.join(HERE, '01_建库建表.sql'), encoding='utf-8') as f:
        cur.executescript(f.read())
    cur.executescript(SEED)
    conn.commit()
    conn.close()


def reset_data():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('DELETE FROM scores')
    cur.execute('DELETE FROM students')
    cur.execute('DELETE FROM courses')
    cur.executescript(SEED)
    conn.commit()
    conn.close()


if not os.path.exists(DB):
    init_db()
    print('已生成练习数据库 demo.db\n')

conn = sqlite3.connect(DB)

print('=' * 50)
print('SQL 交互练习器')
print('表: students(id,name,age,major)')
print('     courses(id,name,credit)')
print('     scores(student_id,course_id,score)')
print('输入 SQL 回车执行 | reset 重置数据 | exit 退出')
print('=' * 50)

while True:
    try:
        sql = input('\nSQL> ').strip()
    except EOFError:
        break
    if not sql:
        continue
    if sql.lower() in ('exit', 'quit'):
        break
    if sql.lower() == 'reset':
        reset_data()
        print('数据已重置')
        continue
    try:
        cur = conn.execute(sql)
        if sql.lstrip().upper().startswith('SELECT'):
            rows = cur.fetchall()
            if rows:
                for r in rows:
                    print(r)
                print(f'({len(rows)} 行)')
            else:
                print('查询结果为空')
        else:
            conn.commit()
            print(f'执行成功，影响 {cur.rowcount} 行')
    except Exception as e:
        print(f'SQL 错误: {e}')

conn.close()
print('再见 👋')
