"""
Next greatest element
triplets
"""
    


d={'(':')',
   '{':'}',
   '[':']'
   }
l=[]
inp=input("Enter the input : ")
c=0
for i in inp:
    c+=1
    if i in d:
        l.append(i)
        
    elif i not in d:
        if len(l)==0:
            
            break
        elif d[l[-1]]==i:
            
            l.pop()
            
if len(l)==0 and len(inp)==c:
    print("Valid")
else:
    print("Invalid")
