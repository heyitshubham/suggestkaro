from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests

def index(request):
    return render(request,'index.html')

#def index(request):
 #   return HttpResponse('''<h1> hello </h1> <a href= "https://www.amazon.in/Aristocrat-Sorento-Polyester-Expandable-Strolley/dp/B07SS9QL92/?tag=cuelinkss15314-21&ascsubtag=20201125cllmqc6ydotp"> honey </a> ''')

def submit(request):
    #djlink=(request.GET.get('link','You entered an incorrect link'))

    link = (request.GET.get('link','You entered an incorrect link'))

    shrt=link.split("ref")
    url=shrt[0]

    pr_url=url.replace("/dp/","/product-reviews/") 
    print(pr_url)

    page = requests.get(pr_url)

    soup = bs(page.content, 'html.parser')

    rating = soup.find_all('span', class_='a-size-medium a-color-base')

    star_rating = []
    for i in range(0, len(rating)):
        star_rating.append(rating[i].get_text())

    # def brk(ll):
    #     for i in ll:
    #         aa = ll[0]
    #         print(aa)

    def convert(string):
        li = list(string.split())
        #print(li)
        com = li[0]
        if com >= str(4.5):
            return("Product is highly recommended \nSo you can buy right now 😍")
        elif com >= str(4) and com <= str(4.5):
            return("Product is recommended \nSo you can buy 🙂")
        elif com >= str(3) and com <= str(3.5):
            return("You can buy if u need it badly 🤨")
        else:
            return("Not Recommended ☹️")

    a = star_rating

    listToStr = ' '.join(map(str, a))
    output_text=convert(listToStr)
    #print(output_text)
    analyzed=output_text
    params={'output_text':analyzed}
    return render(request,'output.html',params)

def about(request):
    #print(request.GET.get('text'))
    #print(djlink)
    return HttpResponse("hello about")
