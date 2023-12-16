from asyncio import get_event_loop

from app.bot import bot, dispatcher

event_loop = get_event_loop()
event_loop.run_until_complete(dispatcher.start_polling(bot))
