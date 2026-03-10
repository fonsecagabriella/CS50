-- INSERT fake user log
INSERT INTO
    "user_logs" ("type", "old_username", "new_username", "old_password", "new_password")
VALUES
    (
        'update',
        'admin',
        'admin',
        (
            SELECT "password" FROM users where username= 'admin'
        ),
        (
            SELECT "password" FROM users WHERE username='emily33'
        )
    );

-- ALTER the password of the website admin
UPDATE "users"
SET "password" = '982c0381c279d139fd221fce974916e7'
WHERE "username" = 'admin';

-- DELETE any logs of the above password change recorded in the database
DELETE FROM
    "user_logs"
WHERE
    "new_password" = '982c0381c279d139fd221fce974916e7'
    AND "new_username" = 'admin'
;

-- INSERT fake data
-- In particular, to frame emily33, make it only appear—in the user_logs table
-- - as if the admin account has had its password changed to emily33’s password.

-- Delete any logs of emily33's orders
DELETE FROM
    "orders"
WHERE
    "user_id" = (SELECT "id" FROM "users" WHERE "username" = 'emily33')
;

-- DELETE any logs for emily33's account creation
DELETE FROM
    "user_logs"
WHERE
    "new_username" = 'emily33' OR "old_username" = 'emily33'
;

