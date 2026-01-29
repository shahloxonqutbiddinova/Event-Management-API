Event Management API
Loyiha haqida

Ushbu loyiha Event Management REST API bo‘lib, foydalanuvchilarga tadbirlar yaratish, chiptalar qo‘shish va tadbir chiptalarini bron qilish imkoniyatini beradi.
Loyiha 8-oy yakuniy imtihoni uchun ishlab chiqilgan va barcha talablar to‘liq bajarilgan.

API Django Rest Framework asosida yozilgan va Swagger orqali hujjatlashtirilgan.

Loyihaning asosiy imkoniyatlari
🔐 Autentifikatsiya (Auth)

Foydalanuvchilar email orqali ro‘yxatdan o‘tadi

Email’ga 6 xonali tasdiqlash kodi yuboriladi

Kod tasdiqlangandan so‘ng foydalanuvchi JWT token oladi

Faqat tasdiqlangan foydalanuvchilar (DONE) asosiy funksiyalardan foydalanadi

📂 Category

Barcha foydalanuvchilar kategoriyalarni ko‘ra oladi

Kategoriya yaratish, tahrirlash va o‘chirish faqat tasdiqlangan foydalanuvchilar uchun

Category CRUD APIView orqali yozilgan

🎉 Event

Tadbirlar yaratish, ko‘rish, tahrirlash va o‘chirish mumkin

Event faqat tasdiqlangan foydalanuvchi tomonidan yaratiladi

Tadbirni faqat uning egasi (owner) tahrirlashi yoki o‘chirishi mumkin

Eventlar kategoriyalarga bog‘langan

Event CRUD ViewSet yordamida amalga oshirilgan

🎫 Ticket

Har bir event uchun bir nechta chipta yaratilishi mumkin

Chiptani faqat event egasi yaratishi mumkin

Ticket’da narx, miqdor va mavjud chipta soni nazorat qilinadi

Ticket CRUD ViewSet orqali yozilgan

🧾 Booking

Foydalanuvchilar chiptalarni bron qilishi mumkin

Booking faqat tasdiqlangan (DONE) foydalanuvchilar uchun

Foydalanuvchi faqat o‘z bronlarini ko‘ra oladi

Booking vaqtida ticket’ning mavjud soni avtomatik kamayadi

Booking CRUD ViewSet orqali yozilgan

🔐 Permissionlar

Loyihada quyidagi permission mantiqlari qo‘llangan:

Faqat autentifikatsiyadan o‘tgan foydalanuvchilar yopiq endpointlarga kira oladi

CRUD amallarida owner tekshiruvi mavjud

Booking va Ticket uchun maxsus permissionlar yozilgan

📘 Swagger dokumentatsiya

Loyiha Swagger (DRF Spectacular) orqali to‘liq hujjatlashtirilgan.

Swagger manzili:

/api/docs/


Bu yerda:

Barcha endpointlar

Request va Response formatlari

JWT token bilan test qilish imkoniyati mavjud

⚙️ Texnologiyalar

Python 3

Django

Django Rest Framework

JWT Authentication (SimpleJWT)

DRF Spectacular (Swagger)

SQLite (development uchun)

▶️ Loyihani ishga tushirish

Repository’ni yuklab oling:

git clone <github-repository-link>


Virtual environment yarating va aktiv qiling:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Kerakli kutubxonalarni o‘rnating:

pip install -r requirements.txt


Migratsiyalarni bajaring:

python manage.py migrate


Serverni ishga tushiring:

python manage.py runserver


Swagger’ni oching:

http://127.0.0.1:8000/api/docs/

🧪 Test qilish

API’ni:

Swagger orqali

Postman yoki curl yordamida

test qilish mumkin.

📌 Xulosa

Ushbu loyiha Event Management API uchun to'liq mos keladi

To‘liq CRUD

To‘g‘ri permissionlar

Swagger dokumentatsiya

Toza va tushunarli loyiha strukturasi
