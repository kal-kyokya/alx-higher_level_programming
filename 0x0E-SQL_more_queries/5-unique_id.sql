-- Script create a Table

-- Command doing the creation
CREATE TABLE
IF NOT EXISTS `id_not_null` (
   id INT DEFAULT 1 UNIQUE,
   name VARCHAR(256)
);
