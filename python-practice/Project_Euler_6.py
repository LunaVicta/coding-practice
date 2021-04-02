import math
squareOfSum = math.pow(((101*100)/2),2)
sumOfSquares = 0
for i in range (1,101):
    sumOfSquares += math.pow(i,2)
diff = squareOfSum - sumOfSquares
print("Square of sum: "+str(squareOfSum))
print("Sum of squares: "+str(sumOfSquares))
print(diff)
