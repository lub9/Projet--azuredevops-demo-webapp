using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.Authorization;

string subscriptionId = Environment.GetEnvironmentVariable("AZURE_SUBSCRIPTION_ID");
string principalId = Environment.GetEnvironmentVariable("AZURE_PRINCIPAL_OBJECT_ID");
string resourceGroup = "MyTestRG";
string storage = "mystoragetestrbac";

var credential = new DefaultAzureCredential();
var client = new ArmClient(credential);

string scope = $"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Storage/storageAccounts/{storage}";
string roleId = $"/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/roleDefinitions/ba92f5b4-2d11-453d-a403-e96b0029c9fe";

var collection = client.GetRoleAssignments(new ResourceIdentifier(scope));
string assignmentId = Guid.NewGuid().ToString();

var data = new RoleAssignmentData(roleId, principalId);
var result = await collection.CreateOrUpdateAsync(WaitUntil.Completed, assignmentId, data);

Console.WriteLine($"Role assigned: {result.Value.Id}");
