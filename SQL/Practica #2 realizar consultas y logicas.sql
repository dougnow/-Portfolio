--1. explorar nuestros datos y verifique las tablas que te permita extraer la informaci�n
--base de datos CONTOSO
Select*
FROM Sales

--2.	Realiza una consulta donde extraigas los 16 diferentes colores que existen

Select DISTINCT(ColorName)
From Product
ORDER BY ColorName

--3. Extrae la Venta por Color y agrupa su resultado obteniendo �nicamente los primeros 
--  10 ID del color, asimismo confecciona una columna condicional nueva con los diferentes colores 
-- (en espa�ol). Para ello puedes tomar de referencia los nombres en ingl�s del resultado de la 
--  consulta anterior y ordena sus datos por ID de Color.

--Prueba de agrupaci�n por ID, Color y la suma del monto ventas
Select TOP (10) [ColorID]
ColorID, SUM(SalesAmount) Suma_Ventas_Color, ColorName
FROM Sales, Product
Group By ColorName, ColorID
ORDER By ColorID


-- Prueba cambio de nombres en espa�ol
Select
ColorName,
CASE
WHEN ColorName = 'Azure' THEN 'Azur'
WHEN ColorName = 'Black' THEN 'Negro'
WHEN ColorName = 'Blue' THEN 'Azul'
WHEN ColorName = 'Brown' THEN 'Cafe'
WHEN ColorName = 'Gold' THEN 'Dorado'
WHEN ColorName = 'Green' THEN 'Verde'
WHEN ColorName = 'Grey' THEN 'Gris'
WHEN ColorName = 'Orange' THEN 'Naranja'
WHEN ColorName = 'Pink' THEN 'Rosado'
WHEN ColorName = 'Purple' THEN 'Purpura'
WHEN ColorName = 'Red' THEN 'Rojo'
WHEN ColorName = 'Silver' THEN 'Plateado'
WHEN ColorName = 'Silver Grey' THEN 'Gris Plata'
WHEN ColorName = 'Transparent' THEN 'Transparente'
WHEN ColorName = 'White' THEN 'Blanco'
WHEN ColorName = 'Yellow' THEN 'Amarillo'
ELSE 'No Existe' END AS Color_espanol
From Product


--Query Final en donde se incluye el TOP , el ordenado, y Color en espa�ol
Select TOP (10) [ColorID]
ColorID, SUM(SalesAmount) Suma_Ventas_Color, ColorName,
CASE
WHEN ColorName = 'Azure' THEN 'Azur'
WHEN ColorName = 'Black' THEN 'Negro'
WHEN ColorName = 'Blue' THEN 'Azul'
WHEN ColorName = 'Brown' THEN 'Cafe'
WHEN ColorName = 'Gold' THEN 'Dorado'
WHEN ColorName = 'Green' THEN 'Verde'
WHEN ColorName = 'Grey' THEN 'Gris'
WHEN ColorName = 'Orange' THEN 'Naranja'
WHEN ColorName = 'Pink' THEN 'Rosado'
WHEN ColorName = 'Purple' THEN 'Purpura'
WHEN ColorName = 'Red' THEN 'Rojo'
WHEN ColorName = 'Silver' THEN 'Plateado'
WHEN ColorName = 'Silver Grey' THEN 'Gris Plata'
WHEN ColorName = 'Transparent' THEN 'Transparente'
WHEN ColorName = 'White' THEN 'Blanco'
WHEN ColorName = 'Yellow' THEN 'Amarillo'
ELSE 'No Existe' END AS Color_espanol
FROM Sales, Product
Group By ColorName, ColorID
ORDER By ColorID


-- 4.	Extrae la Venta por Nombre del D�a (Saturday, Sunday, Monday, ect) para la Regi�n de Asia 
-- y Europa, del a�o 2018 y crea una columna condicional: si es s�bado o domingo que indique 
-- Fin de Semana, de lo contrario Semana Laboral.

Select*
FROM Sales

Select*
FROM Geography

Select*
FROM Date

Select
DiaSemana,[Nombre del Dia], SUM(SalesAmount) AS Venta_DiaSemana,
CASE
WHEN [Nombre del Dia] = 'domingo' THEN 'Fin de Semana'
WHEN [Nombre del Dia] = 's�bado' THEN 'Fin de Semana'
ELSE 'Semana Laboral' END AS Dia_Laboral
From Sales, Date, Geography
WHERE ContinentName = 'Asia'
OR ContinentName = 'Europe'
Group By [Nombre del Dia] , DiaSemana
ORDER BY DiaSemana

--5. Realiza una consulta que extraiga la venta por Mes y A�o. Sin embargo, 
--el mes debe de traer �nicamente las primeras 3 iniciales del mes en 
--formato may�scula para ello utilice las funciones de texto.

Select*
FROM Sales

Select*
FROM Date

--Solucion 1
Select
NumeroMes, SUM(SalesAmount) AS Suma_Ventas,
CHOOSE (NumeroMes, 'ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN', 'JUL', 'AGO', 'SEPT', 'OCT', 'NOV', 'DIC') AS Mes_Abre
FROM Sales, Date
Group By NumeroMes
ORDER BY NumeroMes

--solucion 2
Select
NumeroMes, Mes, SUM(SalesAmount) AS Suma_Ventas,
UPPER (LEFT(Mes,3)) AS Mes_Abre
FROM Sales, Date
Group By NumeroMes, Mes
ORDER BY NumeroMes


--6.	Realiza un query que contenga en su Select:
-- Nombre del Mes, Nombre del Canal , Tipo de Tienda, Nombre del Continente
-- Venta Monetaria y en Unidades, Ord�nalo de Mayor a Menor seg�n las unidades
-- Esta informaci�n ser� �nicamente del a�o 2018 y 2019 y de los D�as de Lunes a viernes

Select*
FROM Sales

Select*
FROM Date

Select*
FROM Channel

Select*
FROM Stores

Select 
Mes, ChannelName, StoreType, ContinentName , SalesQuantity
FROM Sales, Date , Channel , Stores , Geography
WHERE A�o = 2019
OR A�o = 2018
AND DiaSemana BETWEEN 0 AND 4
ORDER BY SalesQuantity DESC

Select TOP 
Mes, [Nombre del Dia], ChannelName, StoreType, ContinentName ,  SalesAmount, SalesQuantity
FROM Sales, Date , Channel , Stores , Geography
WHERE A�o = 2019
OR A�o = 2018
AND DiaSemana BETWEEN 0 AND 4
ORDER BY SalesQuantity DESC

Select TOP (10000) SalesQuantity
Mes, ChannelName, ContinentName , SalesQuantity
FROM Sales, Date , Channel , Stores , Geography
WHERE A�o IN (2018,2019)
AND DiaSemana BETWEEN 0 AND 4
ORDER BY SalesQuantity 
