# Intro to SQL | Week 06 - Scaling

## Intro to MySQL

- Login at MySQL server: `mysql -u root -h 127.0.0.1 -P 3306 -p `
    - `-u`user
    - `h`host
    - `-P` password
    - `-p` password

- `SHOW DATABASES`: meta information on the server

- `CREATE DATABASE 'mba' `

- `USE 'db'`

- `SHOW 'db'`

- `DESCRIBE 'table'`: shows information about db

- In MySQL you use backticks (`) instead of (')  or (")

### Types

- Tinyint (1 byte)
- Smallint
- MediumInt
- Int
- BigIt (63 bits)
- Unassign (non-negative values)
- Float: A number, 4 bytes
- Double precision: A number, 8 bytes
- Decimal (M, D)
- Char(M): where M is the maximum size of the string
- VarChar: where M is the maximum size of the string
- Text: stores long text like paragraph or pages
    - TinyText
    - Text
    - Mediumtext
    - Longtext
- Blob: Binary as you give it
- Enum: Fixed range of values you can have (only one value)
- Set: You can store from a set of values, but set more than one value
- Date
- Time (fsp): You can specify how precisely you want to keep track of time
- Datetime (fsp)
- Timestamp (fsp)
- Year

### Create table: Examples

```sql
CREATE TABLE 'stations'(
    'id' INT AUTO_INCREMENT,
    'name' VARCHAR(32) NOT NULL,
    'line' ENUM('blue', 'red', 'green', ...) NOT NULL,
    PRIMARY KEY ('id')
)
```

```sql
CREATE TABLE 'swipes'(
    ...,
    'type' ENUM('enter', ...) NOT NULL,
    'datetime' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'amount' DECIMAL(5,2) NOT NULL CHECK ('amount'!=0)
)

```

### MySQL and Docker 🐳

- Start MySQL:
    - `docker container run --name mysql -p 3306:3306 -v /workspaces/$RepositoryName:/mnt -e MYSQL_ROOT_PASSWORD=crimson -d mysql`
- Connect to the server with 'crimson' as password:
    - `mysql -h 127.0.0.1 -P 3306 -u root -p`

- To mount locally:

```bash
docker run --name cs50-mysql \
  -p 3306:3306 \
  -v "$PWD":/mnt \
  -e MYSQL_ROOT_PASSWORD=crimson \
  -e MYSQL_DATABASE=linkedin \
  -d mysql:8.0
```
- Then: `docker exec -it cs50-mysql mysql -uroot -p`

- Then, inside MySQL:

```sql
USE db;
SOURCE /mnt/schema.sql;
```




