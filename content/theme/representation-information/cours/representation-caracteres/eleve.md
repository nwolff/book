# Représentation des caractères

Toute l'information est représentée dans un ordinateur par des nombres
encodés sous forme binaire par des 0 et des 1. Se pose alors la question
de la représentation des caractères, ne serait-ce que parce que la communication
avec les ordinateurs s'opère essentiellement sous forme textuelle.

## Principe

La solution retenue a consisté à définir une table de conversion qui indique
de façon univoque une concordance entre une valeur numérique et un caractère:

| Caractère | Décimal | Hexadécimal | Binaire  | | | | | Caractère | Décimal | Hexadécimal | Binaire  |
|-----------|---------|-------------|----------|-|-|-|-|-----------|---------|-------------|----------|
|     A     |    65   |    0x41     | 01000001 | | | | |     a     |    97   |    0x61     | 01100001 |
|     B     |    66   |    0x42     | 01000010 | | | | |     b     |    98   |    0x62     | 01100010 |
|     C     |    67   |    0x43     | 01000011 | | | | |     c     |    99   |    0x63     | 01100011 |
|     …     |    …    |     …       |    …     | | | | |     …     |    …    |     …       |    …     |
|     Z     |    90   |    0x5A     | 01011010 | | | | |     z     |   122   |    0x7A     | 01111010 |


Chaque caractère frappé sur le clavier engendre le nombre correspondant.

Chacun des caractères de la phrase que vous lisez a ainsi été stocké,
transmis et manipulé par les ordinateurs sous la forme d'une suite
de nombres qu'on nomme **chaîne de caractères**.

Lorsqu'il s'agit de représenter ce texte à l'écran ou à l'impression
à destination des êtres humains, les logiciels utilisent la table
dans l'autre sens pour rendre cela intelligible.

En plus des lettres, les caractères qui représentent
les nombres (les chiffres arabes)
sont eux-mêmes listés dans la table de conversion.
Contre-intuitivement, la valeur binaire du caractère
ne correspond généralement pas au nombre.

| Caractère | Décimal | Hexadécimal | Binaire  |
|-----------|---------|-------------|----------|
|     0     |    48   |    0x30     | 00110000 |
|     1     |    49   |    0x31     | 00110001 |
|     …     |    …    |     …       |    …     |
|     9     |    57   |    0x39     | 00111001 |


Ces tables donnent également une représentation des caractères de ponctuation
et des symboles mathématiques, ainsi que des caractères non-imprimables comme
le retour à la ligne.

En réalité, il n'existe pas une table de conversion unique, mais des dizaines
de tables de conversion. Certaines tables ont été proposées à l'origine
par des constructeurs d'ordinateurs ou des éditeurs de systèmes d'exploitation.

## Table ASCII

La première table à s'imposer historiquement était la table ASCII
(pour American Standard Code for Information Interchange).
Malgré sa large acceptation, avec ses **7 bits par caractère**,
cette table avait pour principal défaut de ne pas prendre en compte
les caractères qui n'existent pas dans la langue anglaise,
ne serait-ce que les lettres accentuées.

Des tables multiples, mutuellements incompatibles, ont alors émergé: une table
pour les européens, une autre pour les japonais et ainsi de suite.

Progressivement, notamment avec l'émergence du Web au cours des années 1990,
l'augmentation de l'interconnexion des ordinateurs personnels a amené
au début des années 2000 à la mise en place d'une énorme table
intégrant le contenu de toutes les tables existantes.


L'exemple ci-dessous vous renvoie la valeur binaire du texte que vous écrivez.

```{codeplay}

texte = input("Le texte : ")

print("Le texte d'origine est : " + str(texte))

res = ' '.join(format(ord(i), 'b') for i in texte)

print("Le texte en binaire est : " + str(res))
```



`````{panels}
:column: col-lg
ASCII Art
^^^
Dès l'introduction de l'encodage ASCII, et jusqu'à aujourd'hui,
une pratique répandue dans les milieux informatiques
est d'utiliser les caractères ASCII comme support de créativité artistique.

Les caractères ont un poids minimal en code binaire,
c'est donc une façon très efficace de transmettre une information visuelle.

````{toggle}
```{codeplay}
print ("""
  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$
 /$$__  $$ /$$__  $$| $$  /$$/|_  $$_/| $$__  $$
| $$  \ $$| $$  \__/| $$ /$$/   | $$  | $$  \ $$
| $$$$$$$$|  $$$$$$ | $$$$$/    | $$  | $$$$$$$/
| $$__  $$ \____  $$| $$  $$    | $$  | $$____/
| $$  | $$ /$$  \ $$| $$\  $$   | $$  | $$
| $$  | $$|  $$$$$$/| $$ \  $$ /$$$$$$| $$
|__/  |__/ \______/ |__/  \__/|______/|__/

""")
```

[Cet outil](https://www.patorjk.com/software/taag/#p=display&f=Small&t=Entrez%20votre%20texte)
vous permet de transformer n'importe quel texte en ASCII.


La vidéo suivante présente "l'asciiquarium",
un aquarium en ASCII dans le terminal.

```{youtube} pAfvoVtsA64
````
`````





## Standard UTF

Le [standard Unicode](https://home.unicode.org/) UTF (Universal Character Set Transformation Format)
s'est imposé pour l'échange, car il permet d'agréger sur **64 bits par caractère**
l'entier des caractères utilisés dans toutes les langues humaines… et même extraterrestres,
puisque le [Klingon](https://www.kli.org/about-klingon/klingon-history/) est également intégré.

Les caractères liés à l'édition des partitions de musique ou les émojis
y sont également intégrés.



### Variantes

Pour éviter de consommer 64 bits par caractère, des variantes plus compactes
ont été mises à disposition.

La plus connue – des européens, puisqu'elle regroupe les caractères
qui nous concernent… – est la table UTF-8. Elle se concentre
sur les premiers 8 bits de la table UTF complète.



