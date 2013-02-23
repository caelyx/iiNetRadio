#!/usr/bin/python

"""iiNet Radio - A script to make it easy to listen to Freezone radio
Copyright Simon Brown, 2011.

You will need to have mpg321 installed in order to make use of this script.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from os import execl
import argparse
from random import shuffle
from stationlist import buildStationList

# Change this to reflect your mpg321 binary's location
mpg321 = '/usr/local/bin/mpg321'

stations = buildStationList()

def printStationList():
    print "Please select from the following stations:\n "
    ks = stations.keys()
    ks.sort()
    for x in ks:
	print x

def searchForPrefix(prefix):
    ks = stations.keys()
    shuffle(ks) # Randomises; 'difm' will give you a random 'di.fm' station each time. 
    for k in ks:
        p_length = len(prefix)
        if (k[:p_length] == prefix):
            return (stations[k], k)
    return (None, None)

def searchForSubstring(substring): 
    ks = stations.keys()
    shuffle(ks)
    for k in ks: 
        if substring in k: 
            return (stations[k], k)
    return (None, None)

def playURL(url):
    execl(mpg321, mpg321, url)

def main():
  parser = argparse.ArgumentParser(description='Play iiNet Freezone Radio through mpg321.')
  parser.add_argument('station', metavar='S', nargs='?', help='which station to play.')
  parser.add_argument('-l', '--list', action='store_true', help='display the list of stations and exit.')
  args = parser.parse_args()

  # If list requested or no station specified, print list of known stations.
  if ((args.list) or not (args.station)): 
      printStationList()

  # If the station has been specified in full, play it. 
  if (stations.has_key(args.station)):
      playURL(stations[args.station])

  # If the start of a station is specified, play it; if multiple stations share
  # the same prefix, play one of them at random. 
  (stationURL, stationName) = searchForPrefix(args.station)
  if (stationName):
      print "Found prefix match; playing station %s\n\n" %stationName
      playURL(stationURL)

  # If part of a station's name is specified, play it; again, choose among
  # multiple matches at random.
  (stationURL, stationName) = searchForSubstring(args.station)
  if (stationName):
      print "Found substring match; playing station %s\n\n" %stationName
      playURL(stationURL)

  # If all else fails, fail.
  print "Unknown station."


if __name__ == "__main__": 
    main()
