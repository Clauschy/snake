aliens = 2
password = "ALIENS"
print("Vite! Des aliens envahissent la planète!")
print("Tu dois activer la plateforme de défense mondiale!")
print("J'espère que tu connais le mot de passe...")
print()
print(30*"*")
print("BIENVENUE DANS LA DEFENSE MONDIALE")
print(30*"*")
print()
deviner = input("Entre le mot de passe: ").upper()
while deviner != password:
    print()
    print("MOT DE PASSE INCORRECT")
    print()
    aliens = aliens **2
    print("Il y a", aliens, "aliens sur la Terre. Réessaie!")
    print()
    print("Indice mot de passe: les créatures qui nous attaquent.")
    print()
    deviner = input("Vite! Entre le mot de passe! ").upper()
    if aliens > 7400000000:
        print("Noooooon! Les aliens sont plus nombreux que nous! Tu as perdu!")
        break
    else:
        print("Hourra! Nous avons gagné, le monde est sauvé!")
