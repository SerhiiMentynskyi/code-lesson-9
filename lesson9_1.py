import urllib.request as ur

print('HTTP Requests')
print('https://httpbin.org/get')

opener = ur.build_opener()
# resp = opener.open('https://httpbin.org/get')

resp = opener.open('https://httpbin.org/get')
print(resp.read())
