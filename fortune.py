
import random

fortunes = open("fortune.txt").read()
fortune = fortunes.split("%")

print(random.choice(fortune))
