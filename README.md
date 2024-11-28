# ETL Testing Environment

This project sets up an ETL (Extract, Transform, Load) testing environment using Docker. It includes an API server and three different database services: MongoDB, MSSQL, and PostgreSQL.

## Services

### API Server
A Flask-based API server that provides endpoints to interact with sample data.

- **Endpoints**:
  - `GET /data`: Returns a subset of the sample data. The number of items returned can be controlled using the `limit` query parameter.
  - `GET /data/<int:item_id>`: Returns a specific item from the sample data based on the provided `item_id`. If the item is not found, it returns a 404 error.
  - `POST /data`: Simulates adding a new item to the sample data. The new item's `name` and `value` are taken from the JSON payload of the request. The new item is assigned an `id` that is one greater than the current maximum `id` in the sample data.

### MongoDB
A NoSQL database service.

- **Port**: 27017
- **Environment Variables**:
  - `MONGO_INITDB_ROOT_USERNAME`: root
  - `MONGO_INITDB_ROOT_PASSWORD`: password

### MSSQL
A Microsoft SQL Server database service.

- **Port**: 1433
- **Environment Variables**:
  - `SA_PASSWORD`: YourStrong@Passw0rd
  - `ACCEPT_EULA`: Y
  - `MSSQL_TCP_PORT`: 1433
  - `MSSQL_PID`: Express

### PostgreSQL
A relational database service.

- **Port**: 5432
- **Environment Variables**:
  - `POSTGRES_USER`: user
  - `POSTGRES_PASSWORD`: password
  - `POSTGRES_DB`: testdb

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Build and start the services**:
    ```sh
    docker-compose up --build
    ```

3. **Access the API server**:
    - The API server will be available at `http://localhost:5001`.

## Usage

- **API Endpoints**:
  - `GET /data`: Retrieve a subset of sample data.
  - `GET /data/<int:item_id>`: Retrieve a specific item by ID.
  - `POST /data`: Add a new item to the sample data.

## Notes

- Ensure Docker and Docker Compose are installed on your system.
- Modify the `docker-compose.yml` file to change environment variables or ports as needed.

## License

This project is licensed under the MIT License.