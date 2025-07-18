### イメージ作成&コンテナ起動
```bash
docker compose -f docker-compose.dev.yml up -d --build
```

### マイグレーション
```bash
docker-compose -f docker-compose.dev.yml exec app python manage.py makemigrations
```

### マイグレーション適用
```bash
docker-compose -f docker-compose.dev.yml exec app python manage.py migrate
```

### Categoryテーブルに初期データ投入
```bash
docker-compose -f docker-compose.dev.yml exec app python manage.py loaddata basic_information/questions/fixtures/category.json
```

### スーパーユーザーを登録
```bash
docker-compose -f docker-compose.dev.yml exec app python manage.py createsuperuser
```

### 機能毎にアプリ作成　例:stampアプリ
```bash
docker-compose -f docker-compose.dev.yml run app python manage.py startapp stamp basic_information/stamp
```
