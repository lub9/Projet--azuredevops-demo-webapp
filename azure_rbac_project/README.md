# Azure RBAC Sample Project

This project demonstrates how to manage Azure Role-Based Access Control (RBAC) using:

- Azure CLI
- Python SDK
- C# SDK

## 📂 Project Structure

```
azure-rbac-sample-project/
│
├── cli/
│   └── setup-rbac.sh
│
├── python/
│   ├── assign_rbac.py
│   ├── requirements.txt
│   └── README.md
│
├── csharp/
│   ├── AzureRbacSample.sln
│   └── AzureRbacSample/
│       ├── Program.cs
│       └── AzureRbacSample.csproj
│
└── README.md
```

---

## 🚀 Azure CLI Usage

The CLI script automates:
- Resource Group creation  
- Storage Account creation  
- Service Principal creation  
- RBAC assignment (Storage Blob Data Contributor)

Run:

```bash
bash cli/setup-rbac.sh
```

---

## 🐍 Python SDK Usage

Setup:

```bash
export AZURE_SUBSCRIPTION_ID="<subscription>"
export AZURE_PRINCIPAL_OBJECT_ID="<object id>"
pip install -r python/requirements.txt
```

Run:

```bash
python python/assign_rbac.py
```

---

## 💻 C# SDK Usage

Navigate to the project:

```bash
cd csharp/AzureRbacSample
dotnet run
```

---

## ✔ Requirements

- Azure CLI  
- .NET 8.0 SDK  
- Python 3.x  
- Azure subscription  
- Permissions to assign RBAC roles  

---



