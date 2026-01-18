# 段詞系統
from ckip_transformers import __version__
from ckip_transformers.nlp import CkipWordSegmenter
import requests
import json
import time

url = 'https://graph.facebook.com/v24.0/me/posts?access_token='
token = 'EAAbmrF1wdnUBQTtgDxIKJkKjZCYwHV0F6Tlw7umsDqfc11xCp0AH2Y0mZBHF9ee3qApaARdV0yczw2o09HgKqBWZAfpi3wtjumwp9EW2NFtrfUkTfb8qJ2SWUCPZAV183yGRiTsVUyONbggXXrPHSobLAqm0lKJPHUTYAW6Pn3MUAuiTsyB3Nkqsi3VflQLLSQ4Sg9UBZCrAANTuQAa6ltoOe6ozzXWK7DRkQod2ZAXd4VsbbZAIZBbeFhI6N873IherZA3QBTBS3QxZAEOR3e74ZANDnnC5f9ISQIw9VZAQjxtKlsOZAfxWBk3oSf1MrcasbzCzZBvXQZD'
params = {'access_token': token}
res = requests.get( url, params=params, timeout = 5 )
jd = json.loads( res.text )

ws_driver = CkipWordSegmenter(model = "albert-base", device = -1) # -1確保使用ＣＰＵ
cor = []
for post in jd['data']:
    if 'message' in post:
        # print( post[ "message" ] )
        cor += ws_driver([post['message']])[0]

page = 0
while page < 10 and jd['data'] != []:
    page += 1
    print( f'Page: {page}' )
    time.sleep( 1 )
    res = requests.get( jd['paging']['next'] )
    jd = json.loads( res.text )
    for post in jd['data']:
        if 'message' in post:
            cor += ws_driver([post['message']])[0]

# print(cor)
dicor = {}
for c in cor:
    if c in dicor:
        dicor[c] += 1
    else:
        dicor[c] = 1
print( dicor )
for e in dicor.items():
    if "  " not in e[0]:
        if "/n" not in e[0]:
            print( e[0], e[1] )




