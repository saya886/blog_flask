import unittest
import json
import re
from base64 import b64encode
from app import create_app, db
from app.models import User, Post, Comment