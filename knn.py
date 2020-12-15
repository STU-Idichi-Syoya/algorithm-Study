import numpy as np

class Data:
    def __init__(self,vec:np.array,spector:str) -> None:
        self.vec=vec
        self.spec=spector


A=np.random.randint(0,100,(10))
B=np.random.randint(0,100,(10))
C=np.random.randint(0,100,(10))
D=np.random.randint(0,100,(10))
E=np.random.randint(0,100,(10))

VectorsArray=[Data(A,'A'),Data(B,'B'),Data(C,'A'),Data(D,'B'),Data(E,'A')]


def getDistance(vec:np.array,vec2:np.array):
    # r=np.sqrt((vec-vec2).sum()**2)
    r=np.linalg.norm(vec-vec2,ord=2)
    # assert r==r1
    return r


'''
spec,count
[(str,int)...]
'''
def getNearVecSpec(vec:np.array,VectorsArray=VectorsArray,k=3)  :
    distance=[]
    for v in VectorsArray:
        d=getDistance(vec,v.vec)
        distance.append((v.spec,d))
    distance.sort(key=lambda X: X[1])
    print(distance)
    diss={}
    for i in range(k):
        v=distance[i]
        spec=v[0]
        if spec in diss:
            diss[spec]+=1
        else:
            diss[spec]=1
    
    return diss
if __name__ == "__main__":
    a=np.random.randint(0,100,size=(10))
    print(getNearVecSpec(a))
