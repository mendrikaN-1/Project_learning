import requests, csv
from dotenv import load_dotenv
import os

#nom des villes : 
villes = ['Antananarivo', 'Toamasina', 'Mahajanga']
liste_result = []
#recuperation du cle de l'api
load_dotenv()
cle_api = os.getenv('cle_api')
print(cle_api)

for ville in villes : 
    reponses = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={cle_api}&units=metric&lang=fr")
    print(reponses.status_code)
    print("\n")
    donnees = reponses.json()

    #placement des resultat dans un dict
    result = {"nom de la ville " : f"{donnees['name']}",
              "temperature" : f"{donnees['main']['temp']}",
              "humidite" : f"{donnees['main']['humidity']}",
              "description": f"{donnees['weather'][0]['description']}"}
    
    #affichage des resultats 
    for cle, valeur in result.items() :
        
        print(f"{cle} : {valeur}")
        print("\n")

    #ajout des resulats dans une liste 
    liste_result.append(result)

    #sauvegarde en csv : 
with open("liste_result.csv", "w", encoding="utf-8", newline="") as f : 
    writer = csv.DictWriter(f, fieldnames=liste_result[0].keys())
    writer.writeheader()
    writer.writerows(liste_result)

if os.path.exists("liste_result.csv"):
    print("sauvegarde reussie??")

    

    




