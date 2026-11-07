-- ============================================
-- 01 建库建表（MySQL 语法）
-- ============================================

CREATE DATABASE IF NOT EXISTS StudyDB DEFAULT CHARACTER SET utf8mb4;
USE StudyDB;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    major VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    credit INT
);

CREATE TABLE IF NOT EXISTS scores (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
