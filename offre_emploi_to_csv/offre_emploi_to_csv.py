import requests, csv, time 
from bs4 import BeautifulSoup

def recuperer_page(url) : 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0'
}

    reponses = requests.get(url, headers=headers)
    if reponses.status_code == 200 : 
        return BeautifulSoup(reponses.text, 'html.parser')
    else :
        return None
    
def extraction_donnees(soup) : 
    liste_offre = []
    all_offre = soup.find_all("div", class_="card")
    for offre in all_offre : 
        titre = offre.find("h2", class_="title is-5").get_text(strip = True)
        entreprise = offre.find("h3", class_="subtitle is-6 company").get_text(strip = True)
        localisation = offre.find("p", class_="location").get_text(strip = True)
        #stockage : 
        if "python" in titre.lower() : 
            conteneur = {'titre' : titre, 'entreprise' : entreprise, 'localisation': localisation}
            liste_offre.append(conteneur)
            
        
    return liste_offre


        
    
def affichage_offre(liste_offre) :
    for element in liste_offre : 
        print(f"{element['titre']} , {element['entreprise']}, {element['localisation']} ")
    
def sav(liste_offre, nom_fichier):
    if not liste_offre:
        return
    with open(nom_fichier, "w", newline="", encoding="utf-8") as f :
        writer = csv.DictWriter(f, fieldnames=liste_offre[0].keys())
        writer.writeheader()
        writer.writerows(liste_offre)

def main() :
    tous_les_offres = []
    lien= "https://realpython.github.io/fake-jobs/"
    soup = recuperer_page(lien)
    if soup : 
        donnees = extraction_donnees(soup)
        if donnees : 
                tous_les_offres.extend(donnees)
                print("extraction des donnees fait avec succes!!!")
        else : 
            print("liste vide , pas d'offre concernant python ")
        
        

    affichage_offre(tous_les_offres)
    nom_fichier = "sauvegarde.csv"
    sav(tous_les_offres, nom_fichier)
    print("fichier sauvegarder avec succes !!!")

if __name__ == "__main__":
    main()










   






