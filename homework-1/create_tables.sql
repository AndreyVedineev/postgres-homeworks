-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(30) NOT NULL,
	last_name varchar(30) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(20)
);

SELECT * FROM orders;
SELECT * FROM employees;
SELECT * FROM public.customers ORDER BY customer_id ASC;