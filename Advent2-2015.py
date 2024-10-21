import math
def Day2_1(Input):
    SInp = Input.split("\n")
    #SInp = ["2x3x4","1x1x10"]
    TotalNeed = 0
    for i in SInp:
        Dim = i.split("x")
        Dim = [int(j) for j in Dim]
        Sides = []
        for j in range(len(Dim)-1):
            for k in range(j+1,len(Dim)):
                Sides.append(Dim[j]*Dim[k])
        TotalNeed += 2*sum(Sides) + min(Sides)
    print(TotalNeed)
    return(TotalNeed)

def Day2_2(Input):
    SInp = Input.split("\n")
    #SInp = ["2x3x4","1x1x10"]
    TotalNeed = 0
    for i in SInp:
        Dim = i.split("x")
        Dim = [int(j) for j in Dim]
        TotalNeed += math.prod(Dim)
        Dim.pop(Dim.index(max(Dim)))
        TotalNeed += 2*sum(Dim)
    print(TotalNeed)
    return(0)
        
with open("C:\\Users\\natal\\OneDrive\\Documents\\Code\\Learning\\Advent of Codes\\Input.txt","r") as x:
    Input = x.read()
#print(Input)
Day2_2(Input)
