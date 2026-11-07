-- ============================================
-- 01 建库建表：学生成绩管理系统
-- 语法兼容 SQLite（零安装直接练）；MySQL 差异已注释标注
-- ============================================

-- 学生表
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- MySQL 写法: INT AUTO_INCREMENT
    name TEXT NOT NULL,                     -- 姓名
    age INTEGER,                            -- 年龄
    major TEXT                              -- 专业
);

-- 课程表
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,                     -- 课程名
    credit INTEGER                          -- 学分
);

-- 选课成绩表（学生-课程 多对多关联）
CREATE TABLE IF NOT EXISTS scores (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    score INTEGER,                          -- 分数
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
