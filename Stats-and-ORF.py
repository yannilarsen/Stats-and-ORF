import re
import sys
import statistics
import subprocess
import math

#defines function my_fun1
def my_fun1(stuff):
#sets variable 'total' equal to sum of numbers in 'stuff'
	total = sum(stuff)
#sets variable 'half' equal to one half of total
	half = total / 2
#define it as 'ordered'
	ordered = sorted(stuff, reverse=True)
#define variable 'running' and set it equal to zero
	running = 0
#iterate through values in 'ordered'
	for i in ordered:
#add each value to the variable 'running'
		running += i
#once 'running' is greater than 'half' stop iterating
#define variable 'final' as the last number added to 
#'running' and stop iterating
		if running >= half:
			final = i
			break
#print final value added to 'running' to the command line
#returns N50 value for sequencing data
	print("N50: ", final)

#defines function 'my_fun2 that takes 2 inputs
def my_fun2(cool, thing):
#define a variable 'count' that starts at 0
	count = 0
#iterate through first input entered in my_fun2 (cool)
	for x in cool:
#parse first input 'cool', if anything in 'cool' matches 
#'thing' add 1 to the running count
		for y in x:
			if y == thing:
				count += 1
#once all of 'cool' has been parsed for 'thing' return final #count of 'thing' in 'cool'
	return count


#MAIN

#create variables defline and str to hold sequence 
#identifier (defline) and sequence (str)
#create empty dictionary 'dict'
#create 2 empty arrays, 'array1' and 'array2'

str = ""
dict = {}
defline = ""
array1 = []
array2 = []

#open whatever file follows myScript.py in command line and 
#read it line by line
with open(sys.argv[1], "r") as in_file:
	input = in_file.readlines()

#iterate through input file
for x in input:
#if character '>' is found
	if re.match(">", x):
#substitute character '\n' with nothing in defline
		x = re.sub("\n", "", x)
#if defline is not empty
		if defline:
#add defline and str to dictionary
			dict[defline] = str
#clear contents of str
			str = ""
#set current line to defline variable
		defline = x
#if the line does not begin with '>' it is a sequence line
	else:
#substitute character '\n' with nothing in sequence line
		x = re.sub("\n", "", x)
#add sequence line to a temporary variable
		str = str + x
#add sequence to dictionary
dict[defline] = str

#iterate through dictionary values (sequences from input)
for x in dict.values():
#add sequence to array1
	array1.append(x)
#add length of sequence to array2
	array2.append(len(x))


#run prodigal to identify open reading frames in input file
#output is text file containing open reading frames 
#'FASTA_ORF'
subprocess.run(["prodigal", "-i", sys.argv[1], "-d", "FASTA_ORF"])

#print number of sequences, length of shortest sequence, 
#length of longest sequence, mean sequence length and 
#median sequence length to the command line

print("Total Number of Sequences: ", len(array2))
print("Shortest Length: ", min(array2))
print("Longest Length: ", max(array2))
print("Median Length: ", statistics.median(array2))
print("Mean Length: ", statistics.mean(array2))

#run my_fun1 on array2 (sequence lengths) which prints the 
#total number of codons in all sequences, 1/2 of that 
#number, and the N50 value for the sequencing data to the 
#command line

my_fun1(array2) 

#run my_fun2 on array1 (sequences) which returns the count 
#of the specified characters (in this case 'T' and 'G')
#adds together the count of 'G' and 'T' in all sequences 
#and divides it by total sequence length, output is 
#percentage of codons in sequences that are 'G' or 'T' and 
#prints it to the command line
print("GC Content: ", ((my_fun2(array1, "G") + my_fun2(array1, "C")) / sum(array2)))
