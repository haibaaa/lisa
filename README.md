# Lisa — Remote Configuration Service

Lisa is a small remote configuration and feature flag service inspired by systems like Firebase Remote Config.

It allows applications to dynamically change behavior at runtime without redeploying code, while maintaining strict boundaries between public read access and privileged write access.

---
## Useful Links

- **Mona CLI on PyPI**  
  The command-line tool i created to sync local configuration with the Lisa backend — available on PyPI:  
  https://pypi.org/project/mona-cli/

- **Example Application Repository**  
  An example of Lisa with Python app using Mona and a Vite + React frontend: 
  https://github.com/haibaaa/lisa-demo.git
---

## Problem Statement

Modern applications often need to change behavior after deployment:

- enable or disable features  
- adjust UI themes  
- tune limits or thresholds  

Hard-coding these values couples configuration to releases, increasing risk and slowing iteration.

Lisa solves this by providing a centralized, read-only configuration API for applications, and a protected write interface for operators.

---

## High-Level Architecture

Lisa is composed of three parts:

1. **Backend API (Flask)**
   - Public read-only endpoints for applications
   - Private write endpoints for configuration updates
   - Enforces trust boundaries structurally

2. **CLI (Mona)**
   - Used by developers/operators to sync local configuration
   - Interacts only with privileged endpoints

3. **Client Applications**
   - Consume configuration via simple JSON over HTTP

```

Mona (CLI) ──▶ Lisa (Flask + DB)
                ▲
                │ JSON over HTTP
                │
            Client App

````

---

## Trust Boundaries

Lisa enforces two distinct trust levels:

### public read plane
- endpoint: `get /client/projects/<client_api>`
- accessible with a public identifier
- read-only by construction
- safe to embed in client applications

### private write plane
- endpoint: `post /sync/<config_api>`
- requires a secret configuration api key
- used only by operators and the cli
- allows mutation of configuration state

Public keys identify projects.  
Private keys authorize mutation.

---

## API Design

### Create Project
`POST /create/<project_name>`

Creates a new project and returns:
- `client_api` — public read key
- `config_api` — private write key

Keys are shown only once and must be stored safely.

### Read Configuration (Public)
`GET /client/projects/<client_api>`

Returns a resolved key–value map:

```json
{
  "feature_x_enabled": true,
  "theme": "dark"
}
````

### Sync Configuration (Private)

`POST /sync/<config_api>`

Accepts a JSON blob and synchronizes it with the project’s stored configuration.

---

## Data Model

### Project

* Owns API keys
* Acts as a namespace for configuration

### RemoteConfig

* Key–value configuration entries
* Typed values (bool, string, number)
* Always associated with a project

No configuration exists without a project.
This invariant is enforced at the database level.

---

## Configuration Resolution Model

Lisa resolves configuration server-side and returns only the final values to clients.

Clients never receive:

* rules
* metadata
* write capabilities

---

## Client Consumption Model

Lisa does not support a complete client SDK like other mature services yet so users need adapt a thin wrapper around the api for now

Example (React):

```ts
fetch(".../client/projects/<client_api>")
  .then(res => res.json())
  .then(config => {
    if (config.feature_x_enabled) enableFeature()
  })
```

The demo React app polls the API periodically to detect configuration changes without requiring a page refresh.

---

## Failure Modes & Observability

* Invalid keys return clear HTTP errors
* Public endpoints cannot mutate state
* Sync operations overwrite atomically
* Errors are logged at the API boundary

The system favors explicit failure over silent misconfiguration.

---

## AI Usage

AI tools were used to:

* accelerate boilerplate generation
* validate architectural ideas
* refine explanations and documentation

AI was not used to:

* design trust boundaries
* make security decisions
* introduce new abstractions without review

All AI-generated code was manually reviewed and adapted to preserve system invariants.

---

## Out of Scope (By Design)

* user authentication
* per-user targeting
* real-time push updates
* secrets management
* role-based access control

These features are omitted to keep the system understandable and focused on its core guarantees.

---

## Possible Extensions

* configuration versioning
* percentage-based rollouts
* conditional targeting
* audit logs

The current structure allows these to be added without breaking existing clients.

---

## Final Note

Lisa is intentionally small.

The goal is not to replicate Firebase, but to demonstrate how a well-structured system enforces correctness through design rather than convention.

```
