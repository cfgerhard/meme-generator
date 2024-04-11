import random

catString = "--Whiskers--, --Spot--, --Meow--, \
--Tiger--, --Kitty--, --Henry--, --Mr.Paws--"


def random_cat(string_list):
    cat_list = string_list.split(', ')  # split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)


print(f'{random_cat(catString)} is a good kitty')

story =  ("Once upon a time there was a very long string that was "
          "over 100 characters long and could not all fit on the "
          "screen at once.")
print(story)