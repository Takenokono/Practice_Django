# Practice Djaongo
This repository is for practicing Web Application *Django*.

`pip install django`

---

## Memo
### 0. To run server
`python manage.py runserver`

### 1. To create new project 
`django-admin startproject [PROJECT NAME]`

### 2. To migrate 
`python manage.py migrate`

### 3. To create new app
`python manage.py startapp [APP NAME]`

---
## MEMO
- Creating `urls.py` in each app and Adding `include()` at `urlpattern[]` in `django_app/urls.py` are better.
- Insert AppName in `INSTALLED_APPS` in `django_app_setting`
- To crate template, you should make `templates/[APP NAME]` in each App.

---

### 4. To create DB
- Edit `models.py` for creating DataBase. 
- After you define DB template in `models.py`, try `python manage.py makemigrations`.
- Then `python manage.py migrate`. 

# 2022/03/04 : 23sectionまで

## Template tags
- {{}}
- {% load static %}
- {% url [NAME]%}
