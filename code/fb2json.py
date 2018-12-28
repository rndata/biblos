import xmltodict
import json

def fb2j(fi='data/bibliya.fb2', fo='data/biblos.json'):
    with open(fi, 'rb') as f:
        d = xmltodict.parse(f.read())

    d = json.dumps(d)
    
    with open(fo, 'w') as f:
        json.dump(d, f)

if __name__ == '__main__':
    fb2j()
