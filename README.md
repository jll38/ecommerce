# E-commerce Project

## Introduction
This is an e-commerce project built using React as the frontend, MaterialUI and Tailwind CSS for styling, and FastAPI as the backend. The project also utilizes PostgreSQL as the database, and incorporates CI/CD concepts with containerization, deployment pipelines through GitHub Actions, and automatic image updates on the host server using Watchtower.

## Technologies Used
- **Frontend**: React, MaterialUI, Tailwind CSS
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **CI/CD**: GitHub Actions, Docker Hub
- **Reverse Proxy**: Nginx
- **Automatic Updates**: Watchtower

## Features
- **User Registration and Authentication**: Customers can register and log in to the platform.
- **Product Catalog**: Customers can browse and search for products.
- **Shopping Cart**: Customers can add products to their cart and proceed to checkout.
- **Order Management**: Customers can view their order history and track the status of their orders.
- **Admin Panel**: Admins can manage products, orders, and user accounts.

## Architecture Overview
- **Frontend**: The frontend is built using React, with MaterialUI and Tailwind CSS for styling. It communicates with the backend API using HTTP requests.
- **Backend**: The backend is built using FastAPI, a Python web framework that provides a robust and scalable API.
- **Database**: The project uses PostgreSQL as the database to store product information, user accounts, and order details.
- **Containerization**: Both the frontend and backend components are containerized using Docker, making it easier to package and deploy the application.
- **CI/CD**: The project uses GitHub Actions to automate the build and deployment process. Whenever changes are pushed to the repository, GitHub Actions builds the Docker images and pushs them to Docker Hub.
- **Automatic Updates**: Watchtower is used to monitor the Docker Hub repository for updates to the application's Docker images. When a new image is available, Watchtower automatically pulls the updated image and restarts the containers on the host server.


## Deployment
The project uses GitHub Actions to automate the build and deployment process. Whenever changes are pushed to the repository, GitHub Actions will:
1. Build the Docker images for the frontend and backend.
2. Push the images to Docker Hub.
3. Update the Docker containers on the host server using Watchtower.

The host server must have Docker and Watchtower installed to automatically pull the updated images and restart the containers.

## License
This project is licensed under the [MIT License](LICENSE).