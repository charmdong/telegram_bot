import sys
import time
import telepot
import urllib.request
from bs4 import BeautifulSoup
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from selenium import webdriver

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='학생회관 메뉴', callback_data='1')],
        [InlineKeyboardButton(text='찬 스카이라운지', callback_data ='2')],
        [InlineKeyboardButton(text='우정당', callback_data ='3')],
        [InlineKeyboardButton(text='진관홀', callback_data ='4')],
        ])
    bot.sendMessage(chat_id, 'Select the num', reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    if query_data == '1':
        url = urllib.request.urlopen('http://m.sejong.ac.kr/front/cafeteria.do')
        soup = BeautifulSoup(url)
        food_list = soup.find_all('div','th')
        price_list = soup.find_all('div','td price')
        count = len(food_list)
        cnt_list = [i for i in range(count)]
       	name = ""
       	price = ""
       	total = "\n<학생회관 학식 메뉴>\n\n"
        
        for i in cnt_list:
        	name = str(food_list[i])[str(food_list[i]).find('>')+1: str(food_list[i]).find('</')] 
        	price = str(price_list[i])[str(price_list[i]).find('>')+1 :str(price_list[i]).find('</')]
        	total = total + name + " : "+ price + "\n"
        bot.sendMessage(from_id,total)
    
    elif query_data == '2':
        web = webdriver.Firefox()
        web.get('http://m.sejong.ac.kr/front/cafeteria.do')

        btn = web.find_elements_by_class_name('tab')
        btn[1].click()

        url = urllib.request.urlopen('http://m.sejong.ac.kr/front/cafeteria.do')
        soup = BeautifulSoup(url)
        day_list = soup.find_all('div','th')
        food_list = soup.find_all('div','td price')
        count = len(food_list)
        cnt_list = [i for i in range(count)]
       	name = ""
       	price = ""
       	total = "\n<찬 스카이라운지 메뉴>\n\n"
        
        for i in cnt_list:
        	name = str(food_list[i])[str(food_list[i]).find('>')+1: str(food_list[i]).find('</')] 
        	price = str(price_list[i])[str(price_list[i]).find('>')+1 :str(price_list[i]).find('</')]
        	total = total + name + " : "+ price + "\n"
        bot.sendMessage(from_id,total)

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
