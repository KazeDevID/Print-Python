from prettytable import PrettyTable#Install to module 'pip install prettytable'

t = PrettyTable(['Name', 'Age'])
t.add_row(['KazeDevID', 18])

print(t)