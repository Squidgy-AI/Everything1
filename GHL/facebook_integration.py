 ### ticket no #2861180


import requests
import webbrowser


client_id = "673feeff6d29e38a913dc2b7-m3s5b8mt"
client_secret = "56468d3d-6927-48ab-8adc-0d8f22b4da90"
'''
url = "https://marketplace.leadconnectorhq.com/oauth/chooselocation"
params = {
    "response_type": "code",
    "redirect_uri": "https://squidgy.ai/",
    "client_id": client_id,
    "scope": (
        "conversations/message.readonly conversations/message.write "
        "businesses.readonly businesses.write companies.readonly "
        "calendars.readonly calendars.write calendars/events.readonly "
        "calendars/events.write calendars/groups.readonly calendars/groups.write "
        "calendars/resources.readonly calendars/resources.write campaigns.readonly "
        "conversations.readonly conversations.write conversations/reports.readonly "
        "contacts.readonly contacts.write objects/schema.readonly objects/schema.write "
        "objects/record.readonly objects/record.write courses.write courses.readonly "
        "forms.readonly forms.write invoices.readonly invoices.write "
        "invoices/schedule.readonly invoices/schedule.write invoices/template.readonly "
        "invoices/template.write links.readonly lc-email.readonly links.write "
        "locations.write locations.readonly locations/customValues.readonly "
        "locations/customValues.write locations/customFields.readonly "
        "locations/customFields.write locations/tasks.readonly locations/tasks.write "
        "locations/tags.readonly locations/tags.write locations/templates.readonly "
        "medias.readonly medias.write funnels/redirect.readonly funnels/page.readonly "
        "funnels/funnel.readonly funnels/pagecount.readonly funnels/redirect.write "
        "oauth.write oauth.readonly opportunities.readonly opportunities.write "
        "payments/orders.readonly payments/orders.write payments/integration.readonly "
        "payments/integration.write payments/transactions.readonly payments/subscriptions.readonly "
        "payments/custom-provider.readonly payments/custom-provider.write products.readonly "
        "products.write products/prices.readonly products/prices.write "
        "products/collection.readonly products/collection.write saas/company.read "
        "saas/company.write saas/location.read saas/location.write snapshots.readonly "
        "snapshots.write socialplanner/oauth.readonly socialplanner/oauth.write "
        "socialplanner/post.readonly socialplanner/post.write socialplanner/account.readonly "
        "socialplanner/account.write socialplanner/csv.readonly socialplanner/csv.write "
        "socialplanner/category.readonly socialplanner/tag.readonly store/shipping.readonly "
        "store/shipping.write store/setting.readonly store/setting.write surveys.readonly "
        "users.readonly users.write workflows.readonly emails/builder.write "
        "emails/builder.readonly wordpress.site.readonly blogs/post.write "
        "blogs/post-update.write blogs/check-slug.readonly blogs/category.readonly "
        "blogs/author.readonly socialplanner/category.write socialplanner/tag.write"
    )
}

response = requests.Request('GET', url, params=params).prepare()

webbrowser.open(response.url)
'''

'''
url = "https://services.leadconnectorhq.com/oauth/token"

client_id = "673feeff6d29e38a913dc2b7-m3s5b8mt"
client_secret = "56468d3d-6927-48ab-8adc-0d8f22b4da90"

payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "authorization_code",
    "code": "e5ead5ba9064e6d8a7cb45ff53d65d2c3b09786f"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
'''

access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoQ2xhc3MiOiJMb2NhdGlvbiIsImF1dGhDbGFzc0lkIjoibEJQcWdCb3dYMUNzakhheTEyTFkiLCJzb3VyY2UiOiJJTlRFR1JBVElPTiIsInNvdXJjZUlkIjoiNjczZmVlZmY2ZDI5ZTM4YTkxM2RjMmI3LW0zczViOG10IiwiY2hhbm5lbCI6Ik9BVVRIIiwicHJpbWFyeUF1dGhDbGFzc0lkIjoibEJQcWdCb3dYMUNzakhheTEyTFkiLCJvYXV0aE1ldGEiOnsic2NvcGVzIjpbImNvbnZlcnNhdGlvbnMvbWVzc2FnZS5yZWFkb25seSIsImNvbnZlcnNhdGlvbnMvbWVzc2FnZS53cml0ZSIsImJ1c2luZXNzZXMucmVhZG9ubHkiLCJidXNpbmVzc2VzLndyaXRlIiwiY29tcGFuaWVzLnJlYWRvbmx5IiwiY2FsZW5kYXJzLnJlYWRvbmx5IiwiY2FsZW5kYXJzLndyaXRlIiwiY2FsZW5kYXJzL2V2ZW50cy5yZWFkb25seSIsImNhbGVuZGFycy9ldmVudHMud3JpdGUiLCJjYWxlbmRhcnMvZ3JvdXBzLnJlYWRvbmx5IiwiY2FsZW5kYXJzL2dyb3Vwcy53cml0ZSIsImNhbGVuZGFycy9yZXNvdXJjZXMucmVhZG9ubHkiLCJjYWxlbmRhcnMvcmVzb3VyY2VzLndyaXRlIiwiY2FtcGFpZ25zLnJlYWRvbmx5IiwiY29udmVyc2F0aW9ucy5yZWFkb25seSIsImNvbnZlcnNhdGlvbnMud3JpdGUiLCJjb252ZXJzYXRpb25zL3JlcG9ydHMucmVhZG9ubHkiLCJjb250YWN0cy5yZWFkb25seSIsImNvbnRhY3RzLndyaXRlIiwib2JqZWN0cy9zY2hlbWEucmVhZG9ubHkiLCJvYmplY3RzL3NjaGVtYS53cml0ZSIsIm9iamVjdHMvcmVjb3JkLnJlYWRvbmx5Iiwib2JqZWN0cy9yZWNvcmQud3JpdGUiLCJjb3Vyc2VzLndyaXRlIiwiY291cnNlcy5yZWFkb25seSIsImZvcm1zLnJlYWRvbmx5IiwiZm9ybXMud3JpdGUiLCJpbnZvaWNlcy5yZWFkb25seSIsImludm9pY2VzLndyaXRlIiwiaW52b2ljZXMvc2NoZWR1bGUucmVhZG9ubHkiLCJpbnZvaWNlcy9zY2hlZHVsZS53cml0ZSIsImludm9pY2VzL3RlbXBsYXRlLnJlYWRvbmx5IiwiaW52b2ljZXMvdGVtcGxhdGUud3JpdGUiLCJsaW5rcy5yZWFkb25seSIsImxjLWVtYWlsLnJlYWRvbmx5IiwibGlua3Mud3JpdGUiLCJsb2NhdGlvbnMud3JpdGUiLCJsb2NhdGlvbnMucmVhZG9ubHkiLCJsb2NhdGlvbnMvY3VzdG9tVmFsdWVzLnJlYWRvbmx5IiwibG9jYXRpb25zL2N1c3RvbVZhbHVlcy53cml0ZSIsImxvY2F0aW9ucy9jdXN0b21GaWVsZHMucmVhZG9ubHkiLCJsb2NhdGlvbnMvY3VzdG9tRmllbGRzLndyaXRlIiwibG9jYXRpb25zL3Rhc2tzLnJlYWRvbmx5IiwibG9jYXRpb25zL3Rhc2tzLndyaXRlIiwibG9jYXRpb25zL3RhZ3MucmVhZG9ubHkiLCJsb2NhdGlvbnMvdGFncy53cml0ZSIsImxvY2F0aW9ucy90ZW1wbGF0ZXMucmVhZG9ubHkiLCJtZWRpYXMucmVhZG9ubHkiLCJtZWRpYXMud3JpdGUiLCJmdW5uZWxzL3JlZGlyZWN0LnJlYWRvbmx5IiwiZnVubmVscy9wYWdlLnJlYWRvbmx5IiwiZnVubmVscy9mdW5uZWwucmVhZG9ubHkiLCJmdW5uZWxzL3BhZ2Vjb3VudC5yZWFkb25seSIsImZ1bm5lbHMvcmVkaXJlY3Qud3JpdGUiLCJvYXV0aC53cml0ZSIsIm9hdXRoLnJlYWRvbmx5Iiwib3Bwb3J0dW5pdGllcy5yZWFkb25seSIsIm9wcG9ydHVuaXRpZXMud3JpdGUiLCJwYXltZW50cy9vcmRlcnMucmVhZG9ubHkiLCJwYXltZW50cy9vcmRlcnMud3JpdGUiLCJwYXltZW50cy9pbnRlZ3JhdGlvbi5yZWFkb25seSIsInBheW1lbnRzL2ludGVncmF0aW9uLndyaXRlIiwicGF5bWVudHMvdHJhbnNhY3Rpb25zLnJlYWRvbmx5IiwicGF5bWVudHMvc3Vic2NyaXB0aW9ucy5yZWFkb25seSIsInBheW1lbnRzL2N1c3RvbS1wcm92aWRlci5yZWFkb25seSIsInBheW1lbnRzL2N1c3RvbS1wcm92aWRlci53cml0ZSIsInByb2R1Y3RzLnJlYWRvbmx5IiwicHJvZHVjdHMud3JpdGUiLCJwcm9kdWN0cy9wcmljZXMucmVhZG9ubHkiLCJwcm9kdWN0cy9wcmljZXMud3JpdGUiLCJwcm9kdWN0cy9jb2xsZWN0aW9uLnJlYWRvbmx5IiwicHJvZHVjdHMvY29sbGVjdGlvbi53cml0ZSIsInNhYXMvY29tcGFueS5yZWFkIiwic2Fhcy9jb21wYW55LndyaXRlIiwic2Fhcy9sb2NhdGlvbi5yZWFkIiwic2Fhcy9sb2NhdGlvbi53cml0ZSIsInNuYXBzaG90cy5yZWFkb25seSIsInNuYXBzaG90cy53cml0ZSIsInNvY2lhbHBsYW5uZXIvb2F1dGgucmVhZG9ubHkiLCJzb2NpYWxwbGFubmVyL29hdXRoLndyaXRlIiwic29jaWFscGxhbm5lci9wb3N0LnJlYWRvbmx5Iiwic29jaWFscGxhbm5lci9wb3N0LndyaXRlIiwic29jaWFscGxhbm5lci9hY2NvdW50LnJlYWRvbmx5Iiwic29jaWFscGxhbm5lci9hY2NvdW50LndyaXRlIiwic29jaWFscGxhbm5lci9jc3YucmVhZG9ubHkiLCJzb2NpYWxwbGFubmVyL2Nzdi53cml0ZSIsInNvY2lhbHBsYW5uZXIvY2F0ZWdvcnkucmVhZG9ubHkiLCJzb2NpYWxwbGFubmVyL3RhZy5yZWFkb25seSIsInN0b3JlL3NoaXBwaW5nLnJlYWRvbmx5Iiwic3RvcmUvc2hpcHBpbmcud3JpdGUiLCJzdG9yZS9zZXR0aW5nLnJlYWRvbmx5Iiwic3RvcmUvc2V0dGluZy53cml0ZSIsInN1cnZleXMucmVhZG9ubHkiLCJ1c2Vycy5yZWFkb25seSIsInVzZXJzLndyaXRlIiwid29ya2Zsb3dzLnJlYWRvbmx5IiwiZW1haWxzL2J1aWxkZXIud3JpdGUiLCJlbWFpbHMvYnVpbGRlci5yZWFkb25seSIsIndvcmRwcmVzcy5zaXRlLnJlYWRvbmx5IiwiYmxvZ3MvcG9zdC53cml0ZSIsImJsb2dzL3Bvc3QtdXBkYXRlLndyaXRlIiwiYmxvZ3MvY2hlY2stc2x1Zy5yZWFkb25seSIsImJsb2dzL2NhdGVnb3J5LnJlYWRvbmx5IiwiYmxvZ3MvYXV0aG9yLnJlYWRvbmx5Iiwic29jaWFscGxhbm5lci9jYXRlZ29yeS53cml0ZSIsInNvY2lhbHBsYW5uZXIvdGFnLndyaXRlIl0sImNsaWVudCI6IjY3M2ZlZWZmNmQyOWUzOGE5MTNkYzJiNyIsImNsaWVudEtleSI6IjY3M2ZlZWZmNmQyOWUzOGE5MTNkYzJiNy1tM3M1YjhtdCJ9LCJpYXQiOjE3MzQwMDUzNjYuMzg3LCJleHAiOjE3MzQwOTE3NjYuMzg3fQ.c0vrfqgrPj4cZZoWrMq4dM-Qt-GL3Eh8buO2RBn3oteyLJLh4XsOrtOSRf7tg6ZV6HilrQZmzqUwAI8q73PeRNZ-z2SkkjkhNuoYMZKjWvY0atY0jmsxyApdX9amzagA2Gmz1Um656YVSFrPLt3Pq89pL_mYYj_h0_YwAWf09R2YhJukR5OTDtIXaULan0M4vDQBWyh2DvhVxyCrlBn1pckaENdDc0UZL3bn-ZtFrFLAM61QRq0zx9gQbTKxHQBYjhtkbUVnZZxkrrPBHTEyg-1-_JUXUPj2ukYkK9eGMRxvsFKlDtOzaAXDVrhQRWDZ9X_WxliARbO9C5FvdkXiCUFnsr1WuX9SKqr_A4F_qHICFvm2RZyorfoEBcmfitu9BhwF6y7IRMpe02emuX3ohk_Hm-ogrviHZq5tmEGUeq7AAoDr6YQ4gQ05wNPZGyRIpwAMvUKW1McGCqC4qEsAZafjUnFKM4uNzNUPb2gLKo3yGxqP7REG6x9AGsYFW1RAiGvsPBmtgNG-bgbodnJUOEowJTbHMXjdYGR0OwOw7NoHRL4wDMueAwVHrGxM4F6BzEEmsAO76XQi3-xWcUGGdI_ybakuHN6Kka-AZOeGHLQB0ha2zbddTKR-yHVHZ3C6oy2sULhAFhXFEpcPBgw8vbqx6QbNsECaqGij9heejP0"

sub_account_id = 'lBPqgBowX1CsjHay12LY'
sub_account_user_id = 'aZ0n4etrNCEB29sona8M'

# Construct the URL
url = "https://services.leadconnectorhq.com/social-media-posting/oauth/facebook/start"

querystring = {"locationId":sub_account_id,"userId":sub_account_user_id, "page":"integration", "reconnect": "true"}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Version": "2021-07-28",
    "Accept": "application/json"
}

response1 = requests.Request('GET', url, headers=headers, params=querystring).prepare()
print("**************************************************")
print(response1.url)

# Open the cleaned URL in the browser
webbrowser.open(response1.url)

