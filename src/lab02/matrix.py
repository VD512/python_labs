def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return mat
    len_line=len(mat[0])
    len_column=len(mat)
    for line in mat:
        if len(line)!=len_line:
            return ValueError
    new_mat=[[0 for x in range(len_column)] for y in range(len_line)]
    for x in range(len_column):
        for y in range(len_line):
            new_mat[y][x]=mat[x][y]
    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    same_len=len(mat[0])
    sum_mat=[]
    for line in mat:
        if len(line)!=same_len:
            return ValueError
        sum_mat.append(sum(line))
    return sum_mat
    
def col_sums(mat: list[list[float | int]]) -> list[float]:
    same_len=len(mat[0])
    sum_mat=[0]*same_len
    for line in mat:
        if len(line)!=same_len:
            return ValueError
    for x in range(same_len):
        for y in range(len(mat)):
            sum_mat[x]+=mat[y][x]
    return sum_mat
        