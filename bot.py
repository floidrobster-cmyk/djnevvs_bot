import feedparser
import asyncio
from telegram import Bot

# Вставь сюда свой токен от BotFather
TOKEN = "8617452823:AAFFBo1yEpueWbDXlpJBNzs7YzaNU7eZhw0"

# Вставь сюда свой chat_id
CHAT_ID = "8258643868"

bot = Bot(token=TOKEN)
sent_news = set()

RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"

async def check_news():
    global sent_news
    feed = feedparser.parse(RSS_URL)
    entry = feed.entries[0]
    if entry.link not in sent_news:
        text = f"📰 {entry.title}\n{entry.link}"
        await bot.send_message(chat_id=CHAT_ID, text=text)
        sent_news.add(entry.link)

async def main():
    while True:
        await check_news()
        await asyncio.sleep(600)

asyncio.run(main())
