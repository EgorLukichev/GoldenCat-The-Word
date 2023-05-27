import telebot
import requests
import json
bot = telebot.TeleBot('')
API = ''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! В каком городе узнаем погоду? Напиши название.')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')
        weather_data_structure = json.dumps(requests.get(url).json(), indent=2)
        weather_data = requests.get(url).json()
        ttemp = weather_data['wind']['speed']
        temperaturefeels = round(weather_data['main']['feels_like'])
        tttemp = weather_data['sys']['country']
        ttttemp = weather_data['wind']['speed']
        temperature = weather_data['main']['temp']
        temperature_feels = round(weather_data['main']['feels_like'])
        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./dat/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
        bot.reply_to(message, f'Вот ваша погода: {temp} °C ощущается как {temperature_feels} | {ttemp} Скорость ветра М/С')   


    else:
       image = 'errore.png'
       file = open('./dat/' + image, 'rb')
       bot.send_photo(message.chat.id, file)
       bot.reply_to(message, 'Ошибка! У вас нет сети или город введён не верно!')

bot.polling(none_stop=True)
