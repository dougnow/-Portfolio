---1.	Selecciona de la Tabla Date las primeras 100 Filas
Select TOP 100*
FROM Date

-- Realiza una consulta Distintiva de la columna Año y ordene del año mas reciente al mas antiguo. 
--Esto nos permitirá entender los alcances que tendrá nuestra Base de Datos.

Select distinct (Año)
FROM Date
ORDER BY Año DESC

--Extrae los fines de semana (sábado y domingo) en tu base de datos, del año 2018.

Select*
FROM Date
WHERE [Nombre del Dia] IN ('sábado','domingo')
AND Año = 2018 

--Realiza una consulta que traiga los meses agrupados y ordénalos de enero a diciembre

Select distinct NumeroMes, Mes
FROM Date
order by NumeroMes


--De la Tabla Padron Electoral, realiza una búsqueda de las personas que tengan la inicial del 
--nombre igual a la inicial de tu propio nombre y que además su primer apellido sea igual a tu 
-- propio primer apellido. Por ejemplo, si tu nombre es Esteban Madrigal, la consulta debería 
-- traer a todas las personas de apellido Madrigal y que su nombre inicie con "E".
-- Richard Douglas
Select*
FROM Registro_Nacional
WHERE Nombre LIKE 'R%'
AND Primer_Apellido = 'DOUGLAS'