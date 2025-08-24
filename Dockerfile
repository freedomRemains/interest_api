# Python 3.12 ベース
FROM python:3.12-slim

# 作業ディレクトリ
WORKDIR /app

# 必要パッケージをコピーしてインストール
COPY requirements.txt requirements-dev.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt -r requirements-dev.txt

# ソースコードをコピー
COPY app ./app
COPY dbinit ./dbinit

# FastAPI 実行（ホットリロードなしで本番想定）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
