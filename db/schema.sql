USE master;
Go

CREATE DATABASE beverage;
Go

CREATE TABLE dbo.pop (
    id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(20) NOT NULL,
    color VARCHAR(20) NOT NULL
);
Go

INSERT INTO dbo.pop (name, color)
VALUES
('RC Cola', 'brown'),
('Sprite', 'clear'),
('Verners', 'brown'),
('Mt. Lightening', 'green');
Go