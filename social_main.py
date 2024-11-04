import yt_dlp
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv
import shutil
from datetime import datetime
import requests.exceptions

load_dotenv()

API_TOKEN = os.getenv('')
bot = telebot.TeleBot(token=API_TOKEN)

social_media_sites = [
    "YouTube",
    "Instagram",
    "TikTok",
    "Facebook",
    "Twitter",
    "Reddit",
    "VK",
    "Snapchat",
    "Pinterest",
    "Tumblr"
]

@bot.message_handler(commands=['start', 'social_media'])
def send_social_media_list(message):

    markup = InlineKeyboardMarkup()
    item1 = InlineKeyboardButton(text='Facebook', callback_data='facebook') 
    item2 = InlineKeyboardButton(text='YouTube', callback_data='youtube') 
    item3 = InlineKeyboardButton(text='Instagram', callback_data='instagram') 
    item4 = InlineKeyboardButton(text='Tiktok', callback_data='tiktok') 
    item5 = InlineKeyboardButton(text='Twitter', callback_data='twitter') 
    item6 = InlineKeyboardButton(text='Reddit', callback_data='reddit') 
    item7 = InlineKeyboardButton(text='Snapchat', callback_data='snapchat') 
    item8 = InlineKeyboardButton(text='Pinterest', callback_data='pinterest')
    markup.row(item1, item2, item3)
    markup.row(item4, item5, item6) 
    markup.row(item7, item8) 
    
    bot.send_message(message.chat.id, "هناك العديد من مواقع التواصل الاجتماعي والمنصات التي يمكن لهذا البوت تنزيل الفيديوهات منها.\n\nومن اهم هذه المواقع: ", reply_markup=markup)
    bot.register_next_step_handler(message, get_message)

downloaded_files = []

def my_hook(d, chat_id, download_msg):
    
    if d['status'] == 'finished':  
        file_name = d['info_dict']['_filename']
        if file_name not in downloaded_files:  
            downloaded_files.append(file_name)

@bot.message_handler(func=lambda message: True)
def get_message(message):
    user_input = message.text
    if user_input.startswith("http"):

        download_msg = bot.send_message(message.chat.id, "جاري تنزيل الفيديو...")

        folder_name = create_download_folder()
        download_videos(user_input, folder_name, message.chat.id, download_msg)  

        if downloaded_files:  
            for file_name in downloaded_files:  
                video_path = os.path.join(folder_name, os.path.basename(file_name))  
                try:
                    with open(video_path, 'rb') as video_file:
                        bot.send_video(message.chat.id, video=video_file, timeout=50)
                except requests.exceptions.SSLError:
                    bot.send_message(message.chat.id, "حدث خطأ في الاتصال أثناء إرسال الفيديو. حجم الفيديو كبير جداً.")
                    return  

            bot.delete_message(message.chat.id, download_msg.message_id)

            clear_download_folder(folder_name)
            downloaded_files.clear()  
            print('Finish')
        else:
            bot.send_message(message.chat.id, "فشل في تنزيل الفيديو.")
    else:
        bot.send_message(message.chat.id, f"لقد أرسلت رسالة: {user_input}")

def create_download_folder():
    folder_name = f"downloads_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def get_video_info(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False) 
        return info_dict

def download_videos(url, folder_name, chat_id, download_msg):
    global downloaded_files
    downloaded_files.clear()  

    info_dict = get_video_info(url)

    file_size = info_dict.get('filesize')

    duration = info_dict.get('duration')

    if file_size is None or duration is None:
        ydl_opts = {
            'format': 'bestvideo[height<=480]+bestaudio/best',
            'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
            'progress_hooks': [lambda d: my_hook(d, chat_id, download_msg)],
            'merge_output_format': 'mp4'
        }
    else:
        if file_size > 45 * 1024 * 1024 or duration > 1800:
            ydl_opts = {
                'format': 'bestvideo[height<=360]+bestaudio/best',
                'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
                'progress_hooks': [lambda d: my_hook(d, chat_id, download_msg)],
                'merge_output_format': 'mp4'
            }

        elif file_size > 45 * 1024 * 1024 or duration > 600: 
            ydl_opts = {
                'format': 'bestvideo[height<=720]+bestaudio/best', 
                'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
                'progress_hooks': [lambda d: my_hook(d, chat_id, download_msg)],
                'merge_output_format': 'mp4'
            }
        else:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  
                'outtmpl': os.path.join(folder_name, '%(title)s.%(ext)s'),
                'progress_hooks': [lambda d: my_hook(d, chat_id, download_msg)],
                'merge_output_format': 'mp4'
            }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url]) 

def clear_download_folder(folder_name):
    shutil.rmtree(folder_name)

bot.infinity_polling()