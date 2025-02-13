# Medical Appointment Management, Authentication, and User Management Project

## Description
This project is a microservices-based system for medical appointment management and user management. It consists of a backend developed with FastAPI and Flask, along with a MySQL database, deployed using Docker. Additionally, it includes an authentication system that manages login and logout using Redis for token management.

## Technologies Used
- **Backend:** FastAPI (Python), Flask (Python)
- **Database:** MySQL
- **Authentication:** AWS Cognito and Redis
- **Containers:** Docker & Docker Compose
- **Dependency Manager:** pip
- **ORM:** PyMySQL and SQLAlchemy
- **API Gateway:** GraphQL-Gateway

## Backend Microservices Architecture
The system follows a microservices-based architecture, where each core functionality has its own independent service:

### Available Microservices
#### **Appointment Management**
1. **Create Service** (`/cart/add` - Port `8001`)
   - Allows doctors to create new medical appointments.
2. **Read Service** (`/cart/{user_id}` - Port `8002`)
   - Retrieves stored medical appointments.
3. **Update Service** (`/cart/update` - Port `8003`)
   - Allows modifying the details of an existing appointment.
4. **Delete Service** (`/cart/delete` - Port `8004`)
   - Allows deleting registered appointments.

#### **Authentication**
5. **Login Service** (`/auth/login` - Port `8000`)
   - Authenticates users and generates JWT tokens.
6. **Logout Service** (`/auth/logout` - Port `8005`)
   - Invalidates JWT tokens by storing them in Redis.

#### **User Management**
7. **Delete Users Service** (`/users/delete` - Port `5001`)
   - Allows administrators to delete registered users.
8. **Edit Users Service** (`/users/edit` - Port `5002`)
   - Allows modifying user details.
9. **View Users Service** (`/users/view` - Port `5003`)
   - Allows viewing registered user information.

Each microservice has its own `Dockerfile` and `requirements.txt`, ensuring independence and scalability.

## Setup and Deployment
### Prerequisites
- Install Docker and Docker Compose.
- Configure environment variables in the `.env` files for each microservice.

### Starting the Microservices
To start all services, run:
```bash
docker-compose up -d --build
```
This will start the following containers:
- `mysql_db`: MySQL database
- `redis`: Redis server for token management
- `create_service`: Appointment creation service
- `read_service`: Appointment retrieval service
- `update_service`: Appointment update service
- `delete_service`: Appointment deletion service
- `login-service`: User authentication service
- `logout-service`: Logout service
- `delete_users`: User deletion service
- `edit_users`: User editing service
- `view_users`: User viewing service

### Stopping the Services
```bash
docker-compose down
```

## Security and Authentication
- All endpoints are protected by JWT, validating tokens against AWS Cognito.
- Only doctors (`role_id=2`) can create, update, or delete appointments.
- Only administrators (`role_id=1`) can manage users.
- Redis is used for JWT token invalidation in the logout service.
- Secure database connections are ensured using environment variables.

## Database
The service uses MySQL as the primary database. The connection is configured in `.env`:
```
DB_HOST=appointment_db
DB_USER=admin
DB_PASSWORD=nala1234
DB_NAME=appointment_management
DB_PORT=3306
```

## API Gateway
A `GraphQL-Gateway` is implemented to integrate appointment creation, retrieval, update, and deletion services, along with user management, improving request efficiency.

## Contribution
1. Fork the repository.
2. Create a branch for the new functionality.
3. Submit a pull request for review.

## Contact
For inquiries or support, contact the project administrators.


#ARCHITECTURE IMAGE

![Image](https://github.com/user-attachments/assets/ce76a496-dcf4-4757-9c3b-a1792c2b6b0d)

