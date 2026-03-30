# Intro to SQL | Week 04 - Viewing

## Views and temporary views

- **View**: A virtual table

| Feature | Standard VIEW | TEMPORARY VIEW |
| :--- | :--- | :--- |
| **Lifespan** | **Permanent** (stays until explicitly dropped). | **Session-based** (deleted when you disconnect). |
| **Visibility** | **Global** (visible to all users with permissions). | **Private** (visible only to your current session). |
| **Storage** | Query definition is saved in the **system catalog**. | Definition is stored in **temporary memory**. |
| **Cleanup** | Must be deleted **manually** using `DROP VIEW`. | Deleted **automatically** by the database engine. |
| **Best For** | Common, shared reports and security layers. | Intermediate steps in complex scripts/ETL. |

- Reasons to use a view:
    - Simplifying / reducing complexity
    - Aggregating
    - Partitioning
    - Securing

- Example:

```sql
CREATE VIEW "rural" AS
SELECT * FROM "census"
WHERE "locality" LIKE '%rural%';
```

## CTEs
- **CTE** Common Table Expression: exists only during the query

```sql
WITH "name" AS (
    SELECT ...
)
```

## Triggers

```sql
CREATE TRIGGER name
INSTEAD OF DELETE ON view
FOR EACH ROW
-- Alternative
-- FOR EACH ROW WHEN -- condition
BEGIN
    -- run this other statement
    ;
END;

```


- Example (instead of inserting in a view - not possible, update value)
```sql
CREATE TRIGGER "insert_when _exists"
INSTEAD OF INSERT ON "current_collections"
FOR EACH ROW
WHEN NEW."accession_number" IN (
    SELECT "accession_number" FROM "collections"
)
BEGIN
    UPDATE "collections" SET "deleted"= 0
    WHERE "accession_number"= NEW."accession_number"
END;

;
```