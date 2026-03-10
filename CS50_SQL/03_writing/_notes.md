# Intro to SQL | Week 03 - Writing


- `.import --csv --skip 1 filetoimport.csv table_data_will_land`: import csv file to table (must be logged in sqlite3)
    - `--csv`: says the type of the file
    - `--skip 1`: skips first row


- `.import --csv mfa.csv temp`: import data to temporary table

- Insert columns from one table to another another table
```sql
INSERT INTO table1 (column1_table1)
SELECT column1 FROM table2
```

- When you import values from a .csv, the fields will be sent as text. This can be an issue because NULL values will show as a blank space; You need to treat these cases with an UPDATE

## Action triggers

```sql
FOREIGN KEY ("artist_id") REFERENCES "artists"("id")
ON DELETE SET NULL -- example
```

Other possible actions:

- `RESTRICT`: doesn't allow to happen
- `NO ACTION`: allow deletion with no consequence
- `CASCADE`: multiple deletions 
- `SET NULL`:
- `SET DEFAULT`:

## Update table

- If you are updating all values in a column, do:
```sql
UPDATE "voted" SET "title"= trim("title");
```

## Triggers

```sql
CREATE TRIGGER name
BEFORE DELETE ON table
FOR EACH ROW
BEGIN
    -- do something;
END;
```