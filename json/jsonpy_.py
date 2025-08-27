import json


pythonValue = {'isCat': True,'miceCaught': 0,'name':'Zophie','felineIQ':None}

stringofJsonData = json.dumps(pythonValue)
print(stringofJsonData)