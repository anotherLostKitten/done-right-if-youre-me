from random import sample
class B:
    def __init__(self,r,c,m):
        self.g=0
        self.r=r
        self.c=c
        self.m=m
        self.b=[0]*r*c
        for i in sample(range(r*c),m):
            self.b[i]=-1
            for j in(-c,0,c):
                for k in(-1,0,1):
                    if(k!=0 or j!=0)and-1<i+j+k<r*c and-1<(i+j)%c+k<c and self.b[i+j+k]>=0:
                        self.b[i+j+k]+=1
        self.v=[1]*r*c
        self.l=r*c
    def __str__(self):
        return "\n".join(" ".join(str(j)if j<0 else" "+str(j)for j in self.b[i*self.c:(i+1)*self.c])for i in range(self.r))
    def clk(self,r,c,t):
        if self.v[self.c*r+c]==0:
           if self.b[self.c*r+c]==sum(1 if(k!=0 or j!=0)and-1<r+j<self.r and-1<c+k<self.c and-1==self.v[self.c*(r+j)+c+k]else 0 for k in(-1,0,1)for j in(-1,0,1)):
               for j in(-1,0,1):
                   for k in(-1,0,1):
                       if(k!=0 or j!=0)and-1<r+j<self.r and-1<c+k<self.c:
                           if self.b[self.c*(r+j)+c+k]==-1:
                               return-1
                           else:
                               self.dsc(r+j,c+k)
        elif t and self.v[self.c*r+c]==1:
            if self.b[self.c*r+c]==-1:
                return-1
            else:
                self.dsc(r,c)
        elif not t and self.v[self.c*r+c]!=0:
            self.v[self.c*r+c]*=-1
        return sum(0 if(self.v[i]==-1 and-1==self.b[i])or(self.v[i]==0 and-1!=self.b[i])else 1 for i in range(len(self.b)))
    def dsc(self,r,c):
        if self.v[self.c*r+c]!=0:
            self.v[self.c*r+c]=0
            if self.b[self.c*r+c]==0:
                for j in(-1,0,1):
                    for k in(-1,0,1):
                        if(k!=0 or j!=0)and-1<r+j<self.r and-1<c+k<self.c:
                            self.dsc(r+j,c+k)
if __name__=="__main__":
    print(B(16,16,40))
