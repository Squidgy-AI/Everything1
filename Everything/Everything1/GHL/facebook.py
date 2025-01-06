import requests
import webbrowser
Company_Id = 'lp2p1q27DrdGta1qGDJd'
Agency_Api_Key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55X2lkIjoibHAycDFxMjdEcmRHdGExcUdESmQiLCJ2ZXJzaW9uIjoxLCJpYXQiOjE3MzE3NzMzOTIzNTgsInN1YiI6Ik11VklrS3NEVm12YnRTUlliTzRiIn0.2PIUrvtQYpmKxQXoss1IV9vdIU1VnmbDHcpFw2dodLo'
Relationship_Id = '0-099-130'
Agency_Access_Key = 'pit-ad700aa3-8481-4cff-b555-bcaac7532592'
nescafe_id = '6ZHPyo1FRlZNBGzH5szG'
maggie_id = 'Fj1JPxueiId1Ki15fZZA'
kitkat_id = 'kmfwpeEjk5QjgGVdD4Su'
Nestle_Api_Key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6ImxCUHFnQm93WDFDc2pIYXkxMkxZIiwidmVyc2lvbiI6MSwiaWF0IjoxNzMxOTkyNDg3MDU0LCJzdWIiOiJhWjBuNGV0ck5DRUIyOXNvbmE4TSJ9.czCh27fEwqxW4KzDx0gVbYcpdtcChy_31h9SoQuptAA'
Nestle_access_token = 'pit-98e16ccd-8c1e-4e6f-a96d-57ef6cb2cf62'
sub_account_id = 'lBPqgBowX1CsjHay12LY'
kitkat_id = 'kmfwpeEjk5QjgGVdD4Su'
full_sub_account_access = 'pit-919acc3c-591e-4a60-a352-532136cc0d53'

calendar_id1 = 'nNKMeKxstubPEDQHnOW7'
sub_account_user_id = 'aZ0n4etrNCEB29sona8M'
client_id = "673feeff6d29e38a913dc2b7-m3s5b8mt"
client_secret = "56468d3d-6927-48ab-8adc-0d8f22b4da90"



# Construct the URL
url = f"https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start"

querystring = {"locationId":sub_account_id,"userId":sub_account_user_id, "page":"integration", "reconnect": "true"}

headers = {
    "Authorization": f"Bearer {full_sub_account_access}",
    "Version": "2021-07-28",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

print(response)

'''
https://www.facebook.com/login.php?
skip_api_login=1
&api_key=390181264778064&
kid_directed_site=0&
app_id=390181264778064&signed_next=1
&next=https://www.facebook.com/dialog/oauth?response_type=code&client_id=390181264778064&redirect_uri=https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/finish&scope=email,pages_show_list,pages_read_engagement,pages_manage_metadata,pages_manage_posts,pages_manage_engagement,pages_read_user_content,business_management,public_profile,read_insights&state=lBPqgBowX1CsjHay12LY,6ZHPyo1FRlZNBGzH5szG,undefined,undefined,undefined,undefined,undefined&ret=login&fbapp_pres=0&logger_id=752fc3b0-c36d-4d1a-aa60-5d7f6a7cb889&tp=unspecified&cancel_url=https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/finish?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=lBPqgBowX1CsjHay12LY,6ZHPyo1FRlZNBGzH5szG,undefined,undefined,undefined,undefined,undefined#_=_
'''


# Get the final redirected URL
redirected_url = response.url


response1 = requests.Request('GET', url, headers=headers, params=querystring).prepare()

webbrowser.open(response1.url)

print("Redirected URL:", response1.url)




"""
url = "https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start"

querystring = {"locationId":sub_account_id,"userId":nescafe_id}

headers = {
    "Authorization": f"Bearer {full_sub_account_access}",
    "Version": "2021-07-28",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)
"""

"""
import requests

url = "https://services.leadconnectorhq.com/social-media-posting/oauth/google/start"

querystring = {"locationId":sub_account_id,"userId":nescafe_id}

headers = {
    "Authorization": f"Bearer {full_sub_account_access}",
    "Version": "2021-07-28",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

with open("response.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response written to response.txt")
"""

"""
curl --request GET --url 'https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start?locationId=lBPqgBowX1CsjHay12LY&userId=6ZHPyo1FRlZNBGzH5szG' --header 'Accept: application/json' --header 'Authorization: Bearer pit-919acc3c-591e-4a60-a352-532136cc0d53' --header 'Version: 2021-07-28'

"""