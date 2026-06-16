import requests, csv
from bs4 import BeautifulSoup

#recuperer page : 
def recuperer_page(url):
    reponses = requests.get(url)
    if reponses.status_code == 200 : 
        return BeautifulSoup(reponses.text, 'html.parser')
    else:
        print(f"erreur {reponses.status_code} pour {url}")
        return None
    
def extraire_citation(soup) :
    liste_citation = []
    all_citation = soup.find_all("div", class_='quote')
    for citation in all_citation: 
        texte = citation.find('span', class_='text').text.strip()
        auteur = citation.find('small', class_= 'author').text.strip()
        dictionnaire = {'texte': texte, 'auteur' : auteur}
        liste_citation.append(dictionnaire)
    return liste_citation


def afficher_citation (citation) : 
    for element in citation:
        print(f"{element['texte']} - {element['auteur']}")

def sauvegarde_csv(citation, nom_fichier):
    if not citation : 
        return 
    with open(nom_fichier,"w", encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=citation[0].keys())
        writer.writeheader()
        writer.writerows(citation)

def main() :
    tous_les_citations = []
    for page in range(1, 6) : 
        print(f"scraping de la page {page}")
        url = f"https://quotes.toscrape.com/page/{page}/"
        soup = recuperer_page(url)

        if soup : 
            citation_pages = extraire_citation(soup)
            tous_les_citations.extend(citation_pages)

    afficher_citation(tous_les_citations)
    nom_fichier = "result.csv"
    sauvegarde_csv(tous_les_citations, nom_fichier)
    print("\n fichier sauvegarder avec succes !! \n")

if __name__ == "__main__" :
    main()
    

        



    





    




