from time import sleep

def progress(percent=0, width=30):

    hashes = width * percent // 100
    blanks = width - hashes

    print('\r[', hashes*'#', blanks*' ', ']', f' {percent:.0f}%', sep='',
        end='', flush=True)

print('This will take a moment')
for i in range(101):
    progress(i)
    sleep(0.1)


print()