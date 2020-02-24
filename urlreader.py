import requests
from bs4 import BeautifulSoup

class urlreader:

    def webpageConnect():
        url = 'https://www.bonappetit.com/sitemap?year=2018&month=9&week=4'
        #print(test)
        webpage = requests.get(url)
        webpage.raise_for_status()
        #parse the text of html into a bs4 object
        data = BeautifulSoup(webpage.text)
        data = str(data)
        return data

    def getRecipeUrl(data):
        urlList = data.split('a href')

        for i in urlList:
            if 'https://www.bonappetit.com/recipe/' in i:
                print(i)
            else:
                pass
    
    data = webpageConnect()
    getRecipeUrl(data)




  

    #nest loop to get year,month,week values I need
    def sitemapLoop():
        for x in range(2016, 2020):
            for y in range (1,13):
                for z in range (1,5):
                    #find all base urls that contian the /recipes
                    print('https://www.bonappetit.com/sitemap?year=' + str(x) +'&month=' + str(y) + '&week=' + str(z))