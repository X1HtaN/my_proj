import config
import logging
import emoji
import test19_1

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    await message.reply("привет!\nНапиши мне что-нибудь")

@dp.message_handler(commands="help")
async def process_help_command(message: types.Message):
    await message.reply("напиши мне что-нибудь и я отправлю этот текст тебе обратно")

@dp.message_handler(commands="eblan")
async def process_eblan_command(message: types.Message):
    await bot.send_message(message.from_user.id, "соси хуй быдло")

# @dp.message_handler(commands="list")
# async def process_list_command(message: types.Message):
#     await message.reply("введите запрос")
#     while True:
#         @dp.message_handler()
#         async def varior_help(message: types.Message):
#             await bot.send_message("выберите функцию: \n 1 перевод слова \n 2 добавление слова \n 3 удаление слова \n 4 открыть список \n 5 завершение работы\n")
#         @dp.message_handler()
#         async def varior_send(message: types.Message):
#             varior = message
#             await bot.send_message(message.from_user.id, varior)


    # if varior == "1":
    #     wordTrans = str(input("введите слово на английском: "))
    #     test19_1.translate(wordTrans)
    #     print("\n")
    # if varior == "2":
    #     wordAdd = str(input("введите слово на англ и через пробел его перевод: "))
    #     wordAdd = wordAdd.split()
    #     test19_1.add(wordAdd[0], wordAdd[1])
    # if varior == "3":
    #     wordDel = str(input("введите слово на англ, которое хотите удалить: "))
    #     test19_1.delete(wordDel)
    # if varior == "4":
    #     print("Список: ")
    #     test19_1.opening()
    # if varior == "5": 
    #     break

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)