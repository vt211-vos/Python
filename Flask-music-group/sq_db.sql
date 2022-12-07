CREATE TABLE IF NOT EXISTS mainmenu (
    id integer PRIMARY KEY  AUTOINCREMENT,
    title text NOT NULL,
    url text NOT NULL
);

CREATE TABLE IF NOT EXISTS albums(
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL ,
    year int NOT NULL ,
    info text NOT NULL ,
    info2 text NOT NULL
);