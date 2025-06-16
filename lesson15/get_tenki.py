import requests, os, platform, json
save_file = r'C:\Users\kkeigo\Desktop\天気.txt'
#api_url = 'https://api.aoikujira.com/tenki/week.php?fmt=ini&city=319'
api_url = 'https://api.aoikujira.com/tenki/week.php?fmt=json&city={city}'
city = '319'
tenki = json.loads(requests.get(api_url).text)
#print(tenki['319'])

#with open(save_file, 'wt', encoding='utf-8') as f:
with open(save_file, 'a', encoding='utf-8') as f:
    #f.write(tenki)
    #f.write(json.dumps(tenki))
    f.write(f"{tenki[city][0]['date']}:{ tenki['319'][0]['forecast']}")