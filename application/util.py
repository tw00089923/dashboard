

def sort_value_tojson(data,keys,values,reversed=True):
    '''
    
    '''
    is_list = isinstance(data,list)
    origin_dict = {}
    if is_list :
        for i in data:
            # String -> String
            key = getattr(i,keys) 
            # String -> float 
            value = round(float(getattr(i,values)),2)
            if key in origin_dict  :
                origin_dict[key].append(value)
            else :
                origin_dict[key] = [value]
        # tuple -> sorted : ("Example", float(value) )
        sorted_value = sorted(origin_dict.items(),key=lambda x:x[1],reverse=reversed)
        # Rank 
        return { x :str(round(float(sum(y)/len(y)),2)) for x,y in sorted_value  } 
    else:
        return {"message":"false"}


import requests 
from application.models import User, Task, Sensor, CwbModel

def getcwbweather():
    # opendata Cwb api 
    auth = "CWB-AFE4E688-3773-4D4A-8AF6-38D58FFC4AE8"
    dataid= "F-C0032-001"
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/" + dataid + "?Authorization=" + auth
    r = requests.get(url)
    if r.status_code == 200 :
        answer = False
        json = r.json()
        location = json["records"]["location"]
        if answer:
            for i in location:
                for j in i["weatherElement"]: 
                    for k in j["time"]:
                        locationName = i.get("locationName",None)
                        elementName = j.get("elementName",None)
                        startTime = k.get("startTime",None)
                        endTime = k.get("endTime",None)
                        parameterName = k["parameter"].get("parameterName",None)
                        parameterValue = k["parameter"].get("parameterValue",None)
                        parameterUnit =  k["parameter"].get("parameterUnit",None)
                        cwbmodel = CwbModel(
                            locationName=locationName,
                            elementName=elementName,
                            startTime=datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S"),
                            endTime=datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S"),
                            parameterName=parameterName,
                            parameterUnit=parameterUnit,
                            parameterValue=parameterValue,
                            )
                        cwbmodel.save_to_db()
                        #2018-09-17 06:00:00


def save_data(data,update=False):
    '''
    Data isinstant Model
    '''
    if not update :
        try :
            data.save_to_db()
        except Exception as e:
            print(e)
    else :
        print("Command rejected!!")


