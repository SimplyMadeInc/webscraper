class Recipe:
    
    ##initialize the recipe object
    def __init__(self, url, name, description, author, servings, ingredients, steps):
        self.url = url
        self.name = name
        self.description = description
        self.author = author
        self.servings = servings
        self.ingredients = ingredients
        self.steps = steps

	def __get__(self):
		return(self.url, self.name, self.description, self.author, self.servings, self.ingredients, self.steps)

##this is a change