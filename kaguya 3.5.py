import base64
import time
from urllib.request import build_opener

opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
pastebin = opener.open('https://pastebin.com/raw/ZQ8C8su2').read()
pastebin = pastebin.decode("utf-8") 
pastebin=pastebin.split('\r\n')
x=0
print("Kaguya Wants to be Confessed To: The Geniuses' War of Love and Brains\nかぐや様は告らせたい　～天才たちの恋愛頭脳戦～\nKaguya-sama wa Kokurasetai - Tensaitachi no Renai Zunousen\n\n")
line=0

print("Chapter list:\n-------------")
while x<len(pastebin):
    print(pastebin[x].split(' -')[0])
    x+=1
print("-------------\n\nInput the number of the chapter that you wish to download (Example: 50), or a range of chapters (Example: 1-43).")
raw=input("Chapter(s): ")
x=0

if raw.rfind('-')!=-1:
    start=raw.split('-')[0]
    end=raw.split('-')[1]
else:
    start=raw
    end=raw

while True:
    try:
      while float(start)<=float(end):
        if start.rfind('.0')!=-1:
            start=start.split('.0')[0]
        while x<len(pastebin):
            if pastebin[x].lower().rfind("kaguya"+start+" ")!= -1:
                line = pastebin[x]
                print('Downloading...')
            x+=1

        if line != 0:
            response = opener.open(line.split('- ')[1].split(' ')[0])
            response2 = opener.open(line.split('- ')[1].split(' ')[1])
            response3 = opener.open(line.split('- ')[1].split(' ')[2])
            with open('Kaguya'+start+'.zip', 'wb') as f:
                f.write(bytearray(base64.b64decode(response.read()+response2.read()+response3.read())))
            print('Successfully created Kaguya'+start+'.zip!')
        else:

            if start==end:
                print('Chapter '+raw+" not uploaded.")
        line=0
        start=str(float(start)+0.5)
        x=0
    except ValueError:
      print("Cannot convert", start, "to a string, a decimal number.\n")
      print("Input the number of the chapter that you wish to download (Example: 50.5), or a range of chapters (Example: 20-53).")
      raw=input("Chapter(s): ")
      continue

print("Finished downloading all chapters!")
