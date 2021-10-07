import numpy as np
import time

def bubble_sort(L,*args,**kwargs):
    def swap(i,j):
        t = L[i]
        L[i] = L[j]
        L[j] = t
    
        
    length = len(L)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if L[j] > L[j+1]:
                swap(j,j+1)
        #print(f'iter {length - i} : {L}')
    return L

def insertion_sort(L):
    length = len(L)
    
    for i in range(1,length):
        key = L[i]
        
        for j in range(i-1,-1,-1):
            if key < L[j]:
                L[j+1] = L[j]
            else:
                L[j+1] = key
                break
        #print(f'iter {length - i} : {L}')    
    return L

def selection_sort(L,*args,**kwargs):
    def swap(i,j):
        t = L[i]
        L[i] = L[j]
        L[j] = t
        
    length = len(L)
    for i in range(length):
        minimum = L[i]
        min_idx = i
        for j in range(i,length):
            if minimum > L[j]:
                minimum = L[j]
                min_idx = j                
        swap(i,min_idx)
    return L
        
        
def merge_sort(L,*args,**kwargs):
    def merge(left_list, right_list):
        merged_list = []
        while len(left_list) > 0 or len(right_list) > 0:
            if  len(left_list)*len(right_list) !=0:
                if left_list[0] >= right_list[0]:
                    merged_list.append(right_list.pop(0))
                else :
                    merged_list.append(left_list.pop(0))
            elif len(left_list) >0 :
                merged_list.append(left_list.pop(0))
            else :
                merged_list.append(right_list.pop(0))
        
        return merged_list
        
    if len(L) <=1 :
        return L
    mid = int(len(L)/2)
    
    left = L[:mid]
    right = L[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def quick_sort(L,*args,**kwargs):
    
    if len(L) <= 1 :
        return L
    
    left = []
    right= []
    pivot = L.pop()
    for item in L:
        if pivot < item:
            right.append(item)
        else :
            left.append(item)
    
    left = quick_sort(left)
    right = quick_sort(right)
    L_sorted = left + [pivot] + right
    return L_sorted
    
def counting_sort(L,d):
    c = [0] *(d+1)
    for i in L:
        c[i] += 1
    
    for j in range(1, d+1):
        c[j] = c[j-1] +c[j]
        
    n = len(L)
    t = [0]*n
    for i in range(n-1,-1,-1):
        j = L[i]
        t[c[j]-1] = j
        c[j] = c[j] -1
        
    for i in range(0,n):
        L[i] = t[i]
    
    return L
    
def radix_sort(L,d):
    for r in range(0,d):
        c = [0]*10
        m = d-r-1
        for i in L:
            key = int(str(i)[m])
            c[key] += 1
        for j in range(1,10):
            c[j] = c[j-1] + c[j]
        n = len(L)
        t = [0] * n
        for i in range(n-1, -1, -1):
            key = int(str(L[i])[m])
            t[c[key]-1] = L[i]
            c[key] = c[key] -1
        for i in range(0,n):
            L[i] = t[i]
    return L
            
    
if __name__ == '__main__':

    L = [1,2,3,4,5,9,8,7,6]
    print(bubble_sort(L))
    
    L = [1,2,3,4,5,9,8,7,6]
    print(insertion_sort(L))
    
    L = [1,2,3,4,5,9,8,7,6]    
    print(selection_sort(L))
    
    L = [1,2,3,4,5,9,8,7,6]    
    print(merge_sort(L))
    
    L = [1,2,3,4,5,9,8,7,6]    
    print(quick_sort(L))
    
    L = [1,2,3,4,5,9,8,7,6]    
    print(counting_sort(L,10))
    
    L = [1,2,3,4,5,9,8,7,6]
    print(radix_sort(L,1))
    