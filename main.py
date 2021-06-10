from math import sqrt

fibonacci = [0,1]
nbOr = (1 +sqrt(5))/2
for x in range (10):
    fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci [len(fibonacci)-2])
    print (fibonacci[len(fibonacci)-1]/fibonacci [len(fibonacci)-2],nbOr)

print (fibonacci)