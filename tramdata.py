import math
import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './data/tramnetwork.json'

def build_tram_stops(jsonobject):
    
    dict = json.load(jsonobject)
    dict_tram_stops = {}
    
    for stop in dict:
        dict_tram_stops[stop] = {}
        dict_tram_stops[stop].update({'lat:': dict[stop]['position'][0]})
        dict_tram_stops[stop].update({'lon': dict[stop]['position'][1]})
        
    return dict_tram_stops

    # build a STOP dictionary where: 

    # 1: KEYS are NAMES of tram stops 
    # 2: VALUES are dictionaries with: 
    #    -the latitude 
    #    -the longitude
    
    ## EXAMPLE OF OUTPUT:
    
    #    {
    #  'Majvallen': {
    #    'lat': 57.6909343,
	#'lon': 11.9354935
    #    }
    # }
    
    # pass

def build_tram_lines(fullList):
    ## YOUR CODE HERE 
    
    tramLineDict = {}
    for i in range(len(fullList)):
        if i % 2 == 0:
            tramLineDict[fullList[i][:-1]] = [" ".join(stop[:-1]) for stop in [trimmed.split() for trimmed in fullList[i+1]]]
    return tramLineDict
            
 

    
    
    # build a line dictionary where: 
    # 1: KEYS are NAMES (usually digits, but treated as strings) 
    # 2: VALUES are lists of stop names, in order in which the tram runs: 
    #    
      
    ## EXAMPLE OF OUTPUT:
    #      {
    # "9": [
    #   "Angered Centrum",
    #    "Storås",
    #    "Hammarkullen",
	#    # many more stops in between
    #    "Sandarna",
    #    "Kungssten"
    #  
    # }
 #pass
 
def build_stop_times(fullList):
    stopTimeDict = {}

    for i in range(1, len(fullList), 2):  # Start from index 1 and step by 2
        for j in range(len(fullList[i]) - 1):
            stop1 = " ".join(fullList[i][j].split()[:-1])
            stop2 = " ".join(fullList[i][j + 1].split()[:-1])
            timeBetween = int(fullList[i][j + 1].split()[-1][-2:]) - int(fullList[i][j].split()[-1][-2:])

            if stop1 in stopTimeDict:
                stopTimeDict[stop1].update({stop2: timeBetween})
            else:
                stopTimeDict[stop1] = {stop2: timeBetween}

    return stopTimeDict

#def time_dictionary(keys as stop names, values as dictionaries from stop names to nr of minutes):

def format_textfile(file):
    fullList = []
    with open(file, encoding='utf-8') as f:
        text = f.read()
        paragraphs = text.split("\n\n")
        for lines in paragraphs:
            lines = lines.split("\n", 1)
            fullList.append(lines[0])
            fullList.extend(lines[1].split("\n"))
    return fullList


def build_tram_network(stopfile, linefile):
    
     with open(linefile) as f:
        dict_tram_stops = build_tram_stops(f)
        print("dict_tram_stops", dict_tram_stops)
        formatted_list = format_textfile(stopfile)
        print("formatted_list:", formatted_list)
        tramLineDict = build_tram_lines(formatted_list)
        print("tramLineDict:", tramLineDict)
        stopTimeDict = build_stop_times(formatted_list)
        print("stopTimeDict:", stopTimeDict)
        linedict = {"stops":dict_tram_stops, "lines" : tramLineDict, "times":stopTimeDict}
        
        with open('tramnetwork.json', 'w', encoding="utf-8") as f:
            json.dump(linedict, f, indent=4, ensure_ascii=False)

       
    
    
    ## YOUR CODE HERE
    #this one puts everything together, reads the two input files and
    #writes a third one "tramnetwork.json"
    #this one consists of all three distionaries
    
    #EXAMPLE:
  #          {
  #  "stops": {
  #      "Östra Sjukhuset": {
  #          "lat": 57.7224618,
  #          "lon": 12.0478166
  #			},  # and so on, the entire stop dict			
  #		}
  #    },
  #  "lines": {
  #      "1": [
  #          "Östra Sjukhuset",
  #          "Tingvallsvägen",
  #			# and so on, all stops on line 1
  #			],  # and so on, the entire line dict
  #		},
  #  "times": {
  #      "Tingvallsvägen": {
  #          "Kaggeledstorget": 2
  #          },  # and so on, the entire time dict
  #      }
  #  }

    #pass
def lines_via_stop(linedict, stop):
     resultlist = []
     for line in linedict["lines"]:
        if stop in linedict["lines"][line]:
            resultlist.append(line)
        if len(resultlist) > 0:
            return resultlist
        else:
         return "Unkown arguments"
    ## YOUR CODE HERE
    
    # this lists all the lines that go via the given stop
    # the lines should be sorted in their numeric order dvs 2 before 10
    
   # pass

def lines_between_stops(linedict, stop1, stop2):
        resultlist = []
        for line in linedict["lines"]:
            if stop1 in linedict["lines"][line] and stop2 in linedict["lines"][line]:
             resultlist.append(line)
        if len(resultlist) > 0:
          return resultlist
        else:
          return "Unkown arguments"
    ## YOUR CODE HERE
    # this lists all the lines that go from stop1 to stop2
    # the lines should be sorted in their numeric order
    # OBS! each line is assumed to serve in both directions, the direction listed explicitly and the opposite
    
    
   # pass
   
def distance_between_stops(stopdict, stop1, stop2):
    if stop1 not in stopdict or stop2 not in stopdict:
        return "Error: Stop not found."

    lat1, lon1 = stopdict[stop1]
    lat2, lon2 = stopdict[stop2]

    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = math.radians(lat1), math.radians(lon1)
    lat2, lon2 = math.radians(lat2), math.radians(lon2)

    # Calculate the change in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula to calculate distance
    mean_lat = (lat1 + lat2) / 2
    distance = R * math.sqrt(dlat**2 + (math.cos(mean_lat) * dlon)**2)
    return round(distance,3)
    
    ## YOUR CODE HERE
    
    # calculates the geographic distance between any two stops, based on their lang and long
    # the distance is hence not depended on the tram lines
    # use this formula:[this Wikipedia description](https://en.wikipedia.org/wiki/Geographical_distance#Spherical_Earth_projected_to_a_plane), and notice that the `math` library is needed in the Python code. 
    
    # OBS eftersom det finns en ny version 3.11 av python som kan definea detta bättre
    # länk: [Haversine](https://pypi.org/project/haversine/).
    # kan man få extra poäng om man inte gör det med en library som i ursprungsversionen
    #pass
    
def time_between_stops(linedict, timedict, line, stop1, stop2):
    if line not in linedict["lines"]:
        return "Error: Line not found."

    stopSet = linedict["lines"][line]
    if stop1 not in stopSet.index(stop1) or stop2 not in stopSet.index(stop2):
        return "Error: Stops not found on the given line."

    index1 = stopSet.index(stop1)
    index2 = stopSet.index(stop2)

    journey_set = stopSet[min(index1, index2): max(index1, index2) + 1]
    total_time = 0

    for i in range(len(journey_set) - 1):
        current_stop = journey_set[i]
        next_stop = journey_set[i + 1]

        if current_stop in timedict and next_stop in timedict[current_stop]:
            total_time += timedict[current_stop][next_stop]
        else:
            return "Error: Time information not available for stops {} and {}".format(current_stop, next_stop)

    return total_time
    ## YOUR CODE HERE
    
    #calculates the time from stop1 to stop2 along the given line 
    # this is obtained by the sum of all distances between adjacent stops
    # if the stops are not along the same line, an error message is printed
        
    #pass

def dialogue(tramfile=TRAM_FILE):
    with open(TRAM_FILE, encoding="utf-8") as file:
        tram_data = json.load(file)

    while True:
        user_input = input("> ").lower()

        if user_input.startswith("quit"):
            print("Program terminated.")
            break

        result = answer_query(tram_data, user_input)
        print(result)
    

    ## YOUR CODE HERE
    
    # implements a dialouge about tram information
    # reads the data from "tramnetwork.json" which has been produced by your program
    # takes user input and answers to any number of questions by using your query functions
    
    #EXEMPEL:
    #- `via <stop>`, answered by `lines_via_stop()`
    #- `between <stop1> and <top2>`, answered by `lines_between_stops()`
    #- `time with <line> from <stop1> to <top2>`, answered by `time_between_stops()`
    #- `distance from <stop1> to <top2>`, answered by `distance_between_stops()`
    #- `quit` - terminating the program
    #- input with non-existing line or stop names results in the message "unknown arguments" and a new prompt
    #- any other input results in the message "sorry, try again" and a new prompt
    #- the prompt is `> `.
    
    #the challenge is to deal correctly with stop names that consist of more than one word.
    # a hint for this is to locate the positions of keywords such as "and", which can appear between stop names,
    # and consider slices starting or ending at them.
    # the simplest method is the standard "index()" method of strings
    # also the regular expression library "re" could be used, but its probably more complicated to learn if you dont know it from before
    
    ##VAD SOM FAKTISKT SKA VA I DENNA:
    # reads the file into a dictionary, loops by asking for input, and for each input prints the value returned by
    # "answer_query" except for input "quit" (terminates the loop) and for an uninterpreted input (ask user to try again)
    
    
  #  pass

def answer_query(tramdict, query):
    if "via" in userInput:
        stop = " ".join(userInput.split()[1:])
        return lines_via_stop(dict, stop)
    elif "between" in userInput and "and" in userInput:
        userInput = userInput.split()
        andIndex = userInput.index("and")
        stop1 = " ".join(userInput[1:andIndex])
        stop2 = " ".join(userInput[andIndex+1:])
        return lines_between_stops(dict, stop1, stop2)
    elif "time with" in userInput:
        userInput = userInput.split()
        fromIndex = userInput.index("from")
        toIndex = userInput.index("to")
        line = userInput[2:fromIndex][0]
        stop1 = " ".join(userInput[fromIndex+1:toIndex])
        stop2 = " ".join(userInput[toIndex+1:])
        return time_between_stops(dict, line, stop1, stop2)
    elif "distance from" in userInput:
        userInput = userInput.split()
        fromIndex = userInput.index("from")
        toIndex = userInput.index("to")
        stop1 = " ".join(userInput[fromIndex+1:toIndex])
        stop2 = " ".join(userInput[toIndex+1:])
        return distance_between_stops(dict["stop"], stop1, stop2)
    else:
        return "Sorry, try again"

    ## YOUR CODE HERE
    
    # takes the query string and returns the answer as a value (list integer or float, or false if the query cannot be interpreted)
    
    #pass



if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
       build_tram_network("tramlines.txt","tramstops.json")
       
    else:
      dialogue("tramnetwork.json")