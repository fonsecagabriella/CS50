# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the CS50 SQL final project — a SQLite database design project. The deliverables are:

- **`schema.sql`** — `CREATE TABLE`, `CREATE INDEX`, and `CREATE VIEW` statements with inline comments explaining design choices
- **`queries.sql`** — representative SQL queries a user would run against the database, with comments
- **`DESIGN.md`** — written design document covering scope, functional requirements, entity representation, relationships (including an ER diagram), optimizations, and limitations

## Running Queries

```bash
# Load schema into a new database
sqlite3 my_database.db < schema.sql

# Run queries interactively
sqlite3 my_database.db

# Run queries from file
sqlite3 my_database.db < queries.sql
```

## Project Requirements

The CS50 SQL final project expects:

1. **Schema** — normalized tables with appropriate types, constraints (`NOT NULL`, `UNIQUE`, `CHECK`, foreign keys), indexes for common lookups, and views for convenience queries.
2. **Queries** — cover the main use cases described in DESIGN.md (inserts, selects with joins/aggregations, updates, deletes).
3. **DESIGN.md** — must be filled in completely; the ER diagram can be embedded as an image or ASCII art.

## Architecture Pattern

SQLite is the target database. Design decisions should favor:
- Explicit foreign key constraints (SQLite requires `PRAGMA foreign_keys = ON;` at runtime to enforce them)
- `INTEGER PRIMARY KEY` for auto-increment rowid aliases
- `TEXT` for strings, `NUMERIC`/`REAL` for numbers, `INTEGER` for counts/flags, `BLOB` for binary data