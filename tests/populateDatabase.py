# Adds fake data to GrowDB
import requests

def amountOfCycles():
    response = requests.get('http://127.0.0.1:8000/growDataAPI/cycle')
    cycle = response.json()
    numOfCycles = len(cycle)
    return(numOfCycles)

def creatingFakeData(numOfFakeCycles, numOfFakeTents, numOfFakePlants, numOfFakeSensors):
    while numOfFakeCycles > 0:
        
        cycleAPI = "http://127.0.0.1:8000/growDataAPI/cycle/" 
        tentAPI = "http://127.0.0.1:8000/growDataAPI/tent/" 
        plantAPI = "http://127.0.0.1:8000/growDataAPI/plant/"
        sensorAPI = "http://127.0.0.1:8000/growDataAPI/sensor/"
        
        numOfCycles = str(amountOfCycles()+1) #number of exiting cycles in DB +1
        
        cycleName = "Cycle " + numOfCycles #names cycle based on num of existing cycles
        cycleURL = cycleAPI + numOfCycles + '/' #new cycle url used for tent post request
        
        print(cycleURL)
        requests.post(cycleAPI, data = {'name': cycleName}) # Create new cycle in DB
        
        #where the fake tents are made
        if numOfFakeTents > 0:
            counter = 1 #used for names of tents
            tentName = "Tent" + str(counter) #creates tent name
            requests.post(tentAPI, data= {'name': tentName, 'cycle': cycleURL, 'lightWatts': 600, 'numOfLights': 1}) #Adds tents to the cycle that was just created
            tentURL = tentAPI + tentName + '/'
            print(tentURL)
            ++counter

        #requests.post(plantAPI, data= {})

        numOfFakeCycles = numOfFakeCycles - 1
        


def main():
    numOfCycles = int(input("How many Cycles do you want to make?: "))
    numOfTents = int(input("How many Tents do you wanna make?: "))
    numOfPlants = int(input("How many Plants do you wanna make?: "))
    numOfSensors = int(input("How many Sensors do you wanna make?: "))

    creatingFakeData(numOfCycles, numOfTents, numOfPlants, numOfSensors)

if __name__ == "__main__":
    main()