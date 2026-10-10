CREATE DATABASE IF NOT EXISTS portal;
USE portal;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50),
  password VARCHAR(100),
  role VARCHAR(20)
);
INSERT INTO users (username, password, role) VALUES
  ('admin', 'S3cureP@ss2026', 'admin'),
  ('jsmith', 'password123', 'employee');
