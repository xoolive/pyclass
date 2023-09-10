---
title: Cartes du monde, cartes de France
subtitle: Planisphères & projections
author: Xavier Olive
theme: utopia
lang: french
mainlang: french
polyglossia-lang:
  name: french
header-includes:
  - \PassOptionsToPackage{usenames,dvipsnames}{xcolor}
  - \usetikzlibrary{shapes, shapes.misc}
  - \definecolor{mDarkGreen}{HTML}{239541}
  - \usepackage{xpatch}
  - \xapptocmd\ttfamily{\XeTeXinterchartokenstate=0 }{}{}
---

## The Blue Marble

![](img/blue_marble.jpg){ height=80% }

# De la sphère au plan

## Projections azimutales

![](img/proj_azimut.pdf)

## Projections cylindriques

![](img/proj_cylindrique.pdf){ height=80% }

## Projections coniques

![](img/proj_conique.pdf)

## Propriétés des projections

Deux propriétés mutuellement exclusives:

- les projections **conformes** conservent les distances;

- les projections **équivalentes** conservent les surfaces.

Beaucoup de projections sont des compromis qui ne conservent ni angles ni surfaces.

# Projections

## La projection de Mercator

- Une projection définie par Mercator au XVIe siècle
- La projection de référence pour la navigation:  
  _Les lignes de cap constant sont des lignes droites_
- De vrais problèmes de perception des tailles: [http://thetruesize.com](http://thetruesize.com)

## La projection de Mercator

![](img/world-mercator.jpg)

## La projection conforme conique de Lambert

- Une des projections définies par J. H. Lambert (1772)
- Système adopté en France pendant la 1re guerre mondiale
- La **projection officielle dans plusieurs pays d'Europe**  
  notamment la France, la Belgique, l'Estonie, etc.
- La **projection de référence en aéronautique**  
  _Le plus court chemin entre deux points (grand cercle) est (localement) une ligne droite._

## La projection Lambert 93 à l'IGN

![](img/ign-morzine.jpg){ height=80% }

## Carte de France en Lambert 93

![](img/france-lambert.png){ height=80% }

## Carte d'Europe en Lambert 93

![](img/europe-lambert.jpg){ height=80% }

## Projections standards dans les autres pays d'Europe

![](img/europe-standard.png)

## La projection Winkel-Tripel

Projection construite afin de minimiser les distorsions de surface, de direction et de distance (cf. _tripel_)

- ni conforme, ni équivalente;
- aucune formule de passage inverse;
- adoptée par la National Geographic Society depuis 1998

## La projection Winkel-Tripel

![](img/world-winkel.png)

## Projection de Bertin

![](img/world-bertin.png)

## Projection orthographique

![](img/world-korea.png){ height=80% }

## http://xkcd.com/1799

![](img/bad_map_projection_time_zones.png)

## http://xkcd.com/1784

![](img/bad_map_projection_liquid_resize.png){ height=80% }
