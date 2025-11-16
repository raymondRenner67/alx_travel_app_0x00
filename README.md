# alx_travel_app_0x00

This folder is a duplicated project for grading. The inner project directory is `alx_travel_app/` and contains the `listings` app with models, serializers, and a `seed` management command.

## Quickstart (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r ../requirement.txt
cd alx_travel_app
python manage.py migrate
python manage.py seed
```

This will create `db.sqlite3`, two users (`host1`, `guest1`) and sample listings.
