-- MySQL CREATE TABLE for DatasetSureTrust.csv
-- Corporate Financial Analytics Project

CREATE TABLE IF NOT EXISTS suretrust_sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    unit_cost DECIMAL(10, 4) NOT NULL,
    quantity INT NOT NULL,
    sales DECIMAL(12, 2),
    profit DECIMAL(12, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_order_date (order_date),
    INDEX idx_category (category),
    INDEX idx_region (region)
);

-- Column Descriptions:
-- id: Unique identifier for each record
-- order_date: Date when the order was placed (format: DD-MM-YYYY)
-- product_name: Name of the product
-- category: Product category (Furniture, Office Supplies, etc.)
-- region: Geographic region (South, West, East, North)
-- unit_cost: Cost per unit
-- quantity: Number of units ordered
-- sales: Total sales amount
-- profit: Profit earned on the sale
-- created_at: Timestamp of when record was inserted
