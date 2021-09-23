import numpy as np
import time

def bubble_sort(L):
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

def selection_sort(L):
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
        
def merge_sort(L):
    
    
if __name__ == '__main__':
    L = [1,2,3,4,5,9,8,7,6]
    print(bubble_sort(L))
    L = [1,2,3,4,5,9,8,7,6]
    print(insertion_sort(L))
    L = [1,2,3,4,5,9,8,7,6]    
    print(selection_sort(L))

    