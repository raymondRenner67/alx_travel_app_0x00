# alx_travel_app_0x01

A Django REST Framework API for managing travel listings and bookings.

## Overview

This project extends `alx_travel_app_0x00` with RESTful API endpoints for listings and bookings management. Built with Django REST Framework, it provides complete CRUD operations for travel listings and booking reservations.

## Features

- **Listings API**: Create, read, update, and delete travel property listings
- **Bookings API**: Manage booking reservations with full CRUD operations
- **RESTful Design**: Follows REST best practices with proper HTTP methods
- **Authentication**: IsAuthenticatedOrReadOnly permissions (read-only for anonymous users)
- **Auto Router**: DRF's DefaultRouter for clean, conventional URL patterns

## Project Structure

```
alx_travel_app/
 listings/
    models.py          # Listing, Booking, Review models
    serializers.py     # DRF serializers
    views.py           # ViewSets for API endpoints
    urls.py            # API routing configuration
    management/
        commands/
            seed.py    # Seed command for sample data
 settings.py
 urls.py                # Main URL configuration
 wsgi.py
```

## API Endpoints

### Listings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/listings/` | List all listings |
| POST | `/api/listings/` | Create a new listing (authenticated) |
| GET | `/api/listings/{id}/` | Retrieve a specific listing |
| PUT | `/api/listings/{id}/` | Update a listing (authenticated) |
| PATCH | `/api/listings/{id}/` | Partial update of a listing (authenticated) |
| DELETE | `/api/listings/{id}/` | Delete a listing (authenticated) |

### Bookings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a new booking (authenticated) |
| GET | `/api/bookings/{id}/` | Retrieve a specific booking |
| PUT | `/api/bookings/{id}/` | Update a booking (authenticated) |
| PATCH | `/api/bookings/{id}/` | Partial update of a booking (authenticated) |
| DELETE | `/api/bookings/{id}/` | Delete a booking (authenticated) |

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Quick Start (PowerShell)

```powershell
# Navigate to project directory
cd c:\Users\Latitude7480\Downloads\pf\alx_travel_app_0x01

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
python -m pip install django djangorestframework

# Navigate to the Django project
cd alx_travel_app

# Run migrations
python manage.py migrate

# Create a superuser (optional, for admin access)
python manage.py createsuperuser

# Seed sample data
python manage.py seed

# Run the development server
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`

## Testing with Postman

### 1. List All Listings
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/api/listings/`
- **Expected**: 200 OK with array of listings

### 2. Create a Listing
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/api/listings/`
- **Headers**: `Content-Type: application/json`
- **Body** (JSON):
```json
{
    "title": "Cozy Beach House",
    "description": "Beautiful beachfront property",
    "price": "250.00"
}
```
- **Expected**: 201 Created (requires authentication)

### 3. Retrieve a Single Listing
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/api/listings/1/`
- **Expected**: 200 OK with listing details

### 4. Update a Listing
- **Method**: PUT
- **URL**: `http://127.0.0.1:8000/api/listings/1/`
- **Body** (JSON):
```json
{
    "title": "Updated Beach House",
    "description": "Newly renovated beachfront property",
    "price": "300.00"
}
```
- **Expected**: 200 OK (requires authentication)

### 5. Partial Update a Listing
- **Method**: PATCH
- **URL**: `http://127.0.0.1:8000/api/listings/1/`
- **Body** (JSON):
```json
{
    "price": "275.00"
}
```
- **Expected**: 200 OK (requires authentication)

### 6. Delete a Listing
- **Method**: DELETE
- **URL**: `http://127.0.0.1:8000/api/listings/1/`
- **Expected**: 204 No Content (requires authentication)

### 7. Create a Booking
- **Method**: POST
- **URL**: `http://127.0.0.1:8000/api/bookings/`
- **Body** (JSON):
```json
{
    "listing": 1,
    "start_date": "2025-12-01",
    "end_date": "2025-12-07",
    "total_price": "1750.00"
}
```
- **Expected**: 201 Created (requires authentication)

### 8. List All Bookings
- **Method**: GET
- **URL**: `http://127.0.0.1:8000/api/bookings/`
- **Expected**: 200 OK with array of bookings

## Authentication

For authenticated requests in Postman:
1. Go to the **Authorization** tab
2. Select **Basic Auth**
3. Enter your username and password (created via `createsuperuser`)

Alternatively, use Django REST Framework's browsable API by visiting the endpoints in your browser while logged into the admin panel.

## Database Models

### Listing
- `title`: CharField (max 200 characters)
- `description`: TextField
- `price`: DecimalField (8 digits, 2 decimal places)
- `host`: ForeignKey to User
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)

### Booking
- `listing`: ForeignKey to Listing
- `guest`: ForeignKey to User
- `start_date`: DateField
- `end_date`: DateField
- `total_price`: DecimalField
- `status`: CharField (pending/confirmed/cancelled)
- `created_at`: DateTimeField (auto)

## Sample Data

Run the seed command to populate the database with sample data:

```powershell
python manage.py seed
```

This creates:
- 2 users: `host1` and `guest1` (password: `password123`)
- Multiple sample listings
- Sample bookings

## API Response Examples

### Listing List Response
```json
[
    {
        "id": 1,
        "title": "Cozy Beach House",
        "description": "Beautiful beachfront property",
        "price": "250.00",
        "host": "host1",
        "created_at": "2025-11-30T10:00:00Z"
    }
]
```

### Booking Detail Response
```json
{
    "id": 1,
    "listing": 1,
    "guest": "guest1",
    "start_date": "2025-12-01",
    "end_date": "2025-12-07",
    "total_price": "1750.00",
    "status": "pending"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- `200 OK`: Successful GET, PUT, PATCH
- `201 Created`: Successful POST
- `204 No Content`: Successful DELETE
- `400 Bad Request`: Invalid data
- `401 Unauthorized`: Authentication required
- `404 Not Found`: Resource not found

## Development Notes

- All ViewSets use `ModelViewSet` for complete CRUD functionality
- Permissions are set to `IsAuthenticatedOrReadOnly` (anonymous users can read, authenticated users can write)
- The `perform_create` methods automatically set the `host` and `guest` to the current user
- URLs are automatically generated using DRF's `DefaultRouter`

## Next Steps

To add Swagger documentation:

```powershell
# Install drf-yasg
pip install drf-yasg

# Add to INSTALLED_APPS in settings.py
# 'drf_yasg',

# Update urls.py with Swagger configuration
```

## License

This project is part of the ALX Software Engineering program.

## Author

ALX Travel App Team
# alx_travel_app_0x01
