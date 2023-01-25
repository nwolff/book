# TP ALU

L'unité arithmétique (ALU) et logique permet de choisir parmi un certain nombre d'opérations. Un registre permet de mémoriser un des opérandes de ce calcul.

Mais tout d'abord, nous commençons avec une petite révision des portes logiques.

## Loi de Morgan

La **loi de Morgan** dit qu'une porte ET peut être fabriquée avec une porte OU et des inverseurs, et vice-versa.

- Créez une porte ET en utilisant des portes OU et NON.
- Vérifiez son bon fonctionnement.

```{logic}
:ref: morgan
:height: 300
:showonly: in out not or
{

}
```

- Créez une porte OU en utilisant des portes ET et NON.
- Vérifiez son bon fonctionnement.

```{logic}
:ref: morgan
:height: 300
:showonly: in out not and
{

}
```

## Sélectionneur

Le sélectionneur permet de choisir entre les deux signaux 

- lent (période de 2 s)
- rapide (période de 250 ms)

Recréez un tel sélecteur avec des portes NON, ET, OU.

```{logic}
:ref: mux
:height: 400
:showonly: in out clock not and or
{
  "v": 4,
  "in": [
    {"type": "clock", "pos": [40, 120], "id": 73, "period": 250},
    {"type": "clock", "pos": [40, 30], "id": 81, "period": 2000},
    {"pos": [140, 130], "orient": "n", "id": 82, "name": "S0", "val": 0},
    {"pos": [80, 310], "id": 91, "name": "sel", "val": 1}
  ],
  "out": [
    {"pos": [470, 70], "id": 74, "name": "Z0"},
    {"pos": [470, 260], "id": 92}
  ],
  "gates": [
    {"type": "AND", "pos": [250, 230], "in": [83, 84], "out": 85},
    {"type": "AND", "pos": [250, 300], "in": [86, 87], "out": 88},
    {"type": "NOT", "pos": [170, 310], "in": 89, "out": 90}
  ],
  "components": [
    {"type": "mux-2to1", "pos": [140, 70], "in": [51, 52, 53], "out": 54}
  ],
  "wires": [[73, 52], [54, 74, {"propagationDelay": 1000}], [81, 51], [82, 53], [90, 87], [91, 89]]
}
```

## Multiplexeur

Le multiplexeur (MUX) permet de choisir entre deux signaux 4-bits nommés a et b.
Ajoutez les éléments qui manquent. 

- Ajoutez une deuxième entrée 4-bits avec un affichage.
- Ajoutez un décodeur et affichage à 7 segments.

```{logic}
:ref: mux
:height: 400
:showonly: in in.nibble out.nibble-display out.nibble decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 100], "id": [33, 34, 35, 36], "val": [1, 0, 1, 0], "name": "a"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [120, 100], "id": [37, 38, 39, 40]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [220, 150], "in": [20, 21, 22, 23, 24, 25, 26, 27, 28], "out": [29, 30, 31, 32]}
  ],
  "wires": [[33, 20], [34, 21], [35, 22], [36, 23], [33, 37], [34, 38], [35, 39], [36, 40]]
}
```

## Sélection d'opérations

Complétez le circuit qui permet de sélectionner enter les deux opérations `a ET b` et `a OU b`.

- Connectez a et b au portes OU
- Ajoutez une entrée de sélection pour le multiplexeur

```{logic}
:ref: mux
:height: 450
:showonly: in in.nibble out.nibble-display out.nibble quad-gate
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 70], "id": [24, 25, 26, 27], "val": [0, 1, 0, 0], "name": "a"},
    {"type": "nibble", "pos": [50, 170], "id": [28, 29, 30, 31], "val": [0, 0, 0, 0], "name": "b"}
  ],
  "out": [
    {"type": "nibble", "pos": [410, 170], "id": [57, 58, 59, 60], "name": "a ET/OU b"}
  ],
  "components": [
    {"type": "quad-gate", "subtype": "AND", "pos": [200, 120], "in": [3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14]},
    {"type": "quad-gate", "subtype": "OR", "pos": [200, 330], "in": [32, 33, 34, 35, 36, 37, 38, 39], "out": [40, 41, 42, 43]},
    {"type": "mux-8to4", "pos": [320, 170], "in": [44, 45, 46, 47, 48, 49, 50, 51, 52], "out": [53, 54, 55, 56]}
  ],
  "wires": [[24, 3], [25, 4], [26, 5], [27, 6], [28, 7], [29, 8], [30, 9], [31, 10], [11, 44], [12, 45], [13, 46], [14, 47], [53, 57], [54, 58], [55, 59], [56, 60]]
}
```

Un clic droit sur la porte quadruple permet de choisir son type (AND, OR, XOR, NAND, NOR, XNOR).

## ALU

L'unité arithmétique et logique, ALU (arithmetic and logic unit), est la partie de l'ordinateur qui effectue les différents calculs arithmétiques et logiques.

Ci-dessous vous pouvez voir les circuits logiques d'une ALU 4-bits très utilisé dans les années 60 et 70, le modèle 74181.

![ALU](https://upload.wikimedia.org/wikipedia/commons/c/c0/74181aluschematic.png)

L'ALU dont nous disposons peut effectuer 4 opérations :

- addition (00)
- soustraction (01)
- OU logique (10)
- ET logique (11)

Ajoutez la deuxième entrée, un bloc de visualisation pour la sortie et les 2 entrées de sélection. Ensuite, testez les 4 opérations.

```{logic}
:ref: alu
:height: 400
:showonly: in out in.nibble out.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 150], "id": [72, 73, 74, 75], "val": [1, 0, 1, 0]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [340, 200], "id": [68, 69, 70, 71]},
    {"type": "nibble-display", "pos": [130, 150], "id": [80, 81, 82, 83]}
  ],
  "components": [
    {"type": "alu", "pos": [230, 200], "in": [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], "out": [62, 63, 64, 65, 92, 67, 66]}
  ],
  "wires": [[62, 68], [63, 69], [64, 70], [65, 71], [72, 51], [73, 52], [74, 53], [75, 54], [72, 80], [73, 81], [74, 82], [75, 83]]
}
```

## Addition et soustraction

Ajoutez un circuit qui calcule a+b-c et affiche le résultat.
Par exemple pour a=7, b=5, c=3, le résultat affiché devrait être 9.

```{logic}
:ref: mux
:height: 400
:showonly: alu in out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [60, 80], "id": [11, 12, 13, 14], "val": [1, 1, 1, 0], "name": "a"},
    {"type": "nibble", "pos": [60, 180], "id": [79, 80, 81, 82], "val": [1, 0, 1, 0], "name": "b"},
    {"type": "nibble", "pos": [60, 280], "id": [105, 106, 107, 108], "val": [1, 1, 0, 0], "name": "c"}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 80], "id": [67, 68, 69, 70]},
    {"type": "nibble-display", "pos": [110, 180], "id": [83, 84, 85, 86]},
    {"type": "nibble-display", "pos": [110, 280], "id": [114, 115, 116, 117]}
  ],
  "wires": [[11, 67], [12, 68], [13, 69], [14, 70], [79, 83], [80, 84], [81, 85], [82, 86], [105, 114], [106, 115], [107, 116], [108, 117]]
}
```

## Addition signée

Interprétez les nombres binaires comme des nombres signés. Vous pouvez le configurer avec le menu contextuel. Complétez l'additionneur 4-bit et montrez que l'addition de -2 et -3 donne bien -5.

```{logic}
:ref: addsigned
:height: 400
:showonly: alu in in.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [60, 80], "id": [0, 1, 2, 3], "val": [0, 1, 1, 1]}
  ],
  "out": [
    {"type": "nibble-display", "pos": [110, 80], "id": [4, 5, 6, 7], "radix": -10}
  ],
  "components": [
    {"type": "alu", "pos": [230, 130], "in": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "out": [19, 20, 21, 22, 23, 24, 25]}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [0, 8], [1, 9], [2, 10], [3, 11]]
}
```

## Addition 8-bits

Pour additionner un nombre à 8-bits, il faut combiner deux ALU 4-bits.
Complétez le circuit pour afficher l'addition de deux nombres binaires 8-bits.
Ajoutez une option pour soustraire deux nombres.

```{logic}
:ref: add8
:height: 500
:showonly: alu in in.byte out.byte-display
{
  "v": 4,
  "in": [
    {"type": "byte", "pos": [40, 110], "id": [24, 25, 26, 27, 28, 29, 30, 31], "val": "00001010"},
    {"type": "byte", "pos": [40, 320], "id": [74, 75, 76, 77, 78, 79, 80, 81], "val": "00000100"}
  ],
  "out": [
    {"type": "byte-display", "pos": [100, 110], "id": [32, 33, 34, 35, 36, 37, 38, 39]},
    {"type": "byte-display", "pos": [400, 170], "id": [66, 67, 68, 69, 70, 71, 72, 73]}
  ],
  "components": [
    {"type": "alu", "pos": [220, 130], "in": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "out": [11, 12, 13, 14, 15, 16, 17]},
    {"type": "alu", "pos": [220, 360], "in": [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], "out": [59, 60, 61, 62, 63, 64, 65]}
  ],
  "wires": [[24, 32], [25, 33], [26, 34], [27, 35], [28, 36], [29, 37], [30, 38], [31, 39], [17, 58], [24, 0], [25, 1], [26, 2], [27, 3], [28, 48], [29, 49], [30, 50], [31, 51], [11, 66], [12, 67], [13, 68], [14, 69], [74, 4], [75, 5], [76, 6]]
}
```

## Égalité (`a == b`)

Parfois il est nécessaire de comparer deux valeurs numériques.

- Créez un comparateur qui met la sortie **Égal** à 1 si les deux nombres a et b sont égaux.

```{logic}
:ref: mux
:height: 300
:showonly: in alu
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 130], "id": [4, 5, 6, 7], "val": [1, 0, 1, 0], "name": "a"},
    {"type": "nibble", "pos": [40, 230], "id": [8, 9, 10, 11], "val": [1, 1, 1, 0], "name": "b"}
  ],
  "out": [
    {"pos": [320, 180], "id": 30, "name": "Egal"}
  ],
  "components": [
    {"type": "alu", "pos": [140, 180], "in": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], "out": [23, 24, 25, 26, 31, 28, 27]}
  ],
  "wires": [[5, 13], [6, 14], [7, 15], [8, 16], [9, 17], [10, 18], [11, 19], [4, 12]]
}
```

## Multiplier 1 bit

Les règles de la multiplication 1-bit sont très simples. Voici la table de vérité.

| a | b | a x b |
|---|---|:-----:|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

On voit tout de suite que ceci correspond à la porte ET.
Dans l'exemple si dessous vous voyez une porte ET pour multiplier a et b, les deux ayant juste 1 bit.

- Vérifiez le bon fonctionnement du multiplicateur 1-bit
- Ensuite, utilisez 4 portes ET pour créer un multiplicateur **a** (4-bits) fois **b** (1-bit).
- Basculez b entre 0 et 1 pour vérifier si votre circuit fonctionne correctement.

```{logic}
:ref: mul1
:height: 400
:showonly: in and in.nibble out.nibble-display
{
  "v": 4,
  "in": [
    {"pos": [70, 50], "id": 0, "name": "a", "val": 1},
    {"pos": [70, 70], "id": 4, "name": "b", "val": 0},
    {"type": "nibble", "pos": [70, 200], "id": [6, 7, 8, 9], "val": [0, 0, 1, 0], "name": "a"},
    {"pos": [70, 290], "id": 10, "name": "b", "val": 1}
  ],
  "out": [
    {"pos": [210, 60], "id": 5, "name": "a x b"},
    {"type": "nibble-display", "pos": [350, 200], "id": [11, 12, 13, 14], "name": "a x b"}
  ],
  "gates": [
    {"type": "AND", "pos": [140, 60], "in": [1, 2], "out": 3}
  ],
  "wires": [[0, 1], [4, 2], [3, 5]]
}
```

## Multiplier par 2, 4, 8

La multiplication par une puissance de 2 est facile. Il suffit de décaler les bits.
Le circuit ci-dessous calcule 2a en décalant d'un bit en direction du poids fort.

- Complétez le circuit pour calculer et afficher 4a et 8a.
- Vérifiez avec a=5. Votre affichage devrait montrer 10, 20 et 40.

```{logic}
:ref: mul2
:height: 400
:showonly: in.nibble out.nibble-display out.byte-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 60], "id": [0, 1, 2, 3], "val": [1, 1, 0, 0], "name": "a"}
  ],
  "out": [
    {"type": "byte-display", "pos": [220, 60], "id": [4, 5, 6, 7, 8, 9, 10, 11], "name": "2a"},
    {"type": "nibble-display", "pos": [90, 60], "id": [12, 13, 14, 15]},
    {"type": "byte-display", "pos": [220, 160], "id": [16, 17, 18, 19, 20, 21, 22, 23], "name": "4a"},
    {"type": "byte-display", "pos": [220, 260], "id": [24, 25, 26, 27, 28, 29, 30, 31], "name": "8a"}
  ],
  "wires": [[0, 12], [1, 13], [2, 14], [3, 15], [0, 5], [1, 6], [2, 7], [3, 8]]
}
```

## Multiplier par bit

Le circuit ci-dessus utilise un multiplexeur 8x4 pour faire l'addition 1-bit, au lieu des 4 portes ET.

Pour les 4 bits b0 à b3, chaque bit contrôle la multiplication par son poids (1, 2, 4, 8)

- a x b0 x 1
- a x b1 x 2
- a x b2 x 4
- a x b3 x 8

Pour compléter l'opération de multiplication 4x4 bits, la dernière étape sera d'additionner les 4 nombres.

Complétez le circuit avec :

- deux entrées que vous appelez **b2** et **b3**
- un affichage 8 bits qui affiche 4a sous contrôle de b2
- un affichage 8 bits qui affiche 8a sous contrôle de b3

```{logic}
:ref: mul3
:height: 450
:showonly: in in.nibble out.nibble-display out.byte-display mux-8to4
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 230], "id": [0, 1, 2, 3], "val": [1, 0, 1, 0], "name": "a"},
    {"pos": [150, 50], "orient": "s", "id": 39, "name": "b0", "val": 1},
    {"pos": [240, 50], "orient": "s", "id": 108, "name": "b1", "val": 1}
  ],
  "out": [
    {"type": "nibble-display", "pos": [250, 340], "id": [35, 36, 37, 38]},
    {"type": "nibble-display", "pos": [90, 230], "id": [49, 50, 51, 52]},
    {"type": "byte-display", "pos": [350, 350], "id": [67, 68, 69, 70, 71, 72, 73, 74]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [150, 180], "in": [22, 23, 24, 25, 26, 27, 28, 29, 30], "out": [31, 32, 33, 34]},
    {"type": "mux-8to4", "pos": [240, 180], "in": [53, 54, 55, 56, 57, 58, 59, 60, 61], "out": [62, 63, 64, 65]},
    {"type": "mux-8to4", "pos": [350, 180], "in": [75, 76, 77, 78, 79, 80, 81, 82, 83], "out": [84, 85, 86, 87]},
    {"type": "mux-8to4", "pos": [460, 180], "in": [95, 96, 97, 98, 99, 100, 101, 102, 103], "out": [104, 105, 106, 107]}
  ],
  "wires": [[0, 26], [1, 27], [2, 28], [3, 29], [31, 35], [32, 36], [33, 37], [34, 38], [39, 30], [0, 49], [1, 50], [2, 51], [3, 52], [0, 57], [1, 58], [2, 59], [3, 60], [62, 68], [63, 69], [64, 70], [65, 71], [0, 79], [1, 80], [2, 81], [3, 82], [0, 99], [1, 100], [2, 101], [3, 102], [108, 61]]
}
```

## Multiplier 4 bits

La multiplication 4 x 4 bits nécessite:

- 4 multiplexeurs  pour la multiplication 4 x 1 bit
- 3 additionneurs pour additionner les 4 opérandes décalés

Pour multiplier `0101` x `1001` = `00101101`  (5 x 9 = 45) nous écrivons en colonnes ceci :

```
1     1001
0    0000
1   1001
0 +0000
----------
  00101101
```

Modifiez a et b dans le circuit multiplicateur 4 x 4 bits ci-dessus vérifiez que vous obtenez bien le produit de a et b. Faites une capture avec la plus grande valeur possible.

```{logic}
:ref: mul4
:height: 600
:showonly: in in.nibble out.nibble-display out.byte-display mux-8to4 adder
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [40, 490], "id": [19, 20, 21, 22], "val": [1, 0, 0, 1], "name": "a"},
    {"type": "nibble", "pos": [40, 70], "id": [23, 24, 25, 26], "val": [1, 0, 1, 0], "name": "b"}
  ],
  "out": [
    {"type": "byte-display", "pos": [630, 420], "id": [115, 116, 117, 118, 119, 120, 121, 122]},
    {"type": "nibble-display", "pos": [90, 70], "id": [141, 142, 143, 144]},
    {"type": "nibble-display", "pos": [90, 490], "id": [145, 146, 147, 148]}
  ],
  "components": [
    {"type": "mux-8to4", "pos": [80, 220], "in": [45, 46, 47, 48, 49, 50, 51, 52, 53], "out": [54, 55, 56, 57]},
    {"type": "mux-8to4", "pos": [140, 340], "in": [58, 59, 60, 61, 62, 63, 64, 65, 66], "out": [67, 68, 69, 70]},
    {"type": "alu", "pos": [210, 290], "in": [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133], "out": [134, 135, 136, 137, 138, 139, 140]},
    {"type": "mux-8to4", "pos": [290, 410], "in": [149, 150, 151, 152, 153, 154, 155, 156, 157], "out": [158, 159, 160, 161]},
    {"type": "alu", "pos": [360, 360], "in": [162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172], "out": [173, 174, 175, 176, 177, 178, 179]},
    {"type": "mux-8to4", "pos": [440, 480], "in": [192, 193, 194, 195, 196, 197, 198, 199, 200], "out": [201, 202, 203, 204]},
    {"type": "alu", "pos": [510, 430], "in": [205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215], "out": [216, 217, 218, 219, 220, 221, 222]}
  ],
  "wires": [[19, 49], [20, 50], [21, 51], [22, 52], [23, 53], [19, 62], [20, 63], [21, 64], [22, 65], [67, 127], [68, 128], [69, 129], [70, 130], [55, 123], [56, 124], [57, 125], [24, 66], [54, 115], [134, 116], [23, 141], [24, 142], [25, 143], [26, 144], [19, 145], [20, 146], [21, 147], [22, 148], [19, 153], [20, 154], [21, 155], [22, 156], [135, 162], [136, 163], [137, 164], [158, 166], [159, 167], [160, 168], [161, 169], [25, 157], [173, 117], [140, 165], [139, 152], [174, 205], [175, 206], [176, 207], [178, 195], [201, 209], [202, 210], [203, 211], [204, 212], [19, 196], [20, 197], [21, 198], [22, 199], [179, 208], [216, 118], [217, 119], [218, 120], [219, 121], [222, 122], [26, 200]]
}
```

## Registre

Le registre que nous allons voir plus en détail dans le prochain chapitre permet de mémoriser une donnée.
Avec un coup d'horloge (clock), les 4-bits de données sont mémorisés.

Ajoutez un deuxième registre, décodeur et affichage à 7 segments, pour permettre d'afficher un nombre décimal de 00 à 99 ou un nombre hexadécimal de 00 à FF.

```{logic}
:ref: reg
:height: 500
:showonly: in in.nibble register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 130], "id": [11, 12, 13, 14], "val": [1, 0, 0, 0]},
    {"pos": [100, 310], "id": 15, "name": "clock", "val": 0, "isPushButton": true},
    {"type": "nibble", "pos": [50, 230], "id": [35, 36, 37, 38], "val": [0, 0, 0, 0]}
  ],
  "out": [
    {"type": "7seg", "pos": [410, 140], "id": [27, 28, 29, 30, 31, 32, 33, 34]}
  ],
  "components": [
    {"type": "register", "pos": [220, 130], "in": [0, 1, 2, 3, 4, 5, 6], "out": [7, 8, 9, 10], "state": [0, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [330, 130], "in": [16, 17, 18, 19], "out": [20, 21, 22, 23, 24, 25, 26]}
  ],
  "wires": [[11, 3], [12, 4], [13, 5], [14, 6], [15, 0], [7, 16], [8, 17], [9, 18], [10, 19], [20, 27], [21, 28], [22, 29], [23, 30], [24, 31], [25, 32], [26, 33]]
}
```

## Accumulateur

Un accumulateur est un registre spécial qui *accumule* une somme. La sortie de ce registre doit être reliée avec l'entrée B de l'alu. À chaque coup d'horloge du registre, le calcul `a + acc` est effectué et affiché.

Complétez le circuit et calculez la somme 1+3+7.

**Attention:** tenez le bouton suffisamment longtemps pour laisser propager les signaux jusqu'au bout.

```{logic}
:ref: acc
:height: 500
:showonly: in in.nibble register alu out.nibble-display
{
  "v": 4,
  "in": [
    {"type": "nibble", "pos": [50, 80], "id": [0, 1, 2, 3], "val": [1, 0, 0, 0], "name": "a"},
    {"pos": [340, 280], "orient": "n", "id": 37, "name": "clear", "val": 0, "isPushButton": true},
    {"pos": [210, 280], "id": 38, "name": "add", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "nibble-display", "pos": [100, 80], "id": [47, 48, 49, 50]},
    {"type": "nibble-display", "pos": [460, 130], "id": [51, 52, 53, 54]}
  ],
  "components": [
    {"type": "alu", "pos": [210, 130], "in": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "out": [15, 16, 17, 18, 19, 20, 21]},
    {"type": "register", "pos": [340, 130], "ref": "acc", "in": [22, 23, 24, 25, 26, 27, 28], "out": [29, 30, 31, 32], "state": [1, 1, 0, 1]}
  ],
  "labels": [
    {"pos": [330, 30], "text": "accumulateur"}
  ],
  "wires": [[0, 4], [1, 5], [2, 6], [3, 7], [15, 25], [16, 26], [17, 27], [18, 28], [0, 47], [1, 48], [2, 49], [3, 50], [29, 51], [30, 52], [31, 53], [32, 54]]
}
```

## Décodeur de touche

Quand on appuie sur une touche d'une calculatrice électronique, telle que la TI-30, la valeur de la touche est transformée en binaire, enregistré dans un registre, et affiché avec un affichage à 7 segments. Les étapes sont :

- une **touche** 0 - 9 est appuyé
- une conversion en **binaire** est faite
- une entrée **clock** est produite
- la valeur est mémorisée dans un **registre**
- la valeur est décodée vers les signaux a-g 
- la valeur numérique est montrée sur l'**affichage** à 7 segments

Complétez le circuit pour traiter les touches 0 à 3

```{logic}
:ref: but
:height: 500
:showonly: in or or3 register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"pos": [50, 80], "id": 63, "name": "0", "val": 0, "isPushButton": true},
    {"pos": [50, 120], "id": 69, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 160], "id": 70, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 200], "id": 71, "name": "3", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "7seg", "pos": [470, 150], "id": [12, 13, 14, 15, 16, 17, 18, 19]}
  ],
  "gates": [
    {"type": "OR", "pos": [150, 130], "in": [64, 65], "out": 66},
    {"type": "OR", "pos": [150, 190], "in": [77, 78], "out": 79},
    {"type": "OR3", "pos": [200, 300], "in": [80, 81, 82], "out": 83}
  ],
  "components": [
    {"type": "register", "pos": [310, 140], "in": [41, 42, 43, 44, 45, 46, 47], "out": [48, 49, 50, 51], "state": [1, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [390, 140], "in": [52, 53, 54, 55], "out": [56, 57, 58, 59, 60, 61, 62]}
  ],
  "labels": [
    {"pos": [50, 30], "text": "touche"},
    {"pos": [140, 30], "text": "vers binaire"},
    {"pos": [230, 30], "text": "clock"},
    {"pos": [300, 30], "text": "registre"},
    {"pos": [390, 30], "text": "décodeur"},
    {"pos": [480, 30], "text": "affichage"}
  ],
  "wires": [[48, 52], [49, 53], [50, 54], [51, 55], [56, 12], [57, 13], [58, 14], [59, 15], [60, 16], [61, 17], [62, 18], [69, 64], [71, 78], [83, 41]]
}
```

## Décodeur pour 8 touches

Complétez le circuit pour traiter les touches 0 à 7

```{logic}
:ref: but8
:height: 500
:showonly: in or or3 or4 register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"pos": [50, 80], "id": 63, "name": "0", "val": 0, "isPushButton": true},
    {"pos": [50, 120], "id": 69, "name": "1", "val": 0, "isPushButton": true},
    {"pos": [50, 160], "id": 70, "name": "2", "val": 0, "isPushButton": true},
    {"pos": [50, 200], "id": 71, "name": "3", "val": 0, "isPushButton": true},
    {"pos": [50, 240], "id": 89, "name": "4", "val": 0, "isPushButton": true},
    {"pos": [50, 280], "id": 90, "name": "5", "val": 0, "isPushButton": true},
    {"pos": [50, 320], "id": 91, "name": "6", "val": 0, "isPushButton": true},
    {"pos": [50, 360], "id": 92, "name": "7", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "7seg", "pos": [470, 150], "id": [12, 13, 14, 15, 16, 17, 18, 19]}
  ],
  "components": [
    {"type": "register", "pos": [310, 140], "in": [41, 42, 43, 44, 45, 46, 47], "out": [48, 49, 50, 51], "state": [1, 0, 0, 0]},
    {"type": "decoder-7seg", "pos": [390, 140], "in": [52, 53, 54, 55], "out": [56, 57, 58, 59, 60, 61, 62]}
  ],
  "labels": [
    {"pos": [50, 30], "text": "touche"},
    {"pos": [140, 30], "text": "vers binaire"},
    {"pos": [230, 30], "text": "clock"},
    {"pos": [300, 30], "text": "registre"},
    {"pos": [390, 30], "text": "décodeur"},
    {"pos": [480, 30], "text": "affichage"}
  ],
  "wires": [[48, 52], [49, 53], [50, 54], [51, 55], [56, 12], [57, 13], [58, 14], [59, 15], [60, 16], [61, 17], [62, 18]]
}
```

## Incrémenter/décrémenter

Certains appareils électroniques ont très peu de touches et on doit utiliser juste deux boutons.
C'est le cas pour régler la température ou le volume.

Compléter le circuit pour les boutons

- **up** pour incrémenter la valeur (clock)
- **down** pour décrémenter la valeur (clock + soustraction)
- **clear** pour mettre la valeur à zéro

Attention au délai de transmission par défaut de 100 ms. Il faut soit appuyer plus longtemps sur les boutons, ou diminuer ce délai.

```{logic}
:ref: incdec
:height: 500
:showonly: in or or3 or4 register decoder-7seg out.7seg
{
  "v": 4,
  "in": [
    {"pos": [80, 370], "id": 75, "name": "clear", "val": 0, "isPushButton": true},
    {"pos": [80, 330], "id": 78, "name": "down", "val": 0, "isPushButton": true},
    {"pos": [80, 290], "id": 82, "name": "up", "val": 0, "isPushButton": true}
  ],
  "out": [
    {"type": "7seg", "pos": [490, 150], "id": [27, 28, 29, 30, 31, 32, 33, 34]}
  ],
  "gates": [
    {"type": "OR", "pos": [210, 320], "in": [79, 80], "out": 81}
  ],
  "components": [
    {"type": "register", "pos": [300, 140], "in": [0, 1, 2, 3, 4, 5, 6], "out": [7, 8, 9, 10], "state": [0, 0, 1, 0]},
    {"type": "decoder-7seg", "pos": [410, 140], "in": [16, 17, 18, 19], "out": [20, 21, 22, 23, 24, 25, 26]},
    {"type": "alu", "pos": [160, 140], "in": [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "out": [68, 69, 70, 71, 72, 73, 74]}
  ],
  "wires": [[7, 16], [8, 17], [9, 18], [10, 19], [20, 27], [21, 28], [22, 29], [23, 30], [24, 31], [25, 32], [26, 33], [7, 57], [8, 58], [9, 59], [10, 60], [68, 3], [69, 4], [70, 5], [71, 6]]
}
```