import requests
from bs4 import BeautifulSoup
import datetime
from subprocess import call

url = "https://www.hackerrank.com/contests"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

contest_name = []
end_date = []

a = soup.find_all("ul" , {"class": "contests-active"})
b = a[0].find_all("li")
for i in range(len(b)): 
    c = b[i].div.find_all("div", {"class": "contest-name"})
    print(c[0].get_text())
    contest_name.append(c[0].get_text())

print()

d = b[0].div.find_all("div", {"class": "contest-status"})
print(d[0].get_text())
end_date.append(d[0].get_text())

for i in range(1,len(b)): 
    d = b[i].div.find_all("div", {"class": "contest-status"})
    e = d[0].find_all("meta", {"itemprop": "endDate"})
    date_posted = e[0]['content']
    last_date = datetime.datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%S.%fZ')
    print(last_date)
    end_date.append(last_date)

for t in range(len(contest_name)):
    call(["notify-send",contest_name[t],"\n",'End Date:'+end_date[t]])    
    #call(["notify-send",A[t],"\n",B[t],"\n",'Start Date:'+C[t],"\n",'End Date:'+D[t]])