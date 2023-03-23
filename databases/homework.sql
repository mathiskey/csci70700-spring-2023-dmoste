--Create table
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name VARCHAR,
  age INTEGER,
  gender VARCHAR
);

--Insert data
INSERT INTO cats (name, age, gender) VALUES
("Milton", 6, "M"),
("Marlowe", 6, "M"),
("Midnight", 9, "F"),
("Shadow", 7, "F");

--Display data
SELECT * FROM cats;

--Display just name and age
SELECT name, age FROM cats;

--Display using conditionals
SELECT * FROM cats WHERE gender = "F";
SELECT * FROM cats WHERE age < 8 and gender = "M";

--Display using ORDER
SELECT * FROM cats ORDER BY age;

--Make a change using UPDATE
UPDATE cats SET age = 10 WHERE name ="Midnight";

--Display using ORDER
SELECT * FROM cats ORDER BY name DESC;