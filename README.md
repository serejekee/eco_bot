# 🤖 Простой чат-бот API на FastAPI

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

Простой API чат-бота на FastAPI. Принимает сообщения, отвечает (эхо-ответом) и сохраняет историю общения в базе данных.

---

## 🚀 Функциональность

- 📩 Приём сообщений от пользователя (`POST /message`)
- 💬 Ответ в формате: `Вы сказали: <текст>`
- 🗃️ Логирование всех сообщений в базу (SQLite)
- 📜 Получение истории переписки по `user_id` (`GET /history/{user_id}`)

---

## 🧰 Стек технологий

- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🛢️ [SQLite](https://www.sqlite.org/index.html) + [SQLAlchemy](https://www.sqlalchemy.org/)
- 🔐 [Pydantic](https://docs.pydantic.dev/)
- 🚀 [Uvicorn](https://www.uvicorn.org/)

---

## 📦 Установка и запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/fastapi-chatbot.git
cd fastapi-chatbot
```
2. Установить зависимости:  
```bash
pip install fastapi uvicorn sqlalchemy
```
3. Запустить сервер:
```bash
uvicorn main:app --reload
```
🔄 Примеры запросов
✅ Отправить сообщение

Запрос:
```json
{
  "user_id": "user123",
  "text": "Привет, бот!"
}
```
Reply:
```json
{
  "user_id": "user123",
  "text": "Привет, бот!",
  "response": "Вы сказали: Привет, бот!",
  "timestamp": "2025-05-14T12:00:00"
}
```

📜 Получить историю сообщений
GET /history/user123
Ответ:
```json
[
  {
    "user_id": "user123",
    "text": "Привет",
    "response": "Вы сказали: Привет",
    "timestamp": "2025-05-14T12:00:00"
  },
  ...
]
```

## 💡 Возможные улучшения
🔐 JWT-авторизация  
🤖 Интеграция с Telegram  
🌐 Веб-интерфейс (на React/Vue)  
📊 Аналитика и статистика по сообщениям  

## 📝 Лицензия
[MIT License](LICENSE) — бесплатно для использования,адаптируй, и изменяй 🤘
