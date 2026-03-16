-- Find all usernames of users who have logged in since 2024-01-01.
-- Ensure your query uses the search_users_by_last_login index

-- EXPLAIN QUERY PLAN
SELECT "username"
FROM "users"
WHERE "last_login_date" > '2024-01-01';