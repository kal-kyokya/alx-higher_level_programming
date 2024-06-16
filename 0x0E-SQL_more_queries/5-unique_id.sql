-- Script create a Table

-- Command doing the creation
CREATE TABLE
IF NOT EXISTS `unique_id` (
   id INT UNIQUE DEFAULT 1,
   name VARCHAR(256)
);
