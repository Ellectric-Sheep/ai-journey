"""SQLite 可视化练习窗口（零安装：纯 Python 标准库）
双击 start-gui.bat 打开
"""
import sqlite3
import os
import tkinter as tk
from tkinter import ttk, messagebox

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


if not os.path.exists(DB):
    init_db()


class App:
    def __init__(self, root):
        self.root = root
        root.title('SQL 练习窗口 (SQLite)')
        root.geometry('1000x620')

        # 左侧：表列表
        left = ttk.Frame(root, width=170)
        left.pack(side='left', fill='y', padx=6, pady=6)
        ttk.Label(left, text='数据表（点击浏览）').pack(anchor='w')
        self.tables = tk.Listbox(left)
        self.tables.pack(fill='both', expand=True, pady=4)
        self.tables.bind('<<ListboxSelect>>', self.show_table)

        # 右侧：SQL 输入 + 结果
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
        ttk.Button(btns, text='清空结果', command=lambda: self.fill([], [])).pack(side='left')

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
        conn = sqlite3.connect(DB)
        rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
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
        conn = sqlite3.connect(DB)
        try:
            cur = conn.execute(sql)
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
        if os.path.exists(DB):
            os.remove(DB)
        init_db()
        self.refresh_tables()
        self.fill(['结果'], [['数据已重置']])


if __name__ == '__main__':
    root = tk.Tk()
    App(root)
    root.mainloop()
