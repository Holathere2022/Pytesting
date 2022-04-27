import xml.etree.ElementTree as ET
from datetime import timedelta, date

def UpdateXML(x,y): 
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    for item in root.findall('./REQUEST/TP'):
        for child in item:
            print(child.tag)
            if child.tag == 'DEPART':
                child.text = (date.today() + timedelta(days=x)).strftime("%Y-%m-%d")
            elif child.tag == 'RETURN':
                child.text = (date.today() + timedelta(days=y)).strftime("%Y-%m-%d")

    tree.write('output.xml')


if __name__ == '__main__':
    UpdateXML(10,30)
      
      
