CREATE TABlE IF NOT EXISTS bartenders(
  id SERIAL PRIMARY KEY,
  name TEXT,
  hometown TEXT,
  birthyear INTEGER
);

CREATE TABLE IF NOT EXISTS ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price INTEGER
  );


CREATE TABLE IF NOT EXISTS ingredients_drinks (
  id SERIAL PRIMARY KEY,
  drink_id INTEGER,
  ingredient_id INTEGER
);

CREATE TABLE IF NOT EXISTS drinks (
    id SERIAL PRIMARY KEY,
    name TEXT,
    calories INTEGER,
    price INTEGER,
    alcoholic INTEGER
  );


  CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    hometown TEXT,
    birthyear INTEGER
  );

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    drink_id INTEGER,
    bartender_id INTEGER
  );

  INSERT INTO bartenders (name, hometown, birthyear) VALUES
  ('moe', 'springfield', 1965),
  ('selma', 'milwaukee', 1970),
  ('patty', 'philly', 1970);

INSERT INTO customers (name, hometown, birthyear) VALUES
  ('bart simpson', 'springfield', 2008),
  ('maggie simpson', 'milwaukee', 2016),
  ('lisa simpson', 'philly', 2006);



INSERT INTO drinks (name, calories, price, alcoholic) VALUES
  ('egg cream soda', 80, 3, 0),
  ('milkshake', 300, 5, 0),
  ('rootbeer', 180, 6, 0),
  ('ice cream float', 250, 8, 0),
  ('duff beer', 200, 7,  1),
  ('gin and tonic', 200, 7, 1);


INSERT INTO orders (customer_id, drink_id, bartender_id) VALUES
  (1, 1, 1),
  (1, 1, 1),
  (2, 5, 2),
  (2, 5, 1),
  (2, 5, 1),
  (3, 6, 3),
  (1, 2, 1),
  (2, 3, 2),
  (3, 4, 3);


INSERT INTO ingredients_drinks (drink_id, ingredient_id) VALUES
  (1, 6),
  (1, 5),
  (2, 3),
  (2, 5),
  (6, 1),
  (6, 2);

INSERT INTO ingredients (name, price) VALUES
  ('gin', 3),
  ('tonic', 4),
  ('milk', 2),
  ('rootbeer', 2),
  ('icecream', 2),
  ('seltzer', 2),
  ('rootbeer', 3),
  ('duff beer', 5);
