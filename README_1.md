# Smart Career Roadmap Generator

A beginner-friendly full-stack web app where users enter their skills and career goal,
and receive a personalized step-by-step learning roadmap.

---

## Tech Stack

| Layer     | Technology                    |
|-----------|-------------------------------|
| Frontend  | React.js, HTML, CSS, Axios    |
| Backend   | Python, Django, DRF           |
| Database  | SQLite (SQL)                  |
| Auth      | Django Token Auth             |

---

## Folder Structure

```
smart-career-roadmap/
├── frontend/               # React app
│   ├── public/
│   └── src/
│       ├── api/            # Axios API calls
│       ├── components/     # Reusable UI pieces
│       ├── pages/          # Full page views
│       └── App.jsx
├── backend/                # Django project
│   ├── roadmap/            # Roadmap app (models, views, urls)
│   ├── users/              # User registration/login
│   ├── career_project/     # Django settings
│   └── manage.py
└── README.md
```

---

## How to Run

### Step 1 — Clone / create the project folder
```bash
mkdir smart-career-roadmap && cd smart-career-roadmap
```

### Step 2 — Set up the Django backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py createsuperuser # optional admin account
python manage.py runserver       # runs on http://localhost:8000
```

### Step 3 — Set up the React frontend
```bash
cd ../frontend
npm install
npm start    # runs on http://localhost:3000
```

### Step 4 — Open the app
Visit **http://localhost:3000** in your browser.

---

## How the App Works (for interviews)

1. User registers/logs in via the React frontend.
2. React sends the user's skills and career goal to the Django REST API using Axios.
3. Django looks up a matching roadmap template from the SQL database.
4. Django builds a personalised roadmap and sends it back as JSON.
5. React displays the roadmap as a visual step-by-step plan.
6. The roadmap is saved to the database so the user can view it later.

---

## Resume Bullet Points

- Built a full-stack career roadmap generator using React.js and Django REST Framework, enabling users to receive personalised learning plans based on their skills and career goals.
- Designed and implemented RESTful API endpoints in Django to handle user registration, skill input, and dynamic roadmap generation, integrating a relational SQL database with Django ORM.
- Developed an interactive React frontend with Axios for async API communication, featuring a skills dashboard and multi-phase roadmap view with progress tracking.
- Managed end-to-end project lifecycle including database schema design, token-based authentication, cross-origin resource sharing (CORS) configuration, and local deployment.

---

## Interview Questions & Answers

**Q: What is Django REST Framework?**
A: It is a library on top of Django that makes it easy to build REST APIs. It handles serialization (converting Python objects to JSON), request routing, and authentication.

**Q: Why did you use Axios instead of plain Fetch?**
A: Axios automatically parses JSON responses, provides cleaner error handling, and makes it easy to set a base URL and auth headers globally.

**Q: What is CORS and why did you need it?**
A: CORS (Cross-Origin Resource Sharing) is a browser security rule that blocks requests from a different domain. Since React runs on port 3000 and Django on port 8000, I used django-cors-headers to allow this.

**Q: How does token authentication work in your project?**
A: When a user logs in, Django generates a unique token and sends it to the frontend. React stores this token and includes it in every subsequent API request header. Django checks the token to identify the user.

**Q: How is the roadmap stored in the database?**
A: I have a Roadmap model with fields for user (foreign key), career goal, and a JSON field for the phases. Each phase is stored as structured data in the SQL database.

**Q: What SQL operations does your app perform?**
A: CREATE (saving new roadmaps and users), READ (fetching user roadmaps), UPDATE (marking topics complete), and DELETE (removing saved roadmaps) — basic CRUD operations.
