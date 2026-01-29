#!/usr/bin/env python
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == '__main__':
    from app import app
    app.run(debug=True, host='localhost', port=5000)
