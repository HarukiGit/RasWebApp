# ベースイメージとしてPythonを使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip list

# アプリケーションのソースコードをコピー
COPY . .

# コンテナ実行時のコマンドを指定
CMD ["python", "app.py"]
