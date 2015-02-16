from app import app
import os

if __name__ == "__main__":

    # Development server settings
    dev_port = int(os.getenv('PORT', 5444))
    dev_debug = bool(os.getenv('DEBUG', False))

    app.run(host='0.0.0.0', port=dev_port, debug=dev_debug)
