import sys
import time
import telepot
import urllib.request
from bs4 import BeautifulSoup
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Moive Ranking', callback_data='1')],
        [InlineKeyboardButton(text='Food Menu', callback_data ='2')],
        [InlineKeyboardButton(text='Choice 3', callback_data ='3')],
        ])
    bot.sendMessage(chat_id, 'Select the num', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    if query_data == '1':
        url = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
        soup = BeautifulSoup(url)
        pkg_list=soup.find_all('div','tit3')

        count =1
        final = "< Movie Ranking >\n"
        for i in pkg_list:
            title=i.find_all('a')
            #print(count, ".: ", str(title)[str(title).find('title="')+7:str(title).find('">')])
            
            cnt = str(count)
            string = cnt +" >>  "+ str(title)[str(title).find('title="')+7:str(title).find('">')] +"\n"
            count = count+1
            final = final + string
        bot.sendMessage(from_id, final)
    elif query_data == '2':
        bot.sendMessage(from_id,'< Food Menu >')
    elif query_data == '3':
        bot.sendMessage(from_id,'You select 3')
    
    bot.answerCallbackQuery(query_id, text='Got it')
# TOKEN = sys.argv[1]  # get token from command-line
TOKEN = '323407110:AAEEorwHpL9Rk-W7IDWj9GJlZlim0LemiJ4'

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message,'callback_query': on_callback_query})
print('Listening ...')

while 1:
    time.sleep(10)
