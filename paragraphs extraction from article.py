import re
fa=open("DATA.txt","r")
l=[]
content=fa.read()
fa.seek(0)
paragraphs = re.search('(.+?\n\n|.+?$)',fa.read(),re.DOTALL)
fa.seek(0)
for match in re.finditer(r'(?s)((?:[^\n][\n]?)+)',fa.read()):
   l.append(content[match.start(): match.end()])

   
