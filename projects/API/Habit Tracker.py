# pixela

import requests


endpoint="https://pixe.la/v1/users"
parameter={"token":"asdfgh754jksssdf"
        ,"username":"maanav"
        ,"agreeTermsOfService":"yes"
        ,"notMinor":"yes"}

response=requests.post(url=endpoint,json=parameter)

print(response.text)
