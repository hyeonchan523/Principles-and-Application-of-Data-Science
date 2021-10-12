"""
**Instruction**
Please see instruction document.

"""

def P2(s:str):
    ##### Write your Code Here #####
    
    # make dictionary
    string = dict()
    for key in set(s):
        string[key] = 0
        
    # count the number of used
    for i, char in enumerate(s):
        string[char] += 1
    
    # check unique
    for i, char in enumerate(s):
        if string[char] == 1:
            return i
        else :
            continue
    return -1
    
    ##### End of your code #####

if __name__ == '__main__':
    print(P2('loveprogram'))
    print(P2('llooveeprogram'))
    print(P2('computingfoundationfordatascience'))
    print(P2('aabbcc'))