## [Task description](task.pdf)


#### === Simply usage ===

```bash
git clone ... <dir>
cd <dir>
docker-compose up -d
...
docker-compose down
```


#### === Build & run dev-mode ===
```bash
docker-compose -f docker-compose.dev.yml up --build
...
CTRL+C
```


#### === Build & run test-mode ===
```bash
docker-compose -f docker-compose.test.yml up -d --build
...
docker-compose -f docker-compose.test.yml down
```


#### === manage.py ===

1. Startup {stage}
2. Run `./util/{stage}/manage.sh command`


#### === makemigrations (on dev-mode ONLY) ===

1. Startup dev-mode
2. `./util/dev/manage.sh makemigrations`


#### === Params ===
- `django_app/config/{stage}/.env`
    - `DB_AUTO_MIGRATE` for applying migrations on startup
    - `DB_LOADDATA_SAMPLE` for loading sample data on startup
    - `COLLECT_STATIC` for collecting static on startup (test-mode only)
