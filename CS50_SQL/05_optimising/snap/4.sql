--  Find the username of the most popular user,
-- defined as the user who has had the most messages sent to them.
-- Ensure your query uses the search_messages_by_to_user_id index

--EXPLAIN QUERY PLAN
SELECT "username"
FROM "users"
WHERE "id" IN
    (
        SELECT "users"."id"
        FROM "users"
        INNER JOIN "messages"
        ON "users"."id" = "messages"."to_user_id"
        GROUP BY "users"."id"
        ORDER BY COUNT("messages"."id") DESC
        LIMIT 1
        );