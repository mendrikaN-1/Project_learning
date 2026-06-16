# Weather Data Extractor

Un script Python simple qui utilise l'API OpenWeatherMap pour récupérer les données météo en temps réel de plusieurs villes de Madagascar[cite: 2].

## Fonctionnalités
* Récupère la météo pour Antananarivo, Toamasina et Mahajanga[cite: 2].
* Extrait : température, taux d'humidité et description du ciel[cite: 2].
* Masquage de la clé API via un fichier `.env` pour la sécurité[cite: 2].
* Exportation automatique des données récupérées dans un fichier `liste_result.csv`[cite: 2].

## Technologies utilisées
* Python 3
* Requests (Appels API)
* Python-dotenv (Gestion sécurisée des variables d'environnement)
* CSV