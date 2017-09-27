#!/usr/bin/env python
# _*_ encoding: utf-8 _*_
# ---------------------------------------
# Created by: Jlfme<jlfgeek@gmail.com>
# Created on: 2017-09-26 18:37:18
# ---------------------------------------


from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand


app = create_app('default')
manager = Manager(app)
manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    app.run(host='10.10.10.4', port=8888, use_reloader=True)
    # manager.run()
