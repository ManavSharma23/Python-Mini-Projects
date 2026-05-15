# pixela

import requests


endpoint="https://pixe.la/v1/users"
parameter={"token":"asdfgh754jksssdf"
        ,"username":"maanav"
        ,"agreeTermsOfService":"yes"
        ,"notMinor":"yes"}

response=requests.post(url=endpoint,json=parameter)

print(response.text)

graph_endpoint="https://pixe.la/v1/users/maanav/graphs"
headers = {"X-USER-TOKEN": token}
response=requests.get(url=graph_endpoint,headers=headers)
graph_parameter={
        "id":"graph1",
        "name":"Racing Graph",
        "hours":"hrs",
        "type":"float",
        "color":"ajisai"
}

response=requests.post(url=graph_endpoint,json=graph_parameter,headers=headers)

