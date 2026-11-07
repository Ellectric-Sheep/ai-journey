-- ============================================
-- 02 增删改查（CRUD · MySQL 语法）
-- ============================================

USE StudyDB;

INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');

INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);

INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);

SELECT * FROM students;

SELECT name, age FROM students WHERE age >= 20 ORDER BY age DESC;

SELECT s.name AS 学生, c.name AS 课程, sc.score AS 分数
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id;

SELECT c.name AS 课程, AVG(sc.score) AS 平均分
FROM scores sc
JOIN courses c ON sc.course_id = c.id
GROUP BY c.name;

UPDATE students SET age = 22 WHERE name = '李四';

DELETE FROM scores WHERE score < 80;
