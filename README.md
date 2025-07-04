# ☕ Chai aur Code

**Chai aur Code** is a full-stack Django application showcasing traditional chai varieties, allowing users to browse, review, and find stores that sell their favorite blends. Built with Django and Tailwind CSS, this project emphasizes modern design with a classic desi flavor.

---

## 🚀 Features

* View detailed chai varieties with images
* User reviews and rating system
* Store locator by chai selection
* Custom Django Admin integration
* Responsive Tailwind CSS UI

---

## 📂 Project Structure

```bash
Django/
├── venv/                           # Python virtual environment
├── chaiaurDjango/                 # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
├── chai/                          # Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── chai/
│           ├── all_chai.html
│           ├── chai_detail.html
│           └── chai_store.html
├── manage.py
├── db.sqlite3
├── media/                         # Uploaded media files
├── statics/                       # Static assets
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── (your image files)
├── templates/                     # Global templates directory
│   ├── layout.html
│   └── website/
│       ├── index.html
│       ├── about.html
│       └── contact.html
├── theme/                         # Tailwind CSS / Node.js config
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── (other Tailwind assets)

---

## 💪 Tech Stack

* **Backend:** Django 5.x
* **Frontend:** Tailwind CSS 3.x
* **DB:** SQLite (development)
* **Media:** Django Media Uploads

---

## 🛠️ Local Development

```bash
git clone https://github.com/YOUR_USERNAME/chai-aur-code.git
cd chai-aur-code

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> Don't forget to run `python manage.py createsuperuser` for admin access.

---

## 🛎️ Deployment (Free Hosting Options)

* [Render](https://render.com) (Recommended)
* [Railway](https://railway.app)

Ensure:

* `gunicorn` and `whitenoise` are in `requirements.txt`
* `collectstatic` is run before deploy

Example `Procfile`:

```
web: gunicorn chaiaurDjango.wsgi
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Special Thanks

* Django Community
* Tailwind CSS
* FontAwesome for icons
* The culture of chai ☕
