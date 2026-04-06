# cybersecurity26
This project is developed as part of the Cybersecurity 2026 course at the University of Helsinki. It demonstrates common security vulnerabilities by intentionally building software with known flaws, analyzing them, and providing solutions.

The project focuses on five vulnerabilities from the OWASP Top 10 (2021) and explains how each issue works, why it is dangerous, and how it can be fixed.

我帮你整理成标准 README 里常见的 **“Setup / Installation”** 部分格式，更清晰一点👇

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Ensure Python is installed on your system.

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

