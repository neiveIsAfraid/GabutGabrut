#mapping the entire alphabet inside of the number
import sys

alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
alphabetUpper = {'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51}
number = {0: 'a',1 :'b', 2: 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 :  'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 :  'w', 23 : 'x', 24 : 'y', 25 : 'z'}
numberUpper = {26 : 'A', 27 : 'B', 28 : 'C', 29 : 'D', 30 : 'E', 31 : 'F', 32 : 'G', 33 : 'H', 34 : 'I', 35 : 'J', 36 : 'K', 37 : 'L', 38 : 'M', 39 : 'N', 40 : 'O', 41 : 'P', 42 : 'Q', 43 : 'R', 44 : 'S', 45 :'T', 46 : 'U', 47 : 'V', 48 : 'W', 49 : 'X', 50 : 'Y', 51 : 'Z'}

#Function To encode
def caesar_encode(alphabet, number, words, subtitte):
	str_to_list = list(words) #change the words to list
	number_list = [alphabet[word] for word in str_to_list] #change list to map 
	hashed = [(i + subtitute) % 26 for i in number_list]
	word_list = []
	for i in hashed:
		word_list.append(number[i])
	kata_out = "".join(word_list)
	return kata_out

#Function To decode
def caesar_decode(alphabet, number, words, subtitute):
	str_to_list = list(words) #change the words to list
	number_list = [alphabet[word] for word in str_to_list] #change list to map 
	hashed = [(i - subtitute) % 26 for i in number_list]
	word_list = []
	for i in hashed:
		word_list.append(number[i])
	kata_out = "".join(word_list)
	return kata_out

#Main Function Of this dumbass program

#Asking the condition
decode_encode = input("Do you want to (e)encode or (d)decode ? ")
if decode_encode != "e" and decode_encode != "d" and decode_encode != "D" and decode_encode != "E": #checks whether the condition is true or not
	raise TypeError("You are a dummy")
valid_input = input(str("Input: "))
subtitute = int(input("How far you want to subtitute: "))
if decode_encode == "d" or decode_encode == "D":
	print(caesar_decode(alphabet, number, valid_input, subtitute))
elif decode_encode == "e" or decode_encode == "E":
	print(caesar_encode(alphabet, number, valid_input, subtitute))


