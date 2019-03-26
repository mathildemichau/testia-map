Test Testia
=================

Carte interactive

Reconnaissance de la position et calcul de la distance entre l'utilisateur et la position choisie en cliquant
Persistance des données dans une base de données

Pour installer le projet en local:

`git clone https://github.com/mathildemichau/testia-map.git`

Pour le back-end: 
````
cd testia-map;
virtualenv -p python3 venv;
source venv/bin/acivate;
pip install -r server_map/requirements.txt;
python server_map/manage.py runserver;
````

Pour le front-end:
````
cd client_map/;
npm install;
npm run serve;
````
