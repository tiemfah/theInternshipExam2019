import xmltodict, json, os


xml_string = open('city.xml').read()
json_temp = xmltodict.parse(xml_string)
json_temp = json.dumps(json_temp)
path = os.getcwd() + '/xmltojson.json'
open(path, "w+").write(json_temp)
