# 🚀 Databricks CI/CD with Declarative Automation Bundles

An end-to-end **Databricks CI/CD implementation** using **Declarative Automation Bundles (DABs), GitHub Actions, GitHub, and Databricks**.

This project demonstrates an automated **Dev → Production deployment workflow** for a PySpark ETL workload.

---

## 📌 Project Overview

The goal of this project is to implement a practical CI/CD workflow for Databricks workloads.

Whenever code is pushed to GitHub, GitHub Actions automatically:

1. Checks out the repository
2. Installs the Databricks CLI
3. Detects the deployment environment
4. Validates the Databricks bundle
5. Deploys the bundle
6. Executes the Customer ETL job

The project supports separate **Development** and **Production** targets.

---

## 🏗️ Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ├── dev branch
    │      │
    │      ▼
    │   GitHub Actions
    │      │
    │      ├── Bundle Validation
    │      ├── Dev Deployment
    │      └── ETL Job Execution
    │
    └── main branch
           │
           ▼
       GitHub Actions
           │
           ├── Bundle Validation
           ├── Production Deployment
           └── ETL Job Execution
                    │
                    ▼
                Databricks
```

---

## 🔄 CI/CD Workflow

### Development

Changes pushed to the `dev` branch trigger:

```text
Push to dev
     ↓
GitHub Actions
     ↓
Databricks Bundle Validate
     ↓
Deploy to Dev
     ↓
Run Customer ETL Job
```

### Production

Changes promoted to the `main` branch trigger:

```text
Push / Merge to main
        ↓
GitHub Actions
        ↓
Databricks Bundle Validate
        ↓
Deploy to Production
        ↓
Run Customer ETL Job
```

This provides environment-specific deployments using the same Databricks bundle.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Databricks | Data processing and job execution |
| PySpark | ETL transformations |
| Declarative Automation Bundles | Databricks resource deployment |
| GitHub | Source control |
| GitHub Actions | CI/CD automation |
| Databricks CLI | Bundle validation, deployment and execution |
| YAML | Bundle and workflow configuration |

---

## 📂 Project Structure

```text
databricks-cicd-dab-project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── resources/
│   └── customer_job.yml
│
├── customer_etl.py
├── databricks.yml
└── README.md
```

### Key Files

**`customer_etl.py`**  
PySpark notebook source containing the sample customer ETL transformation.

**`resources/customer_job.yml`**  
Defines the Databricks Customer ETL job resource.

**`databricks.yml`**  
Defines the Databricks bundle and Dev/Production deployment targets.

**`.github/workflows/deploy.yml`**  
GitHub Actions workflow responsible for automated validation, deployment, and job execution.

---

## ⚙️ Environment Configuration

The bundle contains two deployment targets:

```yaml
targets:
  dev:
    mode: development
    default: true

  prod:
    mode: production
```

The GitHub Actions workflow automatically selects the appropriate target based on the branch:

```text
dev  → dev target
main → prod target
```

---

## 🔐 GitHub Secrets

Databricks authentication credentials are stored securely using **GitHub Actions Secrets**.

Required secrets:

```text
DATABRICKS_HOST
DATABRICKS_TOKEN
```

Credentials are not hardcoded in the repository.

---

## 🧪 Customer ETL Pipeline

The sample PySpark pipeline:

- Creates customer data
- Applies DataFrame transformations
- Standardizes customer names
- Segments customers based on total spend
- Executes automatically through a Databricks job

Example segmentation:

```text
total_spend >= 40000 → Premium
total_spend < 40000  → Standard
```

---

## 🚀 Automated Deployment

The workflow uses Databricks CLI commands such as:

```bash
databricks bundle validate -t <target>
databricks bundle deploy -t <target>
databricks bundle run customer_etl_job -t <target>
```

The deployment target is selected dynamically by GitHub Actions.

---

## 🌿 Branch Strategy

```text
feature branch
      │
      ▼
     dev
      │
   Testing
      │
      ▼
 Pull Request
      │
      ▼
     main
      │
      ▼
 Production
```

This separates development work from production deployments.

---

## ✅ CI/CD Validation

The pipeline has been successfully tested for:

- Databricks bundle validation
- Development deployment
- Production deployment
- Automated Customer ETL job execution
- GitHub Actions integration
- Branch-based environment selection
- Dev/Production bundle targets

---

## 🎯 Key Learnings

This project demonstrates practical experience with:

- Databricks CI/CD
- Declarative Automation Bundles
- GitHub Actions
- PySpark ETL development
- Environment-specific deployments
- Git branching and pull requests
- Automated Databricks job execution
- Secure credential management

---

## 👨‍💻 Author

**Syed Saud Alam**

Data Engineer | AI Engineer

GitHub: `syedsaud15`

---

## 📌 Project Status

**Completed ✅**

Both Development and Production CI/CD pipelines have been successfully deployed and tested.
