import random
import numpy
import math

#Input
print("Number of types:")
PType = int(input())

numberList = []

for i in range(PType):
    print("Number of type %i" %(i+1))
    testNum = int(input())
    numberList.append(testNum)
    

#File Creation

#Line 1 - number of particles 
n = sum(numberList)
f = open("coords-0.1.dat", "a")
f.write(str(n))
f.write("\n")
f.close()

#Determine Box Size (note that ideal density is dens per sigmaLJ^3)

dens = 0.1
print("Sigma LJ for this system:")
sigmaLJ = float(input())
indBoxLen = 2.15443469 * sigmaLJ
indBoxSize = indBoxLen**3
totBoxLenInIndBox = math.ceil(n**(1/3))
totBoxLen = totBoxLenInIndBox * indBoxLen + 2.5

#line 2-4 = box matrix

f = open("coords-0.1.dat", "a")
f.write("%f          0          0" %totBoxLen)
f.write("\n")
f.write("0          %f          0" %totBoxLen)
f.write("\n")
f.write("0          0          %f" %totBoxLen)
f.write("\n")
f.close()

#The xyz loop

f = open("coords-0.1.dat", "a")

parList = []

for p in range(len(numberList)):
    for q in range(numberList[p]):
        parList.append((p+1))

for i in range(totBoxLenInIndBox):
    parPosX = round(i*indBoxLen + indBoxLen/2,6)    
    for j in range(totBoxLenInIndBox):
        parPosY = round(j*indBoxLen + indBoxLen/2,6)    
        for k in range(totBoxLenInIndBox):
            parPosZ = round(k*indBoxLen + indBoxLen/2,6)    
            
            #pick particle type
            if len(parList) != 0:
                pickedPType = random.choice(parList)
                parList.remove(pickedPType)
            
                newline = "C{}     {}     {}     {}".format(pickedPType, parPosX, parPosY, parPosZ)
                f.write(newline+ "\n") 

        
f.close()

#The rotation loop
f = open("coords-0.1.dat", "a")

for i in range(PType):
    for j in range(numberList[i]):
        
        
        r1 = round(random.uniform(0,1),8)
        r2 = round(random.uniform(0,1),8)
        r3 = round(random.uniform(0,1),8)
        
        fac = (2*r1**2+r2**2+r3**2)**(1/2)
        
        r1 = r1/fac
        r2 = r2/fac
        r3 = r3/fac
        
        newline = "        {}        {}        {}        {}".format(r1,r2,r3,r1)
        f.write(newline+ "\n")        

f.close()
    