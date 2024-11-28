# استخدام صورة بايثون الرسمية
FROM python:3.10

# تعيين مجلد العمل
WORKDIR /app

# نسخ الملفات إلى داخل الحاوية
COPY . /app


RUN pip install -r requirements.txt

# تشغيل الكود
CMD ["python", "app.py"]


