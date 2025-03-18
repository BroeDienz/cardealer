# Car Dealer Project

This project is designed to manage and visualize car dealership data. Below is an overview of the tools and technologies used in this project.

## Tools and Technologies

### 1. **uv Python Package**
    - The `uv` Python package is utilized for various functionalities within the project. It helps streamline development and manage project dependencies. Follow or click link to install uv
    https://docs.astral.sh/uv/getting-started/installation/

### 2. **Project Manager**
    - A project management tool is used to organize and maintain the structure of the project, ensuring smooth development workflows.

### 3. **Docker**
    - Docker is used to containerize the application, making it easy to build, ship, and run the project in any environment.
    - Docker images are created to encapsulate the application and its dependencies.

### 4. **PostgreSQL**
    - PostgreSQL is the database management system used in this project to store and manage data efficiently.

### 5. **DataGrip**
    - DataGrip is employed to visualize and interact with the PostgreSQL database, providing an intuitive interface for database management.

## Getting Started

### Prerequisites
- Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Install Python and required dependencies (e.g., `uv` package).
- Set up PostgreSQL and configure the database.

### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd cardealer
    ```
2. Build the Docker image:
    ```bash
    docker build -t cardealer-app .
    ```
3. Run the Docker container:
    ```bash
    docker run -p 8000:8000 cardealer-app
    ```

### Database Setup
- Ensure PostgreSQL is running and properly configured.
- Update the DATABASES setting in core/settings.py to match your PostgreSQL configuration:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cardealer',
            'USER': 'your-db-user',
            'PASSWORD': 'your-db-password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

- Use DataGrip or any other database tool to visualize and manage the database.

## Usage
- Start the application using Docker.
- Access the application via the specified port (e.g., `http://localhost:8000`).
- Use DataGrip to interact with the PostgreSQL database.

## Contributing
Contributions are welcome! Please follow the standard Git workflow:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Thanks to the developers of `uv`, Docker, PostgreSQL, and DataGrip for their amazing tools.
- Special thanks to the open-source community for their contributions.
