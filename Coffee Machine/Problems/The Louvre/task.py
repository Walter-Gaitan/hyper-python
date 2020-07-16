class Painting:
	museum = 'Louvre'
	
	def __init__(self, title, artist, year):
		self.title = title
		self.artist = artist
		self.year = year
	
	def __repr__(self):
		return f'"{self.title}" by {self.artist} ({self.year}) hangs in the {self.museum}.'


painting = Painting(input(), input(), int(input()))
print(painting)
