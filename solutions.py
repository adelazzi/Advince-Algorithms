import numpy as np

from geneticalgorithm import geneticalgorithm as ga

# Vecteur x donné

x = np.array ( [ 4 , 5 , 3 , 6 , 7 , 5 , 5 , 5 , 5 , 7 , 4 , 1 , 8 ] )

# Fonction pour calculer la somme de A et B

def sum_A_B ( chromosome ) :
    A_sum = sum( x [ i ] for i in range ( len ( x ) ) if chromosome [ i ] == 1 )
    B_sum = sum( x [ i ] for i in range ( len ( x ) ) if chromosome [ i ] == 0 )
    return A_sum , B_sum

# Fonction de coût à minimiser (différence absolue entre les sommes de A et B)

def fitness ( chromosome ) :
    A_sum , B_sum = sum_A_B( chromosome )
    return abs ( A_sum - B_sum )

# Paramètres de l'algorithme génétique

varbound = np.array( [ [ 0, 1 ] ] * len ( x ) )  # chaque élément peut être soit 0 (B) soit 1 (A)

# Configuration de l'algorithme génétique

model = ga (
    function = fitness ,
    dimension = len ( x ) ,  # Nombre d'éléments dans x
    variable_type = 'int' ,  # Chaque variable est entière (0 ou 1)
    variable_boundaries = varbound  # Chaque variable est entre 0 et 1
)

# Exécution de l'algorithme génétique

model.run( )

# Résultat

best_solution = model.output_dict [ 'variable' ]

A = [ x [ i ] for i in range ( len ( x ) ) if best_solution[i] == 1 ]

B = [ x [ i ] for i in range ( len ( x ) ) if best_solution[i] == 0 ]

# Affichage des résultats

print( " Solution optimale trouvée : " )

print( f" A = {A} " )

print( f" B = {B} " )

print( f" Somme de A = { sum ( A ) } " )

print( f" Somme de B = { sum ( B ) } " )
