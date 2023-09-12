listele=[]
size=int(input("enter the size of the list"))
for i in range(0,size):
    n=int(input())
    listele.append(n)
if(listele[0]==listele[-1]):
    print("the first and last elements are same")
else:
    print("the first and last elements are not same")