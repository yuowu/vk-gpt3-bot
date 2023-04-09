import os

from vkbottle.bot import Bot, Message
import openai


openai.api_key = os.getenv('openai_api_key')
bot = os.getenv('vkbottle_token')


messages = []        
queue = []


@bot.on.message(text="!бот <msg>")
async def upload_handler(message: Message, msg):
    try:
        if len(queue) >= 3:
            await message.reply("падажди")
        else:
            messages.append({"role": "user", "content": msg})
            queue.append(msg)
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
            reply = chat.choices[0].message.content
            await message.reply(f"{reply}")
            queue.remove(msg)
            messages.append({"role":"assistant", "content": reply})
    except openai.error.InvalidRequestError as e:
        await message.reply(f"Произошла ошибка: {e}")
        queue.remove(msg)
    except openai.error.OpenAIError as e:
        queue.remove(msg)
        await message.reply(f"Ошибка: {e.error} HTTP: ({e.http_status})")


if __name__ == "__main__":
  bot.run_forever()
