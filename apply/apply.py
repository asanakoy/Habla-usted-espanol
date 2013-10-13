import subprocess as sp
import math

def execute(cmd):
    return sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, shell=True).communicate()

test = open("spanish.txt.test.clean.utf-8", "r")
answer = open("answer.txt", "w")

def check(word):
    return word.isalpha()

for line in test:
    splitted = line.split()
    wordform = splitted[0]
    execute("echo " + wordform + "| flookup ../Espanol.bin > temp.log") 
    temp = open("temp.log", "r")
    nouns, verbs, adjectives = set(), set(), set()
    for row in temp:
        parts = row.split("+")
        print parts
        if len(parts) <= 1:
            continue
        if parts[1] == 'V' and check(parts[0]):
            verbs.add(parts[0])
        elif parts[1] == 'N' and check(parts[0]):
            nouns.add(parts[0])
        elif parts[1] == 'A' and check(parts[0]):
            adjectives.add(parts[0])
    best_noun, best_verb, best_adj = "","", ""
    has_noun, has_verb, has_adj = False, False, False
    if len(nouns) > 0:
        best_noun = min(nouns)
        has_noun = True
    if len(verbs) > 0:
        best_verb = min(verbs)
        has_verb = True
    if len(adjectives) > 0:
        best_adj = min(adjectives)
        has_adj = True
    print >> answer, wordform,

    full_count = 0
    if has_verb:
        print >> answer, best_verb + "+V",
        full_count += 1
    if has_noun:
        print >> answer, best_noun + "+N",
        full_count += 1;
    if has_adj and full_count < 2:
        print >> answer, best_adj + "+A",
    print >> answer, ""

