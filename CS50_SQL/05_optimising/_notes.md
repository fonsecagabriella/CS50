# Intro to SQL | Week 05 - Optimising

- `Index`: Structure used to speed up the retrieval of rows from a table

```sql
CREATE INDEX "person_index" ON "starts"("person_id");
```


-  `EXPLAIN QUERY PLAN`: Sql shows the plan it intends to use to get to results.

```sql
EXPLAIN QUERY PLAN
SELECT * FROM "movies" WHERE "title"= 'Cars';
```

- `COVERING INDEX`: An index in which queries data can be retrieved from the index itself (it doesn't need to go back to the table to find data, so the query is optimised)

- `PARTIAL INDEX`: An index that includes only a subset of rows from a table (that are more likely to be searched, for example); to create, use the same syntax of INDEX with WHERE condition.

```sql
CREATE INDEX "person_index" ON "starts"("person_id")
WHERE;
```

## Vacuum

- A way to "clean" the db;
- Use: `VACCUM` as a command in a .sql file. 
-  `du -b movies.db`: check the size of bytes of a DB

## Transactions / Concurrency

- `Transaction`: A unit of work in a database; it cannot be broken down into smaller units. Properties:
    - **ACID**: Atomicity; Consistency; Isolation; Durability
    - All the commands inside a transaction will happen 'at the same time', or not at all.

```sql
BEGIN TRANSACTION;

...

COMMIT;
```

- `ROLLBACK`: use as the final of a transaction, to 'undo' commands if a condition fails due a constraint.

## Locks

- UNLOCKED
- SHARED
- EXCLUSIVE