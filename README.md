# cybersecurity26
This project is developed as part of the Cybersecurity 2026 course at the University of Helsinki. It demonstrates common security vulnerabilities by intentionally building software with known flaws, analyzing them, and providing solutions.

The project focuses on five vulnerabilities from the OWASP Top 10 (2021) and explains how each issue works and how it can be fixed.
It includes 5 flaws: A01Broken Access Control, A03 Injection, A07 Identification and Authentication Failures, A05 Security Misconfiguration, A10:2021 – Server-Side Request Forgery (SSRF) 

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

