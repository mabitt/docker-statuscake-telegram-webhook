# docker-statuscake-telegram-webhook

Service to receive StatusCake webhooks and call Telegram Bot API to send alerts.

Usage:

```sh
docker run \
-e SC_USER='username (lowercase) ' \
-e SC_APIKEY='apikey' \
-e TELEGRAM_BOT_TOKEN='0000000:key' \
-e TELEGRAM_CHAT_ID='user or group id' \
-p 5000:5000 \
mabitt/statuscake-telegram-webhook
```

To debug, add:

```sh
-e LOGLEVEL='INFO' \
```
