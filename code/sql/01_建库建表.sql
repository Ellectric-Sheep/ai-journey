-- ============================================
-- 01 建库建表（SQL Server / T-SQL 语法）
-- 连接后执行本文件即可
-- ============================================

-- 建库（已存在则跳过）
IF DB_ID('StudyDB') IS NULL
    CREATE DATABASE StudyDB;
GO

USE StudyDB;
GO

-- 学生表
CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,   -- 自增主键（从1开始每次+1）
    name NVARCHAR(50) NOT NULL,         -- 姓名
    age INT,                            -- 年龄
    major NVARCHAR(50)                  -- 专业
);

-- 课程表
CREATE TABLE courses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50) NOT NULL,         -- 课程名
    credit INT                          -- 学分
);

-- 选课成绩表（学生-课程 多对多）
CREATE TABLE scores (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT,                          -- 分数
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
GO
