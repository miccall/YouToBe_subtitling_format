import re
file = open("C:/Users/miccall/Desktop/a.txt")

current = 0 ;
miss = 4 
while 1:

    line = file.readline()
    current += 1  
    if (current + 1 ) % miss == 0 and current > 2 :
    	# print(line)
    	pattern = re.compile(r'</?\w+[^>]*>')
    	line = pattern.sub('',line)
    	print(line)
    	pass
    if not line:
        break
    pass

print(current)