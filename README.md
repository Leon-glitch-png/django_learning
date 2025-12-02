


# Django Project

A simple Django project built for learning and practice.  
This project demonstrates Django views, templates, forms, Tailwind CSS, and basic CRUD operations.

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/Leon-glitch-png/django_learning.git
cd django_learning
````

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Tailwind CSS

If your project uses Tailwind (django-tailwind):

```bash
python manage.py tailwind install
python manage.py tailwind start
```

---

##  Apply Database Migrations

```bash
python manage.py migrate
```

---

## Run the Development Server

```bash
python manage.py runserver
```

Open your browser:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



## Main Project URLs (urls.py)

```bash
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('first/', include('firstApp.urls')),
]

```

## App URLs (firstApp/urls.py)

```bash
urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('info/', views.info, name='info'),
    path('model_info/', views.model_form_info, name='model_info'),
    path(
        'info_success/<str:name>/<int:age>/<str:email>/<str:address>/',
        views.info_success,
        name='info_success'
    ),
]


```



