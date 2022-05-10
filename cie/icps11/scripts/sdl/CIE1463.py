import xml.etree.ElementTree as ET

sdl_results=[1,'N/A']

path="/Users/CIE/Documents/OWRBuild/binary/sdle.xml"

root = ET.parse(path).getroot()

if int(root.get('failures'))>0:

    for child in root.iter():
        if child.tag=='failure':
                failure_message=str(child.attrib.get('message'))
    sdl_results[1]=failure_message
    sdl_results[0]=2

print(str(sdl_results))
