import os

import asyncio
from azure.identity.aio import ClientSecretCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

credential = ClientSecretCredential(
    os.getenv('tenant_id'),
    os.getenv('client_id'),
    os.getenv('client_secret')
)


# Key learnings 
# -Use test tenant
# -Use application permissions
# grant admin consent


scopes = ['User.Read']
auth_provider = AzureIdentityAuthenticationProvider(credential)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)
print(client)

async def get_user():
    try:
        user = await client.users_by_id('PattiF@r1gy.onmicrosoft.com').get()  #shem_ogumbe@r1gy.onmicrosoft.com
        print(user.display_name)



    except Exception as e:
        print(f"Error: {e.error.code}: {e.error.message}")


    
asyncio.run(get_user())
