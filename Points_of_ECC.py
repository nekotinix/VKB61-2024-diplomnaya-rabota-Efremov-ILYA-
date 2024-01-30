class ECC:
    def __init__(self,a,b,mod):
        self.a=a
        self.b=b
        self.mod=mod

    def __repr__(self):
        return('('+str(self.a)+'; '+str(self.b)+'; '+str(self.mod)+')')


class Point:
    
    def __init__(self,x,y,ECC):
        self.x=x
        self.y=y
        self.ECC=ECC

    def __repr__(self):
        return('('+str(self.x)+'; '+str(self.y)+')')

    def __add__(self,other):
        
        def modul(a,b,mod):
            x=a//b
            z=abs(a%b)
            b=abs(b)%mod
            k=evklid(mod,b,[0,1])
            return ((x+z*k)%mod)
    
        def evklid(a,b,y,i=2):
            y.append(y[i-2]-(a//b)*y[i-1])
            i=i+1
            a=a%b
            if a==0: return(y[-2])
            return (evklid(b,a,y,i))
        
        if isinstance(other, int):
            return Point(self.x,self.y,self.ECC)
        
        if other.x!=self.x or other.y!=self.y:
            if (other.x-self.x)%self.ECC.mod==0:
                return Point(0,0,self.ECC)
            k=modul((other.y-self.y),(other.x-self.x),self.ECC.mod)
            x3=(k*k-self.x-other.x)%self.ECC.mod
            y3=(k*(self.x-x3)-self.y)%self.ECC.mod
            
            return Point(x3,y3,self.ECC)
        else:
            if self.y==0:
                return Point(0,0,self.ECC)
            k=modul(3*(self.x**2)+self.ECC.a, 2*self.y, self.ECC.mod)
            x=(k**2-2*self.x)%self.ECC.mod
            y=(k*(self.x-x)-self.y)%self.ECC.mod
            return Point(x,y,self.ECC)
            
        
    def __sub__(self,other):
        y=(other.y*(-1))%self.ECC.mod
        new=self+Point(other.x,y,other.ECC)
        return (new)
    def __mul__(self,other):
        t=self
        p=0
        for i in range(other.bit_length()):
            if i!=0:
                t=t+t
            if (other>>i)&0x01:
                p=t+p
                
            if not isinstance(p, int) and p.x==p.y==0:
                print("Порядок точки превышен. Порядок равен ",i+2)
                break
        return p
    def __rmul__(self,other):
        t=self
        p=0
        for i in range(other.bit_length()):
            if i!=0:
                t=t+t
            if (other>>i)&0x01:
                p=t+p
                
            if not isinstance(p, int) and p.x==p.y==0:
                print("Порядок точки превышен. Порядок равен ",i+2)
                break
        return p

