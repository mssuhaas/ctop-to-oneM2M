import requests
import json
import schedule
import time

XM2MORIGIN = 'admin:admin'


def get_ctop_data(ctop_url):
    response = requests.get(ctop_url)
    data = eval(response.json()["m2m:cin"]["con"])
    bindata = json.loads(data[0])
    binval = next(iter(bindata))
    x = json.loads(data[2:][1]) 
    ret = [binval] + bindata[binval][:2] + data[1:3] +x["V1"][:2]
    return ret


def post_om2m_data(om2m_path, data):
    try:
        payload = "{\n    \"m2m:cin\":{\n        \"lbl\":[\n            \"Node-1\"\n        ],\n        \"con\":" + data + "\n\n    }\n}\n\n"
        headers = {
        'X-M2M-Origin': XM2MORIGIN,
        'Content-Type': 'application/json;ty=4'
        }
        response = requests.post( om2m_url, headers=headers, data=payload )
        if response.status == 201:
            print("Node Created Successully")
    except Exception as e:
        print("Error! : " + e)

def get_and_post_data():
    data = get_ctop_data(url)
    post_om2m_data(om2m_path,data)


# schedule.every(10).minutes.do(get_and_post_data)
