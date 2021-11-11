from telegram.ext import * 
import django 
import os
API_KEY= '2146792885:AAHJ3rF1CyX4Bx71V6cZmNrowT74T1s6E6M'
os.environ['DJANGO_SETTINGS_MODULE'] = 'telegram_bot.settings'
django.setup()
from bot.helper import get_data
import re
def isValidPinCode(pinCode):
     
    # Regex to check valid pin code
    # of India.
    regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$";
 
    # Compile the ReGex
    p = re.compile(regex);
     
    # If the pin code is empty
    # return false
    if (pinCode == ''):
        return False;
         
    # Pattern class contains matcher() method
    # to find matching between given pin code
    # and regular expression.
    m = re.match(p, pinCode);
     
    # Return True if the pin code
    # matched the ReGex else False
    if m is None:
        return False
    else:
        return True

def num(s):
    return any(i.isdigit() for i in s)

def handle_message(update,context):
    text=str(update.message.text).lower()
    if(num(text)):
        if(isValidPinCode(text)):
            d=get_data(text)
            update.message.reply_text(d)
        else:
            update.message.reply_text(f'Invalid pincode')
    else:
        update.message.reply_text(f"Hi,{update['message']['chat']['first_name']}")
        update.message.reply_text(f'please entre your pincode')
    # update.message.reply_text(f"Hi"+update.message.chat.first_name)
if __name__ == '__main__':
    
    update = Updater(API_KEY,use_context=True)
    dp = update.dispatcher
    # print(dp)
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    # print(dp.ad/d_handler)
    update.start_polling(1.0)
    update.idle()