import json
from urllib.parse import urljoin
import jsonpath
import requests


class SimpleBook:
    def authentication(self):
        global token
        with open("Authetication.json", 'r')as body:
            global token
            requestbody = body.read()
            body = json.loads(requestbody)
            baseurl = "https://simple-books-api.glitch.me"
            resource = "/api-clients/"
            response = requests.post(urljoin(baseurl, resource), json=body)
            # print(response)
            # print(response.status_code)
            res = json.loads(response.text)
            token = jsonpath.jsonpath(res, 'accessToken')
            print(token)

    def SubmitOrder(self):
        with open("body1.json", "r")as body1:
            global ID
            body1 = body1.read()
            body2 = json.loads(body1)
            baseurl = "https://simple-books-api.glitch.me"
            resource = "/orders"
            headers = {'Authorization': 'Bearer '+token[0]}
            response1 = requests.post(urljoin(baseurl, resource), json=body2, headers=headers)
            print(response1)
            res1 = json.loads(response1.text)
            ID = jsonpath.jsonpath(res1, 'orderId')
            print(ID)

    def updateOrder(self):
        with open("update.json","r")as update:
            update = update.read()
            update1 = json.loads(update)
            baseurl = "https://simple-books-api.glitch.me"
            resource = "/orders/"+str(ID[0])
            headers = {'Authorization': 'Bearer ' + token[0]}
            res2=requests.patch(urljoin(baseurl,resource),json=update1,headers=headers)
            # res = json.loads(res2.text)
            print(res2.status_code)

    def getorder(self):
        baseurl = "https://simple-books-api.glitch.me"
        resource = "/orders/" + str(ID[0])
        headers = {'Authorization': 'Bearer ' + token[0]}
        orders = requests.get(urljoin(baseurl, resource),headers=headers)
        Order = json.loads(orders.text)
        print(Order)

    def Deleteorder(self):
        baseurl = "https://simple-books-api.glitch.me"
        resource = "/orders/" + str(ID[0])
        headers = {'Authorization': 'Bearer ' + token[0]}
        orders = requests.delete(urljoin(baseurl, resource), headers=headers)
        print(orders.status_code)


s = SimpleBook()
s.authentication()
s.SubmitOrder()
s.updateOrder()
s.getorder()
s.Deleteorder()
