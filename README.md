# 每天一小点 · AI 学习工作流

> 目标：每天 25~40 分钟 AI 学习，全部同步到 GitHub，形成「学习痕迹 + 复试作品集」
> 铁律：**考研优先** —— 每天先完成考研任务，AI 时间作为最后的「奖励时段」；考研执行未达标，次日砍掉 AI。

---

## 0. 核心原则

1. **每天一小点**：不追求一次学很多，只求「每天前进一点，留下一点」。
2. **全链路留痕**：学的东西 → 写成笔记 → 写成代码 → commit 到 GitHub。
3. **一石二鸟**：线代、概率、数据结构 = AI 地基 = 考研科目，AI 学习不冲突考研。
4. **复试即简历**：初试结束后，这个 GitHub 仓库就是你的 AI 经历证明。

---

## 1. 每日循环（Daily Loop · 25~40 分钟）

```
┌─ ① 学一点（15~20 分钟）
│    看一小节视频/文档（B站吴恩达、文档等）
├─ ② 记一笔（5~10 分钟）
│    用自己的话写笔记 → notes/ 对应 md 文件
├─ ③ 敲一点（10 分钟）
│    跑一小段代码（哪怕 10 行）→ code/ 对应文件夹
└─ ④ 留个痕（2 分钟）
     git add . && git commit && git push
     在 progress.md 打卡一行
```

**时间放哪**：建议固定放睡前 30 分钟，或考研任务完成后的「奖励时段」。

---

## 2. GitHub 仓库结构

```
ai-journey/
├── README.md          # 本工作流 + 目标
├── progress.md        # 每日打卡日志
├── notes/             # 学习笔记（按主题）
│   ├── python.md
│   ├── numpy-pandas.md
│   └── ml-week1.md
├── code/              # 练习代码（按主题分文件夹）
│   ├── python-basics/
│   ├── numpy-pandas/
│   └── ml-exercises/
├── projects/          # 小项目（初试后集中做）
└── resources.md       # 资料清单
```

---

## 3. Commit 规范与打卡

- Commit 格式：`day001: python 变量与类型`
- progress.md 打卡一行：

```
| 日期 | 天序号 | 学的内容 | commit |
| 2026-11-06 | day001 | Python 变量/类型 | a1b2c3d |
```

- **GitHub 贡献图变绿**是最好的可视化激励：每天一个小方块。

---

## 4. 学习路线图（按周 · 每天一小点）

| 周 | 主题 | 产出物 |
|---|---|---|
| 第 1~2 周 | Python 基础（变量、控制流、函数、文件） | notes/python.md + code/python-basics/ |
| 第 3~4 周 | NumPy + Pandas（矩阵运算、数据清洗） | notes/numpy-pandas.md + code/numpy-pandas/ |
| 第 5~8 周 | 吴恩达《Machine Learning》（作业用 NumPy 实现） | notes/ml-week*.md + code/ml-exercises/ |
| 之后 | **暂停**（考研冲刺期，仓库挂「暂停中」标记） | — |
| 初试后 | 深度学习 + PyTorch + 1~2 个小项目 | projects/ |

> 数学支撑：线性代数、概率论直接来自考研数学一；数据结构来自 408 —— AI 学习随时和考研互相印证。

---

## 5. 资料清单（全免费）

| 阶段 | 资料 | 渠道 |
|---|---|---|
| Python | 《Python编程：从入门到实践》/ 廖雪峰 Python 教程 | 书/网页 |
| 数学 | 吴恩达课程自带复习 + 考研线代概率 | B站 |
| 机器学习 | **吴恩达《Machine Learning》** | B站（免费） |
| 初试后 | 李沐《动手学深度学习》、PyTorch 官方教程 | B站/官网 |

---

## 6. 与考研的整合规则

- 🟢 **同步期（现在 ~ 2027.6）**：每天 25~40 分钟，考研达标才做。
- 🔴 **暂停期（2027.7 ~ 12）**：AI 全停，README 加「考研冲刺中，2028.1 恢复」。
- 🟢 **爆发期（2028.1 ~ 复试前）**：集中做深度学习 + 小项目，复试/联系导师直接展示 repo。

---

## 7. 今日启动（5 步）

```bash
# ① 在 GitHub 新建仓库 ai-journey（Public，不勾选 README）
# ② 本地初始化
mkdir ai-journey && cd ai-journey
git init

# ③ 把本工作流文档存为 README.md，并建目录
mkdir notes code projects

# ④ 首次提交
git add .
git commit -m "day000: 初始化 AI 学习工作流"
git branch -M main
git remote add origin https://github.com/<你的用户名>/ai-journey.git
git push -u origin main

# ⑤ 每日打卡（以后每天就是这 3 条）
git add .
git commit -m "day001: <今天学的内容>"
git push
```

> 新手可用 **GitHub Desktop** 替代命令行，效果一样。
> 编辑器用 **VS Code**；Python 可以本地装或用 Google Colab（在线免安装）。

---

### 一句话
**每天 30 分钟 → 学一点 → 记一笔 → 敲一点 → commit 一次。** 一年后你有一个「连续变绿的 GitHub + 完整笔记 + 代码作品」，复试时它就是你的 AI 简历。
