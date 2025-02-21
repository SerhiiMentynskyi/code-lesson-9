import urllib.request as ur

print('HTTP Requests')
print('https://httpbin.org/get')

opener = ur.build_opener()
print(type(opener))
