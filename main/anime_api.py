from utilities.utilities import get_animes, extract, transform

ANIMES = ['Naruto', 'Bleach', 'One Piece']

anime = extract(ANIMES)
print(transform(anime))