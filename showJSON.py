#!/usr/bin/env python3

import requests
import json
import sys

if len(sys.argv) != 2:
   print('\nUsage: python3',sys.argv[0],'http://HOST.JSON\n\nor\n\t\bpython3',sys.argv[0],'file.json\n')
   sys.exit(1)

if 'http' in str(sys.argv[1]):
    url = str(sys.argv[1])
    jcode = requests.get(url).text

else:
    f = open(str(sys.argv[1]), 'r')
    jcode = f.read()

jshow = json.loads(jcode)
jshow = json.dumps(jshow, indent=4, sort_keys=True)

print(jshow)
