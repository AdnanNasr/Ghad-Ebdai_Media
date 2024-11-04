import os
import re
import uuid
import yt_dlp
import random
import string
import asyncio
import subprocess
from PIL import Image
import assemblyai as aai
import aiofiles
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from concurrent.futures import ThreadPoolExecutor
from youtube_transcript_api import YouTubeTranscriptApi
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


load_dotenv()

executor = ThreadPoolExecutor()

TOKEN = os.getenv('token')
bot = AsyncTeleBot(TOKEN)
channel_id = '@ghad_ebdai_com'

# الاوامر الاساسية
#------------------------------------------------------------------------------------------------------------------------------------------------------
# امر البداية
@bot.message_handler(commands=['start'])
async def start(message):
    if await chick_follow(message):
        await main_menu(message.chat.id)

# امر رسالة المساعدة
@bot.message_handler(commands=['help'])
async def help(message):
    if await chick_follow(message=message):
        help_text = """
✨ مرحبًا بك في بوت Ghad-Ebdai Media! 🚀
مساعدك الذكي لتحميل ومشاركة المحتوى من مواقع التواصل الاجتماعي بسهولة وسرعة.

🔔 خطوات استخدام البوت:

1️⃣ الاشتراك في قناة البوت:

اضغط هنا للانضمام: 🔗 @ghad_ebdai_com

2️⃣ طرق التفاعل مع البوت:

🔹 من خلال الأوامر:

- /video لتحميل فيديو
- /audio لتحميل صوت
- /photo لتحميل صورة مصغرة
- /text لاستخراج النص من الفيديو

✨ بعد اختيار الأمر المناسب، أرسل رابط الفيديو الذي ترغب بمعالجته، وسيقوم البوت بالباقي.

🔹 من خلال الأزرار:

للبدء، أرسل أمر /start وستظهر لك قائمة بالأزرار المتاحة.
اضغط على الزر المطلوب، ثم أرسل الرابط المطلوب ليبدأ البوت في تنفيذ الأمر.

💡 استمتع بتجربة سلسة وواجهة مستخدم بسيطة مع Ghad-Ebdai Media!

"""

    await bot.send_message(message.chat.id, help_text)
    await main_menu(message.chat.id)

# دالة التواصل
@bot.message_handler(commands=['contact'])
async def contact(message):
    markup = InlineKeyboardMarkup(row_width=1)
    
    # إضافة أزرار الوصول للمواقع
    buttons = [
        InlineKeyboardButton("🌐 موقعي الرسمي", url="https://ghad-ebdai.com"),
        InlineKeyboardButton("📘 صفحتي على فايسبوك", url="https://www.facebook.com/ADN557/"),
        InlineKeyboardButton("💬 حسابي على تيليجرام", url="https://t.me/AdnCyber"),
        InlineKeyboardButton("👨‍💻 حسابي على GitHub", url="https://github.com/AdnanNasr")
    ]
    # إضافة الأزرار إلى اللوحة
    markup.add(*buttons)
    
    # إرسال رسالة تحتوي على اللوحة
    await bot.send_message(message.chat.id, "يمكن التواصل معي من خلال المواقع التالية: ", reply_markup=markup)

user_state = {}     # متغير لحفظ حالة المستخدم وتشغيل الوظائف

# دالة امر تحميل الفيديوهات
@bot.message_handler(commands=['video'])
async def vdieo_command(message):
    await bot.send_message(message.chat.id, 'ارسل لي رابط الفيديو الذي تريد تحميله.')
    user_state[message.chat.id] = 'video_url'
    
# دالة امر تحميل الاصوات
@bot.message_handler(commands=['audio'])
async def audio_command(message):
    await bot.send_message(message.chat.id, 'ارسل لي رابط الفيديو لإستخراج الصوت.')
    user_state[message.chat.id] = 'audio_url'

# دالة امر تحميل الصور المصغرة
@bot.message_handler(commands=['photo'])
async def photo_command(message):
    await bot.send_message(message.chat.id, 'ارسل لي رابط الفيديو لإستخراج الصورة المصغرة.')
    user_state[message.chat.id] = 'photo_url'

# دالة امر استخراج النص
@bot.message_handler(commands=['text'])
async def text_command(message):
    await bot.send_message(message.chat.id, 'ارسل لي رابط الفيديو لإستخراج النص.')
    user_state[message.chat.id] = 'text_url'

# دوال القوائم
#-------------------------------------------------------------------------------------------------------------------------------------------------------
user_button_message_ids = {}

# القائمة الرئيسية
async def main_menu(user_id):
    buttons = [
        ('تحميل فيديو', 'download_video'),
        ('تحميل صورة مصغرة', 'download_thumbnail'),
        ('تحميل صوت', 'download_audio'),
        ('استخراج النص من الفيديو', 'extract_text'),
    ]
    await send_buttons(user_id, 'قم باختيار الوظيفة التي تريد استخدامها من القائمة التالية:', buttons)


async def send_buttons(user_id, text, buttons):
    if user_id in user_button_message_ids:
        try:
            await bot.delete_message(user_id, user_button_message_ids[user_id])
        except Exception as e:
            print(f"Error deleting message: {e}")

    # إعداد الأزرار
    keyboard = InlineKeyboardMarkup()
    for i in range(0, len(buttons), 2):
        row = buttons[i:i + 2] 
        keyboard.add(*[InlineKeyboardButton(text=button_text, callback_data=callback_data) for button_text, callback_data in row])

    # إرسال الرسالة الجديدة
    message_to_send = await bot.send_message(user_id, text, reply_markup=keyboard)
    user_button_message_ids[user_id] = message_to_send.message_id

# استقبال الرسائل من المستخدم والتعامل معها
#--------------------------------------------------------------------------------------------------------------------------------------------------------
user_selected = {}
send_messages = {}
save_comming_message = {}

@bot.callback_query_handler(func=lambda call: True)
async def btn_handler(call):
    user_id = call.message.chat.id

    markup = InlineKeyboardMarkup()
    cancel = InlineKeyboardButton('الغاء', callback_data='cancel')
    markup.add(cancel)

    if call.data == 'download_video':
        user_selected[user_id] = 'download_video'
        await bot.answer_callback_query(call.id, 'ارسل رابط الفيديو')
        video_text = await bot.send_message(user_id, 'ارسل رابط الفيديو الذي تريد تحميله.', reply_markup=markup)
        send_messages[user_id] = video_text.message_id

    elif call.data == 'download_audio':
        user_selected[user_id] = 'download_audio'
        await bot.answer_callback_query(call.id, 'ارسل رابط الفيديو الذي تريد استخراج الصوت منه')
        audio_text = await bot.send_message(user_id, 'ارسل لي رابط الفيديو الذي تريد استخراج الصوت منه.', reply_markup=markup)
        send_messages[user_id] = audio_text.message_id

    elif call.data == 'download_thumbnail':
        user_selected[user_id] = 'download_thumbnail'
        await bot.answer_callback_query(call.id, 'ارسل رابط الفيديو لاستخراج الصورة المصغرة')
        thumbnail_text = await bot.send_message(user_id, 'ارسل رابط الفيديو لاستخراج الصورة المصغرة', reply_markup=markup)
        send_messages[user_id] = thumbnail_text.message_id

    elif call.data == 'extract_text':
        user_selected[user_id] = 'extract_text'
        await bot.answer_callback_query(call.id, 'ارسل رابط الفيديو لاستخراج النص منه')
        extract_text = await bot.send_message(user_id, 'ارسل رابط الفيديو لاستخراج النص منه', reply_markup=markup)
        send_messages[user_id] = extract_text.message_id
    
    elif call.data == 'cancel':
        if user_id in user_selected:
            del user_selected[user_id]
        if user_id in send_messages:
            message_id = save_comming_message.get(user_id) or send_messages[user_id]
            await bot.delete_message(user_id, message_id)
            del send_messages[user_id]  
        await main_menu(user_id)  

@bot.message_handler(func=lambda message: True)
async def handle_url_message(message):
    user_id = message.chat.id

    markup = InlineKeyboardMarkup()
    cancel = InlineKeyboardButton('الغاء', callback_data='cancel')
    markup.add(cancel)

    helper = ['المساعدة', 'ساعدني', 'احتاج الى مساعدة', 'مساعدة', 'كيف أستخدم البوت']
    welcome = ['مرحبا', 'السلام عليكم', 'أهلاً', 'مرحباً', 'هلا']
    welper = helper + welcome


    if any(word in message.text for word in welcome):
        hello_message = await bot.send_message(user_id, 'أهلاً وسهلاً! كيف يمكنني مساعدتك؟', reply_markup=markup)
        send_messages[user_id] = hello_message.message_id
        return

    if any(word in message.text for word in helper):
        await help(message)
        await main_menu(user_id)

    if user_id not in user_selected and not any(word in message.text for word in helper):
        await bot.send_message(user_id, 'لم تقم باختيار أي من خيارات البوت.\nاذا كنت بحاجة الى مساعدة قم بارسال "مساعدة" او /help')
        return

    # لتحميل الوسائط بناءً على الأوامر
    if user_state.get(user_id) == 'video_url':
        if chick_follow(message):
            if message.text.startswith('http') or message.text in welper:
                await ready_download_video(message)
                del user_state[message.chat.id]
                await main_menu(user_id, message.message_id)
            elif not message.text.startswith('http') or not message.text in welper:
                await bot.send_message(user_id, 'رجاءً ارسل رابط صالح!')

    elif user_state.get(user_id) == 'audio_url':
        if chick_follow(message):
            if message.text.startswith('http'):
                await ready_download_audio(message)
                del user_state[message.chat.id]
                await main_menu(user_id, message.message_id)
            elif not message.text.startswith('http'):
                await bot.send_message(user_id, 'رجاءً ارسل رابط صالح!')

    elif user_state.get(user_id) == 'photo_url':
        if chick_follow(message):
            if message.text.startswith('http'):
                await ready_download_thumbnail(message)
                del user_state[message.chat.id]
                await main_menu(user_id, message.message_id)
            elif not message.text.startswith('http'):
                await bot.send_message(user_id, 'رجاءً ارسل رابط صالح!')

    elif user_state.get(user_id) == 'text_url':
        if chick_follow(message):
            if message.text.startswith('http'):
                await reaey_extract_text(message)
                del user_state[message.chat.id]
                await main_menu(user_id, message.message_id)
            elif not message.text.startswith('http'):
                await bot.send_message(user_id, 'رجاءً ارسل رابط صالح!')

    # لتحميل الوسائط بناءً على الأزار
    selected_option = user_selected[user_id]

    if selected_option == 'download_video':
        if not message.text.startswith('http'):
            await bot.send_message(user_id, 'الرجاء إدخال رابط صالح.')
        else:
            await ready_download_video(message)
            del user_selected[user_id]
            await bot.delete_message(user_id,send_messages[user_id])
            await main_menu(user_id)

    elif selected_option == 'download_audio':
        if not message.text.startswith('http'):
            await bot.send_message(user_id, 'الرجاء إدخال رابط صالح.')
        else:
            await ready_download_audio(message)
            del user_selected[user_id]
            await bot.delete_message(user_id,send_messages[user_id])
            await main_menu(user_id)

    elif selected_option == 'download_thumbnail':
        if not message.text.startswith('http'):
            await bot.send_message(user_id, 'الرجاء إدخال رابط صالح.')
        else:
            await ready_download_thumbnail(message)
            del user_selected[user_id]
            await bot.delete_message(user_id,send_messages[user_id])
            await main_menu(user_id)
    
    elif selected_option == 'extract_text':
        if not message.text.startswith('http'):
            await bot.send_message(user_id, 'الرجاء إدخال رابط صالح.')
        else:
            await reaey_extract_text(message)
            del user_selected[user_id]
            await bot.delete_message(user_id,send_messages[user_id])
            await main_menu(user_id)


#دوال التحميل الجاهزة
#---------------------------------------------------------------------------------------------------------------------------------
# دالة تحميل الفيديوهات
async def ready_download_video(message):
    if await chick_follow(message):
                downloading = await bot.send_message(message.chat.id, 'جاري تحميل الفيديو...')
                video_files = await download_video(message.text)
                for file in video_files:
                    with open(file, 'rb') as video:
                        await bot.send_video(message.chat.id, video)
                    os.remove(file)
                await bot.delete_message(message.chat.id, downloading.message_id)

# دالة تحميل الأصوات
async def ready_download_audio(message):
    if await chick_follow(message):
                downloading = await bot.send_message(message.chat.id, 'جاري تحميل الصوت...')
                audio_files = await download_audio(message.text)
                for file in audio_files:
                    with open(file, 'rb') as audio:
                        await bot.send_audio(message.chat.id, audio)
                    os.remove(file)
                await bot.delete_message(message.chat.id, downloading.message_id)

# دالة تحميل الصور المصغرة
async def ready_download_thumbnail(message):
    if await chick_follow(message):
                downloading = await bot.send_message(message.chat.id, 'جاري تحميل الصور المصغرة...')
                thumbnail_files = await download_thumbnail(message.text)

                if isinstance(thumbnail_files, list):
                    for photo in thumbnail_files:
                        with open(photo, 'rb') as file:
                            await bot.send_photo(message.chat.id, file)
                        os.remove(photo)  
                
                elif thumbnail_files:
                    with open(thumbnail_files, 'rb') as file:
                        await bot.send_photo(message.chat.id, file)
                    os.remove(thumbnail_files)

                await bot.delete_message(message.chat.id, downloading.message_id)

# دالة استخراج النصوص
async def reaey_extract_text(message):
    if await chick_follow(message):
                try:
                    
                    downloading = await bot.send_message(message.chat.id, 'جاري استخراج النص من الفيديو...')
                    text = await transcript_youtube_text(message.text)

                    
                    random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.txt'

                    
                    async with aiofiles.open(random_filename, 'w', encoding='utf-8') as file_text:
                        for line in text:
                            await file_text.write(line + '\n')

                    
                    async with aiofiles.open(random_filename, 'rb') as file_to_send:
                        await bot.send_document(message.chat.id, file_to_send)

                    
                    await bot.delete_message(message.chat.id, downloading.message_id)
                    os.remove(random_filename)

                except Exception:
                    try:
                        await bot.send_message(message.chat.id, 'لم يتم العثور على ملف ترجمة او ملف شرح توضيحي، لذا سيتم استخراج النص باستخدام الذكاء الاصطناعي.\nقد يحتوي على بعض الأخطاء.')
                        audio_files = await extract_audio(message.text)
                        text = []
                        for audio_file in audio_files:
                            transcribed_text =  await transcribe_text(audio_file=audio_file)
                            text.append(transcribed_text)

                        
                        async with aiofiles.open(random_filename, 'w', encoding='utf-8') as save_file:
                            await save_file.write('\n'.join(text))

                        # إرسال الملف
                        async with aiofiles.open(random_filename, 'rb') as sending_file:
                            await bot.send_document(message.chat.id, sending_file)

                        
                        os.remove(random_filename)
                        await bot.delete_message(message.chat.id, downloading.message_id)

                    except Exception as f:
                        print(f'Error: {f}')

# دوال التحميل الخام
#-----------------------------------------------------------------------------------------------------------------------------------
# وظيفة تحميل الفيديوهات
async def download_video(url):
    video_files = []

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'%(id)s_{uuid.uuid4()}.mp4',
        'retries': 3
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=True)
        
        if 'entries' in video_info:
            for entry in video_info['entries']:
                file_name = ydl.prepare_filename(entry)
                if os.path.exists(file_name):
                    video_files.append(file_name)
        else:
            file_name = ydl.prepare_filename(video_info)
            if os.path.exists(file_name):
                video_files.append(file_name)

    return video_files

# وظيفة تحميل الأصوات
async def download_audio(url):

    audio_files = []

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'retries': 3
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=True)
        
        if 'entries' in video_info:
            for entry in video_info['entries']:
                file_name = ydl.prepare_filename(entry)
                if os.path.exists(file_name):
                    audio_files.append(file_name)
        else:
            file_name = ydl.prepare_filename(video_info)
            if os.path.exists(file_name):
                audio_files.append(file_name)

    return audio_files


# وظيفة تحميل الصور المصغرة
async def download_thumbnail(video_url):
    try:
        unique_id = str(uuid.uuid4())
        thumbnail_filename = f'{unique_id}.%(ext)s'

        command_download_thumbnail = [
            'yt-dlp', '--output', thumbnail_filename, '--write-thumbnail', '--skip-download', video_url
        ]

        await asyncio.get_event_loop().run_in_executor(
            None, lambda: subprocess.run(command_download_thumbnail, check=True)
        )

        downloaded_thumbnails = []

        for ext in ('webp', 'jpg'):
            image_path = f"{unique_id}.{ext}"
            if os.path.exists(image_path):
                
                if ext == 'webp':
                    image_path = await convert_image(image_path)
                    os.remove(f"{unique_id}.webp")
                
                downloaded_thumbnails.append(image_path)

        if len(downloaded_thumbnails) == 1:
            return downloaded_thumbnails[0]
        elif downloaded_thumbnails:
            return downloaded_thumbnails

        print("لم يتم العثور على أي صورة مصغرة")
        return None

    except subprocess.CalledProcessError as e:
        print(f"حدث خطأ أثناء تنزيل الصور المصغرة: {e}")
        


# وظيفة استخراج النصوص
async def transcript_youtube_text(url):
    
    match = re.search(r"(?:youtu\.be/|v=|\/v\/|embed\/|watch\?v=|\&v=)([^#\&\?]*)", url)
    text = []
    
    if match:
        video_id = match.group(1)
        print("معرف الفيديو:", video_id)

    try:
        # استدعاء YouTubeTranscriptApi.get_transcript بشكل غير متزامن
        transcript = await asyncio.to_thread(
            YouTubeTranscriptApi.get_transcript, video_id, languages=['ar', 'en', 'de', 'fr', 'es']
        )
        
        # جمع النصوص مباشرة وإرجاعها
        for line in transcript:
            lines = f'{line["text"]} '
            text.append(lines)

        return text

    except Exception as e:
        print(f"خطأ في جلب النصوص: {e}")
        
        try:    
            # تنزيل الصوت في حالة عدم توفر النص
            audio_files = await download_audio(url=url)
            for audio_file in audio_files:
                transcribed_text = await transcribe_text(audio_file=audio_file)
                text.append(transcribed_text)

            return text

        except Exception as f:
            print(f"خطأ في نسخ الصوت: {f}")



#وظائف جانبية
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# وظيفة لتحويل الصور لامتدادات مختلفة
async def convert_image(image):
    try:
        def process_image():
            im = Image.open(f"{image}").convert('RGB')
            im.save(f"{image}.jpg", 'JPEG')
            return f"{image}.jpg"
        
        image_name = await asyncio.get_event_loop().run_in_executor(executor, process_image)
        print('تم تحويل الصورة بنجاح.')
        return image_name

    except Exception as e:
        print(f'حدث خطأ أثناء التحويل: {e}')


# وظيفة تحميل الصوت من اجل النص
async def extract_audio(url):
    audio_files = []
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': './%(title)s.%(ext)s',
        'retries': 3
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=True)
        
        if 'entries' in video_info:
            for entry in video_info['entries']:
                file_name = ydl.prepare_filename(entry)
                if os.path.exists(file_name):
                    audio_files.append(file_name)
        else:
            file_name = ydl.prepare_filename(video_info)
            if os.path.exists(file_name):
                audio_files.append(file_name)

    return audio_files

# وظيفة استخراج النص من الفيديو باستخدام الذكاء الاصطناعي
api_key = os.getenv('assemblyAi')

async def transcribe_text(audio_file):
    aai.settings.api_key = api_key
    config = aai.TranscriptionConfig(
        speech_model=aai.SpeechModel.nano,
        language_detection=True,
        auto_chapters=True
    )
    transcriber = aai.Transcriber()
    
    # استخدام to_thread لجعل الدالة تعمل بشكل غير متزامن
    transcript = await asyncio.to_thread(transcriber.transcribe, audio_file, config=config)
    
    return transcript.text


# تقييد المستخدم
# -------------------------------------------------------------------------------------------------------------------------------------------------------
async def is_follow(user_id):
    try:
        user = await bot.get_chat_member(channel_id, user_id)
        if user.status in ['member', 'administrator', 'creator']:
            return True
    except:
        return False
    return False

async def chick_follow(message):
    user_id = message.from_user.id
    if not await is_follow(user_id):
        markup = InlineKeyboardMarkup()
        item = InlineKeyboardButton('الاشتراك في القناة', url='https://t.me/ghad_ebdai_com')
        markup.add(item)
        await bot.send_message(user_id, 'يرجى الاشتراك في القناة من اجل استخدام البوت: ', reply_markup=markup)
        return False
    return True


# تشغيل البوت
asyncio.run(bot.infinity_polling())