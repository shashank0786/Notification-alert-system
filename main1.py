from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="G:\covid project new\images.ico",
        timeout=7
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__": 
    #notifyMe("shashank","plz stop this covid19")
    myHTMLData=getData('https://www.mohfw.gov.in/')

    soup = BeautifulSoup(myHTMLData,'html.parser')
    #print(soup.prettify())
    Mydatast=""
    for tr in soup.find_all('thead')[1].find_all('tr'):
        Mydatastr +=tr.get_text()
    Mydatastr=Mydatastr[1:]    
    itemList=Mydatastr.split('\n\n')  
    states=['uttar pradesh','telangana','west bangal']
    for item in itemList[0:35]:
        dataList=item.split('\n')
        if dataList[1] in states:
            nTitle='cases of Covid-19'
            nText=f"{States:{dataList[1]} \n IND :{dataList2} \n deaths:{dataList[3]}" 
            notifyMe(nTitle,nText)
            time.sleep(2)

    # if you want to break out this notifiaction per hour then you can put a while loop on it and at last time.sleep(3600).then it will work very fine..        

        
        
    
            
   
    
    