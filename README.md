# 待办清单 (Flask + MySQL + Vue)

一个简单的全栈示例项目，包含两个核心功能：

1. **查看待办列表** — 从 MySQL 读取并展示所有待办
2. **添加 / 完成 / 删除待办** — 增删改待办事项

## 项目结构

```
.
├── backend/          # Flask 后端 API
├── frontend/         # Vue 3 前端
├── docker-compose.yml
└── README.md
```

## 环境要求

- Python 3.10+
- Node.js 18+
- Docker（用于启动 MySQL，也可使用本地 MySQL）

## 快速开始

### 1. 启动 MySQL

```bash
docker compose up -d
```

默认配置：
- 主机：`127.0.0.1:3306`
- 用户：`root`
- 密码：`123456`
- 数据库：`todo_app`

### 2. 启动后端

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # macOS / Linux

python app.py
```

后端运行在 http://127.0.0.1:5000

### 3. 启动前端

```bash
cd frontend
npm install
npm run dev
```

前端运行在 http://127.0.0.1:5173

## API 接口

| 方法   | 路径                  | 说明       |
|--------|-----------------------|------------|
| GET    | `/api/todos`          | 获取待办列表 |
| POST   | `/api/todos`          | 新增待办     |
| PATCH  | `/api/todos/:id`      | 更新待办状态 |
| DELETE | `/api/todos/:id`      | 删除待办     |

## 上传到 Git 仓库

在项目根目录执行：

```bash
git init
git add .
git commit -m "init: flask mysql vue todo app"
git remote add origin <你的仓库地址>
git push -u origin main
```
