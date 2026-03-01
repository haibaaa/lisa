
# iterative goals for remote config service (lisa)

## phase 0 — foundation 
- [x] create `uv` project
- [x] set up flask app factory
- [x] enable hot reload
- [x] expose `/client/config` returning hardcoded values

---

## phase 1 — database connectivity (no features yet)
**goal:** prove the backend can talk to neon via sqlalchemy.

- [x] add sqlalchemy engine using `database_url`
- [x] verify connection on app startup
- [x] create a minimal health endpoint that queries the db
- [x] handle db connection failure gracefully

*deliverable:* app starts and confirms db connectivity.

---

## phase 2 — project entity (isolation boundary)
**goal:** introduce projects without configs.

- [ ] define `projects` table (id, name, public_key)
- [ ] generate public project keys
- [ ] seed one project manually
- [ ] fetch project by `public_key`

*deliverable:* backend can resolve a project from a public key.

---

## phase 3 — config storage (static resolution)
**goal:** store and return config values per project.

- [ ] define `configs` table (project_id, key, value, enabled)
- [ ] insert sample config rows
- [ ] update `/client/config` to require `project_key`
- [ ] return `{ key: value }` for a project

*deliverable:* client api returns db-backed config.

---

## phase 4 — admin write path (minimal auth)
**goal:** allow config modification safely.

- [ ] add simple admin auth (static token)
- [ ] implement `post /admin/configs`
- [ ] validate input
- [ ] insert or update config values

*deliverable:* config can be updated without redeploy.

---

## phase 5 — safety & defaults
**goal:** prevent invalid states.

- [ ] enforce unique `(project_id, key)`
- [ ] ignore disabled configs in client responses
- [ ] return empty config for invalid project keys
- [ ] add basic logging for admin writes

*deliverable:* system behaves safely under bad input.

---

## phase 6 — client-side integration (very small)
**goal:** demonstrate usage from a frontend.

- [ ] create a tiny js config client wrapper
- [ ] fetch config once and cache in memory
- [ ] use one flag to toggle ui behavior

*deliverable:* end-to-end demo of remote config in action.

---

## phase 7 — documentation & wrap-up
**goal:** make the system understandable.

- [ ] document architecture decisions
- [ ] explain trust boundaries
- [ ] describe future multi-user extension
- [ ] prepare walkthrough narrative

*deliverable:* ready-for-review submission.
