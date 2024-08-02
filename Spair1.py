import random
authors = {
    'stray kids': ['Chk Chk Boom', 'S-Class', 'Lalalala'],
    'bts': ['Butter', 'Dynamite', 'Fake Love'],
    'txt': ['Sugar Rush Ride', 'Deja Vu', 'Back for More'],
    'itzy': ['Born To Be', 'Untouchable', 'Cake'],
    'aespa': ['Supernova', 'Drama', 'Armageddon'],
    'babymonster': ['Forever', 'Like That', 'Sheesh'],
    'blackpink': ['Pink Venom', 'Shutdown', 'The Girls']}
b = 0
a = input("Введіть группу:")
a = a.lower()
if a in authors:
    if a == 'stray kids':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'bts':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'txt':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'itzy':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'aespa':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'babymonster':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
    if a == 'blackpink':
        b = random.choice(authors[a])
        print("Рекомандована пісня:", b)
else:
    print("Автор не знайдений!")