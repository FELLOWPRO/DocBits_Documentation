# Documentation k9s runners

The public documentation repository uses a dedicated `k9s` scale set in the
`arc-docs` namespace of the existing dev-stage runner cluster. The shared
Default runner group excludes public repositories, so changing `runs-on` alone
would leave these jobs queued indefinitely.

The **DocBits Documentation** runner group (organization group ID 4) permits
only this repository and the three workflow files on `main` listed in
`group.json`. Pull request and fork workflows are not allowed. Jobs explicitly
select both this group and the `k9s` label.

`k9s-values.yaml` records the installed ARC chart values, including the
existing runner image and pod configuration. The scale set has zero idle
runners and at most three concurrent runners. The existing shared k9s and
k9s-high scale sets are unchanged.

To reconcile the installation, first ensure the `github-app-secret` Secret is
provisioned in `arc-docs`, then use chart version **0.14.1**:

```sh
helm upgrade --install k9s-docs \
  oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set \
  --version 0.14.1 --namespace arc-docs \
  --values .github/runners/k9s-values.yaml
```

No credential material is stored here. The runner image is 2.336.0, which
supports the Node.js 24 actions used by the workflows. The runner-group policy
must be maintained separately through GitHub organization settings/API.
