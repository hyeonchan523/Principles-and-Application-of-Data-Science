def linear_search(l,e):
    found = False
    for i in l:
        if i==e :
            found = True
            break
    return found

def binary_search(l,e):
    low = 0
    high = len(l) -1
    while low<high:
        i = int((high+low)/2)
        if l[i] ==e:
            return i
        elif l[i] < e:
            low = i+1
        else:
            high = i-1
    return -1

if __name__ == '__main__':
    L = [1,2,3,4,5,9,8,7,6]
    print(linear_search(L,7))
    print(binary_search(sorted(L), 7))