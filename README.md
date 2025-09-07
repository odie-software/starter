# Starter template

A complete starter template for a Nuxt 3 / Django Rest Framework stack. Includes:
- Linting for frontend/backend
- Custom composable API structure in the frontend
- Pinia/Quasar set up in the frontend
- Working auth flow using dj-rest-auth
- Production and development docker files
- Testing framework and swagger in the backend
- Celery in the backend
- Custom makefile to set up dev environment, including installing modules locally for IntelliSense/type completions

## Getting Started

To get the development environment up and running, you can use the provided `Makefile`.

### Initial Setup

1.  **Set up environment variables and install dependencies:**
    ```bash
    make
    ```
    This command will:
    - Create a `.env` file with your user and group IDs.
    - Build and start all the Docker containers for the backend, frontend.
    - Install Python and Node.js dependencies locally for better IDE integration (IntelliSense, type completion).
    - Restart the services.

### Common Commands

-   **Start all services:**
    ```bash
    make start
    ```
-   **Build all services:**
    ```bash
    make build
    ```
-   **Run database migrations:**
    ```bash
    make migrate
    ```
-   **Run backend tests:**
    ```bash
    make test
    ```
-   **Open a Django shell:**
    ```bash
    make shell
    ```
-   **Install/update local (host) dependencies:**
    ```bash
    make modules
    ```
-   **Adding a package to the frontend (web):**
    ```bash
    make web_pkg
    ```

-   **Adding a package to the backend (api):**
    ```bash
    make api_pkg
    ```
