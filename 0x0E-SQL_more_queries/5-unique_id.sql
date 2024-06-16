-- Script create a Table

-- Command doing the creation
CREATE TABLE
IF NOT EXISTS `id_not_null` (
   id INT UNIQUE DEFAULT 1,
   name VARCHAR(256)
);
