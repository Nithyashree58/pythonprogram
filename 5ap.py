class Node:
    def __init__(self,coeff,pow):
        self.coeff=coeff
        self.pow=pow
        self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
    def append(self,coeff,pow):
        n=Node(coeff,pow)
        if self.head is None:
            self.head=n
        else:
            tem=self.head
            while tem.next:
                  tem=tem.next
            tem.next=n
    def printpoly(self):
        tem=self.head
        r=[]
        while tem:
            r.append(f"{tem.coeff}x^{tem.pow}")
            tem=tem.next
        print('+'.join(r))
    def add(self,p1,p2):
        a=p1
        b=p2
        newHead=Node(0,0)
        c=newHead
        while a is not None or b is not None:
            if a is None:
                c.next=b
                break
            elif b is None:
                c.next=a
                break
            elif a.pow==b.pow:
                c.next=Node(a.coeff+b.coeff,a.pow)
                a=a.next
                b=b.next
            elif a.pow>b.pow:
                c.next=Node(a.coeff,a.pow)
                a=a.next
            else:
                c.next=Node(b.coeff,b.pow)
                b=b.next
            c=c.next
        return newHead.next
poly1=Polynomial()
poly1.append(5,3)
poly1.append(4,2)
poly1.append(2,0)
poly2=Polynomial()
poly2.append(5,1)
poly2.append(5,0)
print("First Polynomial:")
poly1.printpoly()
print("Second Polynomial:")
poly2.printpoly()
result=Polynomial()
result.head=result.add(poly1.head,poly2.head)
print("Resultant Polynomial:")
result.printpoly()




