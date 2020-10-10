#read in two NxN matricies
def read_matrix_input(matrix_size):
    matrix_a = [] # empty list to put the first matrix in
    for value in range(matrix_size):
        matrix_row = []
        for val_2 in range(matrix_size):
            new_val = int(input("Please enter matrix values for your matrix one by one: "))
            matrix_row.append(new_val)
        matrix_a.append(matrix_row)
    return matrix_a


def print_matrix(matrix_size, matrixname):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrixname[i][j], end = " ")
        print('\n')

            
    
    
def main():
    matrix_size = int(input("Enter the size dimension of the matricies you want to use: "))
    matrix_a = read_matrix_input(matrix_size)
    matrix_b = read_matrix_input(matrix_size)
    print(print_matrix(matrix_size, matrix_a))
    print(print_matrix(matrix_size, matrix_b))
    

if __name__=="__main__": 
    main()