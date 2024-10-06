# PostgreSQL and docker

This project implements the docker compose to run a PostgreSQL database for relational modeling and joins.

# Implementation

Create a `.env` file with the following variables:
DB_NAME=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password

To start the PostgreSQL service, run the following command in the terminal:
docker-compose up -d

To stop the service, use:
docker-compose down