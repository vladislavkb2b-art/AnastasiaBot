# AnastasiaBot - шаблон Telegram-бота для косметолога
В этом архиве — базовый проект Telegram-бота с админ-панелью в Telegram, записью клиентов и заготовкой для интеграции с DIKIDI Business.

## Быстрый старт
1. Установите Python 3.10+
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate   # Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Скопируйте `.env.template` в `.env` и вставьте туда `BOT_TOKEN` и `ADMIN_ID`.
5. Запустите бота:
   ```bash
   python bot.py
   ```

## Что включено
- Меню для клиентов: прайс, акции, запись, чат с админом
- Админ-панель в Telegram: просмотр заявок, создание акции, рассылка
- SQLite база (файл `data/bookings.db`)
- Заготовка `services/dikidi_api.py` для интеграции с DIKIDI Business (нужна доработка под API DIKIDI)
