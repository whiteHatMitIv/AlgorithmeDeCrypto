import numpy as np

#création de la classe Crypt
class Crypt:
    #Initialisation de la classe 
    def __init__(self,texte, key, dimension, ajout):
        self.msg = texte                             #message à chiffrer
        self.key = key                               #clé utilisée pour le cryptage
        self.dim = dimension                         #dimension de la clé
        self.caract_ajouter = ajout                  #Nombre de caractères ajoutés au message de l'utilisateur
        
        #incrementateur qui nous servira à transformer la message numérique en une liste de matrices dimension_de_la_cle*1
        #vu que la taille du message est multiple de la dimension de la clé et que l'on doit découper le message en matrices
        #dimension_de_la_cle*1 l'on obtient donc la valeur ci dessous
        self.incrementor = int(len(self.msg)/self.dim)
        
        self.msg_crypt = []                         #le message crypté
        self.texte_matrix = []                      #liste qui contiendra le message numérique concatenés en sous matrices dimension_de_la_cle*1
        self.crypt = []                             #liste qui contiendra le message cryptés concatenés en sous matrices dimension_de_la_cle*1
        self.msg_crypt_list = []                    #liste qui assemblera les sous matrices en une seule liste
    
    
    #Methode qui transformera le message numérique fournie sous forme de liste en une liste contenant ce message en forme de sous matrices
    def  transform_to_matrix(self):
        j = 0       
        k = self.dim
        for i in range (self.incrementor):
            #on divise le message en dimension_de_la_cle caractères avec self.msg[j:k] à la première itération on aura donc self.msg[0:self.dim]
            # puis on transforme cela en matrice dimension_de_la_cle*1
            self.texte_matrix.append(np.matrix(self.msg[j:k]).reshape(self.dim, 1))    
            j += self.dim       #On modifie l'indice de départ de la prochaine itération en la remplacant par l'indice de fin de l'itération précédente
            k += self.dim       #On modifie l'indice de fin de la prochaine itération en ajoutant la dimension de la clé à l'indice de fin précédent
    
    
    #Methode pour le cryptage du message
    def cryptage(self):
        #On appelle la méthode servant en transformer le message numérique en liste de sous matrices de dimension dimension_de_la_cle*1
        self.transform_to_matrix()
        
        #A chaque sous matrice de la liste on la multiplie par la clé puis on fait le modulo 26 grâce à la méthode np.mod()
        #Le résultat est ajouté dans la liste self.crypt grâce à la méthode append()
        for i in range(self.incrementor):
            self.crypt.append(np.mod(self.key * self.texte_matrix[i],26))
        
        #On appelle la méthode assemble() pour fusionner les sous matrices en une seule liste
        self.assemble()
    
    
    #Lorsque le clé vaut 3 le cryptage correspond au cryptage de césar dans ce cas chaque sous matrice est additionné à la clé puis on effectue
    #le modulo 26 de ce résultat
    def cryptage_cesar(self):
        self.transform_to_matrix()
        
        for i in range(self.incrementor):
            self.crypt.append(np.mod(self.texte_matrix[i] + self.key,26))
        
        self.assemble()
    
    #Methode pour fusionner les sous matrices en une seule liste
    def assemble(self):
        #En parcourant la liste self.crypt on selectionne une matrice matrix; en crée une variable elements qui contiendra la matrice sous forme de liste grâce à la 
        #méthode tolist(). puis on ajoute cet element dans la liste self.msg_crypt_list avec la méthode  extend()
        for matrix in self.crypt:
            elements = matrix.tolist()
            self.msg_crypt_list.extend(elements)
        
        #ensuite on crée une liste self.msg_crypt_numerique grâce à la ligne [element for sous_liste in self.msg_crypt_list for element in sous_liste] expliqué comme suit
        #on selectionne une sous liste dans la liste self.msg_crypt_list puis on selectionne un element contenu dans cette sous liste que l'on ajoute
        #à notre liste self.msg_crypt_numerique. les boucles for servant à parcourir integralement les sous listes et la liste self.msg_crypt_list
        #L'on se retrouvera donc avec une liste constitué des positions du message crypté
        self.msg_crypt_numerique = [element for sous_liste in self.msg_crypt_list for element in sous_liste]
    
    
    #méthode pour retourner le message crypté
    def message_crypte(self):
        #On ajoute les caractères à la liste self.msg_crypt tel que suit:
        #pour chaque position contenue dans self.msg_crypt_numerique on applique chr(97+position) qui retournera la lettre correspondante dans l'alphabet francais
        #97+position correspondant au code ASCII de la lettre. ensuite la lettre est ajouté dans la liste self.msg_crypt
        self.msg_crypt = [chr(97 + position) for position in self.msg_crypt_numerique]
        
        #On définit l'indice de fin du message de départ de l'utilisateur en faisant la soustraction de la longueur de la liste  self.msg_crypt avec
        #le nombre de caractère ajouté self.caract_ajouter
        soustract = len(self.msg_crypt) - self.caract_ajouter
        
        #on fusionne donc tout les caractères de la liste self.msg_crypt jusqu'à l'indice de fin soustract pour en faire une chaine de caractères
        #NB : DU FAIT QUE L'ON AIT AJOUTE DES CARACTERES DE MANIERE ALEATOIRE DANS LE MODULE TEXT_INPUT.PY POUR LES MESSAGES DE TAILLE NON VALIDE, IL EST 
        #PROBABLE QUE POUR UN MEME MESSAGE DE CE TYPE LE CRYPTOGRAMME FOURNIE PAR L'ALGORITHME SOIT DIFFERENT AU NIVEAU DES DERNIERS CARACTERES
        self.msg_crypt = "".join(self.msg_crypt[:soustract])
        
        #on retourne le message crypté
        return self.msg_crypt


#On teste ici notre classe si cette derniere est executé en tant que programme principal
if __name__ == '__main__':
    listes = [[5,8],[17,3]]
    key = np.matrix(listes)
    test = Crypt([9,4,18,20,8,18,7,4,20,17,4,20,18,4],key,2)