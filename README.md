# Voksmonitor Miskolc

Ez az eredeti [voksmonitor](https://github.com/kalkulacka-one/volebni-kalkulacka-2022/tree/voksmonitor) módosítása. Ez elsősorban a frontend személyre szabását jelenti a konkrét problémára. Plusz egy adatbetöltő python scriptet, ami egy bizonyos formátumú Google Sheet-ből kiexportált csv-t (`jovokepek.csv`) alakít a voksmonitor saját formátumára.

Használat:

```bash
python generate_json.py
```

```bash
cd frontend

npm run dev
# vagy
npm run build
```

# volebni-kalkulacka-2022

Volební kalkulačka, nová verze s Česko.Digital v roce 2022

## Frontend

Frontend is SPA Vue.js application.

[README](frontend/README.md)

## Generator

Generator uses Python and FastAPI framework.

[README](generator/README.md)

## Data

Each instance of _volebni-kalkulacka-2022_ uses static dataset on CDN. During development this `.json` data are stored in repository in `data` directory. Any change in content of this directory is deployed to main domain under `https://<domain>/data/` directory.

## Contribution

This project is developed by volunteers at [Česko.Digital](https://cesko.digital). Join us [here](https://cesko.digital/join) and visit our channel [#inkubace-volebni_kalkulacka2022](https://cesko-digital.slack.com/archives/C0311K8LHFX).
