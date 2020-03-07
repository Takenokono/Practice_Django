# Practice Djaongo
This repository is for practicing Web Application *Django*.

`pip install django`

---

## Memo
### 0. To run server
`python manage.py runserver`

### 1. To create new project 
`django-admin startproject [PROJECT NAME]`

### 2. To create new app
`python manage.py startapp [APP NAME]`

- Creating `urls.py` in each app and Adding `include()` at `urlpattern[]` in `django_app/urls.py` are better.
- Insert AppName in `INSTALLED_APPS` in `django_app_setting`