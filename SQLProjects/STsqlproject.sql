SHOW DATABASES;

CREATE DATABASE financial_db;

USE financial_db;

-- ---------- Question-1 ----------
-- Create datasetsuretrust Table

CREATE TABLE datasetsuretrust (
    `Order Date` DATE,
    `Product Name` VARCHAR(255),
    Category VARCHAR(100),
    Region VARCHAR(50),
    Unit_cost FLOAT,
    Quantity INT,
    Cost FLOAT,
    Sales FLOAT,
    Profit FLOAT
);

SHOW TABLES;

SELECT * FROM datasetsuretrust;



-- ---------- Convert Order Date into DATE format ----------
-- Run only if Order Date is stored as text

SET SQL_SAFE_UPDATES = 0;

UPDATE datasetsuretrust
SET `Order Date` = STR_TO_DATE(`Order Date`, '%m/%d/%Y');



-- ---------- Question-2 ----------
-- Query Quarterly Revenue Growth

SELECT
    YEAR(`Order Date`) AS year,
    QUARTER(`Order Date`) AS quarter,
    SUM(Sales) AS revenue
FROM datasetsuretrust
GROUP BY year, quarter
ORDER BY year, quarter;



-- ---------- Question-3 ----------
-- JOIN Product and Region Tables

SELECT
    d.`Product Name`,
    d.Category,
    d.Region,
    d.Sales
FROM datasetsuretrust d
JOIN datasetsuretrust r
ON d.Region = r.Region;



-- ---------- Question-4 ----------
-- GROUP BY Profitability by Segment

SELECT
    Category,
    Region,
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM datasetsuretrust
GROUP BY Category, Region
ORDER BY total_profit DESC;



-- ---------- Question-5 ----------
-- Stored Procedures for Financial KPIs

DELIMITER $$

CREATE PROCEDURE Financial_KPI()
BEGIN
    SELECT
        SUM(Sales) AS Total_Revenue,
        SUM(Cost) AS Total_Cost,
        SUM(Profit) AS Total_Profit
    FROM datasetsuretrust;
END $$

DELIMITER ;

CALL Financial_KPI();



-- ---------- Question-6 ----------
-- Window Functions for YoY Growth

SELECT
    year,
    revenue,
    LAG(revenue) OVER (ORDER BY year) AS previous_year,

    (
        (revenue - LAG(revenue) OVER (ORDER BY year))
        / LAG(revenue) OVER (ORDER BY year)
    ) * 100 AS growth_percent

FROM (
    SELECT
        YEAR(`Order Date`) AS year,
        SUM(Sales) AS revenue
    FROM datasetsuretrust
    GROUP BY year
) t;



-- ---------- Question-7 ----------
-- Top 5 Profitable Products

SELECT
    `Product Name`,
    SUM(Profit) AS total_profit
FROM datasetsuretrust
GROUP BY `Product Name`
ORDER BY total_profit DESC
LIMIT 5;



-- ---------- Question-8 ----------
-- Trigger Alerts for Cost Overruns

DELIMITER $$

CREATE TRIGGER cost_alert
BEFORE INSERT ON datasetsuretrust
FOR EACH ROW
BEGIN
    IF NEW.Cost > 5000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cost exceeds allowed limit';
    END IF;
END $$

DELIMITER ;



-- ---------- Question-9 ----------
-- Export SQL Results to Excel

-- Use MySQL ODBC Connector
-- Connect MySQL database with Excel
-- Import datasetsuretrust table into Excel