import xml.etree.ElementTree as ET, json

tree = ET.parse('city.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.attrib, subchild.text)
    print()