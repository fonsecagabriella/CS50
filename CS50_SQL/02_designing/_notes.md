# Intro to SQL | Week 02 - Designing

-  `sqlite3 db`clear
- `.schema TABLE`: sees the schema of db
- `.read schema.sql`: read the file into db

## Data Types and storage classes

- BLOB: binary large object (good for big objects, like images)

## Constraints types

- `PRIMARY KEY`: it's always UNIQUE and NOT NULL

- `NOT NULL`:  when you have columns that are not PK or FK and you want to make sure the info is not null; if used with PK or FK info is redundant;

- `UNIQUE`: value cannot repeat in this column;

- `DEFAULT`

- `CHECK`

- `CONSTRAINT`

## Table commands

- `DROP TABLE`
- `ALTER TABLE table_name RENAME TO new_name`
- `ALTER TABLE table_name ADD COLUMN new_column TYPE`
- `ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name`
- `ALTER TABLE table_name DROP COLUMN column_name`