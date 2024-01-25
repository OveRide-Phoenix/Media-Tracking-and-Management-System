-- Table for tags
CREATE TABLE tags (
    id INT PRIMARY KEY,
    tag_name VARCHAR(50) UNIQUE,
    author_id INT,
    quality VARCHAR(20), -- 'HD', '4K', etc.
    edited BOOLEAN,
    media_type VARCHAR(10), -- 'photo' or 'video', for example
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Table for authors
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(100) UNIQUE
);

-- Table for media files
CREATE TABLE media (
    id INT PRIMARY KEY,
    filename VARCHAR(255),
    file_path VARCHAR(255),
    tag_id INT,
    FOREIGN KEY (tag_id) REFERENCES tags(id)
);

