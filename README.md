# Proyecto numeros complejos

Programa que hace operaciones las basicas de los numeros complejos tales como:
suma, resta, producto, conjugado, division, modulo y fase, ademas puede hacer
la conversion de coordenadas cartesianas a polares y viceversa.

## Prerequisitos
```
PyCharm instalado en su equipo 
```
## Correr los tests
Para correr los test tendra que modificar los valores de los numeros complejos
que quiera operar, de igual manera el resultado que espera de la operacion.
El siguiente ejemplo muestra donde debe hacer dichas modificaciones.
```
 def test_suma(self):
     c1 = (4, 3)
     c2 = (-1, 2)
     # c1 y c2 son complejos de la forma (a,b) a es real y b imaginaria
     self.assertEqual(cl.suma(c1, c2), (3, 5))
     # donde se ubica (3,5) debe digitar el resultado esperado
```
## Hecho con
* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - IDE usada para la realizacion del proyecto
## Autores
* **Miguel Salamanca**