import numpy as np

class Key_Input:
    def __init__(self):
        self.dim = 0                        #la variable qui nous permettra de recuperer la dimension de la clé
    
    def isModulo(self):
        #On recupère le déterminant de la clé
        self.determinant = int(np.linalg.det(self.key))
        
        if (self.determinant % 2 != 0) and (self.determinant % 13 != 0):
            #Si le determinant est impair et n'est pas multiple de 13 alors la clé est modulo 26 et on retourne true
            return True
        else:
            #dans le cas contraire on retourne false
            return False
    
    def saisir_cle(self):
        self.ok = True                  #la variable ok ici nous permettre d'exécuter en continue la boucle while tant que la dimension n'est pas valide
        
        self.listes = []                #la liste englobant l'ensemble des listes. une liste représentera une ligne de la matrice de la clé. 
                                        #En gros listes représentent la clé sous forme d'une liste
        
        while self.ok == True:
            #le try...except...else nous permet de s'assurer que la dimension entré est valide
            try:
                self.dim = int(input("Entrez la dimension de la clé\t"))
                
                #La dimension se devant d'être positif on ajoute ces lignes pour créer une erreur indiquant que la dimension
                #est négative
                notNul = 1/self.dim
                if self.dim < 0:
                    raise ValueError("Le nombre doit être positif")
            except:
                print("La dimension de la clé doit être un entier non nul veuillez réessayer.\n")
            else:
                self.ok = False
        
        print("\n")
        
        #Code pour entrer la clé en fonction de la dimension entrée
        for i in range(self.dim):
            #On déclare une liste vide qui nous permettra de prendre une ligne de la matrice de la clé
            #En effet pour créer la matrice clé on a besoin de dimension_de_la_cle lignes de chiffres
            #ces lignes nous les representeront sous forme de liste
            self.liste = []
            
            for j in range(self.dim):
                self.ok = True
                
                while self.ok == True:
                    try:
                        self.value = int(input("Entrer la valeur de la ligne {} colonne {}\t".format(i+1,j+1)))
                        if self.value < 0:
                            raise ValueError("Le nombre doit être positif")
                    except:
                        print("La valeur doit être un entier positif pour garantir la qualité du chiffrement")
                    else:
                        self.ok = False
                
                #On ajoute la valeur entré à la liste representant une ligne de la matrice cle
                #cette contiendra dimension_de_la_cle valeur
                self.liste.append(self.value)
            
            #Une fois qu'une ligne est remplit on l'ajoute à la liste correspondant à notre future matrice cle
            self.listes.append(self.liste)
        
        #Une fois que toutes les lignes de la matrice cle ont été entrés on crée la matrice cle avec la liste 
        #qui correspondait à notre clé
        self.key = np.matrix(self.listes)
        
        #On vérifie si la clé fournie est valide pour le cryptage
        self.verificator_key()
    
    
    def verificator_key(self):
        #On appelle la methode affiche_cle() pour afficher la clé saisi par l'utilisateur
        self.affiche_cle()
        
        #On détermine ici le determinant de la clé fournie
        self.determinant = np.linalg.det(self.key)
        
        #Si le determinant est nul alors la clé n'est pas valide et l'utilisateur est invité à entrer une autre clé
        if self.determinant == 0:
            print("La clé n'est pas valide (son determinant est nul). Veuillez réessayer.")
            print("\n")
            self.saisir_cle()
            
        else:
            
            #Si le determinant n'est pas nul alors on verifie si la cle est modulo 26 dans le cas contraire la clé
            #n'est pas valide et l'utilisateur doit entrer une autre clé
            isPremier = self.isModulo()
            if isPremier == False:
                print("La clé n'est pas modulo 26 veuillez réessayer")
                print("\n")
                self.saisir_cle()
    
    #Methode pour afficher la clé à l'utilisateur
    def affiche_cle(self):
        print("\n")
        print("Votre clé est:")
        print(self.key)
        
        ok = 2      
        while ok != 0 and ok != 1:
            try:
                ok = int(input("Est-ce correct? (0 pour non et 1 pour oui)\t"))
                print("\n")
            except:
                print("Veuillez entrer 0 pour modifier la clé et 1 pour valider la clé")
                ok = 2
        
        #Si l'utilisateur souhaite modifié la clé fourni alors on rappelle la methode saisir_cle()
        if ok == 0:
            self.saisir_cle()
    
    #Methode pour recupérer la clé afin de l'utiliser dans la fonction de cryptage
    def cle(self):
        return self.key
    
    #Methode pour recupérer la dimension de la clé
    def dimension(self):
        return self.dim

if __name__ == "__main__":
    test = Key_Input()