import random as r
import os

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

for i in range(200):
    nums = []
    nums = [r.randint(0, 500) for _ in range (0, 3) ]
    if(checkIfDuplicates(nums)):
        print("duplicates !!")
    nums.sort()

    nums = str(nums)[1:-1]
    nums = str(nums).replace(',', '')
    command = "python3 cloud.py " + nums 
    os.system(command)