import os
from vkbottle.bot import Bot, Message
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')
bot = Bot(os.environ.get('VK_API_TOKEN'))


@bot.on.message(text="!бот <msg>")
async def upload_handler(message: Message, msg):
    model_engine = "text-davinci-003"
    prompt = msg
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=400, n=1, stop=None,
                                          temperature=0.5)
    text = completion.choices[0].text
    await message.reply(text)


if __name__ == "__main__":
    bot.run_forever()
