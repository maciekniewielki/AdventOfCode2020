from dataclasses import dataclass

@dataclass
class Case:
    fr: int
    to: int
    letter: str
    passwd: list

# IO
cases = []
for line in open("input.txt").readlines():
    times, letter, passwd = line.split()
    fr, to = times.split("-")
    fr = int(fr)
    to = int(to)
    letter = letter[0]
    cases.append(Case(fr,to,letter,list(passwd)))


# 1st
print(sum(1 for c in cases if c.to >= c.passwd.count(c.letter) >= c.fr))

# 2nd
print(sum(1 for c in cases if (c.passwd[c.fr-1] == c.letter) ^ (c.passwd[c.to-1] == c.letter)))