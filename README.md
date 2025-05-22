# CarDealer Project

A Django-based web application for managing and visualizing car dealership data, with support for API load testing using Locust.

---

## 🚀 Quick Start Guide

Follow these steps to get the project running on your local machine.

---

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/cardealer.git
cd cardealer
```

---

### 2. **Install Prerequisites**

- **Python 3.10+**  
  [Download Python](https://www.python.org/downloads/)
- **Docker**  
  [Install Docker](https://docs.docker.com/get-docker/)
- **uv (Python package manager)**  
  [uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
- **PostgreSQL**  
  [Install PostgreSQL](https://www.postgresql.org/download/)
- **Locust** (for load testing)  
  Will be installed in a later step.

---

### 3. **Configure the Database**

- Make sure PostgreSQL is running and a database named `cardealer` exists.
- Update your database settings in `core/settings.py` if needed:

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

---

### 4. **Install Python Dependencies**

```bash
uv pip install -r requirements.txt
```

---

### 5. **Apply Migrations**

```bash
python manage.py migrate
```

---

### 6. **Create a Superuser (Admin)**

```bash
python manage.py createsuperuser
```

---

### 7. **Load Dummy Data (Optional)**

If you want to load sample car data:

```bash
python manage.py dummycar
```

---

### 8. **Run the Development Server**

```bash
python manage.py runserver
```

- Open your browser and go to: [http://localhost:8000](http://localhost:8000)
- Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

### 9. **Run with Docker (Alternative)**

If you prefer Docker:

```bash
docker build -t cardealer-app .
docker run -p 8000:8000 cardealer-app
```

---

### 10. **Load Testing with Locust**

#### a. **Install Locust**

```bash
uv pip install locust
```

#### b. **Create/Edit your Locust test file**

Make sure you have a `locustfile.py` in your project root or use the provided one.

#### c. **Run Locust**

```bash
locust
```

- Open your browser and go to [http://localhost:8089](http://localhost:8089)
- Enter the host as `http://localhost:8000` and start your load test.

---

### 11. **Database Visualization (Optional)**

- Use [DataGrip](https://www.jetbrains.com/datagrip/) or any other database tool to connect to your PostgreSQL database for visualization and management.

---

## 🛠️ Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙏 Acknowledgments

- Thanks to the developers of `uv`, Docker, PostgreSQL, Locust, and DataGrip.
- Special thanks to the open-source community for their contributions.