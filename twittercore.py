import linecache
import twitter
import random
import sys

try:
    import pyext
    class twittercore(pyext._class):
	"""Example of a simple class which receives messages and prints to the console"""
        
	# number of inlets and outlets
	_inlets=1
	_outlets=2
        _api = twitter.Api()
        
# methods for first inlet
        

        def break_generate(self, strout):
            words = strout.split(' ')
            sumlist = list()
            for word in words:
                sum = 0
                for i in range(len(word)):
                    sum += ord(word[i])
                sumlist.append(sum)
            print sumlist
            if len(sumlist) % 2  == 1:
                sumlist.append(1000)
            self._outlet(2, sumlist)

        def pull_twitter_1(self):
            msg_list = self._api.GetPublicTimeline()
            strout = ""
            while len(msg_list) != 0:               
                msg = msg_list.pop()
                try:
                    strout = str(msg.text)
                    break
                except:
                    continue
            self._outlet(1, strout)
            self.break_generate(strout)

        def pull_file_1(self):
            i = random.randint(0,20)
            strout = linecache.getline("testfile.txt", i)
            self._outlet(1, strout)
            self.break_generate(strout)

except:
    print "ERROR: This script must be loaded by the PD/Max pyext external"


if __name__ == "__main__":
    random.seed()
    api = twitter.Api()
    msg_list = api.GetPublicTimeline()
    i = random.randint(0, 20)
    #    msg = msg_list[i]
    #    print msg.text
    strout = ""
    while len(msg_list) != 0:               
        msg = msg_list.pop()
        try:
            strout = str(msg.text)
            break
        except:
            continue
#    str = linecache.getline("testfile.txt", i)
    print strout
