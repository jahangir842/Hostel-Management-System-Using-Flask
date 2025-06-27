from app import create_app

app = create_app()

# This is the entry point for Vercel serverless function
def handler(request, context):
    return app(request, context) 