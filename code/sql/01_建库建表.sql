-- ============================================
-- 01 建库建表（SQLite 语法，零安装）
-- ============================================

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
);

CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    credit INTEGER
);

CREATE TABLE IF NOT EXISTS scores (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    score INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
