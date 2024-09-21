# Explorateur de Qualité des Vins
Ceci est une application Streamlit qui permet aux utilisateurs d'explorer le dataset Wine Quality. Vous pouvez filtrer les vins en fonction de leur acidité, teneur en alcool et qualité à l'aide de curseurs interactifs. Une façon élégante de jouer avec des données sans avoir besoin de déboucher une bouteille !

## Prise en main
### Prérequis
Python 3.6 ou supérieur 
Docker

## Installation
Clonez ce dépôt. Pas besoin de sommelier pour cette étape.
Installez les paquets Python requis.

pip install -r requirements.txt

streamlit run app.py

## Docker
Pour les amateurs de conteneurs, voici comment faire tourner l'application dans un Docker. Et rassurez-vous, ce Docker-là ne coule pas !

Construisez l'image Docker :

bash
Copier le code
docker build -t wine_quality_app .
Lancez le conteneur Docker :

bash
Copier le code
docker run -p 8501:8501 wine_quality_app


## Utilisation
Ajustez les curseurs pour filtrer les vins selon leurs propriétés. L’application affichera les résultats filtrés et un histogramme de la répartition des qualités des vins. Pas besoin de diplôme en œnologie pour comprendre le graphique, mais cela pourrait rendre vos prochains apéros plus intéressants.

## Licence
Ce projet est sous licence MIT.
