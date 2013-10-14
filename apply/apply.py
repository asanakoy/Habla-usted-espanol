import re
import subprocess as sp
import math

def execute(cmd):
    return sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, shell=True).communicate()

inp = open("result.txt", "r")
answer = open("answer.txt", "w")

def check(word):
    return word.isalpha()

nouns, verbs, adjectives = set(), set(), set()
fcnt = 0

best_noun, best_verb, best_adj = "","", ""

has_noun, has_verb, has_adj = False, False, False
       
wordform =  ""

for line in inp:
        expr = re.compile(r'\+|\t|\n')
        parts = re.split(expr, line) 
        if len(parts) <= 2:
            if fcnt > 0:
                if len(nouns) > 0:
                    best_noun = min(nouns)
                    has_noun = True
                if len(verbs) > 0:
                    best_verb = min(verbs)
                    has_verb = True
                if len(adjectives) > 0:
                    best_adj = min(adjectives)
                    has_adj = True

                printstring = wordform

                full_count = 0
                if has_verb:
                        printstring += "\t"
                        printstring += best_verb + "+V"
                        full_count += 1
                if has_noun:
                        printstring += "\t"
                        printstring += best_noun + "+N"
                        full_count += 1;
                if has_adj and full_count < 2:
                        printstring += "\t"
                        printstring += best_adj + "+A"
                print >> answer, printstring 

            nouns, verbs, adjectives = set(), set(), set()
            fcnt += 1
            best_noun, best_verb, best_adj = "","", ""
            has_noun, has_verb, has_adj = False, False, False

        else :
            fcnt += 1
            wordform = parts[0]
            if parts[2] == 'V' and check(parts[1]):
                verbs.add(parts[1])
            elif parts[2] == 'N' and check(parts[1]):
                nouns.add(parts[1])
            elif parts[2] == 'A' and check(parts[1]):
                adjectives.add(parts[1])
            else:
                verbs.add(wordform)
    

#for line in inp:
#    splitted = line.split()
#    wordform = splitted[0]
#    execute("echo " + wordform + "| flookup ../Espanol.bin > temp.log") 
#    temp = open("temp.log", "r")
#    nouns, verbs, adjectives = set(), set(), set()
#    for row in temp:
#        expr = re.compile(r'\+|\t|\n')
#        parts = re.split(expr, row)
#        if len(parts) <= 1:
#            continue
        
