CREATE TABLE students(id Serial, name text, address text, age int);

INSERT INTO students(name,address,age) VALUES ('Valen','Gran Buenos Aires','20');
INSERT INTO students(name,address,age) VALUES ('Lucia','Bahia Blanca','22');
INSERT INTO students(name,address,age) VALUES ('Yuto','Tokyo','22');

SELECT * FROM students;