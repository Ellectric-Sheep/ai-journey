"""MySQL 练习库初始化（控制台版）
用法: python demo.py（需要 MySQL 服务已启动）
"""
import pymysql

CFG = dict(host='localhost', port=3306, user='root', password='root',
           charset='utf8mb4', autocommit=True)

conn = pymysql.connect(**CFG)
cur = conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS StudyDB DEFAULT CHARACTER SET utf8mb4')
conn.select_db('StudyDB')

for name, ddl in [
    ('students', '''CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT,
        major VARCHAR(50))'''),
    ('courses', '''CREATE TABLE IF NOT EXISTS courses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        credit INT)'''),
    ('scores', '''CREATE TABLE IF NOT EXISTS scores (
        student_id INT NOT NULL,
        course_id INT NOT NULL,
        score INT,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id))'''),
]:
    cur.execute(ddl)

cur.execute('DELETE FROM scores')
cur.execute('DELETE FROM students')
cur.execute('DELETE FROM courses')
cur.execute("INSERT INTO students (name, age, major) VALUES ('张三',20,'计算机科学'),('李四',21,'软件工程'),('王五',19,'人工智能')")
cur.execute("INSERT INTO courses (name, credit) VALUES ('数据结构',4),('操作系统',3),('计算机网络',3)")
cur.execute("INSERT INTO scores VALUES (1,1,92),(1,2,88),(2,1,76),(3,3,95)")

conn.close()
print('StudyDB 已初始化，可打开可视化窗口练习')
