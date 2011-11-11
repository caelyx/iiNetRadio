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

stations = {}
stations['abc-classicfm'] = 'http://streams.radio.3fl.net.au:8000/abc-classicfm'
stations['abc-dig'] = 'http://streams.radio.3fl.net.au:8000/abc-dig'
stations['abc-digcountry'] = 'http://streams.radio.3fl.net.au:8000/abc-digcountry'
stations['abc-digjazz'] = 'http://streams.radio.3fl.net.au:8000/abc-digjazz'
stations['abc-triplej'] = 'http://streams.radio.3fl.net.au:8000/abc-triplej'
stations['chronix-grit'] = 'http://streams.radio.3fl.net.au:8000/chronix-grit'
stations['chronix-metal'] = 'http://streams.radio.3fl.net.au:8000/chronix-metal'
stations['chronix'] = 'http://streams.radio.3fl.net.au:8000/chronix'
stations['difm-breaks'] = 'http://streams.radio.3fl.net.au:8000/difm-breaks'
stations['difm-chillout'] = 'http://streams.radio.3fl.net.au:8000/difm-chillout'
stations['difm-djmixes'] = 'http://streams.radio.3fl.net.au:8000/difm-djmixes'
stations['difm-dnb'] = 'http://streams.radio.3fl.net.au:8000/difm-dnb'
stations['difm-electro'] = 'http://streams.radio.3fl.net.au:8000/difm-electro'
stations['difm-eurodance'] = 'http://streams.radio.3fl.net.au:8000/difm-eurodance'
stations['difm-funkyhouse'] = 'http://streams.radio.3fl.net.au:8000/difm-funkyhouse'
stations['difm-goapsytrance'] = 'http://streams.radio.3fl.net.au:8000/difm-goapsytrance'
stations['difm-hardcore'] = 'http://streams.radio.3fl.net.au:8000/difm-hardcore'
stations['difm-harddance'] = 'http://streams.radio.3fl.net.au:8000/difm-harddance'
stations['difm-hardstyle'] = 'http://streams.radio.3fl.net.au:8000/difm-hardstyle'
stations['difm-house'] = 'http://streams.radio.3fl.net.au:8000/difm-house'
stations['difm-lounge'] = 'http://streams.radio.3fl.net.au:8000/difm-lounge'
stations['difm-minimal'] = 'http://streams.radio.3fl.net.au:8000/difm-minimal'
stations['difm-progressive'] = 'http://streams.radio.3fl.net.au:8000/difm-progressive'
stations['difm-trance'] = 'http://streams.radio.3fl.net.au:8000/difm-trance'
stations['difm-tribalhouse'] = 'http://streams.radio.3fl.net.au:8000/difm-tribalhouse'
stations['difm-vocaltrance'] = 'http://streams.radio.3fl.net.au:8000/difm-vocaltrance'
stations['etn-progressive'] = 'http://streams.radio.3fl.net.au:8000/etn-progressive'
stations['etn-trance'] = 'http://streams.radio.3fl.net.au:8000/etn-trance'
stations['eye97'] = 'http://streams.radio.3fl.net.au:8000/eye97'
stations['eye97dance'] = 'http://streams.radio.3fl.net.au:8000/eye97dance'
stations['hitzradio'] = 'http://streams.radio.3fl.net.au:8000/hitzradio'
stations['radionri'] = 'http://streams.radio.3fl.net.au:8000/radionri'
stations['radioskipper'] = 'http://streams.radio.3fl.net.au:8000/radioskipper'
stations['skyfm-classical'] = 'http://streams.radio.3fl.net.au:8000/skyfm-classical'
stations['skyfm-guitar'] = 'http://streams.radio.3fl.net.au:8000/skyfm-guitar'
stations['skyfm-reggae'] = 'http://streams.radio.3fl.net.au:8000/skyfm-reggae'
stations['skyfm-salsa'] = 'http://streams.radio.3fl.net.au:8000/skyfm-salsa'
stations['skyfm-world'] = 'http://streams.radio.3fl.net.au:8000/skyfm-world'
stations['smoothjazz'] = 'http://streams.radio.3fl.net.au:8000/smoothjazz'
stations['smoothlounge'] = 'http://streams.radio.3fl.net.au:8000/smoothlounge'
stations['somafm-beatblender'] = 'http://streams.radio.3fl.net.au:8000/somafm-beatblender'
stations['somafm-groovesalad'] = 'http://streams.radio.3fl.net.au:8000/somafm-groovesalad'
stations['somafm-illinoisstreetlounge'] = 'http://streams.radio.3fl.net.au:8000/somafm-illinoisstreetlounge'
stations['somafm-secretagent'] = 'http://streams.radio.3fl.net.au:8000/somafm-secretagent'
stations['somafm-spacestation'] = 'http://streams.radio.3fl.net.au:8000/somafm-spacestation'
stations['starpoint'] = 'http://streams.radio.3fl.net.au:8000/starpoint'
stations['virgin-classicrock'] = 'http://streams.radio.3fl.net.au:8000/virgin-classicrock'
stations['virgin-xtreme'] = 'http://streams.radio.3fl.net.au:8000/virgin-xtreme'
stations['virginradio'] = 'http://streams.radio.3fl.net.au:8000/virginradio'
stations['wazee'] = 'http://streams.radio.3fl.net.au:8000/wazee'


def printStationList():
    ks = stations.keys()
    ks.sort()
    for x in ks:
	print x

def searchForUniquePrefix(prefix):
    ks = stations.keys()
    shuffle(ks)
    for k in ks:
        p_length = len(prefix)
        if (k[:p_length] == prefix):
            return (stations[k], k)
    return (None, None)

def main():
  parser = argparse.ArgumentParser(description='Play iiNet Freezone Radio through mpg321.')
  parser.add_argument('station', metavar='S', nargs='?', help='which station to play')
  parser.add_argument('-l', '--list', action='store_true', help='display the list of stations and exit')
  args = parser.parse_args()

  if (args.list): 
      printStationList()
  elif (stations.has_key(args.station)):
      execl('/usr/local/bin/mpg321', '/usr/local/bin/mpg321', stations[args.station])
  else:
    (stationURL, stationName) = searchForUniquePrefix(args.station)
    if (stationName):
        print "Found prefix match; playing station %s\n\n" %stationName
        execl('/usr/local/bin/mpg321', '/usr/local/bin/mpg321', stationURL)
    else:
        print "Unknown station."


if __name__ == "__main__": 
    main()
