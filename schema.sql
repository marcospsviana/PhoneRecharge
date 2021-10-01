CREATE TABLE company
(
  id      INT  NOT NULL,
  name    TEXT NOT NULL,
  product     ,
  PRIMARY KEY (id)
);

CREATE TABLE product
(
  id         INT  NOT NULL,
  id_product TEXT NOT NULL,
  company_id INT  NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE product
  ADD CONSTRAINT FK_company_TO_product
    FOREIGN KEY (company_id)
    REFERENCES company (id);
