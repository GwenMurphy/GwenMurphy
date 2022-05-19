import random

for n in range(1,11):
	print(f'{n}. Printers are like Tom. They\'re annoying.')
    
favact = ["Chloë Grace Moretz", "Ella Balinska", "Brie Larson", "Cara Delevingne", "Karen Gillan", "Xochitl Gomez", "Pom Klementieff", "Asia Kate Dillon", "Keanu Reeves", "Frankie Adams", "Dominique Tipper", "Michelle Rodriguez"]

favact.append("Millie Bobby Brown")
favact.append("Sadie Sink")
favact.append("Alexandra Daddario")
favact.append("Daisy Ridley")
favact.append("Kristen Stewart")
favact.append("Naomi Scott")
for x in favact:
    print('x')


for x in favact:
    print(random.choice(favact))