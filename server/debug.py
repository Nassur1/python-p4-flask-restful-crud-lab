#!/usr/bin/env python3

"""
This debug file is SAFE.
It ONLY opens an interactive shell.
It does NOT import app, does NOT run migrations,
does NOT run seed code, and does NOT interfere with tests.
"""

from app import app
from models import db, Plant

if __name__ == '__main__':
    with app.app_context():
        import code
        code.interact(local=dict(globals(), **locals()))
