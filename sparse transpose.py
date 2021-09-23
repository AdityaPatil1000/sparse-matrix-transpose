#sparse transpose 
def create(s,row_num,col_num,non_zero_values):
    s[0][0]= row_num
    s[0][1] = col_num
    s[0][2] = non_zero_values        
    for k in range(1,non_zero_values+1):
        row = int(input("Enter row value: "))
        col = int(input("Enter col value: "))
        element = int(input("Enter the element: "))
        s[k][0]= row
        s[k][1] = col
        s[k][2] = element        
    
def display(s):
    print("Row\tcol\t Non_Zero_values")
    for i in range(0,(s[0][2]+1)): 
        for j in range(0,3): 
            print(s[i][j], "\t", end='') 
        print() 
def transpose(s1,row_num,col_num,s2,cols,non_zero_values):
    s2[0][0]= col_num
    s2[0][1] = row_num
    s2[0][2] = non_zero_values
    nxt=1
    for c in range(0,col_num+1):
    # for each column scan all the terms for a 'term' in that column 
        for Term in range(0,non_zero_values+1):
            if (s1[Term][0] == c):
	# Interchange Row and Column 
                s2[nxt][0] = s1[Term][1]
                s2[nxt][1] = s1[Term][0]
                s2[nxt][2] = s1[Term][2]
                nxt=nxt+1    
row_num = int(input("Input total number of rows for first matrix: "))
col_num = int(input("Input total number of columns for first matrix: "))
non_zero_values = int(input("Input total number of non-zero values: "))
cols =5
s = [[0 for col in range(cols)] for row in range(non_zero_values+1)]
trans_s = [[0 for col in range(cols)] for row in range(non_zero_values+1)]
create(s,row_num,col_num,non_zero_values)
print("Original sparse matrix is")
display(s)
transpose(s,row_num,col_num,trans_s,cols,non_zero_values)
print("Transposed sparse matrix is")
display(trans_s)
