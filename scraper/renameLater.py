import wikipedia
import urllib
print(wikipedia.geosearch(40.430031, -86.925052, ))
near_articles = wikipedia.geosearch(40.430031, -86.925052)
dday_url = "https://en.wikipedia.org/wiki/Normandy_landings"

print(wikipedia.page("Normandy Landings").coordinates)
print(wikipedia.page("Abraham Lincoln").coordinates)