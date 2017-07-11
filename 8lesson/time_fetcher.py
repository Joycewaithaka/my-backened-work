import urllib.request
time_content = urllib.request.urlopen("http://date.jsontest.com/").read()
print(time_content)