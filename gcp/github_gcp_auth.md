## Setup Github OIDC Authentication with GCP

- Create a new workload Identity pool

```bash
gcloud iam workload-identity-pools create "k8s-pool" \
--project="${PROJECT_ID}" \
--location="global" \
--display-name="k8s Pool"
```
- Create a oidc identity provider for authenticating with Github

```bash
gcloud iam workload-identity-pools providers create-oidc "k8s-provider" \
--project="${PROJECT_ID}" \
--location="global" \
--workload-identity-pool="k8s-pool" \
--display-name="k8s provider" \
--attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.aud=assertion.aud" \
--issuer-uri="https://token.actions.githubusercontent.com"
```
- Create a service account with these permissions

```bash
roles/compute.admin
roles/container.admin
roles/container.clusterAdmin
roles/iam.serviceAccountTokenCreator
roles/iam.serviceAccountUser
roles/storage.admin
```
- Add IAM Policy bindings with Github repo, Identity provider and service account.

```bash
gcloud iam service-accounts add-iam-policy-binding "${SERVICE_ACCOUNT_EMAIL}" \
--project="${GCP_PROJECT_ID}" \
--role="roles/iam.workloadIdentityUser" \
--member="principalSet://iam.googleapis.com/projects/${GCP_PROJECT_NUMBER}/locations/global/workloadIdentityPools/k8s-pool/attribute.repository/${GITHUB_REPO}"
```


[repo-ref](https://github.com/KubeKode/DevOps-Projects/tree/Complete-CI/CD-with-Terraform-GKE)
[video](https://www.youtube.com/watch?v=-cp7GeQE2H0)