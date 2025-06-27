# Deploying the Hostel Management System to Vercel

This guide will walk you through the process of deploying the Hostel Management System Flask application to Vercel using GitHub Actions.

## Prerequisites

1. A [GitHub](https://github.com/) account
2. A [Vercel](https://vercel.com/) account
3. The Hostel Management System code pushed to a GitHub repository

## Setup Steps

### 1. Fork or Clone the Repository

If you haven't already, fork or clone this repository to your GitHub account.

### 2. Set Up Vercel

1. Sign up for a Vercel account at [vercel.com](https://vercel.com) if you don't have one.
2. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```
3. Log in to Vercel from the CLI:
   ```bash
   vercel login
   ```
4. Link your project to Vercel:
   ```bash
   cd Hostel-Management-System-Using-Flask
   vercel link
   ```
   This will create a `.vercel` directory with project configuration.

### 3. Get Vercel Tokens and IDs

You need to get the following values from Vercel:

1. **Vercel Token**: 
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click on your profile picture → Settings → Tokens
   - Create a new token with a descriptive name (e.g., "GitHub Actions")
   - Copy the token value

2. **Project ID and Organization ID**:
   - These can be found in the `.vercel/project.json` file after linking your project
   - Or run `vercel project ls` to list your projects and their IDs

### 4. Set Up GitHub Secrets

1. Go to your GitHub repository
2. Click on "Settings" → "Secrets and variables" → "Actions"
3. Add the following secrets:
   - `VERCEL_TOKEN`: Your Vercel token
   - `VERCEL_PROJECT_ID`: Your Vercel project ID
   - `VERCEL_ORG_ID`: Your Vercel organization ID

### 5. Prepare Your Application for Vercel

The repository already includes:

1. `vercel.json` - Configuration file for Vercel that tells it how to build and serve the Flask application
2. `.github/workflows/vercel-deploy.yml` - GitHub Actions workflow file that automates the deployment

### 6. Deploy to Vercel

1. Push your changes to the main branch:
   ```bash
   git add .
   git commit -m "Set up Vercel deployment"
   git push origin main
   ```

2. The GitHub Actions workflow will automatically trigger and deploy your application to Vercel.

3. You can monitor the deployment in the "Actions" tab of your GitHub repository.

### 7. Access Your Deployed Application

Once the deployment is complete, you can access your application at:

```
https://[your-project-name].vercel.app
```

## Troubleshooting

### Database Issues

Vercel's serverless environment doesn't support SQLite file-based databases for production. For a production deployment, you should:

1. Use a managed database service like PostgreSQL on services like:
   - [Neon](https://neon.tech/) (PostgreSQL)
   - [PlanetScale](https://planetscale.com/) (MySQL)
   - [MongoDB Atlas](https://www.mongodb.com/atlas/database) (MongoDB)

2. Update your application's database configuration to use environment variables:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///hostel.db')
   ```

3. Add the database connection string as an environment variable in Vercel:
   - Go to your project in the Vercel dashboard
   - Navigate to Settings → Environment Variables
   - Add `DATABASE_URL` with your database connection string

### Static Files and Uploads

Vercel's serverless functions don't support file system writes. For file uploads:

1. Use a cloud storage service like:
   - [AWS S3](https://aws.amazon.com/s3/)
   - [Google Cloud Storage](https://cloud.google.com/storage)
   - [Cloudinary](https://cloudinary.com/)

2. Update your application code to use the cloud storage service instead of local file system.

## Continuous Deployment

With the GitHub Actions workflow in place, any push to the main branch will automatically trigger a new deployment to Vercel.

## Manual Deployment

If you prefer to deploy manually without GitHub Actions:

```bash
vercel --prod
```

This will deploy the current state of your project to production.

## Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Flask on Vercel](https://vercel.com/guides/using-flask-with-vercel)
- [GitHub Actions Documentation](https://docs.github.com/en/actions) 