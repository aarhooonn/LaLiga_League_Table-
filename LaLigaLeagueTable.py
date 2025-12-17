import requests


def obtenir_classificacio_laliga(api_key):
    url = "https://api.football-data.org/v4/competitions/PL/standings"


    headers = {
        "X-Auth-Token": api_key 
    }


    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status()
        dades = resposta.json()


        classificacio = dades['standings'][0]['table']


        print("Classificació actual de LaLiga:")
        for equip in classificacio:
            posicio = equip['position']
            nom = equip['team']['name']
            punts = equip['points']
            print(f"{posicio}. {nom} - {punts} punts")


    except requests.exceptions.RequestException as e:
        print(f"Error en fer la consulta: {e}")
    except KeyError:
        print("No s'han pogut obtenir les dades. Comprova si la clau API és correcta o si tens accés.")


# Introdueix la teva clau API aquí
API_KEY = "7c6832e27cb5420ba577d9fae07a0aca"


if __name__ == "__main__":
    obtenir_classificacio_laliga(API_KEY)