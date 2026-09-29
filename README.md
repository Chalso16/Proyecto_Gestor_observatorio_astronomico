
**_Gestor Observatorio Astronómico_**
--

---
Este repositorio contiene la implementación del proyecto "Gestor Observatorio Astronómico". 
	El código corresponde a la Práctica 1 de la asignatura Técnicas de programación avanzada del Grado en Ingeniería Informática (Universidad Nebrija).   

---
Autores

	Carlos Balbás   
	Lucas Parreño   
	Victor Llorente   

---

**_Descripción del Proyecto_**

-Se trata de una aplicación orientada a objetos en Python para la gestión de un observatorio astronómico. 

-Este hito inicial establece el modelo de dominio base, abarcando conceptos fundamentales como el uso de memoria, el ciclo de vida de los objetos y el encapsulamiento. 

-El proyecto está concebido como una aplicación progresiva que irá creciendo y ganando complejidad a lo largo del cuatrimestre.   

 --- 

**_Arquitectura y Modelo de Dominio_**

El dominio se ha modelado identificando responsabilidades claras para proteger la validez de los datos de negocio. 
	Las clases principales implementadas son:   
	
	ObjetoCeleste: Representa una entrada astronómica fija con identificador, tipo y coordenadas almacenadas en una tupla inmutable.   
	
    Telescopio: Modela el instrumento de observación y aplica validaciones estrictas en el nombre y las horas de uso mediante el uso del decorador @property.   
	
    SesionObservacion: Relaciona un objetivo celeste, un telescopio y una fecha concreta utilizando relaciones de agregación.  
	
    CatalogoObservatorio: Agrupa una colección dinámica (en forma de lista) de objetos celestes y controla una capacidad máxima que se calcula una sola vez en el momento de su creación.   

---    

**Estructura de Archivos:**

`modelo.py`: Contiene la implementación inicial de las clases del dominio con type hints y reglas de encapsulamiento.
    
`demo_modelo.py`: Demuestra de manera práctica el ciclo de vida de los objetos, el funcionamiento del aliasing y el rebinding, y cómo el intérprete de CPython libera la memoria cuando el contador de referencias llega a cero (mediante weakref).
    
`demo_estado_compartido.py`: Ilustra el defecto arquitectónico de usar argumentos por defecto mutables (listas vacías) y aplica el patrón idiomático de Python usando None para garantizar contenedores independientes.   
    
`test_modelo.py`: Programa de pruebas que demuestra la diferencia fundamental entre identidad en memoria (operador is) e igualdad por valor (operador ==) usando como datos de prueba a los integrantes del grupo.   
