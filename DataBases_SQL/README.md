# CS50 SQL - Project Portfolio

By Angel Gabriel Elias Diaz

This repository contains a collection of SQL projects, including work completed for Harvard University's CS50 SQL course ([https://cs50.harvard.edu/sql/2024/](https://cs50.harvard.edu/sql/2024/)) and a personal project. The CS50 SQL projects, named `01_querying.ipynb`, `02_relating.ipynb`, `03_writing.ipynb`, and `04_viewing.ipynb`, explore different aspects of database design, querying, and data manipulation using SQLite within a Jupyter Notebook environment. All necessary database files (`.db`) for these projects are located within the `databases` directory.

Additionally, this repository includes a self-initiated project focused on building a database for a language exchange platform, detailed in the [`Exchange_Languages/DESIGN.md`](Exchange_Languages/DESIGN.md) document.

## Project Summaries:

### `01_querying.ipynb` - Cyberchase Episode Database Analysis

* **Problem:** This project involves querying a database (`databases/cyberchase.db`) containing information about episodes of the *Cyberchase* educational television series. The goal is to practice SQL skills by retrieving specific information about episodes based on criteria like season, air date, and educational topic.
* **Database:** `databases/cyberchase.db` with a single table `episodes` containing columns such as `id`, `season`, `episode_in_season`, `title`, `topic`, `air_date`, and `production_code`.
* **Focus:** SQL SELECT statements, filtering with WHERE clauses, and understanding database schema for targeted data retrieval.

### `02_relating.ipynb` - Investigating Missing Packages in Boston

* **Problem:** This project requires analyzing the `databases/packages.db` database to help a mail clerk in Boston locate missing packages. By using the provided database schema and limited customer information, the task is to determine the last known location, address type, and contents of the lost parcels.
* **Database:** `databases/packages.db` with tables including `addresses`, `drivers`, `packages`, and `scans`, establishing relationships between delivery drivers, packages, delivery locations, and scan events.
* **Focus:** Complex SQL queries involving JOIN operations across multiple tables to trace package movements and retrieve related information. The process emphasizes logical deduction and documenting the query steps.

### `03_writing.ipynb` - Importing and Cleaning NASA Meteorite Data

* **Problem:** This project centers around importing a CSV file of historical meteorite landings into a SQLite database (`databases/meteorites.db`) and cleaning the data according to specific requirements. The cleaned data will then be used for further analysis.
* **Database:** Creation of `databases/meteorites.db` with a `meteorites` table containing columns like `id`, `name`, `class`, `mass`, `discovery`, `year`, `lat`, and `long`, derived and cleaned from the CSV data.
* **Focus:** SQL and SQLite commands for database creation, data import, handling NULL values, rounding decimal numbers, filtering data based on specific criteria, sorting, and assigning new unique identifiers.

### `04_viewing.ipynb` - Analyzing Boston AirBnB Data

* **Problem:** This project involves creating SQL views on the `databases/bnb.db` database to gain insights into the AirBnB market in Boston. The goal is to understand the influence of AirBnB on the local tourism scene by examining listings, reviews, and availability data.
* **Database:** `databases/bnb.db` with tables including `listings` (property details), `reviews` (customer feedback), and `availabilities` (booking information and prices).
* **Focus:** SQL CREATE VIEW statements to generate virtual tables that provide specific perspectives on the data without altering the underlying base tables. This involves selecting and joining data from multiple tables to present aggregated or filtered information.

## Personal Project: Exchange Languages Database

This is a self-developed project focused on creating a database to facilitate language exchange between users. The design and schema of this database are detailed in the `Exchange_Languages/DESIGN.md` file.

* **Problem:** To design a database that allows users to connect with others who want to learn the languages they teach and teach the languages they want to learn, considering location and friendship connections.
* **Database:** A SQLite database (`learning_languages.db`) with tables for `users`, `cities`, `languages`, `LearningLanguages`, `TeachingLanguages`, and `friends`.
* **Focus:** Database design principles, entity-relationship modeling, defining table schemas with appropriate data types and constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL), and considering functional requirements like CRUD operations, user matching, and managing friendships.

This collection showcases both coursework from CS50 SQL and independently driven projects, highlighting a comprehensive understanding of relational databases and SQL.