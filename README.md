
---

### 📝 **README.md**


# 🌤️  Blog Website

A simple blog website built with **Django**, allowing users to browse, create, edit, and delete posts.  
It includes category filtering, featured posts, and a modern responsive UI using **Bootstrap**.

---

## 🚀 Features

- 🏠 **Home page**: Displays featured posts and a list of recent articles.  
- 🗂️ **Category filter**: View posts grouped by category.  
- 📝 **Add Post**: Create new blog posts easily with Django forms.  
- ✏️ **Edit Post**: Update existing articles.  
- ❌ **Delete Post**: Remove posts securely with confirmation.  
- 👤 **Author module**: Manage post authors and their information.  
- 🔍 **Search bar**: Quickly find posts by keyword.  
- 💅 **Responsive design** built with Bootstrap 5.

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| **Backend** | Django 5.x |
| **Frontend** | HTML, CSS, Bootstrap 5 |
| **Database** | SQLite (default) |
| **Language** | Python 3.12 |

---

## 📁 Project Structure

```

Django-blog-website
├── my_blogs/
│   ├── authors/                # App for author management
│   ├── blogs/                  # Main blog app
│   │   ├── templates/blogs/    # Templates (HTML files)
│   │   ├── views.py            # Views for home, detail, add, edit, delete
│   │   ├── urls.py             # URL routing
│   │   └── models.py           # Post, Category, etc.
│   ├── static/                 # CSS and static files
│   ├── base.css                # Custom CSS
│   └── manage.py
└── README.md

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/django-blog-website.git
   cd django-blog-website
````

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**

   ```bash
   python manage.py runserver
   ```

7. **Open your browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## 📸 Preview

### 🏠 Home Page

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/ff45ee08-203d-4a6d-a683-dc90b2a916b1" />


---

## 🧑‍💻 Author

**Thien Nguyen**
📧 [[thanhthien176@gmail.com](mailto:thanhtien176@gmail.com)]
🌐 [GitHub Profile](https://github.com/thanhthien176)

---

## 🪪 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

```

---

