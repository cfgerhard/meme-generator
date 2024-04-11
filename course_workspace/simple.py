import random

cat_string = "--Whiskers--, --Spot--, --Meow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
print(cat_string)
fib = [0, 1, 1, 2, 3, 5, 8]
fib_plus_1 = [x+1 for x in fib]
print(fib_plus_1)
split = "split:into:a:list".split(":")
print(split)
strip = "...hello...".strip('...')
print(strip)
clean_cat_list = [cat.strip('--') for cat in cat_string.split(', ')]
print(clean_cat_list)

print(random.randint(0, 10))
random_cat = random.choice(clean_cat_list)

print(f'{random_cat} is a good doggy!')
custom_phrase = " is a good doggy"


def cat_fact(cat, phrase):
    return cat + phrase


print(cat_fact(random_cat, custom_phrase))
