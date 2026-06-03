# Kairos Crypto Dashboard

Тестовое FullStack-приложение, разработанное в соответствии с техническим заданием. Проект включает адаптивную верстку по макету Figma, авторизацию через Google OAuth 2.0 и отображение актуальных цен криптовалют в режиме реального времени через Binance WebSocket API.

## Функциональность

- Адаптивная верстка по макету Figma
- Автоматически воспроизводящееся видео в Hero-секции
- Авторизация через Google OAuth 2.0
- Получение данных пользователя после успешного входа
- Отображение актуальных цен криптовалют в режиме реального времени
- Frontend на Vite
- Backend на FastAPI
- Без использования базы данных

## Структура проекта

```text
kairos-project/
│
├── backend/
│   ├── main.py
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── styles/
│   │   ├── ts/
│   │   └── index.html
│   │
│   ├── package.json
│   ├── vite.config.js
│   └── node_modules/
│
└── README.md
```

## Требования

Перед запуском убедитесь, что установлены:

- Node.js 18+
- npm
- Python 3.8+

---

## Настройка Backend

Перейдите в папку backend:

```bash
cd backend
```

Создайте виртуальное окружение:

```bash
python -m venv venv
```

Активируйте виртуальное окружение.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Установите зависимости:

```bash
pip install fastapi uvicorn requests python-dotenv authlib
```

---

## Создание файла .env

В папке `backend` создайте файл `.env`.

Добавьте в него следующие переменные:

```env
GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI=http://localhost:5000/auth/callback
FRONTEND_URL=http://localhost:5173
```

---

## Запуск Backend

Находясь в папке backend, выполните:

```bash
python main.py
```

После запуска сервер будет доступен по адресу:

```text
http://localhost:5000
```

---

## Настройка Frontend

Откройте новый терминал и перейдите в папку frontend:

```bash
cd frontend
```

Установите зависимости:

```bash
npm install
```

Запустите локальный сервер разработки:

```bash
npm run dev
```

После запуска приложение будет доступно по адресу:

```text
http://localhost:5173
```

---

## Проверка работы приложения

1. Откройте браузер и перейдите по адресу:

```text
http://localhost:5173
```

2. Убедитесь, что фоновое видео в Hero-секции запускается автоматически без звука.

3. Проверьте блок криптовалют. Цены должны обновляться в режиме реального времени через Binance WebSocket API.

4. Нажмите кнопку Google в карточке Online Banking.

5. Выполните вход через аккаунт Google.

6. После успешной авторизации произойдет возврат на сайт, а данные пользователя будут отображены в интерфейсе.

---

## Используемые технологии

### Frontend

- Vite
- Vanilla JavaScript
- CSS3
- WebSocket API

### Backend

- FastAPI
- Uvicorn
- Authlib
- Requests
- Python Dotenv

---

## Криптовалюты

Для получения актуальных данных используются WebSocket-потоки Binance.

Отображаются следующие криптовалюты:

- Bitcoin (BTC)
- Ethereum (ETH)
- Solana (SOL)
- XRP
- Binance Coin (BNB)
- USD Coin (USDC)

Данные обновляются без перезагрузки страницы.

