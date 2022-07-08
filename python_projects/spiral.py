matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

m = 4
n = 4
def make_spiral_list(n,m,matrix):
    list_len = n*m
    spiral_list = []
    col = 0
    row = 0
    right = m
    start = False
    while len(spiral_list) != list_len:
        #move right
        for i in range(right):
            if start == False:
                start = True
            else:
                col += 1
            spiral_list.append(matrix[row][col])
        down = right - 1
        #move down
        for i in range(down):
            row += 1
            spiral_list.append(matrix[row][col])
        left = down
        #move left
        for i in range(left):
            col -= 1
            spiral_list.append(matrix[row][col])
        #move up
        up = left - 1
        for i in range(int(up)):
            row -= 1
            spiral_list.append(matrix[row][col])
        right = up
    print(spiral_list)


matrix = [[1,2,3,4,5],[7,8,9,10,11],[13,14,15,16,17]]
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35]]
matrix = [[1,2,3,4,5],[7,8,9,10,11],[13,14,15,16,17]]
m = 5
n = 3
def make_spiral_list(n,m,matrix):
    list_len = n*m
    spiral_list = []
    col = 0
    row = 0
    right = m
    down = n
    start = False
    while len(spiral_list) <= list_len:
        #move right
        for i in range(right):
            if start == False:
                start = True
            else:
                col += 1
            spiral_list.append(matrix[row][col])
        #move down
        if matrix[row+1][col] in spiral_list:
            break
        else:        
            down = down - 2
            for i in range(down):
                row += 1
                spiral_list.append(matrix[row][col])
        #move left
        left = right
        row += 1
        spiral_list.append(matrix[row][col])
        for i in range(left-1):
            col -= 1
            spiral_list.append(matrix[row][col])
        #move up
        up = down
        for i in range(int(up)):
            row -= 1
            if matrix[row][col] in spiral_list:
                break
            else:
                spiral_list.append(matrix[row][col])
        right = left - 2
    print(spiral_list, len(spiral_list))


make_spiral_list(n,m,matrix)