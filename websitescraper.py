import requests, bs4

class Webscraper:

	##grab the url of the 
	def get_url():
		##hardcoded for now
		url = 'https://www.bonappetit.com/recipe/dashi-oats-with-crunchy-veg'
		return url

	##input url to webpage
	##output raw recipe in list format
	def connect_to_webpage(url):
		webpage = requests.get(url)
		webpage.raise_for_status()
		temp = bs4.BeautifulSoup(webpage.text)
		temp = temp.select('script[type="application/ld+json"]')
		for i in temp[0]:
			recipeList = str(i)
		return recipeList


	##take in the raw recipe from website
	##output the recipe object	
	def create_recipe_object(recipeList, url):
		recipeList = recipeList.split('\n')
		

		##getting and cleaning the ingredients list
		ingredients = recipeList[17].split('","')
		idx = 0
		for i in ingredients:
			ingredients[idx] = ingredients[idx].strip()
			ingredients[idx] = ingredients[idx].strip('"')
			idx += 1



		##getting and cleaning the recipe steps list
		steps = recipeList[20].strip('"},').split("{\"@type\":\"HowToStep\",\"text\":")
		idx = 0
		steps.pop(0)
		for i in steps:
			steps[idx] = steps[idx].strip('"},')
			steps[idx] = steps[idx].strip('"')
			steps[idx] = steps[idx].strip('\'')
			idx += 1


		##getting the recipe name:
		name = recipeList[4]
		name = name.strip(',"name": "')


		##getting the Author
		author = recipeList[8]
		author = author.strip(',"name": "')

		##getting the description
		description = recipeList[13]
		description = description.strip('        ,"description": "')

		##getting the serving size
		servings = recipeList[15]
		servings = servings.strip('        ,"recipeYield": "')
		servings = servings.strip(' servings')
		servings = int(servings)

		## ya girl figure this shit out
		
		recipe = Recipe(url, name, description, author, servings, ingredients, steps)
		return recipe



	def main():
		url = get_url()
		recipeList = connect_to_webpage(url)
		recipe = create_recipe_object(recipeList, url)