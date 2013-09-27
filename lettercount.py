from sys import argv

script, filename = argv
text_file = open(filename)
data = text_file.read()
text_file.close()

# print "The input file %r has %d characters." % (filename, len(data))

ascii_character_count_list = [0]*128

# check every character of the text file
for i in range(len(data)):
    index = ord(data[i].lower())
    ascii_character_count_list[index] += 1
    
# cut up alphabet
alphabet = ascii_character_count_list[97:123]

# ASCII character for a starts at 97
for i in range(len(alphabet)):
    print alphabet[i] 
