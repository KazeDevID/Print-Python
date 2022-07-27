import termtables as tt#install module 'pip install termtables'

string = tt.to_string(
    [["Kaze", 18], ["Kaze2", 18]],
    header=["Name", "Age"],
    style=tt.styles.ascii_thin_double,
    # alignment="ll",
    # padding=(0, 1),
)
#OUTPUT termtables
print(string)
