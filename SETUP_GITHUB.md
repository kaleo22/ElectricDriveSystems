# GitHub Repository Setup Guide

This guide explains how to configure repository protections and project settings
that cannot be enforced through files alone.

> **Audience:** Team Manager / Repository Owner

---

## 1. Protect the `main` Branch

1. Go to **Settings → Branches → Add branch ruleset** (or "Add rule" in classic view).
2. Set **Branch name pattern**: `main`
3. Enable the following:
   - ✅ **Require a pull request before merging**
     - Required approvals: **1** (increase to 2 if desired)
     - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ **Require status checks to pass before merging**
     - Add any CI workflow jobs once they exist.
   - ✅ **Do not allow bypassing the above settings** (applies to admins too)
   - ✅ **Restrict who can push to matching branches** — remove all individuals; force all changes through PRs.
4. Save.

---

## 2. Protect the `dev` Branch (Recommended)

Repeat the steps above with **Branch name pattern**: `dev`.

Suggested settings for `dev`:
- ✅ Require a pull request before merging
- Required approvals: **1**
- ✅ Dismiss stale reviews on new pushes

---

## 3. Create Required Branches

```sh
# From the default branch (main), create dev
git checkout -b dev
git push origin dev
```

Set `dev` as the **default branch** (optional but recommended):
**Settings → General → Default branch** → change to `dev`.

---

## 4. Configure Labels

The recommended label set is documented in [`project-management/LABELS.md`](project-management/LABELS.md).

Create them manually via **Issues → Labels → New label**, or use the GitHub CLI:

```sh
# Install GitHub CLI if not already available
# https://cli.github.com/

# Example: create a label
gh label create "type: feature" --color "0075ca" --description "New feature or work package"
gh label create "type: bug" --color "d73a4a" --description "Something is not working"
gh label create "type: task" --color "e4e669" --description "General task or chore"
gh label create "type: docs" --color "0075ca" --description "Documentation changes"
gh label create "status: in-progress" --color "fbca04" --description "Work is actively underway"
gh label create "status: blocked" --color "b60205" --description "Blocked by another issue or external factor"
gh label create "status: needs-review" --color "d93f0b" --description "Awaiting review"
gh label create "priority: high" --color "b60205" --description "High priority"
gh label create "priority: medium" --color "fbca04" --description "Medium priority"
gh label create "priority: low" --color "0e8a16" --description "Low priority"
gh label create "area: firmware" --color "1d76db" --description "Firmware related"
gh label create "area: hardware" --color "5319e7" --description "Hardware / PCB related"
gh label create "area: simulation" --color "006b75" --description "Simulation related"
gh label create "area: docs" --color "c5def5" --description "Documentation area"
gh label create "area: testing" --color "fef2c0" --description "Testing and measurement"
```

---

## 5. Create a GitHub Project (Board)

1. Go to the repository **Projects** tab → **New project**.
2. Choose **Board** layout.
3. Add columns: `Backlog`, `In Progress`, `In Review`, `Done`.
4. Link issues to the project as they are created.

---

## 6. Configure CODEOWNERS

The file `.github/CODEOWNERS` defines automatic review requests.
Update it with the actual GitHub usernames of your team:

```
# .github/CODEOWNERS
* @kaleo22           # Team Manager — reviews all changes by default
firmware/  @firmware-lead
hardware/  @hardware-lead
docs/      @docs-lead
```

---

## 7. (Optional) Enable Dependabot / Security Alerts

For future use when actual dependencies are added:

**Settings → Security → Dependabot alerts** → Enable.

---

## 8. Invite Team Members

**Settings → Collaborators → Add people**

Recommended roles:
- Team Manager: **Maintain**
- All other members: **Write**

---

## Checklist Summary

- [ ] `main` branch protection rule created
- [ ] `dev` branch protection rule created
- [ ] `dev` set as default branch (optional)
- [ ] Labels created (see `project-management/LABELS.md`)
- [ ] Project board created
- [ ] CODEOWNERS updated with real usernames
- [ ] All 7 team members invited with correct permissions
