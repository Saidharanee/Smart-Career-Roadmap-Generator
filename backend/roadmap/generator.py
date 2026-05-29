# Core logic: generates a roadmap based on career goal and known skills

# Templates for each career path
# Each phase has: title, duration, and a list of topics to learn
ROADMAP_TEMPLATES = {
    "Full Stack Developer": [
        {
            "phase": 1,
            "title": "Web Foundations",
            "duration": "Weeks 1–4",
            "topics": ["HTML5", "CSS3", "Flexbox", "CSS Grid", "Responsive Design"]
        },
        {
            "phase": 2,
            "title": "JavaScript & React",
            "duration": "Weeks 5–10",
            "topics": ["JavaScript ES6+", "DOM Manipulation", "React.js", "useState", "useEffect", "Fetch API"]
        },
        {
            "phase": 3,
            "title": "Backend with Django",
            "duration": "Weeks 11–16",
            "topics": ["Python Basics", "Django ORM", "REST APIs", "Django REST Framework", "Token Auth"]
        },
        {
            "phase": 4,
            "title": "Database & Deployment",
            "duration": "Weeks 17–20",
            "topics": ["SQL Queries", "PostgreSQL", "Git & GitHub", "Deploy on Render"]
        },
    ],

    "Data Analyst": [
        {
            "phase": 1,
            "title": "Python for Data",
            "duration": "Weeks 1–4",
            "topics": ["Python basics", "Pandas", "NumPy", "Jupyter Notebooks"]
        },
        {
            "phase": 2,
            "title": "SQL & Databases",
            "duration": "Weeks 5–8",
            "topics": ["SQL SELECT", "JOINs", "GROUP BY", "Aggregations", "SQLite"]
        },
        {
            "phase": 3,
            "title": "Data Visualisation",
            "duration": "Weeks 9–12",
            "topics": ["Matplotlib", "Seaborn", "Plotly", "Tableau basics"]
        },
        {
            "phase": 4,
            "title": "Statistics & ML Intro",
            "duration": "Weeks 13–16",
            "topics": ["Descriptive stats", "Probability", "Linear Regression", "Scikit-learn"]
        },
    ],

    "Backend Developer": [
        {
            "phase": 1,
            "title": "Python Fundamentals",
            "duration": "Weeks 1–5",
            "topics": ["Python OOP", "File I/O", "Error handling", "Virtual Environments"]
        },
        {
            "phase": 2,
            "title": "Django & REST APIs",
            "duration": "Weeks 6–10",
            "topics": ["Django Models", "Views", "Serializers", "URL routing", "JWT Auth"]
        },
        {
            "phase": 3,
            "title": "Databases",
            "duration": "Weeks 11–14",
            "topics": ["SQL", "PostgreSQL", "Indexing", "Django Migrations"]
        },
        {
            "phase": 4,
            "title": "DevOps Basics",
            "duration": "Weeks 15–18",
            "topics": ["REST design", "Docker intro", "GitHub Actions", "Deployment"]
        },
    ],
    
     "Frontend Developer": [
        {"phase": 1, "title": "Frontend Basics", "duration": "Weeks 1-4",
         "topics": ["HTML5", "CSS3", "Responsive Design", "Flexbox", "CSS Grid"]},
        {"phase": 2, "title": "JavaScript Essentials", "duration": "Weeks 5-8",
         "topics": ["JavaScript ES6+", "DOM Manipulation", "Events", "Async JavaScript"]},
        {"phase": 3, "title": "React Development", "duration": "Weeks 9-13",
         "topics": ["React.js", "Components", "Props", "useState", "useEffect", "React Router"]},
        {"phase": 4, "title": "Frontend Deployment", "duration": "Weeks 14-16",
         "topics": ["API Integration", "Axios", "GitHub", "Netlify Deployment"]},
    ],

    "AI/ML Engineer": [
        {"phase": 1, "title": "Python & Math Foundations", "duration": "Weeks 1-5",
         "topics": ["Python", "Linear Algebra", "Statistics", "Probability"]},
        {"phase": 2, "title": "Data Processing", "duration": "Weeks 6-9",
         "topics": ["NumPy", "Pandas", "Data Cleaning", "Data Visualisation"]},
        {"phase": 3, "title": "Machine Learning", "duration": "Weeks 10-15",
         "topics": ["Scikit-learn", "Regression", "Classification", "Model Evaluation"]},
        {"phase": 4, "title": "Deep Learning & Deployment", "duration": "Weeks 16-20",
         "topics": ["TensorFlow", "Neural Networks", "Flask API", "Model Deployment"]},
    ],

    "DevOps Engineer": [
        {"phase": 1, "title": "Linux & Networking", "duration": "Weeks 1-4",
         "topics": ["Linux Commands", "Shell Scripting", "Networking Basics", "SSH"]},
        {"phase": 2, "title": "Version Control & CI/CD", "duration": "Weeks 5-8",
         "topics": ["Git", "GitHub", "GitHub Actions", "CI/CD Pipelines"]},
        {"phase": 3, "title": "Containers & Cloud", "duration": "Weeks 9-13",
         "topics": ["Docker", "Kubernetes Basics", "AWS Basics", "Cloud Deployment"]},
        {"phase": 4, "title": "Monitoring & Automation", "duration": "Weeks 14-18",
         "topics": ["Jenkins", "Terraform", "Monitoring Tools", "Infrastructure Automation"]},
    ],

    "Software Developer": [
        {"phase": 1, "title": "Programming Fundamentals", "duration": "Weeks 1-4",
         "topics": ["Python Basics", "OOP Concepts", "Data Structures", "Algorithms"]},
        {"phase": 2, "title": "Software Development", "duration": "Weeks 5-9",
         "topics": ["Git & GitHub", "Debugging", "REST APIs", "Unit Testing"]},
        {"phase": 3, "title": "Backend & Databases", "duration": "Weeks 10-14",
         "topics": ["Django", "SQL", "Database Design", "Authentication"]},
        {"phase": 4, "title": "Deployment & Projects", "duration": "Weeks 15-18",
         "topics": ["Cloud Deployment", "Docker Basics", "CI/CD", "Project Building"]},
    ],

    "Data Engineer": [
        {"phase": 1, "title": "Programming & SQL", "duration": "Weeks 1-4",
         "topics": ["Python", "SQL Basics", "Database Concepts", "Data Cleaning"]},
        {"phase": 2, "title": "Data Pipelines", "duration": "Weeks 5-8",
         "topics": ["ETL Pipelines", "Apache Airflow", "Data Warehousing", "APIs"]},
        {"phase": 3, "title": "Big Data Tools", "duration": "Weeks 9-13",
         "topics": ["Spark", "Hadoop", "Kafka", "Cloud Storage"]},
        {"phase": 4, "title": "Cloud & Deployment", "duration": "Weeks 14-18",
         "topics": ["AWS Data Services", "Azure Data Factory", "Docker", "Monitoring"]},
    ],

    "Python Developer": [
        {"phase": 1, "title": "Python Core", "duration": "Weeks 1-4",
         "topics": ["Python Syntax", "Functions", "OOP", "Exception Handling"]},
        {"phase": 2, "title": "Advanced Python", "duration": "Weeks 5-8",
         "topics": ["File Handling", "Decorators", "Modules", "Virtual Environments"]},
        {"phase": 3, "title": "Web Development", "duration": "Weeks 9-13",
         "topics": ["Django", "Flask", "REST APIs", "Authentication"]},
        {"phase": 4, "title": "Projects & Deployment", "duration": "Weeks 14-17",
         "topics": ["SQL", "GitHub", "Deployment", "Testing"]},
    ],

    "App Developer": [
        {"phase": 1, "title": "Programming Basics", "duration": "Weeks 1-4",
         "topics": ["Java/Kotlin", "Dart Basics", "OOP", "Mobile UI Basics"]},
        {"phase": 2, "title": "App Development Frameworks", "duration": "Weeks 5-9",
         "topics": ["Flutter", "React Native", "Navigation", "State Management"]},
        {"phase": 3, "title": "Backend & APIs", "duration": "Weeks 10-13",
         "topics": ["Firebase", "REST APIs", "Authentication", "Push Notifications"]},
        {"phase": 4, "title": "Deployment & Publishing", "duration": "Weeks 14-16",
         "topics": ["App Testing", "Play Store Deployment", "App Optimization", "Version Control"]},
    ],
}



def generate_roadmap(career_goal, known_skills):
    """
    Given a career goal and a list of known skills,
    returns a tailored list of learning phases.

    known_skills: list of strings, e.g. ["Python", "HTML"]
    career_goal: string, e.g. "Full Stack Developer"
    """

    # Get the matching template (default to Full Stack if unknown goal)
    template = ROADMAP_TEMPLATES.get(career_goal, ROADMAP_TEMPLATES["Full Stack Developer"])

    # Normalise known skills to lowercase for comparison
    known = [s.lower().strip() for s in known_skills]

    # Build the roadmap, filtering out topics the user already knows
    roadmap = []
    for phase in template:
        remaining_topics = [
            topic for topic in phase["topics"]
            if topic.lower() not in known
        ]

        # Only include the phase if there are topics left to learn
        if remaining_topics:
            roadmap.append({
                "phase": phase["phase"],
                "title": phase["title"],
                "duration": phase["duration"],
                "topics": remaining_topics,
                "total_topics": len(remaining_topics),
            })

    return roadmap
