-- Find the user IDs of the top 3 users to whom creativewisdom377
-- sends messages most frequently. Order the user IDs by the number of messages
-- creativewisdom377 has sent to those users, most to least.

-- EXPLAIN QUERY PLAN
SELECT  "users"."id"
        --,COUNT("messages"."id") AS "number_messages"
FROM "users"
INNER JOIN "messages"
ON "users"."id" = "messages"."to_user_id"
WHERE "messages". "from_user_id" = (
    SELECT "id" FROM "users" WHERE "username" = 'creativewisdom377'
)
GROUP BY "users"."id"
ORDER BY COUNT("messages"."id") DESC
LIMIT 3;