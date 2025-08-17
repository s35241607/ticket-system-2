# Enterprise Ticket System

This project is a complete, containerized ticket system designed for internal enterprise use. It features a modern backend built with FastAPI and a reactive frontend using Vue 3. The entire stack is orchestrated with Docker Compose for easy setup and deployment.

## Features

- **Ticket Management**: Create, Read, Update, and Delete tickets.
- **Status & Priority**: Manage ticket lifecycle with statuses (Open, In Progress, Closed) and priorities.
- **Approval Workflow**: Basic structure for ticket approval.
- **User Management**: Simple user model (expandable for full auth).
- **Containerized**: All services run in Docker containers.
- **Scalable**: Ready to integrate with Kafka for event-driven architecture and Redis for caching.

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.11
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy
- **Async**: Fully asynchronous with `async/await`.
- **Linting/Formatting**: `black`, `isort`, `flake8`

### Frontend
- **Framework**: Vue 3 (Composition API)
- **Build Tool**: Vite
- **UI Framework**: Vuetify 3
- **Language**: JavaScript
- **API Client**: Axios
- **Linting/Formatting**: `eslint`, `prettier`

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **API Gateway (Recommended)**: Kong or similar (handles JWT validation).
- **Database**: PostgreSQL
- **Cache (Optional)**: Redis
- **Message Broker (Optional)**: Kafka

## Project Structure

The project is a monorepo with two main packages:

- `backend/`: The FastAPI application.
- `frontend/`: The Vue 3 application.

```
.
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── .env.example
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create an environment file**
    Copy the example environment file and customize it if needed. The default values are configured to work with Docker Compose out of the box.
    ```bash
    cp .env.example .env
    ```

3.  **Build and run the services**
    This command will build the Docker images for the frontend and backend, and start all the services defined in `docker-compose.yml`.
    ```bash
    docker-compose up --build
    ```

    - The `--build` flag forces a rebuild of the images. You can omit it for subsequent runs.
    - To run in detached mode, add the `-d` flag.

### Accessing the Application

- **Frontend (Vue App)**: `http://localhost:5173`
- **Backend (FastAPI Docs)**: `http://localhost:8000/docs`
- **PostgreSQL Database**: Port `5432`
- **Redis**: Port `6379`

The backend will automatically create the database tables and a default user with the following credentials:
- **Email**: `admin@example.com`
- **Password**: `password`

The frontend is pre-configured to send requests with `X-User-Id: 1` in the headers to simulate this user being logged in.

## Development

### VS Code Remote - Containers

This project is set up to be used with the [VS Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers) extension.
1.  Open the project in VS Code.
2.  Click the green "><" icon in the bottom-left corner of the window.
3.  Select "Remote-Containers: Reopen in Container". This will open the workspace inside the `backend` Docker container, with all dependencies and tools ready.

### Debugging

The backend is configured with `debugpy`. You can attach the VS Code debugger to the running container using the "Python: FastAPI" launch configuration included in `.vscode/launch.json`.

## CI/CD Pipeline (Recommendations)

A basic CI/CD pipeline (using GitHub Actions or GitLab CI) would look like this:

1.  **Lint & Test**: On every push to a feature branch.
    - Run `flake8`, `black --check`, `isort --check`.
    - Run unit and integration tests (`pytest`).
2.  **Build Docker Images**: On merge to `main` or `develop`.
    - Build and tag `backend` and `frontend` Docker images.
    - Push images to a container registry (e.g., Docker Hub, AWS ECR, Google GCR).
3.  **Deploy**: On merge to `main` (or manually triggered).
    - Deploy the new images to a staging or production environment (e.g., using `docker-compose` on a server, or deploying to Kubernetes).
