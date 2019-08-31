import string 
from structure import Structure
from generator import Generator
 
##***************************************************************************
## This function iterates over the protocol structure and
## fuzzies input from generator data structure into available buffer
##***************************************************************************
def iteratefuzz(structure, fuzz):
  for insertpoint in range(0, len(structure)):
    fileinput = ''
    fuzzed = 'false'
    print 'FUZZING FOR VALUE: ', fuzzvalue
    for row in range(0, len(structure)):
      #print structure[row]['Name']
      if row == insertpoint and structure[row]['Type'] == 'B':
            fuzzed = 'true'
            size = structure[row]['Size']
            fuzzer = fuzz
            while (len(fuzzer) < size):
              fuzzer = fuzzer + fuzz
            fileinput = fileinput + fuzzer
      else:
        fileinput = fileinput + structure[row]['Default']
 
    print fileinput.encode('hex')
 
    if fuzz == '\x00':
      fuzz = 'null'
 
    if fuzzed == 'true':
      # Open a file
      fo = open("C:/Python27/EmanFuzzer/images/test" + fuzz + str(insertpoint) + ".bmp", "wb")
      fo.write(fileinput);
 
      # Close opend file
      fo.close()
 
 
 
  
##****************************************************************************  
  
refStructure = Structure()
GlobalStructure = refStructure.returnStructure()
refGenerator = Generator()
CombinationCount = refGenerator.returnCount()
 
 
print 'Test cases:', CombinationCount , '\n'
 
for x in range(0, CombinationCount):
  print refGenerator.returnNameAt(x)
  fuzzvalue = refGenerator.returnValueAt(x)
  iteratefuzz(GlobalStructure, fuzzvalue)