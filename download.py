from urllib import request
from bs4 import BeautifulSoup

userURL="https://www.chinavoa.com/voa_standard_english/"
html=''

class latestList:
    infoDict={'items':'',
              }
    listeningList=[]

    def getInfo(self,page):
        soup = BeautifulSoup(page, "html.parser")
        a=soup.find_all('a')
        
        num=0
        for line in a:
            #判断是否为听力
            if(line.text.find("VOA常速英语：")!=-1):
                num=num+1
                tempitem={}
                tempitem['name']=line.text[8:]
                tempitem['link']=line['href']
                self.listeningList.append(tempitem)
        #统计个数
        self.infoDict['items']=num
        #print(self.listeningList)

    def getContent(self,page):
        soup = BeautifulSoup(page, "html.parser")
        print(soup)

    def showList(self):
        for line in self.listeningList:
            print("name:",line['name'])
            print("link:",line['link'])

if __name__ == "__main__":
    print("欢迎使用VOA最新常速听力链接获取器。")

    myList=latestList()
    
    response = request.urlopen(userURL)
    html = response.read()
    html = html.decode("utf-8")
    
    myList.getInfo(html)
    myList.showList()
    #myList.getContent(html)

