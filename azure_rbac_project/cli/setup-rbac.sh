#!/bin/bash
set -e

RESOURCE_GROUP="MyTestRG"
LOCATION="eastus"
STORAGE="mystoragetestrbac"
APP_NAME="rbacTestApp"
ROLE="Storage Blob Data Contributor"

az group create -n $RESOURCE_GROUP -l $LOCATION

az storage account create   --name $STORAGE   --resource-group $RESOURCE_GROUP   --location $LOCATION   --sku Standard_LRS

SP=$(az ad sp create-for-rbac -n $APP_NAME --skip-assignment)
APP_ID=$(echo $SP | jq -r '.appId')
TENANT=$(echo $SP | jq -r '.tenant')
PASSWORD=$(echo $SP | jq -r '.password')

SCOPE=$(az storage account show   --resource-group $RESOURCE_GROUP   --name $STORAGE   --query id -o tsv)

az role assignment create   --assignee $APP_ID   --role "$ROLE"   --scope $SCOPE

echo "Service Principal Created:"
echo "App ID: $APP_ID"
echo "Tenant: $TENANT"
echo "Password: $PASSWORD"
echo "RBAC Role assigned successfully"
