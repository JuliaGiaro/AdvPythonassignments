import unittest
from tramdata import *

TRAM_FILE = './tramnetwork.json'

class TestTramData(unittest.TestCase):

    def setUp(self):
        with open(TRAM_FILE) as trams:
            tramdict = json.loads(trams.read())
            self.stopdict = tramdict['stops']
            self.linedict = tramdict['lines']

    def test_stops_exist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    # add your own tests here

    #the task is to write 
    # THREE functions that build dictionaries,
    # FOUR functions that extract information from them,
    # AND a dialouge function that ansvers to queries
    #(the dialouge function should be divided into two parts to enable more accurate testing)
    
    
    #add following tests:
    # all tram lines listed in the original text file, should be included in "linedict"
    # the lists of stops for each tramline is the same in "tramlines.txt" and "linedict"
    # all distances are feasible; meaning less than 20 km (test with smaller nr and see if it fails)
    # time from *a* to *b* is always the same as the time from *b* to *a* along the same line
    
    
    
    
    ## for dialouge tests:
    # test the thing you want to test, then the answer is printed for any query(in a format written by the user)
    # chech if the expected value is the same as the output
    # what you really test is that the queries are parsed and interpreted correctly
    
if __name__ == '__main__':
    unittest.main()
    ##under here there should be a conditional call that checks if "init" in "build_tram_network" is present
    #hint you can check if it is by using "sys.argv"
    # EXEMPEL:   
    # if __name__ == '__main__':
    #    if sys.argv[1:] == ['init']:
    #        build_tram_network("tramlines.txt", "tramstops.json")
    #    else:
    #        dialogue("tramnetwork.json")	
    
    #you also need to import "sys"

