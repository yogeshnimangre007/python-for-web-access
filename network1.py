
#we use urllib to make and handel sockets  decode and encode stuff.
import urllib.request,urllib.error,urllib.parse
fhamp=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhamp:
    print(line.decode())
