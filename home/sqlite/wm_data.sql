CREATE TABLE region (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL UNIQUE,
  active BOOLEAN NOT NULL DEFAULT TRUE
);


DROP TABLE wm;
CREATE TABLE wm (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name  VARCHAR(255) NOT NULL UNIQUE,
  region_id INTEGER NOT NULL,
  active  BOOLEAN NOT NULL DEFAULT TRUE,
  FOREIGN KEY (region_id) REFERENCES regions(id) 
);
