# import CS50 library
from cs50 import SQL


# create connection to db
db = SQL("sqlite:///dont-panic.db")

new_password = "CS50"

# execute
db.execute(
    """
    UPDATE "users"
    SET "password" = ?
    WHERE "username" = 'admin';
    """,

    new_password
)

print("Hacked!")