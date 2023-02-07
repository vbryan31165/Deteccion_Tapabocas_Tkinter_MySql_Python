SELECT us.ID_USUARIO, us.CEDULA, us.NOMBRES, us.APELLIDOS,us.CORREO, us.USUARIO, rol.ROL , 
( CASE WHEN (us.ESTADO = 1 ) THEN "ACTIVO" 
       WHEN (US.ESTADO = 2 ) THEN "INACTIVO"
END )  AS NOMBRE_ESTADO 

FROM usuarios us INNER JOIN roles rol ON (rol.ID_ROL=us.ID_ROL) ORDER BY `us`.`ID_USUARIO` ASC



SELECT * FROM USUARIOS WHERE ESTADO=1 AND USUARIO="b"

SELECT * FROM usuarios WHERE USUARIO LIKE "%r%"

SELECT * FROM usuarios WHERE usuario='b' AND estado=1 LIMIT 1


SELECT COUNT(1) AS Cantidad ,
( CASE WHEN (ESTADO = 1 ) THEN "ACTIVO" 
       WHEN (ESTADO = 2 ) THEN "INACTIVO"
END )  AS NOMBRE_ESTADO FROM usuarios GROUP BY estado


SELECT COUNT(1) AS cantidad ,
( CASE WHEN (ID_ROL = 1 ) THEN "Administrador" 
       WHEN (ID_ROL = 2 ) THEN "Estudiante"
END )  AS NOMBRE_ROL FROM usuarios GROUP BY ID_ROL

SELECT COUNT(1) AS cantidad FROM usuarios

SELECT COUNT(1) AS cantidad,fecha_creacion FROM usuarios GROUP BY fecha_creacion





SELECT (SELECT COUNT(1)  FROM usuarios WHERE estado = 1 ) activo , (SELECT COUNT(1)  FROM usuarios WHERE estado = 2 ) inactivo , (SELECT COUNT(1) FROM usuarios WHERE id_rol=1) Administrador , (SELECT COUNT(1) FROM usuarios WHERE id_rol=2) Estudiante, (SELECT COUNT(1) FROM usuarios) Cantidad FROM DUAL 


COUNT(1) AS activo FROM usuario WHERE estado =1 , SELECT COUNT(1) AS inactivo FROM usuario WHERE estado =2 FROM DUAL





INSERT INTO tapabocas (ID_USUARIO,FECHA_HORA_TAPABOCAS,ESTADO_TAPABOCAS) VALUES (2,'2021-08-07 22:39:51',1)