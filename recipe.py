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

    def get_url(self):
		return(self.url)

	def get_name(self):
		return(self.name)

	def get_description(self):
		return(self.description)

	def get_author(self):
		return(self.author)

	def get_servings(self):
		return(self.servings)

	def get_ingredients(self):
		return(self.ingredients)

	def get_steps(self):
		return(self.steps)