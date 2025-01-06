import requests
import webbrowser

# OAuth URL components

client_id = "673feeff6d29e38a913dc2b7-m3s5b8mt"
client_secret = "56468d3d-6927-48ab-8adc-0d8f22b4da90"

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

# Send a GET request with the parameters
response = requests.get(url, params=params)

# Print the response URL or handle the response
print(response.url)

response = requests.Request('GET', url, params=params).prepare()

# Open the URL in the default web browser
webbrowser.open(response.url)
# code = '42f64d06cdbb6b0d314a1610c47876690cefe4d7'

