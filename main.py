process = True
import fonctions
import key_manager
fonctions.charger()
while process:
    print("Que souhaitez-vous faire ? \n1. Générer une clé \n2. Afficher une clé existante \n3. Supprimer une clé \n4. Quitter")
    request = input()
    if request == '1':
        key = fonctions.generate_key()
        print(f"Voivi votre cle : {key}")
        continue
    elif request == '2':
        if key_manager.keys:
            fonctions.afficher_key(key_manager.keys)
        elif not key_manager.keys:
            print("Vous n'avez pas de clés générées.")
        continue
    elif request == '3':
        if key_manager.keys:
            print("Quel clé souhaitez vous supprimer ?")
            fonctions.afficher_keys(key_manager.keys)
            fonctions.suppr_key(int(input()))
            print("La clé a bien été supprimée")
        elif not key_manager.keys:
            print("Aucune clé n'est enregistré. ")
        continue
    elif request == '4':
        print("Merci d'avoir utilisé nos services")
        break
    else:
        print("Une erreur est survenue veuillez re éssayer")
        continue
