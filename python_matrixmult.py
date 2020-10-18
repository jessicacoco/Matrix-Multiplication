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

def read_input_from_text(matrix_size):
    txtfile = input("Text file for matrix: ")
    my_matrix = [] # makes my matrix an empty list
    val_list = [] #makes the list of values  an empty list
    for line in open(txtfile):
        val_list.append(line.strip())
    count = 0
    for i in range(matrix_size):
        matrix_row = []
        for j in range(matrix_size):
            new_val = val_list[count]
            matrix_row.append(new_val)
            count += 1
        my_matrix.append(matrix_row)
    return my_matrix

def print_matrix(matrix_size, matrixname):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrixname[i][j], end = " ")
        print('\n')


def matrix_multiply(matrix_size, matrix_a, matrix_b):
    results_matrix = [] # make an empty list for the results matrix
    ans = 0 # make an answer variable to keep track of multiplied matrix values
    for i in range(matrix_size):
        new_matrixrow = [] # make an empty list for each row
        for j in range(matrix_size):
            for h in range(matrix_size):
                # calculate product and update the answer
                product = matrix_a[i][h] * matrix_b[h][j]
                ans += product
            new_matrixrow.append(ans)
            ans = 0 # reset answer so it can be used again
        results_matrix.append(new_matrixrow)
    return results_matrix            
    
    
def main():
    matrix_size = int(input("Enter the size dimension of the matricies you want to use: "))
    read_choice = str(input("Enter A to have the matrix read from a text file or B to input manually: "))
    if read_choice != "A" and read_choice != "B":
        print("Error! Please provide the following input!")
        read_choice = str(input("Enter A to have the matrix read from a text file or B to input manually: "))
    if read_choice == "A":
        matrix_a = read_input_from_text(matrix_size)
        matrix_b = read_input_from_text(matrix_size)
    elif read_choice == "B":
        matrix_a = read_matrix_input(matrix_size)
        matrix_b = read_matrix_input(matrix_size)
    print("Matrix A:")
    print_matrix(matrix_size, matrix_a)
    print("Matrix B:")
    print_matrix(matrix_size, matrix_b)
    print("The product of the two:")
    product = matrix_multiply(matrix_size, matrix_a, matrix_b)
    print_matrix(matrix_size, product)

if __name__=="__main__": 
    main()