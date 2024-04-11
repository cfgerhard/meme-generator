import subprocess
import random
p = subprocess.run(['emoj', 'dog'], stdout=subprocess.PIPE)
emoji = p.stdout.decode('utf-8').split(' ')
print(random.choice(emoji))