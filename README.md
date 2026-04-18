# Shop GraphQL API

A simple Django application with a responsive CRUD UI for managing shops. Includes both traditional Django templates and GraphQL API endpoints.

## Features

- **Shop Management**: Create, Read, Update, Delete shops
- **Responsive UI**: Simple, clean interface that works on all devices
- **GraphQL API**: GraphQL endpoints for shop queries and mutations
- **Django Admin**: Built-in Django admin interface

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone git@github.com:Chirag373/shop_graphql_api.git
cd shop_graphql_api
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

## Usage

### Web UI
Open your browser and visit:
- **Shop CRUD**: http://127.0.0.1:8000/shops/
- **Django Admin**: http://127.0.0.1:8000/admin/

### GraphQL API
Visit: http://127.0.0.1:8000/graphql/

## Project Structure

```
shop_graphql_api/
├── core/                    # Project settings and configuration
│   ├── settings.py
│   ├── urls.py
│   └── schema.py
├── shop/                    # Shop application
│   ├── models.py           # Shop model
│   ├── views.py            # CRUD views
│   ├── urls.py             # URL routing
│   ├── schema.py           # GraphQL schema
│   ├── mutations.py        # GraphQL mutations
│   └── templates/          # HTML templates
├── manage.py
└── requirements.txt
```

## Shop Model

Each shop has:
- **name**: Shop name (required)
- **address**: Complete address (required)
- **emails**: List of email addresses
- **phones**: List of phone numbers
- **created_at**: Creation timestamp
- **updated_at**: Last update timestamp

## API Endpoints

### Web UI Routes
- `GET /shops/` - List all shops
- `GET /shops/create/` - Create shop form
- `GET /shops/<id>/` - View shop details
- `GET /shops/<id>/update/` - Edit shop form
- `GET /shops/<id>/delete/` - Delete confirmation
- `POST /shops/` - Create new shop
- `POST /shops/<id>/update/` - Update shop
- `POST /shops/<id>/delete/` - Delete shop

### GraphQL Endpoint
- `POST /graphql/` - GraphQL queries and mutations

## License

MIT License
