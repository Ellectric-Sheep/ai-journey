# Web 全栈（Java 后端）学习区

## 目录结构

```
web/
├── frontend/          # 前端：HTML + CSS + JavaScript
│   ├── index.html
│   ├── style.css
│   └── app.js
└── backend/           # 后端：Java
    └── Main.java      # 入口（目前是占位，后续接 Spring Boot）
```

## 现在怎么跑

**前端**：VS Code 打开 `index.html` → 右键 → 「Open with Live Server」（或直接双击用浏览器打开）。

**后端**（当前占位）：
```bash
cd web/backend
javac Main.java && java Main
```

## 学习路线（建议顺序）

1. 前端基础：HTML → CSS → JavaScript（先把手写页面练熟）
2. Java 后端：JDK 内置 HttpServer 做第一个接口（不引依赖）
3. 进阶：Spring Boot（到时候建独立项目，不混在这个文件夹）
4. 打通：前端 fetch 调后端接口，前后端联调
