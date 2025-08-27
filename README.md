# 📡 Zibro Webhook Project

This project connects **TradingView alerts** to **Telegram** using a simple Flask server.

## 🚀 Features
- Receives webhook alerts from TradingView
- Forwards alerts directly to Telegram
- Lightweight and easy to deploy (Render, Heroku, or any VPS)

## Setup Instructions
1. Install dependencies: `pip install -r requirements.txt`
2. Replace your **Telegram Bot Token** and **Chat ID** in `zibro_webhook.py`
3. Run: `python zibro_webhook.py`
4. Or deploy on Render with:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn zibro_webhook:app`

## TradingView Alert JSON
```json
{
  "message": "Zibro Signal 🚀 BUY EURUSD @ {{close}}"
}
```

## Example Telegram Output
```
Zibro Signal 🚀 BUY EURUSD @ 1.0850
```
# zibro-webhook
# zibro-webhook
# zibro-webhook
