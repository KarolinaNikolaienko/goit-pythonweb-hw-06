# Fullstack Python HW 6

Запустити команду для створення бази даних
```bash
docker run --name school_db -p 5432:5432 -e POSTGRES_PASSWORD=pythonweb6 -d postgres
```

Встановити залежності
```bash
pip install -r requirements.txt
```

Запустити скрипт додавання даних до бази
```bash
python seed.py
```