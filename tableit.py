import TableIt#install module 'pip install TableIt'

table = [
    [1, 4, "Hi"],
    [2, 5, 999999],
    [3, "Hi", "Bye"]
]
#output TableIt
print('\nTableIt')#nametag
TableIt.printTable(table)
print('\nTableIt2')#nametag
TableIt.printTable(table, useFieldNames=True)