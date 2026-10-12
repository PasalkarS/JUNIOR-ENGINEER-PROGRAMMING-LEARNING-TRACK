
-- 1. Display all products
SELECT * FROM products;

-- 2. Display products with low stock
SELECT product_name, quantity
FROM products
WHERE quantity < 20;

-- 3. Add a new product
INSERT INTO products (product_name, category_id, quantity, price)
VALUES ('USB Cable', 1, 30, 199.00);

-- 4. Update product quantity
UPDATE products
SET quantity = 40
WHERE product_name = 'Mouse';

-- 5. Delete a product
DELETE FROM products
WHERE product_name = 'USB Cable';

-- 6. Display products with their categories
SELECT products.product_name,
       categories.category_name,
       products.quantity,
       products.price
FROM products
JOIN categories
ON products.category_id = categories.category_id;

-- 7. Count products in each category
SELECT categories.category_name,
       COUNT(products.product_id) AS total_products
FROM categories
LEFT JOIN products
ON categories.category_id = products.category_id
GROUP BY categories.category_id, categories.category_name;

-- 8. Calculate total inventory value by category
SELECT categories.category_name,
       SUM(products.quantity * products.price) AS inventory_value
FROM categories
JOIN products
ON categories.category_id = products.category_id
GROUP BY categories.category_id, categories.category_name;
