from texttable import Texttable#install module 'pip install texttable'

t = Texttable()
t.add_rows([['Team', 'Member'], ['Abal', 7], ['KazeDevID', 0]])


print(t.draw())
