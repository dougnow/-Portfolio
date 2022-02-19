-- Proyecto Final Richard Douglas Grijalba

--Primer Query:
-- Este query debe de contener en su estructura:
-- Funciones de Texto (al menos 2)
-- Al menos un Join
-- Funciones de Fecha (al menos 2)
-- Operaciones Matemáticas Básicas (al menos 1)
-- Commando Where, Group By, Order By

Select*
FROM Customers$

Select*
FROM Regions$

Select*
FROM Cities$


Select*
FROM Facturas$

Select*
FROM Calendario$

Select*
FROM Categories$

Select Distinct (ProductName)
FROM Products$

Select
A.City,
A.ProductName,
UPPER (CONCAT ('Costa_Rica','-',A.ProductName)) AS Nombre_Producto,
MONTH(B.Date) AS Mes,
DATEPART(QQ,Date) AS Trimestre,
YEAR(B.Date) AS Año,
SUM(A.Quantity * A.UnitPrice)  AS Venta
FROM Facturas$ A INNER JOIN Calendario$ B
ON A.Order_Date = B.Date
WHERE Año LIKE 2018
OR Año LIKE 2017
GROUP BY
City,ProductName,Date
ORDER BY 
Venta DESC

--Este query debe de contener en su estructura:
-- Funciones de Agregación (al menos 2)
--Al menos un Join
--Funciones Lógicas (al menos 1)
--Commando Where (Operaciones Lógicas), Group By, Order By, Having
--Select Anidado (al menos 1)


Select TOP (100)
A.City,
A.Salesperson,
IIF(SUM(A.Quantity * A.UnitPrice) > 8000, 'BIEN', 'MEJORAR') AS Vendedor_Goals,
UPPER (CONCAT ('Costa_Rica','-',A.ProductName)) AS Nombre_Producto,
MONTH(B.Date) AS Mes,
DATEPART(QQ,Date) AS Trimestre,
YEAR(B.Date) AS Año,
SUM(A.Quantity * A.UnitPrice)  AS Venta
FROM Facturas$ A INNER JOIN Calendario$ B
ON A.Order_Date = B.Date
WHERE Año > 2017
GROUP BY
City,ProductName,Date,A.Salesperson
HAVING 
City != 'Berlin'
ORDER BY 
Venta DESC


