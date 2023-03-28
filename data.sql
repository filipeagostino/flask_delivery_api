-- Active: 1673012520730@@127.0.0.1@3306
CREATE DATABASE IF NOT EXISTS delivery;

USE delivery;

CREATE TABLE deliverer (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    phone VARCHAR(14) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE customer (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    zip_code VARCHAR(8) NOT NULL,
    house_number VARCHAR(5) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(14) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE product (
    id INTEGER NOT NULL AUTO_INCREMENT,
    deliverer INTEGER REFERENCES deliverer(id),
    customer INTEGER REFERENCES customer(id),
    product_name VARCHAR(100) NOT NULL,
    delivery_status VARCHAR(10) NOT NULL DEFAULT 'transport',
    PRIMARY KEY(id),
    FOREIGN KEY (deliverer) REFERENCES deliverer(id),
    FOREIGN KEY (customer) REFERENCES customer(id)
);

SET character_set_client = utf8;