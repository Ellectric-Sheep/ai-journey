-- ============================================
-- 03 练习题（T-SQL 版）：先自己做，再看注释里的答案
-- 注意：T-SQL 没有 LIMIT，取前N条用 TOP N
-- ============================================

-- 1. 查出年龄最大的学生的姓名和专业
-- 答案: SELECT TOP 1 name, major FROM students ORDER BY age DESC;

-- 2. 查出每门课的选课人数
-- 答案: SELECT c.name, COUNT(sc.student_id) FROM courses c
--       LEFT JOIN scores sc ON sc.course_id = c.id GROUP BY c.name;

-- 3. 查出平均分高于 85 的课程名
-- 答案: SELECT c.name FROM courses c JOIN scores sc ON sc.course_id = c.id
--       GROUP BY c.name HAVING AVG(sc.score) > 85;

-- 4. 把张三的《数据结构》成绩改成 99
-- 答案:
-- UPDATE scores SET score = 99
-- WHERE student_id = (SELECT id FROM students WHERE name = N'张三')
--   AND course_id = (SELECT id FROM courses WHERE name = N'数据结构');

-- 5. 删除所有没有选课记录的学生
-- 答案: DELETE FROM students WHERE id NOT IN (SELECT DISTINCT student_id FROM scores);
