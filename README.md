# 🌐 Personal Portfolio Website (Django + Bootstrap)

This is a **Personal Portfolio Website** built with *Python, Django, HTML, CSS, Bootstrap, and JavaScript*.  
It showcases your profile, skills, projects, and includes a contact form.  
---
## 🚀 Features
- 🏠 **Home Page** with hero banner  
- 👨‍💻 **About Me Section** with profile picture and description  
- 🛠️ **Tech Stack Section** (Python, Django, FastAPI, Go, HTML, CSS and JS etc.)  
- 📂 **Projects Showcase** with images & links  
- 📩 **Contact Form** (supports database/email integration)  
- 🌗 **Modern UI with Animations (AOS, Bootstrap)**  
- 📱 **Fully Responsive Design**  
- 🎨 **Custom CSS for styling & hover effects**  
---
## 📸 Screenshots (with dummy images)
### Home Page
![Home Screenshot](https://picsum.photos/800/400?random=1)
### Projects Section
![Projects Screenshot](https://picsum.photos/800/400?random=2)
---
## 🛠️ Tech Stack
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap 5, JavaScript  
- **Icons**: FontAwesome  
- **Animations**: AOS (Animate on Scroll)  
- **Database**: SQLite (default)  
---
## 📂 Project Structure
``` 
portfolio/
│── portfolio/             # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── …
│
│── main/                  # Main app
│   ├── templates/main/    # HTML templates
│   │   └── index.html
│   ├── static/main/       # Static files (CSS, JS, images)
│   │   ├── css/style.css
│   │   ├── js/script.js
│   │   └── images/
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
│── db.sqlite3             # SQLite database
│── manage.py              # Django CLI entrypoint
│── README.md              # Project documentation

```
### Create virtual enviroment & activate
```
python -m venv .venv
source .venv/bin/activate

```
### Install dependencies
```
pip  install django
```

### start server
```
python manage.py runserver
Open on brower: http://127.0.0.1:8000/
```