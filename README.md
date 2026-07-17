# 🤖 Ghad Ebdai Media Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Powered-red?style=for-the-badge&logo=youtube&logoColor=white)
![AssemblyAI](https://img.shields.io/badge/AssemblyAI-STT-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A powerful Telegram bot for downloading and extracting media content from social media platforms — powered by AI.**

[Features](#-features) • [Requirements](#-requirements) • [Setup](#-setup) • [Usage](#-usage) • [Contact](#-contact)

---

</div>

## 📋 Overview

**Ghad Ebdai Media Bot** is a feature-rich Telegram bot built with Python that allows users to download and process media content from YouTube and other supported platforms. It leverages `yt-dlp` for robust media downloading and **AssemblyAI** for AI-powered speech-to-text transcription — all through a simple and intuitive Telegram interface.

The bot enforces channel subscription before granting access, ensuring a growing and engaged community.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 **Video Download** | Download the best quality video from any supported URL |
| 🎵 **Audio Extraction** | Extract the best audio track from any video link |
| 🖼️ **Thumbnail Download** | Grab the video thumbnail as a JPEG image |
| 📝 **Text Extraction** | Extract transcripts from YouTube videos via subtitles or AI |
| 🤖 **AI Transcription** | Uses AssemblyAI with auto language detection as a fallback |
| 🔒 **Channel Guard** | Only subscribed members can use the bot |
| ⌨️ **Dual Interface** | Supports both slash commands (`/video`, `/audio`) and inline buttons |

---

## 🛠️ Requirements

- Python **3.10** or higher
- A **Telegram Bot Token** (from [@BotFather](https://t.me/BotFather))
- An **AssemblyAI API Key** (from [assemblyai.com](https://www.assemblyai.com/))
- `ffmpeg` installed and available in your system `PATH` (required by yt-dlp for some formats)

---

## 🚀 Setup

### Step 1 — Create a Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Start a chat and send the command: `/newbot`
3. Follow the on-screen instructions to name your bot.
4. Copy the **API Token** provided — you'll need it in the next step.

### Step 2 — Clone the Repository

```bash
git clone https://github.com/AdnanNasr/Ghad-Ebdai_Media.git
cd Ghad-Ebdai_Media
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure the Bot

Open `app.py` and set the following values:

```python
# Your Telegram Bot Token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'

# Your Telegram channel username (for subscription check)
channel_id = '@YOUR_CHANNEL_USERNAME'
```

Create a `.env` file in the project root and add your AssemblyAI key:

```env
assemblyAi=YOUR_ASSEMBLYAI_API_KEY_HERE
```

### Step 5 — Run the Bot

```bash
python app.py
```

Your bot is now live and ready to use! 🎉

---

## 📖 Usage

### Commands

| Command | Description |
|---|---|
| `/start` | Launch the bot and show the main menu |
| `/help` | Display usage instructions |
| `/video` | Download a video from a URL |
| `/audio` | Extract audio from a video URL |
| `/photo` | Download the thumbnail of a video |
| `/text` | Extract text/transcript from a video |
| `/contact` | Get developer contact information |

### How It Works

1. Send `/start` to open the interactive button menu **or** use a slash command directly.
2. Send the URL of the video you want to process.
3. The bot downloads/processes the media and sends it back to you.

> **Note:** You must be subscribed to the bot's Telegram channel to use it.

---

## 📦 Key Dependencies

| Package | Purpose |
|---|---|
| `pyTelegramBotAPI` | Async Telegram Bot framework |
| `yt-dlp` | Media downloading engine |
| `assemblyai` | AI-powered speech-to-text transcription |
| `youtube-transcript-api` | Fetch YouTube subtitles directly |
| `Pillow` | Image processing (WebP → JPEG conversion) |
| `aiofiles` | Async file I/O operations |
| `python-dotenv` | Load environment variables from `.env` |
| `nest-asyncio` | Nested async event loop support |

---

## 📁 Project Structure

```
Ghad-Ebdai_Media/
├── app.py              # Main bot application
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 👨‍💻 Contact

Developed by **Adnan Nasr**

[![Website](https://img.shields.io/badge/🌐_Website-adnannasr.com-blue?style=flat-square)](https://adnannasr.com)
[![Facebook](https://img.shields.io/badge/📘_Facebook-ADN557-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/ADN557/)
[![Telegram](https://img.shields.io/badge/💬_Telegram-@AdnCyber-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/AdnCyber)
[![GitHub](https://img.shields.io/badge/👨‍💻_GitHub-AdnanNasr-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AdnanNasr)

---

<div align="center">

---

# 🤖 بوت غد إبداعي للوسائط

**بوت تيليجرام قوي لتحميل واستخراج محتوى الوسائط من منصات التواصل الاجتماعي — مدعوم بالذكاء الاصطناعي.**

</div>

## 📋 نظرة عامة

**بوت غد إبداعي للوسائط** هو بوت تيليجرام متكامل مبني بلغة Python، يتيح للمستخدمين تحميل ومعالجة محتوى الوسائط من يوتيوب والمنصات المدعومة الأخرى. يستخدم البوت `yt-dlp` لتحميل الوسائط بشكل موثوق، و**AssemblyAI** لتحويل الكلام إلى نص بالذكاء الاصطناعي — وكل ذلك من خلال واجهة تيليجرام بسيطة وسهلة الاستخدام.

يشترط البوت الاشتراك في القناة قبل منح الوصول لضمان مجتمع متنامٍ ومتفاعل.

---

## ✨ المميزات

| الميزة | الوصف |
|---|---|
| 🎬 **تحميل الفيديو** | تحميل الفيديو بأفضل جودة من أي رابط مدعوم |
| 🎵 **استخراج الصوت** | استخراج أفضل مسار صوتي من أي رابط فيديو |
| 🖼️ **تحميل الصورة المصغرة** | الحصول على الصورة المصغرة للفيديو بصيغة JPEG |
| 📝 **استخراج النص** | استخراج النصوص من فيديوهات يوتيوب عبر الترجمة أو الذكاء الاصطناعي |
| 🤖 **النسخ بالذكاء الاصطناعي** | يستخدم AssemblyAI مع كشف اللغة التلقائي كخيار احتياطي |
| 🔒 **حماية القناة** | الأعضاء المشتركون فقط يمكنهم استخدام البوت |
| ⌨️ **واجهة مزدوجة** | يدعم الأوامر (`/video`, `/audio`) والأزرار التفاعلية |

---

## 🛠️ المتطلبات

- Python **3.10** أو أحدث
- **توكن بوت تيليجرام** (من [@BotFather](https://t.me/BotFather))
- **مفتاح API لـ AssemblyAI** (من [assemblyai.com](https://www.assemblyai.com/))
- تثبيت `ffmpeg` وإضافته إلى متغيرات النظام `PATH` (مطلوب من `yt-dlp` لبعض الصيغ)

---

## 🚀 طريقة الإعداد

### الخطوة 1 — إنشاء توكن بوت تيليجرام

1. افتح تيليجرام وابحث عن [@BotFather](https://t.me/BotFather).
2. ابدأ محادثة وأرسل الأمر: `/newbot`
3. اتبع التعليمات لتسمية البوت.
4. انسخ **التوكن** المُقدَّم — ستحتاجه في الخطوة التالية.

### الخطوة 2 — استنساخ المستودع

```bash
git clone https://github.com/AdnanNasr/Ghad-Ebdai_Media.git
cd Ghad-Ebdai_Media
```

### الخطوة 3 — تثبيت المكتبات

```bash
pip install -r requirements.txt
```

### الخطوة 4 — ضبط الإعدادات

افتح ملف `app.py` وعدّل القيم التالية:

```python
# توكن البوت الخاص بك
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'

# معرف قناتك على تيليجرام (للتحقق من الاشتراك)
channel_id = '@YOUR_CHANNEL_USERNAME'
```

أنشئ ملف `.env` في مجلد المشروع وأضف مفتاح AssemblyAI:

```env
assemblyAi=YOUR_ASSEMBLYAI_API_KEY_HERE
```

### الخطوة 5 — تشغيل البوت

```bash
python app.py
```

البوت الآن يعمل وجاهز للاستخدام! 🎉

---

## 📖 طريقة الاستخدام

### الأوامر

| الأمر | الوصف |
|---|---|
| `/start` | تشغيل البوت وعرض القائمة الرئيسية |
| `/help` | عرض تعليمات الاستخدام |
| `/video` | تحميل فيديو من رابط |
| `/audio` | استخراج الصوت من رابط فيديو |
| `/photo` | تحميل الصورة المصغرة لفيديو |
| `/text` | استخراج نص أو ترجمة من فيديو |
| `/contact` | الحصول على معلومات التواصل مع المطور |

### كيف يعمل البوت

1. أرسل `/start` لفتح قائمة الأزرار التفاعلية **أو** استخدم أحد الأوامر مباشرةً.
2. أرسل رابط الفيديو الذي تريد معالجته.
3. يقوم البوت بتحميل أو معالجة الوسائط وإرسالها إليك.

> **ملاحظة:** يجب أن تكون مشتركًا في قناة البوت على تيليجرام لاستخدامه.

---

## 📦 المكتبات الرئيسية

| المكتبة | الغرض |
|---|---|
| `pyTelegramBotAPI` | إطار عمل بوت تيليجرام غير المتزامن |
| `yt-dlp` | محرك تحميل الوسائط |
| `assemblyai` | تحويل الكلام إلى نص بالذكاء الاصطناعي |
| `youtube-transcript-api` | جلب ترجمات يوتيوب مباشرةً |
| `Pillow` | معالجة الصور (تحويل WebP إلى JPEG) |
| `aiofiles` | عمليات ملفات غير متزامنة |
| `python-dotenv` | تحميل متغيرات البيئة من ملف `.env` |
| `nest-asyncio` | دعم حلقة الأحداث غير المتزامنة المتداخلة |

---

## 👨‍💻 التواصل

تطوير **عدنان نصر**
[![Website](https://img.shields.io/badge/🌐_Website-adnannasr.com-blue?style=flat-square)](https://adnannasr.com)
[![Facebook](https://img.shields.io/badge/📘_Facebook-ADN557-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/ADN557/)
[![Telegram](https://img.shields.io/badge/💬_Telegram-@AdnCyber-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/AdnCyber)
[![GitHub](https://img.shields.io/badge/👨‍💻_GitHub-AdnanNasr-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AdnanNasr)
