CREATE TABLE Praca (
    id NUMBER(3) PRIMARY KEY CHECK(id >= 1),
    tytuł VARCHAR2(500),
    rok NUMBER(4),
    autorzy NUMBER,
    punkty NUMBER
);

CREATE TABLE Autor (
    id VARCHAR2(50) PRIMARY KEY,
    ryzyko NUMBER,
    sloty VARCHAR2(10)
);

CREATE TABLE Autorstwo (
    id NUMBER(3) AUTO_INCREMENT PRIMARY KEY,
    praca NUMBER,
    autor VARCHAR2(50)
);