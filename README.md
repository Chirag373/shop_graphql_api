


<img width="1920" height="875" alt="Screenshot 2026-04-18 at 9 49 39 PM" src="https://github.com/user-attachments/assets/d17cbb91-8e65-49ba-be17-02c1512b32ac" />


# Shop GraphQL API

A Django application with a responsive CRUD UI for managing shops. The web interface uses the GraphQL API internally, providing a unified data layer for both UI and external API consumers.

## Features

- **Shop Management**: Create, Read, Update, Delete shops via web UI or GraphQL API
- **GraphQL-First Architecture**: All data operations go through GraphQL queries and mutations
- **Responsive UI**: Simple, clean interface that works on all devices
- **Web Interface**: Traditional Django templates integrated with GraphQL backend
- **Type Safety**: GraphQL schema ensures data validation and consistency
- **Django Admin**: Built-in Django admin interface

## Tech Stack

- **Backend**: Django 6.0.4
- **GraphQL**: Graphene 3.4.3 + Graphene Django 3.2.3
- **Database**: SQLite (default)
- **Frontend**: Vanilla HTML/CSS (responsive design)

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
The web interface automatically uses GraphQL for all CRUD operations:
- List, view, create, update, and delete shops
- See error messages with helpful feedback
- Fully responsive design works on mobile, tablet, and desktop

### GraphQL API

Access the GraphQL endpoint at: http://127.0.0.1:8000/graphql/

#### Query Examples

**Get all shops:**
```graphql
query {
  allShops {
    id
    name
    address         # Django settings
│   ├── urls.py             # URL routing (includes shops/ and graphql/)
│   └── schema.py           # GraphQL schema (combines Query & Mutation)
├── shop/                    # Shop application
│   ├── models.py           # Shop model with JSONField for emails/phones
│   ├── views.py            # Django views using GraphQL internally
│   ├── urls.py             # URL patterns for shop CRUD routes
│   ├── schema.py           # Shop GraphQL Query definition
│   ├── mutations.py        # Shop GraphQL Mutations (Create, Update, Delete)
│   ├── types.py            # ShopType - GraphQL object type
│   ├── validation.py       # Email and phone validation helpers
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template with CSS
│   │   └── shop/           # Shop-specific templates
│   └── migrations/         # Database migrations
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## How It Works

1. **Web UI** → Django View → GraphQL Query/Mutation → Database
2. **External Client** → HTTP Request to `/graphql/` → GraphQL Query/Mutation → Database

The Django views in `shop/views.py` execute GraphQL queries and mutations using the schema, then pass the results to templates for rendering. This ensures both the web UI and API consumers use the same validated data layer.hop(id: 1) {
    id (HTML)
- `GET /shops/` - List all shops
- `GET /shops/create/` - Display create form
- `GET /shops/<id>/` - View shop details
- `GET /shops/<id>/update/` - Display edit form
- `GET /shops/<id>/delete/` - Display delete confirmation
- `POST /shops/create/` - Create new shop
- `POST /shops/<id>/update/` - Update shop
- `POST /shops/<id>/delete/` - Delete shop

### GraphQL Endpoint
- `POST /graphql/` - GraphQL queries and mutations
- `GET /graphql/` - GraphiQL interactive explorer

## Validation

The API validates data before saving:

### Email Validation
- Pattern: `user@example.com`
- Required format: valid email address

### Phone Validation  
- Format: `+country_code digits` or just digits
- Example: `+14155552671` or `14155552671`

### Shop Required Fields
- `name` (string, max 255 chars)
- `address` (string, required)

### Shop Optional Fields
- `emails` (list of strings)
- `phones` (list of strings)
**Create a shop:**
```graphql
mutation {
  createShop(
    name: "My Store"
    address: "123 Main St, City"
    emails: ["info@mystore.com", "sales@mystore.com"]
    phones: ["+1234567890"]
  ) {
    shop {
      id
      name
    }
    success
    message
  }
}
```

**Update a shop:**
```graphql
mutation {
  updateShop(
    id: 1
    name: "Updated Store Name"
    address: "456 New St, City"
    emails: ["new@store.com"]
    phones: ["+0987654321"]
  ) {
    shop {
      id
      name
    }
    success
    message
  }
}
```

**Delete a shop:**
```graphql
mutation {
  deleteShop(id: 1) {
    success
    message
    deletedId
  }
}
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
