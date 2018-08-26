import xml.etree.ElementTree as EI

tree = EI.parse("xmltest.xml")
root = tree.getroot()
print(root)
print(root.tag)

for child in root:
    print(child.tag,child.attrib)  #遍历每个标签
    for i in child:                #遍历每个标签内容
        print(i.tag,i.text)

for node in root.iter('year'):
    print(node.tag,node.text)
