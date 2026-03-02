# lisa – remote config service

## core api
- [x] `project` model with `client_api` and `config_api`
- [x] `remoteconfig` model with `key`, `value`, `value_type`
- [x] `get /client/projects/<client_api>/configs` — public read endpoint
- [x] `post /create/<project_name>` — creates project, returns `client_api` and `config_api`
- [x] `post /sync/<config_api>` — accepts a json blob and syncs with existing project configs

## auth
- [x] `config_api` column on `project`
- [ ] `@require_config_api` decorator for protected routes

## lisa cli (python package)
- [ ] package setup (`pyproject.toml`, entry point)
- [ ] local config file format (decide: `lisa.json`, `lisa.toml`, or `.env`-style)
- [ ] `lisa sync` command — reads local file, crafts post to `/sync/<config_api>`
- [ ] `lisa init` command — scaffolds the local config file
- [ ] publish to pypi

## studio ui (deprioritized)
- [ ] single html file served by flask at `/studio`
- [ ] full crud on config variables
