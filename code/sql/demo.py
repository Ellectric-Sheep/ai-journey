"""生成 demo.db 练习数据库（控制台版）
用法: python demo.py
"""
import sqlite3
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'demo.db')

if os.path.exists(DB):
    os.remove(DB)

conn = sqlite3.connect(DB)
cur = conn.cursor()

with open(os.path.join(HERE, '01_建库建表.sql'), encoding='utf-8') as f:
    cur.executescript(f.read())

cur.executescript("""
INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');
INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);
INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);
""")

conn.commit()
conn.close()
print('demo.db 已生成，可用可视化窗口打开练习')
