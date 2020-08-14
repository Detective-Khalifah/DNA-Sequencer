import fileinput, re

class Sequencer():

    def __init__(self, path="./DNA.txt"):
        self.dna = ''
        self.dna_sequences = []
        self.path = path
        
    def sequence(self):
        dna_sequences = []
        try:
            with fileinput.input(files=(self.path)) as dna_file:
                for line in dna_file:
                    dna_sequences.append(line.replace('\n', ''))

            dna = str(dna_sequences).replace("'", '').replace(',','').replace('[','').replace(']','').replace(' ', '')        

            self.dna_sequences = dna_sequences            
            self.dna = dna
            
            return(str(dna_sequences))
        except FileNotFoundError:
            print("File cannot be found!")
            
    def find(self, char):
        char_list, index = [], 0
        while index < len(self.dna):
            index = self.dna.find(char, index)
            if index == -1:
                break
            char_list.append(index)
            index += 1
        return ("Occurrences of {}:: {}" .format(char, str(char_list) + '\n') )

    def gatter(self, sequences):
        gat_list = []
        for gat in re.finditer('GAT', sequences):
            beginning, end = gat.start(), gat.end()+1
            print('GAT+ found at {}-{}: {}' .format(beginning, end, (sequences[beginning:end]) ))
            gat_list.append(sequences[beginning:end])
    
        return gat_list




print("Program's started... \n")

sequencer = Sequencer("DNA.txt")

sequences = sequencer.sequence()
print("Sequences:: {}" .format(sequences))
print('Length of the DNA sequence \'{}\' is {}' .format( sequencer.dna, len(sequencer.dna) ) )

# 1a:
print("1a initialised.")
#with open('gat.txt', 'a') as base:
a_bases = sequencer.find('A')
    #base.write(a_bases)
g_bases = sequencer.find('G')
    #base.write(g_bases)
print("1a complete.")
    
# 1b:
print("1b initialised.")
with open('gat.txt', 'w') as result:
    gat_occurences = sequencer.gatter(sequencer.dna)
    result.write("Occurences of \'GAT_\':: {}" .format(gat_occurences))
print("1b complete.")

# 1c:
print("1c initialised.")
new_sequence, position = "", 0
while position < len(gat_occurences):
    new_sequence += (gat_occurences[position])
    position += 1
with open('gat.txt', 'a') as result:
    result.write( '\nSequences appended:: {}' .format(new_sequence) )
print("New Sequence:: {}" .format(new_sequence))
print("1c complete.")


"""
Commented print statements are progress indicators showing task processed.
"""


""" DUMP
dna, sequences, a, g = '', [], [], []
            #itera = re.finditer('GAT', line)
            #print(" \"GAT\" found at", itera.start(), itera.end())
            #for char in line:
            #if line.find('GAT'):
                #print(line.substring(4))
                #gat.append(line.index('GAT'))
            #gat.append([line.find('GAT') for line in list if line.find('GAT') is not (-1)])
            #print('gat:: ' .format(gat))
            #gatters = [str(list).index('G') for char in line if char is 'A' or char is 'G']
            #gat += str(gatters) + '\n'

            #for line in list:
            #print('line:: {}' .format(line))
            #for char in line:
             #   print('char:: {}' .format(char))
            #if 'GAT' in line:
             #   print("Found \'GAT\' at {} " .format(line) )

        #gatts = []
        #gatts.append([ sequences[gat.start():gat.end()+1] for gat in re.finditer('GAT', sequences)])
        print("gatts:: " .format(gatts))
"""
