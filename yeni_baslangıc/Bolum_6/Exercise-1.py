N='Fizik:90*Matematik:70*Kimya:50'
dersler=[]
for i in N.split('*'):
    dersler.append(i.split(':'))

print(dersler)