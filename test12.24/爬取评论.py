import requests
s=requests.get('https://club.jd.com/comment/productPageComments.action?callback=jQuery2998451&productId=4564204&score=0&sortType=5&page=0&pageSize=10&pin=null&_=1608826608805')
print(s.text)