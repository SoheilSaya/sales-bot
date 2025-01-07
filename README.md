# Telegram Keyword Monitoring Bot | ربات نظارت بر کلمات کلیدی تلگرام
![Screenshot](Screenshot.png)
## 🇺🇸 English Description

A Telegram bot that monitors group messages for specific keywords and notifies a designated manager. The bot also maintains a phone number database of users.

### Features
- Monitors messages for specific keywords related to steel products (prices, inventory, rebar, etc.)
- Saves relevant messages to an Excel file with detailed information
- Maintains a phonebook of user contact information
- Sends instant notifications to the manager when keywords are detected
- Prevents duplicate phone number registrations
- Stores message links for easy access to original messages

### Installation
1. Clone this repository
2. Install required packages:
```bash
pip install python-telegram-bot openpyxl requests
```

### Configuration
Set the following variables in the code:
- `TOKEN`: Your Telegram bot token
- `MANAGER_ID`: Telegram ID of the manager who will receive notifications
- `keywords`: List of keywords to monitor

### Usage
1. Run the bot:
```bash
python bot.py
```
2. Start the bot in Telegram using `/start`
3. Share your phone number when prompted
4. The bot will automatically monitor messages and notify the manager when keywords are detected

### File Structure
- `messages.xlsx`: Stores messages containing keywords
- `phonebook.xlsx`: Stores user contact information

---

## 🇮🇷 توضیحات فارسی

یک ربات تلگرام که پیام‌های گروه را برای کلمات کلیدی خاص بررسی می‌کند و به مدیر تعیین شده اطلاع می‌دهد. این ربات همچنین یک پایگاه داده از شماره تلفن کاربران را نگهداری می‌کند.

### ویژگی‌ها
- نظارت بر پیام‌ها برای کلمات کلیدی مرتبط با محصولات فولادی (قیمت‌ها، موجودی، میلگرد و غیره)
- ذخیره پیام‌های مرتبط در فایل اکسل با اطلاعات دقیق
- نگهداری دفترچه تلفن اطلاعات تماس کاربران
- ارسال اعلان‌های فوری به مدیر هنگام تشخیص کلمات کلیدی
- جلوگیری از ثبت شماره تلفن تکراری
- ذخیره لینک پیام‌ها برای دسترسی آسان به پیام‌های اصلی

### نصب و راه‌اندازی
۱. کلون کردن مخزن
۲. نصب پکیج‌های مورد نیاز:
```bash
pip install python-telegram-bot openpyxl requests
```

### پیکربندی
تنظیم متغیرهای زیر در کد:
- `TOKEN`: توکن ربات تلگرام شما
- `MANAGER_ID`: شناسه تلگرام مدیری که اعلان‌ها را دریافت خواهد کرد
- `keywords`: لیست کلمات کلیدی برای نظارت

### نحوه استفاده
۱. اجرای ربات:
```bash
python bot.py
```
۲. شروع ربات در تلگرام با استفاده از `/start`
۳. اشتراک‌گذاری شماره تلفن هنگام درخواست
۴. ربات به طور خودکار پیام‌ها را نظارت کرده و در صورت تشخیص کلمات کلیدی به مدیر اطلاع می‌دهد

### ساختار فایل‌ها
- `messages.xlsx`: ذخیره پیام‌های حاوی کلمات کلیدی
- `phonebook.xlsx`: ذخیره اطلاعات تماس کاربران
