## これまでの事前質問を踏まえ、最初の依頼事項として、次の各項をAIにお願いしたいです。

[READMEに戻る](../README.md)

---

- pythonにてバックエンドのAPIを作成します。
  - pythonプロジェクトの親ディレクトリ名は「interest_api」とします。
  - プロジェクトディレクトリ直下に「md」ディレクトリを作成し、マークダウン資料を配置します。
  - 「md」ディレクトリと名前が被るソースコードディレクトリ構成を避けてください。
- pythonのコーディング規約として、PEP 8（Python Enhancement Proposal 8）に準拠してください。
  - ただしPEP 8よりも新しいコーディング規約がある場合は、その旨教えてください。
- FastAPIを使用してください。
- 作成するプロジェクトの設定には、次の自動チェックツールを含めてください。
  - flake8
  - black
  - isort
  - pylint
- pythonプロジェクトの親ディレクトリ「interest_api」は仮想環境で動かす前提とします。
- 本プロジェクトは自動テストとCI/CDに対応できるようにしてください。
- DBは開発時にh2、CI/CDや本番ではMySQLを使用しますので、そうした設定にも対応してください。
- DB構築を何度もできるよう「dbinit」フォルダに「data.sql」と「schema.sql」を配置してください。
- 「schema.sql」の内容は、次の通りとしてください。
  - DROP TABLE IF EXISTS ITEM;    -- アイテム(ITEM)があれば削除
  - DROP TABLE IF EXISTS INTEREST;    -- 関心事(INTEREST)があれば削除
  - CREATE TABLE IF NOT EXISTS INTEREST(    -- 関心事(INTEREST)を作成  
      INTEREST_ID INT NOT NULL AUTO_INCREMENT,    -- 関心事ID  
      TITLE VARCHAR(256),    -- 件名  
      VERSION INT,    -- バージョン  
      IS_DELETED INT,    -- 削除フラグ(0:未削除、1:削除済)  
      CREATED_BY VARCHAR(128),    -- 作成者  
      CREATED_AT DATETIME,    -- 作成日時  
      UPDATED_BY VARCHAR(128),    -- 更新者  
      UPDATED_AT TIMESTAMP,    -- 更新日時  
      PRIMARY KEY(INTEREST_ID)  
  );
  - CREATE TABLE IF NOT EXISTS ITEM(    -- アイテム(ITEM)を作成  
      ITEM_ID INT NOT NULL AUTO_INCREMENT,    -- アイテムID  
      ARTICLE VARCHAR(8192),    -- 記事  
      LINK VARCHAR(1024),    -- リンク  
      FILE_PATH VARCHAR(1024),    -- ファイルパス  
      INTEREST_ID INT,    -- 関心事ID(外部キー)  
      VERSION INT,    -- バージョン  
      IS_DELETED INT,    -- 削除フラグ(0:未削除、1:削除済)  
      CREATED_BY VARCHAR(128),    -- 作成者  
      CREATED_AT DATETIME,    -- 作成日時  
      UPDATED_BY VARCHAR(128),    -- 更新者  
      UPDATED_AT TIMESTAMP,    -- 更新日時  
      PRIMARY KEY(ITEM_ID)  
  );
- 次のREST APIを初期コードとして、自動テストコードと共に作成してください。
  - 関心事マップ取得(GET)
    - DBをクエリし、関心事(INTEREST)とそれに紐づくアイテム(ITEM)のマップを取得
  - 関心事追加(POST)
    - DBに新しい関心事(INTEREST)のレコードを追加。
  - 関心事更新(PUT)
    - 既存の関心事(INTEREST)のレコードを更新。
  - 関心事削除
    - DBから指定した関心事(INTEREST)とそれに紐づくアイテム(ITEM)を論理削除。
- 依頼内容が多いため、回答いただくソースコードはzipとしてください。

---

[READMEに戻る](../README.md)
