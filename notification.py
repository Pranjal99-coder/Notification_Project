rom plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5
    )
def getdata(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    notifyme("Pranjal","Corona Cases")
    myHtmlData = getdata('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    print(soup.prettify())
