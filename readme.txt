# 📝 BBS (Bulletin Board System) - Django + PostgreSQL

## 📌 Project Overview
This is a simple bulletin board system (BBS) built using Django and PostgreSQL. 
Users can create, read, update, and delete questions. add answers. 
The project uses Django’s built-in template system for rendering HTML pages (no REST API or frontend frameworks involved).

## 🎯 Key Features
- Display a list of all questions (newest first)
- View detailed post content
- Create new questions (via form)
- Edit and delete existing questions
- Create new answers (via form)
- Basic user authentication 
- Admin panel for managing questions and users

## 🏗️ Tech Stack

| Layer       | Technology            |
|-------------|------------------------|
| Backend     | Python 3.10+, Django 4.x |
| Database    | PostgreSQL             |
| Frontend    | Django Templates (HTML/CSS) / Js script : summernote- lite |
| Deployment  | EC2, Nginx, Gunicorn (optional) |