import numpy as np

def generate_random_square_matrix(min_size, max_size):
    # Genera un número aleatorio para determinar el tamaño de la matriz
    size = np.random.randint(min_size, max_size + 1)
    
    # Crea una matriz cuadrada de enteros aleatorios entre 0 y 9
    random_matrix = np.random.randint(10, size=(size, size))
    
    return random_matrix

def main():
    min_size = 2
    max_size = 5
    
    # Genera una matriz aleatoria de enteros
    matrix = generate_random_square_matrix(min_size, max_size)
    
    print("Matriz generada:")
    print(matrix)

    # Calcula los valores propios y vectores propios (no aplicable a matrices de enteros)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    print("\nValores propios:")
    print(eigenvalues)
    print("\nVectores propios:")
    print(eigenvectors)

if __name__ == "__main__":
    main()