"""MySQL 可视化练习窗口
依赖: pip install pymysql（已装）
双击 start-gui.bat 打开
连接: localhost:3306 root/root, 数据库 StudyDB
"""
import tkinter as tk
from tkinter import ttk
import pymysql

DB = 'StudyDB'
CFG = dict(host='localhost', port=3306, user='root', password='root',
           charset='utf8mb4', autocommit=False)

SEED = """
INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');
INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);
INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);
"""


def get_conn(db=None):
    kwargs = dict(CFG)
    if db:
        kwargs['database'] = db
    return pymysql.connect(**kwargs)


def ensure_db():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {DB} DEFAULT CHARACTER SET utf8mb4')
        conn.commit()
    finally:
        conn.close()


ensure_db()


class App:
    def __init__(self, root):
        self.root = root
        root.title('SQL 练习窗口 (MySQL)')
        root.geometry('1000x620')

        left = ttk.Frame(root, width=170)
        left.pack(side='left', fill='y', padx=6, pady=6)
        ttk.Label(left, text='数据表（点击浏览）').pack(anchor='w')
        self.tables = tk.Listbox(left)
        self.tables.pack(fill='both', expand=True, pady=4)
        self.tables.bind('<<ListboxSelect>>', self.show_table)

        right = ttk.Frame(root)
        right.pack(side='right', fill='both', expand=True, padx=6, pady=6)
        ttk.Label(right, text='SQL 输入（Ctrl+Enter 执行，可多句用 ; 分隔）').pack(anchor='w')
        self.sqlbox = tk.Text(right, height=7, font=('Consolas', 11))
        self.sqlbox.pack(fill='x')
        self.sqlbox.bind('<Control-Return>', lambda e: self.run_sql())

        btns = ttk.Frame(right)
        btns.pack(fill='x', pady=4)
        ttk.Button(btns, text='执行 SQL', command=self.run_sql).pack(side='left')
        ttk.Button(btns, text='重置数据', command=self.reset).pack(side='left', padx=8)

        ttk.Label(right, text='结果').pack(anchor='w')
        self.tree = ttk.Treeview(right, show='headings')
        self.tree.pack(fill='both', expand=True)

        self.refresh_tables()

    def show_table(self, _ev=None):
        sel = self.tables.curselection()
        if not sel:
            return
        name = self.tables.get(sel[0])
        self.run_query(f'SELECT * FROM {name} LIMIT 200')

    def refresh_tables(self):
        conn = get_conn(DB)
        try:
            with conn.cursor() as cur:
                cur.execute('SHOW TABLES')
                rows = cur.fetchall()
        except Exception:
            rows = []
        finally:
            conn.close()
        self.tables.delete(0, 'end')
        for r in rows:
            self.tables.insert('end', r[0])

    def run_sql(self):
        sql = self.sqlbox.get('1.0', 'end').strip()
        if not sql:
            return
        for stmt in sql.split(';'):
            stmt = stmt.strip()
            if stmt:
                self.run_query(stmt)

    def run_query(self, sql):
        conn = get_conn(DB)
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                if sql.lstrip().upper().startswith('SELECT'):
                    rows = cur.fetchall()
                    cols = [d[0] for d in cur.description] if cur.description else []
                    self.fill(cols, rows)
                else:
                    conn.commit()
                    self.fill(['结果'], [[f'执行成功，影响 {cur.rowcount} 行']])
                    self.refresh_tables()
        except Exception as e:
            self.fill(['错误'], [[str(e)]])
        finally:
            conn.close()

    def fill(self, cols, rows):
        self.tree.delete(*self.tree.get_children())
        self.tree['columns'] = cols
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120)
        for r in rows:
            self.tree.insert('', 'end', values=[str(v) for v in r])

    def reset(self):
        conn = get_conn(DB)
        try:
            with conn.cursor() as cur:
                cur.execute('DROP TABLE IF EXISTS scores')
                cur.execute('DROP TABLE IF EXISTS students')
                cur.execute('DROP TABLE IF EXISTS courses')
                cur.execute('''CREATE TABLE students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    age INT,
                    major VARCHAR(50)
                )''')
                cur.execute('''CREATE TABLE courses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    credit INT
                )''')
                cur.execute('''CREATE TABLE scores (
                    student_id INT NOT NULL,
                    course_id INT NOT NULL,
                    score INT,
                    PRIMARY KEY (student_id, course_id),
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                )''')
                for stmt in SEED.split(';'):
                    if stmt.strip():
                        cur.execute(stmt)
            conn.commit()
        except Exception as e:
            self.fill(['错误'], [[str(e)]])
        finally:
            conn.close()
        self.refresh_tables()
        self.fill(['结果'], [['数据已重置']])


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
