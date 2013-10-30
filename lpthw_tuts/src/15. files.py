__author__ = 'sushant'

print 'Enter file name '
filename = raw_input()
txt = open(filename)
text = txt.read()
print text