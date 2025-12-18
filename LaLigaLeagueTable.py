import requests

def obtenir_classificacio_laliga(api_key):
   
    url = "https://api.football-data.org/v4/competitions/PD/standings"
    headers = {
        "X-Auth-Token": api_key 
    }

    try:
        
        resposta = requests.get(url, headers=headers)
        
        
        resposta.raise_for_status()
        
        dades = resposta.json()

        
       
        classificacio = dades['standings'][0]['table']

        print(f"{'Pos':<4} | {'Equip':<25} | {'Punts':<5}")
        print("-" * 40)

        for equip in classificacio:
            posicio = equip['position']
            nom = equip['team']['name']
            punts = equip['points']
           
            print(f"{posicio:<4} | {nom:<25} | {punts:<5}")

    except requests.exceptions.RequestException as e:
        print(f"Error en fer la consulta: {e}")
    except KeyError as e:
        print(f"Error en l'estructura de les dades: {e}")
        print("Comprova si la teva clau API té accés a la competició 'PD' (Primera División).")

# Substitueix amb la teva clau API vàlida
API_KEY = #"la_teva_clau_api_aqui"

if __name__ == "__main__":
    obtenir_classificacio_laliga(API_KEY)
