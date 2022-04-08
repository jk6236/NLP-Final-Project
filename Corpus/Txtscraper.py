from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Enter url: ")
topic = input("Enter topic of file: ")
#num = int(input("Enter num of Q's: "))

requestPg = urlopen(url)
pgHTML = requestPg.read()
requestPg.close()

htmlSoup = BeautifulSoup(pgHTML, 'html.parser')
cAnswers = htmlSoup.find_all('div', class_="qa-wrap")
questions = htmlSoup.find_all('strong', class_="question")
paragraphs = htmlSoup.find_all('pre')
num = htmlSoup.find_all("div", class_="qas-wrap", limit=4)
sum = 0
for chunk in num:
    add = chunk.find_all('div')
    sum += len(add)

file1 = open(topic+"Qs.txt", 'a')
file2 = open(topic+"As.txt", 'a')
file3 = open(topic+".txt", 'a')

questions = questions[:sum]
cAnswers = cAnswers[:sum]
paras = paragraphs[:4]

qcount = 0

for q in questions:
    qcount += 1
    if qcount != len(questions):
        file1.write(q.text + '\n')
    else:
        file1.write(q.text)


for ans in cAnswers:
    cAns = ans.find_all('span', class_="answer")
    if len(cAns) == 0:
        cAns = ans.find_all('span', class_="no-answer")
        file2.write("No Answer\n")
    else:
        acount = 0
        for a in cAns:
            acount += 1
            if acount != len(cAns):
                file2.write(a.text + '|')
            else:
                file2.write(a.text + '\n')

for p in paras:
    file3.write(p.text + '\n')