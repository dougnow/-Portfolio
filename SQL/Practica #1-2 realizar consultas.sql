---1.	Selecciona de la Tabla Date las primeras 100 Filas
Select TOP 100*
FROM Date

-- Realiza una consulta Distintiva de la columna A�o y ordene del a�o mas reciente al mas antiguo. 
--Esto nos permitir� entender los alcances que tendr� nuestra Base de Datos.

Select distinct (A�o)
FROM Date
ORDER BY A�o DESC

--Extrae los fines de semana (s�bado y domingo) en tu base de datos, del a�o 2018.

Select*
FROM Date
WHERE [Nombre del Dia] IN ('s�bado','domingo')
AND A�o = 2018 

--Realiza una consulta que traiga los meses agrupados y ord�nalos de enero a diciembre

Select distinct NumeroMes, Mes
FROM Date
order by NumeroMes


--De la Tabla Padron Electoral, realiza una b�squeda de las personas que tengan la inicial del 
--nombre igual a la inicial de tu propio nombre y que adem�s su primer apellido sea igual a tu 
-- propio primer apellido. Por ejemplo, si tu nombre es Esteban Madrigal, la consulta deber�a 
-- traer a todas las personas de apellido Madrigal y que su nombre inicie con "E".
-- Richard Douglas
Select*
FROM Registro_Nacional
WHERE Nombre LIKE 'R%'
AND Primer_Apellido = 'DOUGLAS'