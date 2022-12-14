import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables
yourkey = "6d1c7b0a"#os.getenv()
bot_id = "5919786879:AAHYYjEYuNV2B_0cqiJpVpDJUznQgmz8sU4"#os.getenv()

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')



@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    a = requests.get(f"http://www.omdbapi.com/?apikey={yourkey}&t={message.text[7::]}")  #api call for movie details your key -> omdb api
    a = a.json()  #converting api request to json or dict format
    ans = ''
    poster = 'bob'
    # TODO: 1.3 Show the movie information in the chat window
    #poster = requests.get(f"http://img.omdbapi.com/?apikey={yourkey}&t={message.text[7::]}")
    d = {}
    for i in a:
        if i in ["Title", "Year", "Released", "imdbRating"]:
            d[i] = a[i]
            ans += i+":"+a[i]+"\n"  # i-> dictionary key a[i] -> key value

        if i == "Poster" or a[i][:4:] == "http":
            try:  #try to get poster
                poster = requests.get(a[i])  #poster keywork -> poster url, requests.get() - > sending url api call
            except:  #give up and show question mark
                poster = requests.get("https://upload.wikimedia.org/wikipedia/commons/3/36/NULL.jpg")
    bot.send_photo(message.chat.id, poster.content, caption=ans)
    print(d)
    # TODO: 2.1 Create a CSV file and dump the movie information in it
    try:
        with open('movies.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Title", "Year", "Released", "imdbRating"])
            writer.writeheader()
            writer.writerow(d)
    except:
        bot.reply_to(message,"error creating csv file")
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    global chat_id
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    document = open('movies.csv', 'r')
    bot.send_document(message.chat_id, document)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
