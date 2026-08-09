import secrets
import key_manager
import json

def charger():
    """Charge les clés existantes depuis keys.json au démarrage."""
    try:
        with open("keys.json", "r", encoding="utf-8") as fichier:
            contenu = fichier.read().strip()
            key_manager.keys = json.loads(contenu) if contenu else []
    except FileNotFoundError:
        key_manager.keys = []

def sauvegarder():
    with open("keys.json", "w", encoding="utf-8") as fichier:
        json.dump(key_manager.keys, fichier, indent=4)


def generate_key():
    key = secrets.token_hex(16)
    key_manager.keys.append(key)
    sauvegarder()
    return key

def suppr_key(choix):
    key_manager.keys.pop(choix)
    sauvegarder()

def afficher_keys(list):
    for c, key in enumerate(list):
        print(f"{c} --> {key}")
        

def afficher_key(liste):
    for i in liste:
        print(i)
