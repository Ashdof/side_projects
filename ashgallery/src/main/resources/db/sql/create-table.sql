-- Script to manage database table

CREATE TABLE IF NOT EXISTS ashgallery (
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(250),
    image_path VARCHAR(255),
    image_status SMALLINT DEFAULT 1
);