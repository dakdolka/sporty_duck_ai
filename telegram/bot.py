from aiogram import Bot, Dispatcher
from core.config import settings
import asyncio

from .handlers import rt


bot = Bot(settings.telegram.token)
dp = Dispatcher()

dp.include_router(rt)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('start')
    asyncio.run(main())