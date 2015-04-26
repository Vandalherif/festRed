__author__ = 'ibrahim'
import urllib, json

class team():
    def __init__(self, site):
        url = "http://androidya.hol.es/team.php?s="+site

        response = urllib.urlopen(url)
        data = json.loads(response.read())
        self.name = data[u'name']
        self.rss = data[u'rss']





