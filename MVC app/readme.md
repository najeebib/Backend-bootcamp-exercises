# FastAPI Server with Authentication and Product Display

This FastAPI server provides authentication functionality along with a page for displaying products.

## Project Structure

The project consists of the following components:

### Server

- **`server.py`:** Initializes the FastAPI server and includes routes for authentication and products.
- **Middleware:** Includes middleware for logging requests.

### Routes

- **`auth_route.py`:** Defines routes related to user authentication, such as sign-in.
- **`products_route.py`:** Contains routes for displaying products.

### Utilities

- **`auth_functions.py`:** Contains functions related to user authentication, such as password hashing and JWT token generation.
- **`db_functions.py`:** Provides functions for loading and saving data from/to JSON files.

### Templates

- **`login.html`:** HTML template for user sign-in.
- **`products.html`:** HTML template for displaying products.
- **`logout.html`:** HTML template for user sign-out.

### Static Files

- **`login.css`:** CSS file for styling the sign-in page.
- **`products.css`:** CSS file for styling the product display page.
- **`login.js`:** JavaScript file for client-side functionality of the sign-in page.
- **`products.js`:** JavaScript file for client-side functionality of the product display page.

## How to Run

1. Start the FastAPI server using `uvicorn server:app --reload`.
2. Access the sign-in page at `http://localhost:8000/sign_in` to log in.
3. Upon successful login, you will be redirected to the product display page at `http://localhost:8000/products`.
4. You can log out by clicking the "Log out" button on the product display page.

## Endpoints

- **Authentication Endpoints:**
  - `POST /sign_in`: Sign in a user.
  - `OPTIONS /sign_in`: Handle OPTIONS request for CORS.
- **Product Endpoints:**
  - `GET /products`: Retrieve and display available products.

## HTML Templates

- **`login.html`:** Provides a user interface for signing in.
- **`products.html`:** Displays products retrieved from the server.
- **`logout.html`:** Confirms successful logout.

## Styling

- **`login.css`,**`logout.css`  and `products.css`:** Define the styles for the sign-in and product display pages, respectively.

## JavaScript

- **`login.js`:** Contains client-side JavaScript code for handling user sign-in functionality.
- **`products.js`:** Contains client-side JavaScript code for handling user logout functionality.

