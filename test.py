import requests
url='http://localhost:5000/users/upload'
with open('test\\getUsersEndpt\\success.csv','rb') as f:
    files={'file': ("exampleFileName.csv", f, "text/csv")}
    # values={'upload_file' : 'file.txt' , 'DB':'photcat' , 'OUT':'csv' , 'SHORT':'short'}
    r=requests.post(url,files=files)
    print(r.text)