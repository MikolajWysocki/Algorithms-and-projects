def match(str):
    count=0
    for i in str:
        if i == "(":
            count+=1
        if i == ")":
            count-=1
        if count < 0:
            return False
    return count == 0


print(match(")((())"))