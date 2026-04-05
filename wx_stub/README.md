# wx_stub — Headless DB Build Shims

Stubs for `wx` and `cryptography` so `db_update.py` can run without a GUI or the full dependency stack.

## When to use

`db_update.py` builds `eve.db` from the `staticdata/` JSON files, but it transitively imports `config.py`, which requires `wx` (GUI) and `cryptography` (ESI token encryption). Neither is needed for DB generation.

## Usage

`PYFA_FERNET_KEY` must be set. Export it from your shell or inline it:

```bash
# From the root .env
export PYFA_FERNET_KEY=$(grep PYFA_FERNET_KEY ../../.env | cut -d= -f2)

# Then from packages/Pyfa/
PYTHONPATH=wx_stub python db_update.py
```

Or inline:

```bash
PYFA_FERNET_KEY=$(grep PYFA_FERNET_KEY ../../.env | cut -d= -f2) PYTHONPATH=wx_stub python db_update.py
```

## What the stubs cover

| Module | Stub behaviour |
|---|---|
| `wx.Colour` | No-op constructor |
| `cryptography.fernet.Fernet` | Reads key from `PYFA_FERNET_KEY` env var (errors if unset); encrypt/decrypt are identity functions |

The `cryptography` stub is **only safe for DB generation**. Do not use `wx_stub` at runtime — it will break ESI authentication.
