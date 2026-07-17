# 🤖 Ghad Ebdai Media Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telegram Bot API](https://img.shields.io/badge/Telegram-Bot_API-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Media_Downloader-red?style=for-the-badge&logo=youtube&logoColor=white)
![AssemblyAI](https://img.shields.io/badge/AssemblyAI-Speech--to--Text-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

**A modern Telegram bot for downloading, extracting, and processing multimedia content from hundreds of websites supported by `yt-dlp`, with optional AI-powered speech transcription using AssemblyAI.**

---

### 📚 Navigation

[Overview](#-overview) •
[Features](#-features) •
[Supported Platforms](#-supported-platforms) •
[Requirements](#-requirements) •
[Installation](#-installation) •
[Configuration](#-configuration) •
[Usage](#-usage) •
[Project Structure](#-project-structure) •
[Dependencies](#-key-dependencies) •
[Contributing](#-contributing) •
[License](#-license) •
[Contact](#-contact)

</div>

---

# 📋 Overview

**Ghad Ebdai Media Bot** is an open-source Telegram bot built with **Python** that allows users to download, extract, and process multimedia content from YouTube and hundreds of other websites supported by **yt-dlp**.

The bot provides a simple conversational interface inside Telegram while offering advanced media processing capabilities, including:

- High-quality video downloads
- Audio extraction
- Thumbnail downloading
- Subtitle extraction
- AI-powered speech transcription
- Automatic channel membership verification

Whenever subtitles are unavailable, the bot can automatically transcribe speech using **AssemblyAI**, making it possible to generate text directly from the audio.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 🎬 **Video Download** | Download the highest available video quality from supported websites |
| 🎵 **Audio Extraction** | Extract the best available audio stream from any supported video |
| 🖼️ **Thumbnail Download** | Download video thumbnails as JPEG images |
| 📝 **Subtitle Extraction** | Retrieve subtitles directly from YouTube whenever available |
| 🤖 **AI Speech-to-Text** | Automatically transcribe speech using AssemblyAI when subtitles are unavailable |
| 🌍 **Automatic Language Detection** | Detect spoken language automatically during AI transcription |
| 🔒 **Channel Subscription Guard** | Restrict bot usage to subscribed Telegram channel members |
| ⚡ **Fast Processing** | Efficient downloading and media processing |
| ⌨️ **Dual User Interface** | Supports both interactive buttons and slash commands |
| 📱 **Simple User Experience** | Designed for fast and intuitive interaction |

---

# 🌐 Supported Platforms

The bot supports **YouTube** and hundreds of additional websites through **yt-dlp**, including:

- YouTube
- YouTube Shorts
- TikTok
- Instagram
- Facebook
- X (Twitter)
- Vimeo
- SoundCloud
- Twitch
- Dailymotion

…and many more platforms officially supported by **yt-dlp**.

---

# 🛠️ Requirements

Before running the project, make sure you have the following installed:

- Python **3.10** or newer
- **ffmpeg** (required for audio extraction and media processing)
- Git
- Internet connection

You'll also need:

- A Telegram Bot Token from **@BotFather**
- An AssemblyAI API Key (optional but recommended for AI transcription)

---

# 📥 Installation

## 1. Clone the repository

```bash
git clone https://github.com/AdnanNasr/Ghad-Ebdai_Media.git
```

```bash
cd Ghad-Ebdai_Media
```

## 2. Install the required packages

```bash
pip install -r requirements.txt
```

---

# 🇸🇦 بوت غد إبداعي للوسائط

<div align="center">

**بوت تيليجرام حديث لتحميل واستخراج ومعالجة الوسائط من مئات المواقع التي يدعمها `yt-dlp`، مع إمكانية تحويل الكلام إلى نص باستخدام الذكاء الاصطناعي عبر AssemblyAI.**

</div>

---

# 📋 نظرة عامة

**بوت غد إبداعي للوسائط** هو مشروع مفتوح المصدر مبني بلغة **Python**، يتيح للمستخدمين تحميل ومعالجة الوسائط من يوتيوب ومئات المواقع الأخرى التي يدعمها **yt-dlp**.

يوفر البوت واجهة سهلة داخل تيليجرام مع مجموعة واسعة من المزايا، مثل:

- تحميل الفيديو بأعلى جودة
- استخراج الصوت
- تحميل الصورة المصغرة
- استخراج الترجمة
- تحويل الكلام إلى نص بالذكاء الاصطناعي
- التحقق من الاشتراك في قناة تيليجرام

عند عدم توفر ترجمة للفيديو، يستخدم البوت **AssemblyAI** لتحويل الصوت إلى نص مع دعم الكشف التلقائي عن اللغة.

---

# ✨ المميزات

| الميزة | الوصف |
|---------|--------|
| 🎬 **تحميل الفيديو** | تحميل الفيديو بأفضل جودة متاحة |
| 🎵 **استخراج الصوت** | استخراج أفضل مسار صوتي من الفيديو |
| 🖼️ **تحميل الصورة المصغرة** | تنزيل الصورة المصغرة بصيغة JPEG |
| 📝 **استخراج الترجمة** | جلب ترجمة يوتيوب مباشرةً عند توفرها |
| 🤖 **تحويل الكلام إلى نص** | استخدام AssemblyAI عند عدم وجود ترجمة |
| 🌍 **الكشف التلقائي عن اللغة** | التعرف على لغة المتحدث تلقائياً |
| 🔒 **التحقق من الاشتراك** | السماح باستخدام البوت للمشتركين فقط |
| ⚡ **معالجة سريعة** | سرعة في تحميل ومعالجة الوسائط |
| ⌨️ **واجهة مزدوجة** | يدعم الأوامر والأزرار التفاعلية |
| 📱 **سهولة الاستخدام** | واجهة بسيطة وسهلة لجميع المستخدمين |

---

# 🌐 المنصات المدعومة

يدعم البوت جميع المواقع التي يدعمها **yt-dlp**، ومن أشهرها:

- YouTube
- YouTube Shorts
- TikTok
- Instagram
- Facebook
- X (Twitter)
- Vimeo
- SoundCloud
- Twitch
- Dailymotion

بالإضافة إلى مئات المواقع الأخرى.

---

# 🛠️ المتطلبات

قبل تشغيل المشروع، تأكد من توفر:

- Python **3.10** أو أحدث
- ffmpeg
- Git
- اتصال بالإنترنت

كما ستحتاج إلى:

- توكن بوت من **@BotFather**
- مفتاح **AssemblyAI** (اختياري ولكنه موصى به لتحويل الكلام إلى نص)

---

# 📥 التثبيت

## 1. استنساخ المستودع

```bash
git clone https://github.com/AdnanNasr/Ghad-Ebdai_Media.git
```

```bash
cd Ghad-Ebdai_Media
```

---

# ⚙️ Configuration

Create a `.env` file in the project root and configure the following variables:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHANNEL_USERNAME=@YOUR_CHANNEL_USERNAME
ASSEMBLYAI_API_KEY=YOUR_ASSEMBLYAI_API_KEY
```

> **Note**
>
> Keep your `.env` file private and never upload it to GitHub.

---

# ▶️ Running the Bot

Start the bot by running:

```bash
python app.py
```

If everything is configured correctly, the bot will start listening for incoming Telegram messages.

---

# 📖 Usage

After starting the bot:

1. Open your bot in Telegram.
2. Send the `/start` command.
3. Subscribe to the required Telegram channel (if prompted).
4. Choose one of the available options or use a slash command.
5. Send a supported media URL.
6. Wait for the bot to process your request.
7. Receive the requested media or transcript.

---

# 💬 Available Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot and display the main menu |
| `/help` | Display help information |
| `/video` | Download a video |
| `/audio` | Extract audio from a video |
| `/photo` | Download the video thumbnail |
| `/text` | Extract subtitles or generate an AI transcript |
| `/contact` | Display the developer's contact information |

---

# 📁 Project Structure

```text
Ghad-Ebdai_Media/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── downloads/
│   ├── videos/
│   ├── audio/
│   ├── thumbnails/
│   └── transcripts/
│
└── temp/
```

> The actual project structure may vary depending on future updates.

---

# 📦 Key Dependencies

| Package | Purpose |
|----------|---------|
| pyTelegramBotAPI | Telegram Bot framework |
| yt-dlp | Download videos and audio from supported websites |
| assemblyai | AI speech-to-text transcription |
| youtube-transcript-api | Retrieve YouTube subtitles |
| Pillow | Convert and process images |
| aiofiles | Asynchronous file operations |
| python-dotenv | Load environment variables |
| nest-asyncio | Nested async event loop support |

---

# 🔄 Processing Workflow

```text
User
   │
   ▼
Telegram Bot
   │
   ▼
Validate Channel Subscription
   │
   ▼
Receive URL
   │
   ▼
yt-dlp
   │
   ├──────────────► Video
   │
   ├──────────────► Audio
   │
   ├──────────────► Thumbnail
   │
   └──────────────► Subtitle
                       │
                       ▼
               AssemblyAI (Fallback)
                       │
                       ▼
                 Send Result
```

---

# 🇸🇦 الإعداد

أنشئ ملفًا باسم `.env` داخل مجلد المشروع وأضف المتغيرات التالية:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHANNEL_USERNAME=@YOUR_CHANNEL_USERNAME
ASSEMBLYAI_API_KEY=YOUR_ASSEMBLYAI_API_KEY
```

> **ملاحظة**
>
> لا تقم برفع ملف `.env` إلى GitHub لأنه يحتوي على معلومات حساسة.

---

# ▶️ تشغيل البوت

بعد الانتهاء من الإعداد، شغّل البوت بواسطة:

```bash
python app.py
```

إذا كانت جميع الإعدادات صحيحة فسيبدأ البوت باستقبال الرسائل من تيليجرام.

---

# 📖 طريقة الاستخدام

1. افتح البوت في تيليجرام.
2. أرسل الأمر `/start`.
3. اشترك في القناة إذا طلب منك ذلك.
4. اختر العملية المطلوبة أو استخدم أحد الأوامر.
5. أرسل رابط الوسائط.
6. انتظر حتى تنتهي المعالجة.
7. سيقوم البوت بإرسال النتيجة إليك.

---

# 💬 الأوامر

| الأمر | الوصف |
|---------|--------|
| `/start` | تشغيل البوت |
| `/help` | عرض المساعدة |
| `/video` | تحميل فيديو |
| `/audio` | استخراج الصوت |
| `/photo` | تحميل الصورة المصغرة |
| `/text` | استخراج الترجمة أو تحويل الكلام إلى نص |
| `/contact` | معلومات المطور |

---

# 📁 هيكل المشروع

```text
Ghad-Ebdai_Media/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── downloads/
│   ├── videos/
│   ├── audio/
│   ├── thumbnails/
│   └── transcripts/
│
└── temp/
```

> قد يختلف هيكل المشروع قليلاً مع الإصدارات المستقبلية.

---

# 📦 المكتبات الرئيسية

| المكتبة | الاستخدام |
|----------|-----------|
| pyTelegramBotAPI | إنشاء بوت تيليجرام |
| yt-dlp | تحميل الفيديوهات والصوت |
| assemblyai | تحويل الكلام إلى نص |
| youtube-transcript-api | استخراج ترجمة يوتيوب |
| Pillow | معالجة الصور |
| aiofiles | التعامل مع الملفات بشكل غير متزامن |
| python-dotenv | قراءة متغيرات البيئة |
| nest-asyncio | دعم الحلقات غير المتزامنة |

---

# 🔄 آلية عمل البوت

```text
المستخدم
     │
     ▼
بوت تيليجرام
     │
     ▼
التحقق من الاشتراك
     │
     ▼
استقبال الرابط
     │
     ▼
yt-dlp
     │
     ├────────► فيديو
     ├────────► صوت
     ├────────► صورة مصغرة
     └────────► ترجمة
                     │
                     ▼
                AssemblyAI
                     │
                     ▼
            إرسال النتيجة للمستخدم
```

## 2. تثبيت المكتبات

```bash
pip install -r requirements.txt
```

---

# 🤝 Contributing

Contributions are welcome and appreciated.

If you want to improve the project, fix bugs, or add new features:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push your branch:

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

Before making major changes, please open an issue to discuss your idea.

---

# 🐛 Reporting Issues

If you find a bug or have a suggestion:

- Open a GitHub Issue.
- Describe the problem clearly.
- Include steps to reproduce the issue.
- Provide logs or screenshots if available.

This helps improve the project faster.

---

# ⭐ Support the Project

If you find this project useful:

- Give it a ⭐ on GitHub.
- Share it with others.
- Report bugs and suggest improvements.

Your support helps the project continue growing.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software according to the terms of the license.

See the `LICENSE` file for more information.

---

# 👨‍💻 Contact

Developed by **Adnan Nasr**

<div align="center">

[![Website](https://img.shields.io/badge/Website-adnannasr.com-blue?style=flat-square)](https://adnannasr.com)

[![Facebook](https://img.shields.io/badge/Facebook-ADN557-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/ADN557/)

[![Telegram](https://img.shields.io/badge/Telegram-@AdnCyber-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/AdnCyber)

[![GitHub](https://img.shields.io/badge/GitHub-AdnanNasr-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AdnanNasr)

</div>

---

<div align="center">

**Built with Python, Telegram Bot API, yt-dlp, and AI technologies.**

<br>

© 2026 Adnan Nasr

</div>


---

# 🇸🇦 المساهمة في المشروع

المساهمات مرحب بها ومقدّرة.

إذا كنت ترغب في تطوير المشروع أو إصلاح الأخطاء أو إضافة ميزات جديدة:

1. قم بعمل Fork للمستودع.
2. أنشئ فرعًا جديدًا:

```bash
git checkout -b feature/new-feature
```

3. قم بإجراء التعديلات المطلوبة.
4. أنشئ Commit:

```bash
git commit -m "Add new feature"
```

5. ارفع التغييرات:

```bash
git push origin feature/new-feature
```

6. قم بفتح Pull Request.

قبل إجراء تغييرات كبيرة، يُفضل فتح Issue لمناقشة الفكرة.

---

# 🐛 الإبلاغ عن المشاكل

إذا وجدت خطأ أو لديك اقتراح:

- افتح Issue في GitHub.
- اشرح المشكلة بشكل واضح.
- أضف خطوات إعادة ظهور المشكلة.
- أرفق السجلات أو الصور إن وجدت.

هذا يساعد على تحسين المشروع بشكل أسرع.

---

# ⭐ دعم المشروع

إذا وجدت المشروع مفيدًا:

- قم بإعطائه ⭐ على GitHub.
- شاركه مع الآخرين.
- ساهم بالإبلاغ عن الأخطاء واقتراح التحسينات.

دعمك يساعد على استمرار تطوير المشروع.

---

# 📄 الترخيص

هذا المشروع مرخص تحت **رخصة MIT**.

يمكنك استخدام المشروع وتعديله وتوزيعه وفق شروط الرخصة.

راجع ملف `LICENSE` للمزيد من المعلومات.

---

# 👨‍💻 التواصل

تم تطوير المشروع بواسطة **Adnan Nasr**

<div align="center">

[![Website](https://img.shields.io/badge/Website-adnannasr.com-blue?style=flat-square)](https://adnannasr.com)

[![Facebook](https://img.shields.io/badge/Facebook-ADN557-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/ADN557/)

[![Telegram](https://img.shields.io/badge/Telegram-@AdnCyber-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/AdnCyber)

[![GitHub](https://img.shields.io/badge/GitHub-AdnanNasr-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AdnanNasr)

</div>

---

<div align="center">

**تم تطويره باستخدام Python و Telegram Bot API و yt-dlp وتقنيات الذكاء الاصطناعي.**

<br>

© 2026 Adnan Nasr

</div>
