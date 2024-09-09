# from flask import Flask, jsonify
# from flask_cors import CORS
from data_store import search_customer, detail_customer
#
# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})

from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(middleware=[
    Middleware(CORSMiddleware, allow_origins=["*"])
])


@app.get("/client/search")
def get_search_customer(query=None, q=None):
    if not query and not q:
        return {"result": []}
    result_filter = [x for x in search_customer.get('result') if x.get('name').lower().find(query.lower()) >= 0]
    return result_filter


@app.get("/client/detail/{accountId}")
def get_customer_detail(accountId = None):
    if not accountId:
        return {"result": []}
    result_filter = detail_customer if detail_customer.get('result', {}).get('accountId') == accountId else {"result": []}
    return result_filter


# @app.get("/customer-reviews")
# def get_customer_reviews():
#     """
#     Retrieves customer reviews data.
#
#     Returns:
#         A tuple containing the customer reviews data as JSON and the HTTP status code.
#     """
#     return customer_reviews
#
#
# @app.get('/customizations')
# def get_customizations():
#     """
#     Retrieves the customizations data.
#
#     Returns:
#         A tuple containing the customizations data as JSON and the HTTP status code.
#     """
#     return customizations
#
#
# # if __name__ == '__main__':
# #     app.run(debug=True)

### fastapi dev ice_cream_store_app.py --port=5000