# CS50 Coursework (Solutions + Notes)

This repository contains my solutions, notes, and small projects from Harvard’s CS50 courses.

> ⚠️ If you are currently taking a CS50 course, follow Harvard’s Academic Honesty policy: https://cs50.harvard.edu/ai/2020/honesty/

> [Playlist on Youtube](https://www.youtube.com/playlist?list=PLNDDAVxjlPk3-h1MiH-fZLVEiiawkmplP) with the projects showcase / explanation.

## Courses completed

| Course | Official page | Completed | Final / highlight |
|---|---|---:|---|
| **CS50P — Introduction to Programming with Python** | https://cs50.harvard.edu/python/2022/ | **July 2023** | **Final project:** **Teach Me How to Dutch** — a django web app powered by the OpenAI API: [Teach Me How to Dutch](https://teachmehowtodutch.com/) |
| **CS50AI — Introduction to Artificial Intelligence with Python** | https://cs50.harvard.edu/ai/2020/ | **October 2023** | **Project portfolio:** search, logic, probabilistic reasoning, optimisation, ML, neural nets, NLP (see details below) |
| **CS50 Web — Web Programming with Python and JavaScript** | https://cs50.harvard.edu/web/ | **October 2023** | Projects + a final web app using Python, JavaScript, and SQL (Django / React / Bootstrap) |
| **CS50 SQL — Introduction to Databases with SQL** | https://cs50.harvard.edu/sql/ | **In progress (March 2026)** | Problem sets + final project focused on relational databases (SQLite → PostgreSQL/MySQL) |

## Skills and topics practiced (from this repo)

### AI / ML ([CS50AI](./CS50_AI/))
- **Search:** DFS, BFS, greedy best‑first, **A\***, minimax, alpha‑beta pruning, depth‑limited minimax  
- **Knowledge & logic:** propositional logic, inference, resolution  
- **Uncertainty:** Bayes’ rule, Markov chains, Bayesian networks  
- **Optimisation:** constraint satisfaction, backtracking, local search (hill climbing, simulated annealing)  
- **Learning:** classification (k‑NN), reinforcement learning (Q‑learning), clustering  
- **Neural networks:** gradient descent, CNN basics (convolution/pooling)  
- **Language:** n‑grams, tokenisation, parsing, information retrieval, topic modelling  

### Databases ([CS50 SQL](./CS50_SQL/))
- **Relational modelling:** tables, types, primary/foreign keys, joins
- **Querying:** SELECT, WHERE, ORDER BY, LIMIT/OFFSET, LIKE, aggregates, DISTINCT
- **Data quality/performance:** normalization, constraints, triggers, views, indexes
- **DB engines:** SQLite first; introductions to PostgreSQL and MySQL
- **Integration:** connecting SQL with other languages (e.g., Python, Java)

### Web development ([CS50 Web](./CS50_Web/))
- **Core web:** HTML, CSS, JavaScript
- **Backend:** Python + Django
- **Data layer:** SQL, models, migrations
- **Modern web app concerns:** database design, security, scalability, UX
- **APIs + deployment workflow:** building/using APIs, interactive UIs, GitHub/Heroku



### Libraries/tools used
- **Flask**, **OpenAI API** (CS50P final project)
- **scikit‑learn**, **TensorFlow**, **NLTK**, **Matplotlib** (CS50AI projects)
- **Django**, **React**, **Bootstrap** (CS50 Web)
- **SQLite**, **PostgreSQL**, **MySQL** (CS50 SQL)

## Featured projects

### Teach Me How to Dutch (CS50P final → CS50 Web capstone)

- Live demo: [Teach Me How to Dutch](https://teachmehowtodutch.com/)

- What it does: **Dutchionary (words/expressions)**, **sentence checking**, **translation saving** — in one place. 

- Project evolution:
  - **CS50P final (v1):** “Dutchionary” built with **Flask** (terminal-first workflow).
  - **CS50 Web capstone (v2):** rebuilt as **Django** (“Teach Me How to Dutch”), adding a more complete web-app structure.

- Demo video: (project walkthrough): [Youtube](https://www.youtube.com/watch?v=0YSrAEEi6-0)

- Screenshot (v2)

<img src="./static/teachmehowtodutch_main.png" width="30%">


### CS50AI project set (high-level)
A selection of the projects included in this repository:

- **[Degrees](./CS50_AI/week_00_search/degrees/)** (graph search), **[Tic‑Tac‑Toe](./CS50_AI/week_00_search/tictactoe/)** (minimax)

- **[Knights](./CS50_AI/week_01_knowledge/knights/)** (logic puzzles), **[Minesweeper](./CS50_AI/week_01_knowledge/minesweeper/)** (knowledge representation)

- **[PageRank](./CS50_AI/week_02_uncertainty/pagerank/)** (Markov chain), **[Heredity](./CS50_AI/week_02_uncertainty/heredity/)** (Bayesian network)

- **[Crossword](./CS50_AI/week_03_optimisation/crossword/)** (CSP / backtracking)

- **[Shopping](./CS50_AI/week_04_learning/shopping/)** (k‑NN with scikit‑learn), **[Nim](./CS50_AI/week_04_learning/nim/)** (reinforcement learning)

- **[Traffic](./CS50_AI/week_05_neural_networks/traffic/)** (TensorFlow CNN)

- **[Parser](./CS50_AI/week_06_language/parser/)** (NLP parsing), **[Questions](./CS50_AI/week_06_language/questions/)** (information retrieval)

## Repo navigation
- `static/` contains the screenshots/ images.

- The following files contain a detailed description of each course, week by week:
    - [CS50 AI](./CS50_AI/README.md)
    - [CS50 Python](./CS50_Python/README.md)
    - [CS50 Web](./CS50_Web/README.md)
    - [CS50 SQL](./CS50_SQL/README.md)

