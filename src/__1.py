
update order total based on current prices where price total is empty
UPDATE `order_items`, `products` SET `item_total` = `quantity` * `price` WHERE item_total IS NULL