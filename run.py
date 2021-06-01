from app import create_app
from config.app import set_config
from app.models import *


app = create_app()

if __name__ == '__main__':
    set_config()
    init_db()
    app.run()
