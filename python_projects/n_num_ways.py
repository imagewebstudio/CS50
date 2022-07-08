matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

m = 4
n = 4

def num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
         return num_ways(n-1)+num_ways(n-2)

arry = [ 3,3,6,3]
days  = 0

while len(arry) > 0 :
    while 0 in arry:
        arry.remove(0)
    if len(arry) > 0:
        min_p = min(arry)
        for j in range(len(arry)):
            arry[j] = arry[j] - min_p
        days += 1
print(num_ways(n), arry, days)
