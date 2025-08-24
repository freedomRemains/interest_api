# interest_api

- FastAPI ベースの関心事管理API。
- PEP 8 準拠（black/isort/flake8/pylint 設定込み）。
- **開発時は SQLite（H2 代替）**、CI/CD・本番は **MySQL** を想定。

## セットアップ（Windows）

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

## エンドポイント
- GET `/api/interests` : 関心事と紐づくアイテムのマップ取得
- POST `/api/interests` : 関心事を追加
- PUT `/api/interests/{id}` : 関心事を更新
- DELETE `/api/interests/{id}` : 関心事とアイテムの論理削除

## DB 初期化（MySQL）

```bash
mysql -u root -p interest_db < dbinit/schema.sql
mysql -u root -p interest_db < dbinit/data.sql
```
