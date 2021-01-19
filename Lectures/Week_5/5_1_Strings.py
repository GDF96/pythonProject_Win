# String format

# first simple example
for i in range(11):
    print(i,"\t", i **2, "\t", i **3 )

# better example; specifying using {} where and how variables to show up
string_format = "{0:2} {2:3} {3:$^8} {1:2.2f}" # :3 behind 2 means 3 characters wide, .2f means floatingpoint number

for i in range(11):
    print(string_format.format(i, i ** .5, i ** 2, i ** 3))

# changing the order

string_format = "{3}\t{2}\t{0}\t{1}"

for i in range(11):
    print(string_format.format(i, i ** .5, i ** 2, i ** 3))