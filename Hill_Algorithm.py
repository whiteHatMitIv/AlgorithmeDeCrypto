import Crypt as cp
import Key_Input as ki
import Text_Input as ti
import numpy as np

if  __name__ == "__main__":
    #En-tête du programme
    
    print("\n")
    print("   --------------------------------------------------------------------------------------------------------------")
    print("  |                                     IMPLEMENTATION DE L'ALGORITHME DE HILL                                   |")
    print("   --------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    """ Processus pour l'entrée de la clé de cryptage """
    
    # Nous le mettons ici car dans la suite on devra savoir si l'utilsateur veut crypter un autre message avec la même
    # clé de départ. L'inclure dans la boucle d'en dessous reviendrait à demander à chaque fois à l'utilisateur d'entrer
    # une clé même s'il ne souhaite pas la changer
    
    demandeCle = ki.Key_Input()                 #on instancie un objet demandeCle de la classe Key_Input
    demandeCle.saisir_cle()                     #on appelle la méthode saisir_cle() de l'objet
    key = demandeCle.cle()                      #on stocke la clé
    dimensionkey = demandeCle.dimension()       #on stocke la dimension de la clé
    
    #la boucle while permettra d'executer en continu le programme pour par exemple crypter un autre message
    while True:
        """ Les variables ok1 et ok2 nous servirons plutard dans le programme pour savoir respectivement si
            l'utilisateur souhaite crypter un autre message et si oui s'il compte utiliser la clé. Etant donné qu'on
            verifiera sa préference soit par 0 soit par 1 leur valeur de départ se doit d'être différent de ces chiffres.
        """
        ok1, ok2 = 2, 2
        
        """Processus pour l'entrée du message à crypter de cryptage"""
        
        #Initialisation de la classe Text_Input() du module de même nom. Prenant en paramètre la dimension de la clé
        #Son utilisation est expliqué dans la classe en question
        demandeMessage = ti.Text_Input(dimensionkey)    #on instancie un objet demandeMessage de la classe Text_Input avec en paramètre la dimension de la clé
        demandeMessage.saisir_message()                 #on appelle la méthode saisir_message() de l'objet         
        msg = demandeMessage.texteAChiffrer()           #on stocke la valeur retourné par la methode texteAChiffrer() dans msg
        nbre_caract_ajoute = demandeMessage.caract_ajoute()         #on stocke le nombre de caractères ajoutés au message
        
        # Processus de cryptage
        
        #On initialise la classe Crypt du module de même nom
        cryptage = cp.Crypt(msg, key, dimensionkey, nbre_caract_ajoute)   
        
        #On vérifie si la clé fournie vaut 3 avec la méthode array_equal() de numpy dans ce cas il s'agira d'utiliser
        #la methode implémentant le chiffrement de césar dans le cas contraire on applique l'algorithme de hill
        #avec la methode cryptage() du module  Crypt
        if np.array_equal(key, np.matrix([[3]])):
            cryptage.cryptage_cesar()
        else:
            cryptage.cryptage()
        
        
        cryptedMessage = cryptage.message_crypte()   #On stocke le message crypté retourné par la methode message_crypte()
        
        print("\n")
        print("Le message crypté est:   ",cryptedMessage)
        print("\n")
        
        while ok1 != 0 and ok1 != 1:
            # Demande à l'utilisateur s'il souhaite crypter un autre message
            try:
                ok1 = int(input("Voulez vous crypter un autre message ? (appuyez sur 0 pour non et 1 pour oui)\t"))
            except:
                print("Veuillez appuyer sur 0 pour arretez le programme ou sur 1 pour crypter un autre message")
            finally:
                # Si oui veut il crypter avec la même clé
                if (ok1 == 1):
                    while ok2 != 0 and ok2 != 1:
                        try:
                            ok2 = int(input("Voulez vous crypter avec la même clé ? (appuyez sur 0 pour non et 1 pour oui)\t"))
                        except:
                            print("Veuillez appuyer sur 0 pour crypter avec une autre clé et 1 pour crypter avec la même clé")
        
        # On vérifie ici si l'utilisateur ne souhaite pas crypter un autre message. Si oui alors on quitte la boucle while avec break
        if ok1 == 0:
            print("\n")
            print("Merci d'avoir utiliser le programme :)")
            break
        
        # On vérifie ici si l'utilisateur souhaite crypter avec une autre clé. Si oui il lui est demandé de rentrer une 
        # autre clé.
        if ok2 == 0:
            print("\n")
            demandeCle = ki.Key_Input()
            demandeCle.saisir_cle()
            key = demandeCle.cle()
            dimensionkey = demandeCle.dimension()