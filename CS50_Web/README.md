# CS50 Web — Web Programming with Python and JavaScript (Solutions)

Course: CS50’s Web Programming with Python and JavaScript  
Official course page: https://cs50.harvard.edu/web/  
Walkthrough playlist (my demos): https://www.youtube.com/playlist?list=PLNDDAVxjlPk3-h1MiH-fZLVEiiawkmplP

> Academic honesty: If you are currently taking CS50 Web, follow CS50’s Academic Honesty policy and do not submit these solutions as your own.

## Repo structure (this folder)

- Each **project** has its own folder with code + notes.
- I keep a **week-by-week index** here so you can quickly jump to the relevant work.

## Week-by-week index

| Week | Topic | Course materials | Project(s) most related | My code |
|---:|---|---|---|---|
| 0 | HTML, CSS | https://cs50.harvard.edu/web/weeks/0/ | **Project 0 — Search** (HTML/CSS) | [project 00](./project_00_search/) |
| 1 | Git | https://cs50.harvard.edu/web/weeks/1/ | Project 0 — Search (versioning + workflow) | `./project0-search/` |
| 2 | Python | https://cs50.harvard.edu/web/weeks/2/ | Bridge week → prepares for Django projects | *(notes / exercises, if any)* |
| 3 | Django | https://cs50.harvard.edu/web/weeks/3/ | **Project 1 — Wiki** (Django basics) | `./project1-wiki/` |
| 4 | SQL, Models, Migrations | https://cs50.harvard.edu/web/weeks/4/ | **Project 2 — Commerce** (models, auth, DB) | `./project2-commerce/` |
| 5 | JavaScript | https://cs50.harvard.edu/web/weeks/5/ | **Project 3 — Mail** (JS + API calls) | `./project3-mail/` |
| 6 | User Interfaces | https://cs50.harvard.edu/web/weeks/6/ | Project 3 — Mail (UI) / Project 4 — Network (UI + interactions) | `./project3-mail/` / `./project4-network/` |
| 7 | Testing, CI/CD | https://cs50.harvard.edu/web/weeks/7/ | Project 4 — Network (stability + iteration) | `./project4-network/` |
| 8 | Scalability & Security | https://cs50.harvard.edu/web/weeks/8/ | **Final Project — Capstone** | `./final-project/` |

## Projects (specs + quick links)

- Project 0 — Search (front-end for Google Search): https://cs50.harvard.edu/web/projects/0/search/  
- Project 1 — Wiki (Wikipedia-like encyclopedia): https://cs50.harvard.edu/web/projects/1/wiki/  
- Project 2 — Commerce (eBay-like auctions): https://cs50.harvard.edu/web/2020/projects/2/commerce/  
- Project 3 — Mail (email client using API calls): https://cs50.harvard.edu/web/2020/projects/3/mail/  
- Project 4 — Network (social network): https://cs50.harvard.edu/web/2020/projects/4/network/  
- Final Project — Capstone: https://cs50.harvard.edu/web/projects/final/capstone/

## How to run (typical Django projects)

Most projects are Django apps. Common commands (may vary per project):

1. Create/activate a virtual environment
2. Install deps (if you have requirements.txt): `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations` then `python manage.py migrate`
4. Start server: `python manage.py runserver`
