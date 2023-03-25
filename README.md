# sample-flask-k8s
This repository contains a sample Flask application deployed on a Kubernetes cluster.

### ARGO CD

Retornar a URL da console do Argo CD:
```
kubectl get svc argocd-server -n argocd -o json | jq --raw-output '.status.loadBalancer.ingress[0].hostname'; echo
```
Retornar a senha da console do Argo CD:
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```
