from xml.etree.ElementTree import parse
tree = parse('mybooks.xml')
for e in tree.findall('title'):
    print(e.text)
