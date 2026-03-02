# lisa – remote config service

## core api
- [x] `project` model with `client_api` and `config_api`
- [x] `remoteconfig` model with `key`, `value`, `value_type`
- [x] `get /client/projects/<client_api>/configs` — public read endpoint
- [ ] `post /projects/create` — create project, returns both keys
- [ ] `post /client/projects/<client_api>/configs` — create config (config_api protected)
- [ ] `patch /client/projects/<client_api>/configs/<key>` — update config (config_api protected)
- [ ] `delete /client/projects/<client_api>/configs/<key>` — delete config (config_api protected)

## auth
- [ ] `config_api` column on `project`
- [ ] `@require_write_key` decorator for protected routes

## studio ui
- [ ] single html file served by flask at `/studio`
- [ ] reads `config_api` from environment on startup
- [ ] list all configs for the project
- [ ] add a new config variable
- [ ] edit an existing config variable
- [ ] delete a config variable
