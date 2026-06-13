# Bloggy for Bloggers

A modern blogging platform built with FastAPI and async SQLAlchemy. Create accounts, write posts, manage profiles, and share content with an intuitive API-first design.

## Features

- **User Management**: Registration, authentication, and profile management with secure password hashing
- **Blog Posts**: Create, edit, and delete posts with a clean API
- **User Profiles**: Customizable profiles with image uploads to S3
- **Password Reset**: Secure password reset flow via email
- **Post Pagination**: Efficient browsing with configurable posts per page
- **Security**: CSRF protection, secure headers, and JWT authentication
- **Database Migrations**: Alembic for version-controlled schema changes

## Tech Stack

- **Backend**: FastAPI with async support
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with Argon2 password hashing
- **Storage**: AWS S3 for profile images
- **Email**: SMTP for password reset notifications
- **Frontend**: Jinja2 templates with vanilla JavaScript
- **Containerization**: Docker ready

## Prerequisites

- Python 3.13+
- PostgreSQL database
- AWS S3 bucket (or MinIO for local development)
- SMTP server access for email functionality

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bloggers
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/macOS
```

3. Install dependencies:
```bash
pip install -e .
```

4. Create a `.env` file in the root directory with your configuration:
```env
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/bloggers
SECRET_KEY=your-secret-key-here
S3_BUCKET_NAME=your-bucket-name
S3_REGION=ap-south-1
S3_ACCESS_KEY_ID=your-aws-key
S3_SECRET_ACCESS_KEY=your-aws-secret
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USERNAME=your-email@example.com
MAIL_PASSWORD=your-email-password
MAIL_FROM=noreply@example.com
```

5. Run database migrations:
```bash
alembic upgrade head
```

## Running the Application

Start the development server:
```bash
fastapi dev main.py
```

The application will be available at `http://localhost:8080`

- API documentation: `http://localhost:8080/docs`
- Alternative docs: `http://localhost:8080/redoc`

## Project Structure

```
├── main.py                 # FastAPI application entry point
├── models.py               # SQLAlchemy ORM models
├── schemas.py              # Pydantic request/response schemas
├── database.py             # Database configuration and sessions
├── auth.py                 # Authentication utilities
├── config.py               # Settings management
├── email_utils.py          # Email sending utilities
├── image_utils.py          # Image processing and S3 upload
├── routers/
│   ├── users.py            # User management endpoints
│   └── posts.py            # Post management endpoints
├── templates/              # Jinja2 HTML templates
├── static/                 # CSS, JavaScript, and static assets
├── alembic/                # Database migration files
├── tests/                  # Test suite with pytest
└── Dockerfile              # Container configuration
```

## Configuration

Key settings in `.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SECRET_KEY` | JWT signing key | Required |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token lifetime | 30 |
| `POSTS_PER_PAGE` | Pagination limit | 10 |
| `MAX_UPLOAD_SIZE_BYTES` | Max profile image size | 5MB |
| `RESET_TOKEN_EXPIRE_MINUTES` | Password reset token lifetime | 60 |

## API Endpoints

### Users (`/api/users`)
- `POST /register` - Create new account
- `POST /login` - User authentication
- `GET /profile` - Get user profile
- `PUT /profile` - Update profile
- `POST /request-reset` - Request password reset
- `POST /reset-password` - Complete password reset

### Posts (`/api/posts`)
- `GET /` - List all posts (paginated)
- `POST /` - Create new post
- `GET /{id}` - Get post details
- `PUT /{id}` - Update post
- `DELETE /{id}` - Delete post
- `GET /user/{user_id}` - Get posts by user

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest
```

### Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
alembic upgrade head
```

### Docker

Build and run with Docker:
```bash
docker build -t fastapi-app .
docker run -p 8080:8080 --env-file .env fastapi-app
```


