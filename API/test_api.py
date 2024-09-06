import requests
if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/predict/'
    file = {'file': open('images/early_blight.jpg', 'rb')}
    resp = requests.post(url=url, files=file) 
    print(resp.json())