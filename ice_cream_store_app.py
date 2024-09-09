# from flask import Flask, jsonify
# from flask_cors import CORS
from data_store import menu, special_offers, customer_reviews, customizations
#
# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(middleware=[
    Middleware(CORSMiddleware, allow_origins=["*"])
])


@app.get("/menu")
def get_menu():
    """
    Retrieves the menu data.

    Returns:
        A tuple containing the menu data as JSON and the HTTP status code.
    """
    return menu


@app.get("/special-offers")
def get_special_offers():
    """
    Retrieves the special offers data.

    Returns:
        A tuple containing the special offers data as JSON and the HTTP status code.
    """
    return special_offers


@app.get("/customer-reviews")
def get_customer_reviews():
    """
    Retrieves customer reviews data.

    Returns:
        A tuple containing the customer reviews data as JSON and the HTTP status code.
    """
    return customer_reviews


@app.get('/customizations')
def get_customizations():
    """
    Retrieves the customizations data.

    Returns:
        A tuple containing the customizations data as JSON and the HTTP status code.
    """
    return customizations


# if __name__ == '__main__':
#     app.run(debug=True)
