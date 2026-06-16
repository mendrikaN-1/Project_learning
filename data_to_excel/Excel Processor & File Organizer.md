# Job Board Scraper

Un script de web scraping en Python conçu pour cibler et extraire des offres d'emploi spécifiques depuis un site de simulation d'annonces[cite: 4].

## Fonctionnalités
* Intègre un `User-Agent` dans les headers pour simuler une navigation humaine et éviter les blocages[cite: 4].
* Analyse la structure HTML pour extraire le titre du poste, l'entreprise et la localisation[cite: 4].
* Filtre intelligemment les résultats pour ne conserver que les offres contenant le mot-clé **"Python"**[cite: 4].
* Sauvegarde les offres correspondantes dans un fichier `sauvegarde.csv`[cite: 4].

## Technologies utilisées
* Python 3
* Requests
* BeautifulSoup4
* CSV