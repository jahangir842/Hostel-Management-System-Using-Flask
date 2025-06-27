from app import app

# This is needed for Vercel serverless deployment
handler = app.wsgi_app 