from flask import Flask
from api.app import app

# Vercel serverless function handler
def handler(request, context):
    """
    Vercel serverless function handler
    """
    return app 