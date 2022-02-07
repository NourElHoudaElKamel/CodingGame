def closest(list, K):
    return list[min(range(len(list)), key=lambda i: abs(list[i] - K))]


# Driver code
list = [7,-10, 13, 8, 4, -7.2,-12,-3.7,3.5,-9.6, 6.5,-1.7, -6.2,7, 1.7]
K = 0
var = closest(list, K)
if(list.__contains__(abs(var))):
    var = abs(var)
print(var)