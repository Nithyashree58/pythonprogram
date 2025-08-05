class polynomial:
    def __init__(self,coeffs):
        self.coeffs=coeffs
    def evaluate(self,x):
        result=0
        for exp,coeff in self.coeffs.items():
            result+=coeff*(x**exp)
        return result
    def __add__(self,other):
        r={}
        for exp,coeff in self.coeffs.items():
                r[exp]=coeff
        for exp,coeff in other.coeffs.items():
                r[exp]==r.get(exp,0)+coeff
        return polynomial(r)
    def __str__(self):
        terms=[]
        for exp,coeff in self.coeffs.items():
            if exp==0:
                term=str(coeff)
            elif exp==1:
                term=f"{coeff}x"
            else:
                term=f"{coeff}x^{exp}"
            terms.append(term)
        return "+".join(terms)
poly1=polynomial({2:3,1:2,0:5})
poly2=polynomial({2:2,1:-1,0:3})
print("Polynomial 1:",poly1)
print("Polynomial 2:",poly2)
sum_poly=poly1+poly2
print("Sum:",sum_poly)
xv=2
print(f"Evaluating at X={xv}:")
print("Poly1:",poly1.evaluate(xv))
print("Poly2:",poly2.evaluate(xv))
print("Sum:",sum_poly.evaluate(xv))
