# códigos-SMC
El objetivo de la es la construcción de un sistema LAMP (Linux-Apapche-MySQL-PHP) para la asignatura de Sistema de Monitorización y Control del Máster de Ingeniería Industrial URJC.

A través Arduino se recogerán los datos de los sensores, estos se enviarán a la Raspberry Pi por el puerto serie y posteriormente se mandará a la base de datos creada. Por último, se realizará la representación gráfica de los datos. El equema a seguir es:

![La imagen no se ha cargado correctamente](https://github.com/sanchezco/codigos-SMC/blob/master/Img/esquema.png)

En el repositorio se encuentran todos los códigos que se han utilizado, tanto para los casos prácticos de la asignatura como para 
la entrega:
---
- [**Arduino**](https://github.com/sanchezco/codigos-SMC/tree/master/1%20-%20Arduino) : códigos de la toma de datos de los sensores
---
- [**Python**](https://github.com/sanchezco/codigos-SMC/tree/master/2%20-%20Raspberry) : códigos ejecutables en la Raspberry Pi
---
- [**php**](https://github.com/sanchezco/codigos-SMC/tree/master/4%20-%20php) : códigos de la explotación de datos con GoogleChart
---
