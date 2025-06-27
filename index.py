from app import app

# This is needed for Vercel serverless deployment
def handler(request, context):
    return app 