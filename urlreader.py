import requests
from bs4 import BeautifulSoup

#class urlreader:

def webpageConnect(url):
    webpage = requests.get(url)
    webpage.raise_for_status()
    #parse the text of html into a bs4 object
    data = BeautifulSoup(webpage.text)
    #store it as a string
    data = str(data)
    return data

def getRecipeUrl(data):
    #split raw data by link tags
    urlList = data.split('data-reactid=')
    f = open('recipes.txt', 'a')
    for i in urlList:
        #filter out only the links with recipes
        if 'https://www.bonappetit.com/recipe/' in i:
            begin = i.find('''">''')
            end = i.find('''</a>''')
            i = i[begin+2:end]
            f.write(i +'\n')
            #print(i)
        else:
            pass
    f.close()

def main():
    #nest loop to get year,month,week values I need
    for year in range(2013, 2020):
        for month in range (1,13):
            for week in range (1,6):
                #find all base urls that contian the /recipes
                sitemap = 'https://www.bonappetit.com/sitemap?year=' + str(year) +'&month=' + str(month) + '&week=' + str(week)
                data = webpageConnect(sitemap)
                getRecipeUrl(data)

main()