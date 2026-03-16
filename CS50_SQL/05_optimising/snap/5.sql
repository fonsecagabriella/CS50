-- Given two usernames, lovelytrust487 and exceptionalinspiration482,
-- find the user IDs of their mutual friends.

-- EXPLAIN QUERY PLAN

SELECT "friend_id"
FROM "friends"
WHERE "user_id" IN (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'lovelytrust487'
)

INTERSECT

SELECT "friend_id"
FROM "friends"
WHERE "user_id" IN (
    SELECT "id"
    FROM "users"
    WHERE "username" = 'exceptionalinspiration482'
);