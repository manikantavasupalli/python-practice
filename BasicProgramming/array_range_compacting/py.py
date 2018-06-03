def solution(a):
    a.sort()
    print(a)
    count=0
    content=""
    temp=a[0]
    temp2=a[0]
    rangek=""
    isgood=0
    for i in range(len(a)):
        #print(i)
        if len(a)>i+1:
            print(a[i])
            if a[i+1] == a[i]+1:
                count=count+1
                temp2=a[i+1]
                continue
        isgood=1
        #print(count,a[i])
        if count==1:
            content=content+str(a[i-1])+","+str(a[i])
        elif count>1:
            rangek=str(temp)+"-"+str(temp2)
            content=content+rangek
        else:
            content=content+str(a[i])
        if i!=len(a)-1:
            content=content+","
        count=0
        if i < len(a)-1:
            temp=a[i+1]     
    if isgood==0:
        if count >1:
            rangek=str(temp)+"-"+str(temp2)
            content=content+rangek
        else:
            rangek=str(temp)+","+str(temp2)
            content=content+rangek
    print(content)
array = list(map(int, input().split()))
print("Input:",array)
solution(array)
    