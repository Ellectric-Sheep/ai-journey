-- ============================================
-- 02 增删改查（CRUD · T-SQL 语法）
-- ============================================

USE StudyDB;
GO

-- 增 INSERT
INSERT INTO students (name, age, major) VALUES (N'张三', 20, N'计算机科学');
INSERT INTO students (name, age, major) VALUES (N'李四', 21, N'软件工程');
INSERT INTO students (name, age, major) VALUES (N'王五', 19, N'人工智能');

INSERT INTO courses (name, credit) VALUES (N'数据结构', 4), (N'操作系统', 3), (N'计算机网络', 3);

INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);

-- 查 SELECT
SELECT * FROM students;

SELECT name, age FROM students WHERE age >= 20 ORDER BY age DESC;

-- 查：联表 JOIN
SELECT s.name AS 学生, c.name AS 课程, sc.score AS 分数
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id;

-- 查：聚合 GROUP BY
SELECT c.name AS 课程, AVG(sc.score) AS 平均分
FROM scores sc
JOIN courses c ON sc.course_id = c.id
GROUP BY c.name;

-- 改 UPDATE
UPDATE students SET age = 22 WHERE name = N'李四';

-- 删 DELETE
DELETE FROM scores WHERE score < 80;
GO
