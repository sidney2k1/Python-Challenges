import random
def shuffle(string):
    templist=list(string)
    random.shuffle(templist)
    return ''.join(templist)
uppercaseletter=chr(random.randint(65,90))
uppercaseletter1=chr(random.randint(65,90))
password=uppercaseletter+uppercaseletter1
password=shuffle(password)
print(password)