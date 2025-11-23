from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
import os

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
resource_group = "MyTestRG"
storage_account = "mystoragetestrbac"
principal_id = os.environ["AZURE_PRINCIPAL_OBJECT_ID"]

credential = DefaultAzureCredential()

role_def_id = (
    f"/subscriptions/{subscription_id}"
    "/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe"
)

scope = (
    f"/subscriptions/{subscription_id}"
    f"/resourceGroups/{resource_group}"
    f"/providers/Microsoft.Storage/storageAccounts/{storage_account}"
)

auth_client = AuthorizationManagementClient(credential, subscription_id)
assignment_id = "12345678-1234-1234-1234-" + os.urandom(4).hex()

assignment = auth_client.role_assignments.create(
    scope=scope,
    role_assignment_name=assignment_id,
    parameters={
        "role_definition_id": role_def_id,
        "principal_id": principal_id,
    },
)

print("Role Assigned:", assignment.id)
