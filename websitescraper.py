import requests, bs4

class Webscraper:

	##grab the url of the 
	def get_url():
		##hardcoded for now
		url = 'https://www.bonappetit.com/recipe/dashi-oats-with-crunchy-veg'
		return url

	##input url to webpage
	##output raw recipe
	def connect_to_webpage(url):
		webpage = requests.get(url)
		webpage.raise_for_status()
		temp = bs4.BeautifulSoup(webpage.text)
		temp = temp.select('script[type="application/ld+json"]')
		for i in temp[0]:
			recipeHTML = str(i)
		return recipeHTML


	##take in the raw recipe from website
	##output the recipe object	
	def create_recipe_object(recipeList, url):
		recipeList = recipeHTML.split('\n')

		idx = 0
		##iterate through recipe list
		for i in recipeList:
			##find and set the name of the recipe
			if ''',"@type": "Recipe"''' in i:
				name = recipeList[idx + 1]
				name = name.strip(',"name": "')
			##find and set the name of the author
			elif ''',"author": {''' in i:
				author = recipeList[idx + 2]
				author = author.strip(',"name": "')
			##find and set the description
			elif ''',"description":''' in i:
				description = recipeList[idx]
				description = description.strip('        ,"description": "')
			##find and set the recipe yield
			elif ''' ,"recipeYield":''' in i:
				servings = recipeList[idx]
				servings = servings.strip('        ,"recipeYield": "')
				servings = servings.strip(' servings')
			##find the ingredients and put into an array
			elif ''',"recipeIngredient"''' in i:
				ingredients = recipeList[idx + 1].split('","')
				idx2 = 0
				for i in ingredients:
					ingredients[idx2] = ingredients[idx2].strip()
					ingredients[idx2] = ingredients[idx2].strip('"')
					ingredients[idx2] = ingredients[idx2].replace('\\u0022', '"')
					idx2 += 1
			#find the steps and put into an array
			elif ''',"recipeInstructions":''' in i:
				steps = recipeList[idx + 1].strip('"},').split("{\"@type\":\"HowToStep\",\"text\":")
				idx2 = 0
				steps.pop(0)
				for i in steps:
					steps[idx2] = steps[idx2].strip('"},')
					steps[idx2] = steps[idx2].strip('"')
					steps[idx2] = steps[idx2].strip('\'')
					steps[idx2] = steps[idx2].replace('\\u0022', '"')
					idx2 += 1
			##if none of the conditions are met just pass
			else:
				pass
			idx += 1

		## ya girl figure this shit out
		
		recipe = Recipe(url, name, description, author, servings, ingredients, steps)
		return recipe

	def main():
		url = get_url()
		recipeHTML = connect_to_webpage(url)
		recipe = create_recipe_object(recipeList, url)