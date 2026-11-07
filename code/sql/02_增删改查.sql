-- ============================================
-- 02 增删改查（CRUD）：SQL 最核心的四件事
-- ============================================

-- 增 INSERT：插入数据
INSERT INTO students (name, age, major) VALUES ('张三', 20, '计算机科学');
INSERT INTO students (name, age, major) VALUES ('李四', 21, '软件工程');
INSERT INTO students (name, age, major) VALUES ('王五', 19, '人工智能');

INSERT INTO courses (name, credit) VALUES ('数据结构', 4), ('操作系统', 3), ('计算机网络', 3);

INSERT INTO scores VALUES (1, 1, 92), (1, 2, 88), (2, 1, 76), (3, 3, 95);

-- 查 SELECT：查询所有学生
SELECT * FROM students;

-- 查：条件筛选 + 排序
SELECT name, age FROM students WHERE age >= 20 ORDER BY age DESC;

-- 查：联表查询 JOIN —— 谁、哪门课、多少分
SELECT s.name AS 学生, c.name AS 课程, sc.score AS 分数
FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN courses c ON sc.course_id = c.id;

-- 查：聚合统计 GROUP BY —— 每门课的平均分
SELECT c.name AS 课程, AVG(sc.score) AS 平均分
FROM scores sc
JOIN courses c ON sc.course_id = c.id
GROUP BY c.name;

-- 改 UPDATE：把李四的年龄改成 22
UPDATE students SET age = 22 WHERE name = '李四';

-- 删 DELETE：删除分数低于 80 的记录
DELETE FROM scores WHERE score < 80;
