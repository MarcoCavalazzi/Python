"""
The scenario:

A spy deleted important files from a computer. There were a few witnesses at the scene of the crime, but no one is sure who exactly the spy was. Three possible suspects were apprehended based on surveillance video. Each suspect had a sample of DNA taken from them. The computer's keyboard was also swabbed for DNA evidence and, luckily, one small DNA sample was successfully retrieved from the computer's keyboard.

Given the three suspects' DNA and the sample DNA retreived from the keyboard, it's up to you to figure out who the spy is!

The project should have methods for each of the following:

1. Given a file, read in the DNA for each suspect and save it as a string
2. Take a DNA string and split it into a list of codons
3. Iterate through a suspect's codon list to see how many of their codons match the sample codons
4. Pick the right suspect to continue the investigation on.
"""

sample = ['GTA','GGG','CAC']

# This method will read a suspect's DNA sample.
def read_dna(dna_file):
  dna_data = ""
  with open(dna_file, "r") as f:
    for line in f:
      dna_data = line
  return dna_data

# This method will take a string, create a list of codons from that string, and return the list.
def dna_codons(dna):
  codons = []
  for i in range(0, len(dna), 3):
    if (i+3) > len(dna):
      return codons
    codons.append(dna[i:i+3])
  return codons

# Method that will iterate through both the sample and a suspect's DNA. The method should count the number of times a codon in the sample matches a codon in the suspect's DNA.
def match_dna(dna):
  matches  = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

# This method will do all the hard work of reading a DNA sample from a suspect, comparing it to a DNA sample from the crime scene, and letting the user know whether the suspect is a criminal.
def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  codons = dna_codons(dna_data)
  num_matches = match_dna(codons)
  if num_matches >= 3:
    print "Matches: %d. The investigation should continue." %num_matches
  else:
    print "Matches: %d. The suspect can be freed." %num_matches
  
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")