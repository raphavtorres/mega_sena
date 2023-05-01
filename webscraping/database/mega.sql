CREATE DATABASE mega_sena;

USE mega_sena;

CREATE TABLE mega (
    megaYear INT,
    contest INT,
    n1 VARCHAR(2),
    n2 VARCHAR(2),
    n3 VARCHAR(2),
    n4 VARCHAR(2),
    n5 VARCHAR(2),
    n6 VARCHAR(2),
    dateMega VARCHAR(30),
    PRIMARY KEY (contest)
);

INSERT INTO mega (megaYear, contest, numbers, dateMega)
VALUES ("")
