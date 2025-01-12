import xml.etree.ElementTree as ET
input = """<stuff>
       <users>00
          <user x="2">
            <id>001</id>
            <name>Balaji</name>
          </user>
          <user x = "7">
            <id>009</id>
            <name>Shyam</name>
          </user>
       </users>
    </stuff>"""
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')  #this is a list of users
print('User Count:',len(lst))
for item in lst:
    print('Name:',item.find('name').text)
    print('Id:',item.find('id').text)
    print('Attribute:',item.get("x"))
