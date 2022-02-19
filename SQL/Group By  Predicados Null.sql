-- Groupby - having -Alias
--Alias en columnas (renombrado)

-- Renombrar columnas con un Alias (este cambio no afecta el nombre de las tablas, solo para la consulta)

Select *
FROM Product

Select
ColorID,
ColorName
FROM Product

-- Forma numero 1
Select
ColorID  ID,
ColorName
FROM Product

--Forma numero 2
Select 
ColorID ID,
ColorName AS Color
FROM Product

--Group By (agrupacion)

Select 
ColorID ID,
ColorName AS Color
FROM Product
GROUP BY
ColorID,
ColorName
ORDER BY
ColorID

-- Having (condicion Logica que se le aplica al GroupBy)
Select 
ColorID ID,
ColorName AS Color
FROM Product
GROUP BY
ColorID,
ColorName
HAVING
ColorID >= 10
ORDER BY
ColorID


--Predicados NULL  - Permite seleccionar los valor en condicion NULL

-- IS NULL
Select*
FROM Promotion
WHERE PromotionName IS NULL


--IS NOT NULL   - selecciona los datos No Null
Select * 
FROM Promotion
WHERE PromotionName IS NOT NULL