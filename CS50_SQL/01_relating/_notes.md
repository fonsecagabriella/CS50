# Intro to SQL | Week 01 - Relating

- First define what you need (with WHERE), then GROUP then use HAVING to filter on the group conditions

## The order of the commands

0. `SELECT`: Which columns you will want
1. `FROM`/ `JOIN`: Grab the tables
2. `WHERE`: Filter out individual rows you don't need (*you cannot use aliases for WHERE because in the computer order, the `SELECT`actually happens after this stage 2*)
3. `GROUP BY`: Squash the remaning rows into buckets
4. `HAVING`: Filter out the buckets based on the math (like `COUNT`or `SUM`)
5. `ORDER BY`: Sort the final list
6. `LIMIT`: Cut the list short

- Use `WHERE` if you want the result of one specific row (ie salary_year=2020)
- Use `HAVING` if you want the result of a calculation