````markdown
# FastAPI Auth Demo

پروژه‌ای برای پیاده‌سازی سیستم احراز هویت امن با FastAPI، JWT و OAuth2.

## مراحل نصب

```bash
pip install -r requirements.txt
export DATABASE_URL="postgresql+asyncpg://user:pass@localhost/db"
export JWT_SECRET="your-secret"
````

## اجرای پروژه

برای راه‌اندازی سرور توسعه:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

سپس به آدرس [http://localhost:8000/docs](http://localhost:8000/docs) برو تا مستندات Swagger را ببینی.

## اجرای تست‌ها

۱. اطمینان از در دسترس بودن پایگاه داده تست (می‌توان یک دیتابیس جداگانه ساخت):

```bash
export DATABASE_URL="postgresql+asyncpg://user:pass@localhost/db_test"
```

۲. نصب pytest اگر نصب نیست:

```bash
pip install pytest
```

۳. اجرای تست‌ها:

```bash
pytest --disable-warnings -q
```

## قابلیت‌ها

* ثبت‌نام و ورود با JWT
* ورود با گوگل و گیت‌هاب (OAuth2)
* امنیت CORS/CSRF/HTTPS
* دسترسی نقش‌محور
* مستندسازی Swagger

```bash
pip install -r requirements.txt
export DATABASE_URL="postgresql+asyncpg://user:pass@localhost/db"
export JWT_SECRET="your-secret"
uvicorn app.main:app --reload
```

## قابلیت‌ها

* ثبت‌نام و ورود با JWT
* ورود با گوگل و گیت‌هاب (OAuth2)
* امنیت CORS/CSRF/HTTPS
* دسترسی نقش‌محور
* مستندسازی Swagger

```
```