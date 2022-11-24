
# Positionner - `goto(x, y)`

La fonction `goto(x, y)` permet de positionner la tortue à une position `(x, y)`.


Nous allons voir que :

- la fonction `pos()` retourne la position actuelle de la tortue,
- la fonction `goto(x, y)` positionne la tortue à la position `(x, y)`,
- les fonctions `xcor()` et `ycor()` retournent la coordonnée x ou y,
- les fonctions `setx(x)` et `sety(y)` affectent la coordonnée x ou y.

```{question}
La fonction `pos()` du module `turtle`

{f}`positionne la tortue`  
{f}`retourne la coordonnée x`  
{v}`retourne un tuple de coordonnées`  
{f}`vérifie si une valeur est positive`
```

## La position `pos()`

La fonction `pos()` retourne la position actuelle de la tortue, sous forme d'un tuple `(x, y)`. Dans le dessin de l'escalier, la fonction `write(pos())` affiche les coordonnées de chaque marche, marquée par un point noir.

```{exercise}
Affichez un point (dot) et les coordonnées de chaque point d'inflexion de l'escalier.
```

```{codeplay}
from turtle import *

for i in range(4):
    dot()
    write(pos())    # affiche la position (x, y)
    forward(50)
    left(90)
    forward(30)
    right(90)
    
forward(80)
```

## Valeur `xcor()` et `ycor()`

Les deux fonctions `xcor()` et `ycor()` retournent que la partie x ou y des coordonnées. Dans le dessin de l'escalier, la fonction `write(xcor())` affiche la coordonnée x, et la fonction `write(ycor())` affiche la coordonnée y de chaque marche.

```{exercise}
Transformez l'escalier en un escalier qui descend.
```

```{codeplay}
from turtle import *

for i in range(4):
    forward(50)
    left(90)
    dot()
    write(xcor())   # affiche la coordonnée x
    forward(30)
    right(90)
    dot()
    write(ycor())   # affiche la coordonnée y
    
forward(80)
```

## Positionner avec `goto()`

La fonction `goto(x, y)` positionne la tortue à la position `(x, y)`. Les coordonnées de la position de l’origine de chaque triangle sont affichées.

```{codeplay}
from turtle import *

def triangle():
    down()
    write(pos())
    for i in range(3):
        forward(100)
        left(120)
    up()
        
triangle()      # position à (0, 0)
goto(150, 50)
triangle()      # position à (150, 50)
goto(-200, 80)
triangle()      # position à (-200, 80)
```

## Dessiner un polygone

Avec la fonction `goto(x, y)` nous pouvons facilement dessiner une ligne polygonale.

```{codeplay}
from turtle import *

goto(0, 0)
goto(200, 0)
goto(200, 100)
goto(100, 150)
goto(0, 100)
goto(0, 0)
```

La fonction `goto()` accepte deux coordonnées x, y séparés sous la forme `goto(x, y)` ou alternativement un seul argument sous forme de tuple `goto(p)`.

```{codeplay}
from turtle import *

goto(0, 0)
goto(200, 0)
goto(200, 100)

p = (100, 150)
q = (0, 100)
r = (0, 0)

goto(p)
goto(q)
goto(r)
```

Mais une façon beaucoup plus compacte et flexible, c'est de représenter un polygone avec un tuple de points. Ensuite nous dessinons cette forme géométrique avec une boucle à l'aide de la fonction `goto(p)`.

```{exercise}
Ajoutez 4 points supplémentaires dans le tuple du polygone pour insérer une porte de taille 50x30.
```

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)    # affiche la position (x, y)
```

## Relier les points

Relier les points est un casse-tête en deux dimensions qui comprend une suite de points numérotés à relier.

![dots](media/dots.png)

Le programme suivant numérote les points du polygone.

```{exercise}
Ajoutez encore la porte à la maison, mais dessinez que les points avec un numéro, sans dessiner les lignes, comme dans le jeu relier les points.
```

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

i = 0
for p in poly:
    goto(p)
    write(i)
    i = i + 1
```

## Déplacer un polygone

Avec le polygone représenté par un tuple de ses coordonnées, il est facile de le déplacer et redessiner le polygone ailleurs.

```{exercise}
Déplacez la maison vers une position où elle n'est plus superposée à la première maison.
```

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)
    
color('red')
for p in poly:
    q = p[0] - 150, p[1] - 50
    goto(q)
    write(q)
```

## Changer l'échelle

Avec le polygone représenté par un tuple de ses coordonnées, il est facile de le déplacer et redessiner le polygone ailleurs avec un changement d'échelle.

```{exercise}
Ajoutez une troisième maison encore plus petite.
```

```{codeplay}
from turtle import *

poly = ((0, 0), (200, 0), (200, 100), (100, 150), (0, 100), (0, 0))

for p in poly:
    goto(p)
    write(p)
    
color('red')
for p in poly:
    q = 0.7 * p[0] - 200, 0.7 * p[1] - 100
    goto(q)
    write(q)
```

## Images miroirs

Dans le jeu de Tetris, nous pouvons définir les formes sous forme d'un tuple qui dessine un petit polygone. Multiplier les coordonnées par une variable `a` permet de changer de taille. Changer le signe d'une ou des deux coordonnées permet de trouver l'image miroir.

```{exercise}
Ajoutez l'image miroir manquante.
```

```{codeplay}
from turtle import *

a = 40
L = ((0, 0), (2, 0), (2, 1), (1, 1), (1, 3), (0, 3), (0, 0))

for p in L:
    q = a * p[0], a * p[1]
    goto(q)
    write(p)
    
for p in L:
    q = a * p[0], -a * p[1]
    goto(q)
    
for p in L:
    q = -a * p[0], -a * p[1]
    goto(q)
```

## Direction `heading()`

La fonction `heading()` renvoie la direction actuelle de la tortue.
La fonction `write(heading())` affiche la direction actuelle de la tortue à chaque extrémité.

```{codeplay}
from turtle import *

a = 100
n = 18

for i in range(n):
    forward(100)
    write(heading())
    backward(100)
    left(360/n)
```

La direction (heading) des 8 segments d'un octogone.

```{codeplay}
from turtle import *

n = 8
for i in range(n):
    write(heading())
    forward(70)
    left(360/n)
```

## Orienter avec `seth(a)`

La fonction opposée à `heading()` est `setheading(a)` ou sa version courte `seth(a)` qui permet d'orienter la tortue dans une direction particulière.

Ceci est pratique pour dessiner les pièces dans une direction spécifique.
Par exemple dans le Tetris, les figures peuvent avoir 4 orientations différentes.

```{exercise}
Ajoute deux autres L avec une position et orientation appropriée pour créer un remplissage compact.
```

```{codeplay}
from turtle import *
a = 20

def L():
    down()
    for angle in (0, 90, 90, -90, 0, 90, 90, 0, 0, 90):
        forward(a)
        left(angle)
    up()

L()
goto(3*a, -a)
seth(90)
L()
```

## Tangram

Le tangram, « sept planches de la ruse », ou jeu des sept pièces, est une sorte de puzzle chinois. C'est une dissection du carré en sept pièces élémentaires. Des dissections plus générales, de formes différentes, sont également appelées tangrams.

![tangram](media/tangram0.png)

```{exercise}
Utilisez les fonctions `goto(x, y)` et `setheading(a)` pour ajouter encore deux triangles et former un carré.
```

```{codeplay}
from turtle import *
a = 50

def triangle():
    p = pos()
    forward(2*a)
    left(90)
    forward(2*a)
    goto(p)
    
seth(45)
triangle()
goto(0, 2.82*a)
seth(-45)
triangle()
```

## Multiples polygones

Pour transformer une image en multiples polygones, nous pouvons placer une grille sur l'image ou imprimer l'image sur du papier carré.

![bird](media/poly_bird.jpg)

L'image origami de l'oiseau est composé de 

- 17 points
- 7 polygones

Nous repérons d'abord toutes les coordonnées des points dans une liste `points`.  Avec un indexage du tuple tel que `point[0]` on peut accéder ou point 0.

Les 7 polygones sont tout simplement des tuples avec les indices des points.

```{codeplay}
from turtle import *

points = ((19, 3), (26, 17), (22, 48), (30, 0), (42, 38), 
          (33, 54), (30, 53),  (13, 85), (2, 87), (64, 50),
          (61, 72), (8, 92), (82, 68), (85, 78),(68, 80), 
          (53, 73), (80, 57), (94, 60))
          
polygons = ((0, 1, 2),
            (3, 4, 5, 2),
            (6, 5, 7, 8),
            (4, 9, 10, 11),
            (9, 12, 10),
            (12, 13, 14, 15, 10),
            (16, 17, 13))

up()
i = 0
for p in points:
    goto(-150 + 3 *p[0], -150 + 3*p[1])
    dot(p)
    write(i)
    i = i + 1
```

Pour dessiner multiples polygones, nous devons parcourir la liste des polygones. 
Pour chaque polygone nous parcourons ses points. 

Avec les deux tuples `pos` et `size` nous pouvons choisir la position et la taille des polygones.

    goto(pos[0] + size[0] * p[0], pos[1] + size[1] * p[1])

Pour fermer le polygone, nous revenons sur le premier point de la liste.

    p = points[poly[0]]
    goto(pos[0] + size[0] * p[0], pos[1] + size[1] * p[1])


```{codeplay}
from turtle import *

points = ((19, 3), (26, 17), (22, 48), (30, 0), (42, 38), 
          (33, 54), (30, 53),  (13, 85), (2, 87), (64, 50),
          (61, 72), (8, 92), (80, 57), (85, 78),(68, 80), 
          (53, 73), (82, 68), (94, 60))
          
polygons = ((0, 1, 2),
            (3, 4, 5, 2),
            (6, 5, 7, 8),
            (4, 9, 10, 11),
            (9, 12, 10),
            (12, 13, 14, 15, 10),
            (16, 17, 13))

up()
i = 0
pos = (-150, -150)
size = (3, 3)
for poly in polygons:
    for i in poly:
        p = points[i]
        goto(pos[0] + size[0] * p[0], pos[1] + size[1] * p[1])
        down()
        dot(p)
        write(i)
    p = points[poly[0]]
    goto(pos[0] + size[0] * p[0], pos[1] + size[1] * p[1])
    up()
```

## Exercice

### Tangram

Choisissez un animal est recréez la figure.

![tangram](media/tangram1.jpg)

```{codeplay}
from turtle import *
a = 50

def triangle():
    p = pos()
    begin_fill()
    forward(2*a)
    left(90)
    forward(2*a)
    goto(p)
    end_fill()

seth(90)
color('red')
triangle()
```

### Tangram 2

Choisissez un animal est recréez la figure.

![tangram](media/tangram2.jpg)

```{codeplay}
from turtle import *
a = 50

from turtle import *
a = 50

def triangle():
    p = pos()
    begin_fill()
    forward(2*a)
    left(90)
    forward(2*a)
    goto(p)
    end_fill()

seth(180)
color('orange')
triangle()
```