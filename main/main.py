# from utilities.string_reversal_function import reverse_string

# assert reverse_string('henry') == 'yrneh'

from utilities.utilities import get_animes, extract, transform

ANIMES = ['Naruto', 'Bleach', 'One Piece']

anime = extract(ANIMES)
print(transform(anime))