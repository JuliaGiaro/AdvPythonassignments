import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    ## YOUR CODE HERE
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
    pass

def build_tram_lines(lines):
    ## YOUR CODE HERE
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
    #  ]
    # }
    pass

#def time_dictionary(keys as stop names, values as dictionaries from stop names to nr of minutes):


def build_tram_network(stopfile, linefile):
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

    pass

def lines_via_stop(linedict, stop):
    ## YOUR CODE HERE
    
    # this lists all the lines that go via the given stop
    # the lines should be sorted in their numeric order dvs 2 before 10
    
    pass

def lines_between_stops(linedict, stop1, stop2):
    ## YOUR CODE HERE
    # this lists all the lines that go from stop1 to stop2
    # the lines should be sorted in their numeric order
    # OBS! each line is assumed to serve in both directions, the direction listed explicitly and the opposite
    
    
    pass

def time_between_stops(linedict, timedict, line, stop1, stop2):
    ## YOUR CODE HERE
    
    #calculates the time from stop1 to stop2 along the given line 
    # this is obtained by the sum of all distances between adjacent stops
    # if the stops are not along the same line, an error message is printed
        
    pass

def distance_between_stops(stopdict, stop1, stop2):
    ## YOUR CODE HERE
    
    # calculates the geographic distance between any two stops, based on their lang and long
    # the distance is hence not depended on the tram lines
    # use this formula:[this Wikipedia description](https://en.wikipedia.org/wiki/Geographical_distance#Spherical_Earth_projected_to_a_plane), and notice that the `math` library is needed in the Python code. 
    
    # OBS eftersom det finns en ny version 3.11 av python som kan definea detta bättre
    # länk: [Haversine](https://pypi.org/project/haversine/).
    # kan man få extra poäng om man inte gör det med en library som i ursprungsversionen
    pass

def answer_query(tramdict, query):
    ## YOUR CODE HERE
    
    # takes the query string and returns the answer as a value (list integer or float, or false if the query cannot be interpreted)
    
    pass

def dialogue(tramfile=TRAM_FILE):
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
    
    
    pass

if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        build_tram_network(STOP_FILE,LINE_FILE)
    else:
        dialogue()