#!/usr/bin/env python3
import os
from app.models import User, Role
from flask_script import Manager, Shell
from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_shell_context))


if __name__ == '__main__':
    app.run()
