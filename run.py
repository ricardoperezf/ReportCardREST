from reportcard import reportcard_app

__author__ = "ricardoperezf"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    reportcard_app.run(host='0.0.0.0', port=port)
