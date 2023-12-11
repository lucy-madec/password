# Importation du module 'hashlib' pour le hachage du mot de passe avec l'algorithme SHA-256.
import hashlib

Nb_essais = 4 # Nombre maxiaml de tentatives du mot de passe.

# Fonction permettant de définir le mot de passe avec le respect des exigences de sécurité.
def definir_mdp(mdp):
    return (
        # Défini que le mot de passe est égal ou supérieur à huit caractères.
        len(mdp) >= 8 and
        # Défini que le mot de passe contient au moins une lettre majuscule.
        any(c.isupper() for c in mdp) and
        # Défini que le mot de passe contient au moins une lettre minuscule.
        any(c.islower() for c in mdp) and
        # Défini que le mot de passe contient au moins un chiffre.
        any(c.isdigit() for c in mdp) and
        # Défini que le mot de passe contient au moins un caractère spécial.
        any(c in '!@#$%^&*' for c in mdp)
    )
# Fonction permettant de demander à l'utilisateur d'entrer un mot de passe.
def choix_mdp():
    mdp = input("Veuillez choisir un mot de passe contenant au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial (!@#$%^&*) :")
    return mdp
# Fonction permettant de vérifier si le mot de passe choisi par l'utilisateur est valide.
def valide_mdp():
    essais = 0 # Compteur d'essais à 0

    while essais < Nb_essais:
        mdp = choix_mdp()

        # Si le mot de passe respecte les conditions alors il est affiché comme étant validé.
        if definir_mdp(mdp):
            print("Mot de passe enregistré avec succès.")

            hashed_mdp = hashlib.sha256(mdp.encode()).hexdigest()
            print ("Mot de passe haché (SHA-256) :", hashed_mdp)
            break
        else:
            essais += 1
            print(f"Votre mot de passe ne rentre pas dans les consignes de sécurité. Il vous reste {Nb_essais - essais} tentatives.")
    if essais == Nb_essais:
        print("Nombre maximal de tentatives atteint. Veuillez relancer le programme.")

valide_mdp()