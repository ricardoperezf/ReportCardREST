import os
from reportcard import reportcard_app
from reportcard import *
__author__ = "ricardoperezf"
__version__ = "1.0.0"

if __name__ == "__main__":
    # if not os.path.exists('db.sqlite'):
    #     db.create_all()
    port = int(os.environ.get("PORT", 5000))
    reportcard_app.run(host='0.0.0.0', port=port)
