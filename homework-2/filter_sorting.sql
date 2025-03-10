-- Напишите запросы, которые выводят следующую информацию:

-- 1. заказы, доставленные в страны France, Germany, Spain (таблица orders, колонка ship_country)
SELECT * FROM orders
         WHERE ship_country IN ('France', 'Germany', 'Spain')
		 ORDER BY ship_country;

-- 2. уникальные города и страны, куда отправлялись заказы, отсортировать по странам и городам (таблица orders, колонки ship_country, ship_city)
SELECT order_id, ship_country, ship_city FROM orders
	ORDER BY ship_country;

-- 3. сколько дней в среднем уходит на доставку товара в Германию (таблица orders, колонки order_date, shipped_date, ship_country)
SELECT AVG (order_date - shipped_date) FROM orders
	WHERE ship_country ='Germany';

-- 4. минимальную и максимальную цену среди продуктов, не снятых с продажи (таблица shipped_date, ship_country, колонки unit_price, discontinued не равно 1)
SELECT 	MIN(unit_price) AS минимальная_цена_среди_продуктов,
		MAX(unit_price) AS максимальная_цена_среди_продуктов
		FROM products;

-- 5. минимальную и максимальную цену среди продуктов, не снятых с продажи и которых имеется не меньше 20 (таблица products, колонки unit_price, units_in_stock, discontinued не равно 1)
SELECT 	MIN(unit_price) AS минимальная_цена_среди_продуктов,
		MAX(unit_price) AS максимальная_цена_среди_продуктов
		FROM products
		WHERE units_in_stock >= 20 AND discontinued != 1;
