import numpy as np 
import matplotlib.pyplot as plt

debug = False
debug2 = False

def loadCSV (CSV:str):
    matrice = np.loadtxt(CSV, delimiter=";")
       
    if debug:
        print("Matrice :")
        print(matrice)
    return matrice

def calculPageRank(matrice,nbiteration):
    
    #Obtention du nombre de ligne
    nombre_colonnes = matrice.shape[1]

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
        
    dumpingFactorVector = np.full(nombre_colonnes, 0.85*(1/nombre_colonnes))
    pagerank = dumpingFactorVector.reshape(-1, 1)
    if debug == True :
        print("------- Vecteur Rempli de 0.85  --------")
        print(dumpingFactorVector)

    for i in range(nbiteration):
        #Multiplication de la matrice normalisée par le vecteur 
        pagerank = normalisee@pagerank

        #Ajout de 0.15/n à chaque case de la matrice
        pagerank += 0.15/nombre_colonnes

    if debug2 :
        print("-------Pagerank--------")
        print(pagerank)
            
    return pagerank

def showPageRank(pagerank):
    # Associer les indices et les valeurs dans une liste de tuples
    indices_et_pagerank = [(i + 1, pr) for i, pr in enumerate(pagerank)]

    # Séparer les indices et les valeurs depuis indices_et_pagerank
    indices, valeurs = zip(*indices_et_pagerank)

    # Convertir les valeurs en scalaires si ce sont des tableaux NumPy
    valeurs = [pr.item() if isinstance(pr, np.ndarray) else pr for pr in valeurs]

    # Création de l'histogramme
    plt.figure(figsize=(10, 6))
    plt.bar(indices, valeurs, color='blue', alpha=0.7)

    # Ajouter des titres et des légendes
    plt.title("Histogramme des PageRank (non triés)", fontsize=16)
    plt.xlabel("Indices des pages", fontsize=14)
    plt.ylabel("Valeurs de PageRank", fontsize=14)

    # Ajouter les valeurs exactes au-dessus des barres
    for i, pr in zip(indices, valeurs):
        plt.text(i, pr, f"{pr:.2f}", ha='center', va='bottom', fontsize=10)

    # Afficher la grille
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Afficher l'histogramme
    plt.show()

    if debug2:
        
        # Trier par valeur de PageRank (de manière décroissante)
        indices_et_pagerank_trie = sorted(indices_et_pagerank, key=lambda x: x[1], reverse=True)

        # Afficher les indices et les valeurs triées
        print("\n------- PageRank Trié (décroissant) --------")
        for index, pr in indices_et_pagerank_trie:
            print(f"Index: {index}, PageRank: {pr}")




CSV = "assets/test.csv"

showPageRank(calculPageRank(loadCSV(CSV),50))





    


