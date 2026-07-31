# 本地开发

## 安装

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
npm ci
cp .env.example .env
```

如果只维护后端，不需要安装 `trading` extra。TradingAgents adapter 开发时才执行：

```bash
python -m pip install -e '.[dev,trading]'
```

## 启动

```bash
cd src/backend
python main.py --host 127.0.0.1 --port 8080 --reload
```

现有代码使用 `src/backend` 作为 Python import 根，因此不要在未完成 import 迁移前改变工作目录。

## 测试

```bash
python -m pytest
npm run test:frontend
```

只跑认证与 Plaza 保护用例：

```bash
python -m pytest src/backend/tests -k 'auth or login or plaza or team'
npx vitest run src/frontend/__tests__/login-page-flow.test.js src/frontend/__tests__/plaza-action-paths.test.js
```

## 配置

- `.env.example` 只提供名称和安全默认值。
- 密钥不得写入 team factory、JSON fixture、浏览器存储、测试快照或 Issue。
- CI 使用虚拟值和 mock，不访问真实模型或市场服务。
- `STOCKAGENTS_TRADING_RUNTIME=disabled` 是默认值，第三方运行时必须显式启用。

## 常见问题

如果出现 `ModuleNotFoundError: agents`，请确认从 `src/backend` 启动服务，或通过根目录 `pyproject.toml` 运行 pytest。若前端测试找不到 Vitest，请在仓库根目录执行 `npm ci`。
