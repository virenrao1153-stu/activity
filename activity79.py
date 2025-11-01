import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    
    # Generate random float between 0 and 1
    randomGenerator = random.random()
    
    dateFormat = '%m/%d/%Y'
    
    # Convert string dates to time objects
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    # Generate a random time between start and end
    randomTime = startTime + randomGenerator * (endTime - startTime)
    
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    
    return randomDate

print("Random Date =", getRandomDate("1/1/2016", "12/12/2018"))