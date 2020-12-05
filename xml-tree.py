#this library is used to parse the xml format files
import xml.etree.ElementTree as ET
#xml format file:
data = """
   <person>
    <name>Balaji</name>
    <phone type="int1">
      9182698988
      </phone>
      <email hide="yes"/>
    </person> """
#below the data which was a string type changed to tree so that we can extract nodes from it
tree = ET.fromstring(data)
print("Name:",tree.find('name').text)
print("Attr:",tree.find('email').get("hide"))


print(type(tree))
print(type(data))