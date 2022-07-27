from time import sleep

print('Loading  ', end='', flush=True)
for x in range(3):
    for frame in r'-\|/-\|/':
    
        print('\b', frame, sep='', end='', flush=True)
        sleep(0.2)


print('\b ')