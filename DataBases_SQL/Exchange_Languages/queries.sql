
----------------- IMPLEMENTING SOME QUERIES ----------------------------

-- Finding potential partners for 'user2' who want to teach 'user2'.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_2_id"
    FROM "PotentialPartners"
    WHERE "user_1_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user2'
    )
)
;


-- Finding potential partners for 'user2' who want to learn from 'user2'.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_1_id"
    FROM "PotentialPartners"
    WHERE "user_2_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user2'
    )
)
;


-- Finding mutual potential partners for 'user2' for learning and teaching.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_2_id"
    FROM "PotentialPartners"
    WHERE "user_1_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user2'
    )
)
INTERSECT
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_1_id"
    FROM "PotentialPartners"
    WHERE "user_2_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user2'
    )
)
;


-- Finding mutual potential partners for 'user5' in the same city for
-- learning and teaching.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_2_id"
    FROM "PotentialPartners"
    WHERE "user_1_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
INTERSECT
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_1_id"
    FROM "PotentialPartners"
    WHERE "user_2_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
;


-- Finding female mutual potential partners for 'user5' in the same city
-- for learning and teaching.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_2_id"
    FROM "PotentialPartners"
    WHERE "user_1_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
AND "gender" = 'Female'
INTERSECT
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_1_id"
    FROM "PotentialPartners"
    WHERE "user_2_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
AND "gender" = 'Female'
;


-- Finding mutual potential partners for 'user5' aged 29-35 in the same city
-- for learning and teaching.
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_2_id"
    FROM "PotentialPartners"
    WHERE "user_1_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
AND "age" >= 29 AND "age" <= 35
INTERSECT
SELECT "username"
FROM "users"
WHERE "id" IN (
    SELECT "user_1_id"
    FROM "PotentialPartners"
    WHERE "user_2_id" = (
        SELECT "id"
        FROM "users"
        WHERE "username" = 'user5'
    )
    AND (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_1_id"
    ) = (
        SELECT "id_city"
        FROM "users"
        WHERE "id" = "user_2_id"
    )
)
AND "age" >= 29 AND "age" <= 35
;



