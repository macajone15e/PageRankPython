import numpy as np 

debug = False
debug2 = True


def chargeCSV (CSV:str):
    matrice = np.loadtxt(CSV, delimiter=";")  # Utilisez le délimiteur approprié (par défaut ",")
    if debug:
        print("Matrice :")
        print(matrice)
    return matrice

def calculPageRank(matrice,nbiteration):
    #Obtention du nombre de ligne
    nombre_lignes, nombre_colonnes = matrice.shape 


    #Transposition de la matrice 
    transposee = matrice.T

    if debug == True :
        print("------- Matrice Transposée --------")
        print(transposee)

    #Normalisation de matrice
    sommeColonnes = np.sum(transposee, axis=0)
    sommeColonnes[sommeColonnes == 0] = 1

    normalisee = transposee / sommeColonnes

    if debug == True :
        print("------- Matrice normalisée   --------")
        print(normalisee)


    #Création du vecteur 0.85 en fonction de la taille de la matrice
        
    dumpingFactorVector = np.full(nombre_colonnes, 0.85)
    pagerank = dumpingFactorVector.reshape(-1, 1)
    if debug == True :
        print("------- Vecteur Rempli de 0.85  --------")
        print(dumpingFactorVector)

    for i in range(nbiteration):
        #Multiplication de la matrice normalisée par le vecteur 
        pagerank = normalisee@pagerank

        #Ajout de 0.15/n à chaque case de la matrice
        pagerank += 0.15/nombre_lignes

    if debug2 :
        print("-------Pagerank--------")
        print(pagerank)
            
    return pagerank

def sortPageRank(pagerank):
    # Associer les indices et les valeurs dans une liste de tuples
    indices_et_pagerank = [(i+1, pr) for i, pr in enumerate(pagerank)]

    # Trier par valeur de PageRank (de manière décroissante)
    indices_et_pagerank_trie = sorted(indices_et_pagerank, key=lambda x: x[1], reverse=True)

    # Afficher les indices et les valeurs triées
    print("\n------- PageRank Trié (décroissant) --------")
    for index, pr in indices_et_pagerank_trie:
        print(f"Index: {index}, PageRank: {pr}")


matrice = chargeCSV("test.csv")

pagerank = calculPageRank(matrice,50)

sortPageRank(pagerank)





    
    


