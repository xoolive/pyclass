---
title: Data visualization of collected ADS-B signals
permalink: /adsb-project
layout: default
back: ..
---

L'objectif de la journée est de mettre en pratique les connaissances acquises dans le semaine pour mettre en commun les données collectées la veille et en proposer une visualisation.

Il s'agit de tracer un fond de carte avec d'une couleur, les trajectoires des avions qui atterrissent sur les aéroports parisiens d'Orly (ORY/LFPO) et de Charles de Gaulle (CDG/LFPG), et d'une autre, les trajectoires d'avions qui en décollent.

Dans un premier temps, il s'agira de tracer les données collectées par un groupe, puis une fois cette première carte produite, de faire une deuxième carte avec toutes les données fusionnées.

## Sources de données

Les fonds de carte peuvent être obtenus sur le site de l'IGN:

- la base [ROUTE500](https://geoservices.ign.fr/route500);
- ou la base [BDCARTO](https://geoservices.ign.fr/bdcarto) qui va la remplacer à l'avenir.

La bibliothèque [`cartes`](https://github.com/xoolive/cartes/) peut aussi être utilisée, notamment pour les détails des aéroports.

## Bonus

- À l'aide des données de vitesse sol, vitesse air (_true air speed_ ou TAS), angle de cap (_heading_) et de route (_track_), reconstituer une carte des vents à une tranche d'altitude donnée.

- Tracer une distribution des vitesses verticales moyennes pour les avions au décollage en fonction du type avion. Une base de données des types avion vous sera proposée.
