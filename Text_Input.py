import re               #ce package nous servira à traiter le message de l'utilisateur
import random           #package pour gérer les évènements aléatoires que nous utiliserons dans le code
import string           #Ce package servira à générer une liste contenant les lettres de l'alphabet français

class Text_Input:
    #Initialisation de la classe
    def __init__(self, dim):
        self.msg = ""               #Variable contiendra le message entré par l'utilisateur
        self.concat = dim           #La dimension de la clé de cryptage. Elle permettra entre autre de vérifier si la taille du message est compatible à la dimension de la clé
        self.nbre_caract_ajout = 0  #cette variable stockera le nombre de caractères ajouté au message si celui ci la taille de ce dernier n'est pas compatible
    
    
    #Methode pour permettre à l'utilisateur de saisir son message
    def saisir_message(self):
        print("\n")
        self.msg = input("Entrez le message à crypter (NB: Le message doit être sans caractères spéciaux ni chiffres. Dans le cas contraire ces caractères seront supprimés.):\t").lower()
        
        #On vérifie ici si le message entré contient uniquement des lettres de l'alphabet francais grâce à la classe sub()
        #du module re
        self.msg = re.sub(r'[^a-z]', '', self.msg)
        print("Votre message est:   ",self.msg)
        
        #on encode le message ici
        self.encode_message()
    
    
    #Methode pour encoder le message
    def encode_message(self):
        #permet de transformer le message de chaine de caractères à une liste ou chaque élément représente un caractère
        #du message
        self.msg = list("".join(self.msg.split()))
        
        #la methode est appelé pour vérifier si la taille du message est bien valide
        self.text_length()
        
        #Ici on remplace chaque caractère de la liste par leur position dans l'alphabet francais
        self.encode = [ord(letter) - ord('a') for letter in self.msg]
    
    
    """Methode pour vérifier la longueur du message. En effet pour crypter le message on aura besoin de matrices.
       On multipliera ces matrices avec la clé de cryptage. Les contraintes de multiplication de matrices obligent,
       Nous devons nous assurer que chaque matrice soit de dimension 1 de la forme 1*dimension_de_la_cle pour permettre
       la multiplication entre les matrices et la clé. la taille du message divisé par la dimension de la clé doit donc
       donner un reste nul.Dans le cas contraire on ajoutera des lettres au message pour respecter cela."""

    def text_length(self):
        # On recupère le nombre de caractères excédant la taille valide
        self.caract_rest = len(self.msg) % self.concat
        
        if (self.caract_rest != 0):
            #Si ce nombre est différent de 0 alors on détermine le nombre de caractères à ajouter
            self.nbre_caract_ajout = self.concat - self.caract_rest
        
            #on crée une liste alphabet contenant les lettres de l'alphabet francais
            alphabet = string.ascii_lowercase
            for i in range(self.nbre_caract_ajout):
                #Par itération on ajoute une lettre pris au hasard de notre liste que l'on ajoute au message
                #jusqu'à atteindre le nombre de caractère à ajouter
                self.msg.append(random.choices(alphabet, k=1)[0])
    
    
    #Methode pour recuperer le message à chiffrer pour l'utiliser dans la fonction de cryptage
    def texteAChiffrer(self):
        return self.encode
    
    
    #Methode pour recuperer le nombre de caractères ajoutés
    def caract_ajoute(self):
        return self.nbre_caract_ajout

if __name__ == "__main__":
    test = Text_Input(3)