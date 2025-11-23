# Projet--azuredevops-demo-webapp

# Azure DevOps CI/CD Demo – .NET 8 Web App → Azure App Service

This project is a simple **.NET 8 minimal API** used to demonstrate a full **CI/CD pipeline in Azure DevOps**, including:

- Continuous Integration (build, restore, test, publish)
- Continuous Deployment to **Azure App Service**
- Multi-stage YAML pipelines
- Unit testing with xUnit

---

## 📁 Project Structure

```
azuredevops-demo-webapp/
│
├── src/
│   └── WebApp/
│       ├── Program.cs
│       └── WebApp.csproj
│
├── tests/
│   └── WebApp.Tests/
│       ├── SampleTests.cs
│       └── WebApp.Tests.csproj
│
└── azure-pipelines.yml
```

---

## 🚀 Application Overview

The app exposes a simple endpoint:

```
GET /
```

Returns:

```
Hello from Azure DevOps CI/CD!
```

This keeps the project lightweight and perfect for DevOps demos.

---

## 🧪 Unit Tests

xUnit tests are included under:

```
tests/WebApp.Tests
```

The sample test always passes, ensuring the CI pipeline includes real test validation.

---

## 🔧 Azure DevOps Pipeline

The pipeline performs:

### **CI Stage**
- Restore NuGet packages  
- Build the .NET project  
- Run unit tests  
- Publish build artifacts  

### **CD Stage**
- Download artifact  
- Deploy the app to Azure App Service  

You only need to configure:
- **Azure Service Connection**
- **App Service Name**

Then update these in `azure-pipelines.yml`:

```yaml
azureSubscription: "<YOUR-SERVICE-CONNECTION>"
appName: "<YOUR-APP-SERVICE-NAME>"
```

---

## ☁️ Azure Resources Required

Before running the pipeline, create:

- Resource Group  
- App Service Plan  
- App Service (.NET stack or Linux container)  

---

## 📦 How to Run Locally

```bash
cd src/WebApp
dotnet run
```

Visit:

```
http://localhost:5000/
```

---

## 🛠️ How to Deploy

Push the project to **GitHub** or **Azure Repos**, then Azure DevOps will automatically:

1. Trigger CI on each commit  
2. Build → Test → Publish  
3. Deploy to Azure  

---

## 🏷️ Purpose

This repository is ideal for:

- Azure DevOps training
- CI/CD demos
- LinkedIn posts
- Interview preparation
- Portfolio projects  

---

## 📜 License

MIT License – free to use and modify.
