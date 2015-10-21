import urllib2

def main():
  # open a connection to a URL using urllib2
  webUrl = urllib2.urlopen("http://www.zillow.com/webservice/GetZestimate.htm?zws-id=X1-ZWz1exje6lr66j_agge7&zpid=48749425")

  # get the result code and print it
  print ("result code: " + str(webUrl.getcode()))

  # read the data from the URL and print it
  data = webUrl.read()
  print data

if __name__ == "__main__":
  main()
