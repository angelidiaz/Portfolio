-- the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

--------------------------------------
----- Project: LanguageExchange ------
--------------------------------------


-- Drop the tables if they exist
DROP TABLE IF EXISTS "friends";
DROP TABLE IF EXISTS "TeachingLanguages";
DROP TABLE IF EXISTS "LearningLanguages";
DROP TABLE IF EXISTS "users";
DROP TABLE IF EXISTS "cities";
DROP TABLE IF EXISTS "languages";


-- Drop the view if it exists
DROP VIEW IF EXISTS "PotentialPartners";


-- Drop the index if it exists
DROP VIEW IF EXISTS "search_by_age";


VACUUM;


-- Representing languages that want to be learned or taught
CREATE TABLE "languages" (
    "id" INTEGER,
    "language" TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id")
);


-- Representing cities in the world where users live
CREATE TABLE "cities" (
    "id" INTEGER,
    "country" TEXT NOT NULL,
    "state" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    PRIMARY KEY("id")
);


-- Representing students or users who want to learn or teach languages
CREATE TABLE "users" (
    "id" INTEGER,
    "username" TEXT NOT NULL UNIQUE,
    "age" INTEGER,
    "gender" TEXT,
    "id_city" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("id_city") REFERENCES "cities"("id")
);


-- Representing languages that a user wants to learn
CREATE TABLE "LearningLanguages" (
    "id" NUMBER,
    "id_user" NUMBER,
    "id_language" NUMBER,
    PRIMARY KEY("id"),
    FOREIGN KEY("id_user") REFERENCES "users"("id"),
    FOREIGN KEY("id_language") REFERENCES "languages"("id")
);


-- Representing languages that a user wants to teach
CREATE TABLE "TeachingLanguages" (
    "id" NUMBER,
    "id_user" NUMBER,
    "id_language" NUMBER,
    PRIMARY KEY("id"),
    FOREIGN KEY("id_user") REFERENCES "users"("id"),
    FOREIGN KEY("id_language") REFERENCES "languages"("id")
);


-- Representing friendship connections between users
CREATE TABLE "friends" (
    "id" NUMBER,
    "id_user1" NUMBER,
    "id_user2" NUMBER,
    PRIMARY KEY("id"),
    FOREIGN KEY("id_user1") REFERENCES "users"("id"),
    FOREIGN KEY("id_user2") REFERENCES "users"("id")
);


-- Creating a view to identify potential partners by matching users (user_2) who
-- want to teach a language with users (user_1) who want to learn that language
CREATE VIEW "PotentialPartners" AS
SELECT DISTINCT
    "LearningLanguages"."id_user" AS "user_1_id",
    "TeachingLanguages"."id_user" AS "user_2_id"
FROM "LearningLanguages"
JOIN "TeachingLanguages" ON "LearningLanguages"."id_language" = "TeachingLanguages"."id_language"
WHERE "user_1_id" != "user_2_id"
;


-- Creating an index on the users table
CREATE INDEX "search_by_age" ON "users" ("age");

--------------------------- Inserting Data -----------------------

----------------- QUERIES USING INSERT ----------------------------
-- Inserting 5 languages
INSERT INTO "languages" ("id", "language")
VALUES (1, 'English'),
(2, 'Spanish'),
(3, 'French'),
(4, 'German'),
(5, 'Italian');


-- Inserting 5 cities
INSERT INTO "cities" ("id", "country", "state", "city")
VALUES (1, 'USA', 'California', 'Los Angeles'),
(2, 'UK', 'England', 'London'),
(3, 'Germany', 'Berlin', 'Berlin'),
(4, 'Spain', 'Madrid', 'Madrid'),
(5, 'Switzerland', 'Zurich', 'Zurich');


-- Inserting 10 users
INSERT INTO "users" ("id", "username", "age", "gender", "id_city") VALUES
(1, 'user1', 25, 'Male', 1),
(2, 'user2', 30, 'Female', 2),
(3, 'user3', 22, 'Male', 3),
(4, 'user4', 27, 'Female', 4),
(5, 'user5', 29, 'Male', 5),
(6, 'user6', 24, 'Female', 1),
(7, 'user7', 28, 'Male', 2),
(8, 'user8', 23, 'Female', 3),
(9, 'user9', 26, 'Male', 4),
(10, 'user10', 31, 'Female', 5);


-- Inserting data into LearningLanguages
INSERT INTO "LearningLanguages" ("id", "id_user", "id_language") VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 4),
(4, 4, 2),
(5, 5, 3),
(6, 5, 4),
(7, 5, 5),
(8, 6, 2),
(9, 7, 3),
(10, 8, 3),
(11, 9, 1),
(12, 10, 1);


-- Inserting data into TeachingLanguages
INSERT INTO "TeachingLanguages" ("id", "id_user", "id_language") VALUES
(1, 1, 2),
(2, 2, 3),
(3, 3, 1),
(4, 4, 5),
(5, 5, 1),
(6, 6, 1),
(7, 7, 2),
(8, 8, 3),
(9, 9, 4),
(10, 10, 3),
(11, 10, 4),
(12, 10, 5);


-- Inserting data into Friends
INSERT INTO "friends" ("id", "id_user1", "id_user2") VALUES
(1, 1, 2),
(2, 2, 3),
(3, 3, 4),
(4, 4, 5),
(5, 5, 6),
(6, 6, 7),
(7, 7, 8),
(8, 8, 9),
(9, 9, 10),
(10, 10, 1);


