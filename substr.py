def substring(string1):
    string2=list(string1)
    li=[]
    count=0
    for i in range(0,len(string2)):
        if(string2[i] not in li):
           li.append(string2[i])
           count+=1
    return count
print(substring("abcda"))
