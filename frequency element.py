a = int(input("Enter the no of element:"))
b = []
for i in range(a):
    random_list=int(input("Enter the number:"))
    b.append(random_list)
    print("list of element:",b)
    frequency={}
    for item in b:
        if item in frequency:
         frequency[item]+=1
    else:
            frequency[item]=1
            print("Elements:frequency",frequency);
