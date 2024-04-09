import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('O site não está acessível')
else:
    print('O site está normal.')