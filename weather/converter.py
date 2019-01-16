# needed all module to function
import xmltodict, json, os

#  ask for file name
xml_file = input('xml file name(DO NOT INCLUDE .xml): ')
#  open and read file
xml_string = open(f'{xml_file}.xml').read()
#  parsing from xml format to json format in string
json_temp = xmltodict.parse(xml_string)
json_temp = json.dumps(json_temp, indent=4, sort_keys=True)
#  creating a .json file
path = os.getcwd() + '/xmltojson.json'
open(path, "w+").write(json_temp)
#
print(f'{xml_file}.json')