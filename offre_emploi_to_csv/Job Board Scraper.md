# Excel Processor & File Organizer

Un outil d'automatisation en Python divisé en deux parties principales : la gestion de données financières et le tri de fichiers sur le système[cite: 3].

## Fonctionnalités
* **Partie Excel :** Génère un fichier de suivi client avec mise en forme stylisée (couleurs, polices), puis utilise Pandas pour filtrer et exporter dans un nouveau fichier (`clients_a_relancer.xlsx`) tous les clients ayant un solde négatif[cite: 3].
* **Partie Organisation :** Scanne le répertoire courant et trie automatiquement les fichiers (.xlsx, .csv, .py, etc.) dans des dossiers dédiés selon leur extension pour nettoyer l'espace de travail[cite: 3].

## Technologies utilisées
* Python 3
* OpenPyXL (Mise en page et création Excel)
* Pandas (Filtrage et traitement des données)
* OS & Shutil (Gestion et déplacement des fichiers système)