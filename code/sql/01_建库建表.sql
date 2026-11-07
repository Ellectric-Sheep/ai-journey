-- ============================================
-- 01 建库建表（MySQL 语法）
-- ============================================

CREATE DATABASE IF NOT EXISTS StudyDB DEFAULT CHARACTER SET utf8mb4;
USE StudyDB;

-- 学生表
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增主键
    name VARCHAR(50) NOT NULL,          -- 姓名
    age INT,                            -- 年龄
    major VARCHAR(50)                   -- 专业
);

-- 课程表
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,          -- 课程名
    credit INT                          -- 学分
);

-- 选课成绩表（学生-课程 多对多）
CREATE TABLE IF NOT EXISTS scores (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT,                          -- 分数
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
