print("Welcome T0 Message Encoder")
print()

# Taking input from user
data = input("Enter The Message : ")


# conversion Chart
conversion_code = {

	# Uppercase Alphabets
	'A': '01', 'B': '0A1', 'C': '0B2', 'D': '0B3', 'E': '0C1', 'F': '0C2',
	'G': '0C3', 'H': '0D9', 'I': '0D8', 'J': '0D7', 'K': '0D6', 'L': '0E1',
	'M': '0E2', 'N': '0E3', 'O': '0E4', 'P': '0E5', 'Q': '0F1', 'R': '0F3',
	'S': '0F4', 'T': '0F8', 'U': '0G1', 'V': '0G9', 'W': '0H8', 'X': '0H1',
	'Y': 'OH2', 'Z': 'OH3',

	# Lowercase Alphabets
	'a': '01', 'b': '0A1', 'c': '0B2', 'd': '0B3', 'e': '0C1', 'f': '0C2',
	'g': '0C3', 'h': '0D9', 'i': '0D8', 'j': '0D7', 'k': '0D6', 'l': '0E1',
	'm': '0E2', 'n': '0E3', 'o': '0E4', 'p': '0E5', 'q': '0F1', 'r': '0F3',
	's': '0F4', 't': '0F8', 'u': '0G1', 'v': '0G9', 'w': '0H8', 'x': '0H1',
	'y': 'OH2', 'z': 'OH3',
  
  # Numbers
  '1': '101', '2': '111', '3': '10A', '4': '10B', '5': '10C', '6': '10D',
  '7': '10E', '8': '10F', '9': '110', '0': 'XXX', ' ': '_'
}

# Creating converted output
converted_data = ""


for i in range(0, len(data)):
	if data[i] in conversion_code.keys():
		converted_data += conversion_code[data[i]]
	else:
		converted_data += data[i]

# Printing converted output
print()
print("Encoded Message : ",converted_data)
print()
mess = input("Type A Feedback : ")
