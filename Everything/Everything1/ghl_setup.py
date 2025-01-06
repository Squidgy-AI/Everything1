import requests
import os


ghl_api_key = os.getenv("ghl_api_key")
print(ghl_api_key)

edit_view_user = 'pit-b20fcbd8-c6cf-4be8-b43f-b416878e3e0d'

url = "https://services.leadconnectorhq.com/users/"

payload = {
    "companyId": "ve9EPM428h8vShlRW1KT",
    "firstName": "Soma",
    "lastName": "Post",
    "email": "soma@test.com",
    "password": "soma123",
    "phone": "+17166044029",
    "type": "account",
    "role": "admin",
    "locationIds": ["a0DP9AlkkreShRQEelpt"],
    "permissions": {
        "campaignsEnabled": True,
        "campaignsReadOnly": False,
        "contactsEnabled": True,
        "workflowsEnabled": True,
        "workflowsReadOnly": True,
        "triggersEnabled": True,
        "funnelsEnabled": True,
        "websitesEnabled": False,
        "opportunitiesEnabled": True,
        "dashboardStatsEnabled": True,
        "bulkRequestsEnabled": True,
        "appointmentsEnabled": True,
        "reviewsEnabled": True,
        "onlineListingsEnabled": True,
        "phoneCallEnabled": True,
        "conversationsEnabled": True,
        "assignedDataOnly": False,
        "adwordsReportingEnabled": False,
        "membershipEnabled": False,
        "facebookAdsReportingEnabled": False,
        "attributionsReportingEnabled": False,
        "settingsEnabled": True,
        "tagsEnabled": True,
        "leadValueEnabled": True,
        "marketingEnabled": True,
        "agentReportingEnabled": True,
        "botService": False,
        "socialPlanner": True,
        "bloggingEnabled": True,
        "invoiceEnabled": True,
        "affiliateManagerEnabled": True,
        "contentAiEnabled": True,
        "refundsEnabled": True,
        "recordPaymentEnabled": True,
        "cancelSubscriptionEnabled": True,
        "paymentsEnabled": True,
        "communitiesEnabled": True,
        "exportPaymentsEnabled": True
    }
}
headers = {
    "Authorization": "Bearer {0}".format(ghl_api_key),
    "Version": "2021-07-28",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print(headers)

response = requests.post(url, json=payload, headers=headers)

print(response.json())