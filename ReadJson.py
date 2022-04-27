import json
def UpdateJson(jsonFileName,elementToDelete):
    to_keep = []
    with open(jsonFileName, 'r') as ifile:
      data = json.load(ifile)
      for k, v in list(data.items()):
        if elementToDelete in k:
            data.pop(elementToDelete)
        elif v is not None and elementToDelete in v:
            for key in list(v):
                print(key)
                if elementToDelete == key:
                    if type(v) is list:
                        v.remove(key)
                    elif type(v) is dict:
                        v.pop(key)

    with open('output.json', 'w') as ofile:
        json.dump(data, ofile)

    #print(data)


if __name__ == '__main__':
    UpdateJson(r"C:\tmp\Python_exercises_QA_Engr (5)\Updated_Python_exercises_QA_Engr\test_payload.json",'spreadsheetName')


