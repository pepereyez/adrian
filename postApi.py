import requests
import json
if __name__ == '__main__':
    url='http://httpbin.org/post'
    payload={'nombre':'adrian','curso':'pyhton','nivel':'expert'}

    response=requests.post(url,data=payload)
    print(response.url)

    if response.status_code==200:
        print(response.content)
