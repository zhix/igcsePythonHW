import random

herdNum = 5     ## number of cows in the herd
yieldDict = {}  ## disctionary that stores all the yields for each cow

## creating dict of cow IDs, each assigned to a list to contain milk yields, starting from 100 (because of the 3 digit id requirement)
for i in range(100,100+herdNum): 

  milkYieldofTheWeek = [] 

  ## a list that contains 14 data of the milk yield for the whole week 
  for j in range(14):
    milkYield = random.randint(5, 50)/10 ## using a random first to test it out, the real data should come from machine
    milkYieldofTheWeek.append(milkYield)
    # print (milkYieldofTheWeek) 
  
  yieldDict[i] = milkYieldofTheWeek 
  

print(yieldDict)    ## use this to show 
