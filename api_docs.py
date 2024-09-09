import json

scoopsie_api_docs = {
    "base_url": "http://localhost:5000/",
    "endpoints": {
        "/client/search": {
            "method": "GET",
            "description": "Retrieve the client using parameters.",
            "parameters": "Using the query parameter you can perform searches",
            "response": {
                "description": "A JSON object containing summary information for all clients found based on the parameters sent.",
                "content_type": "application/json"
            }
        },
        "/client/detail": {
            "method": "GET",
            "description": "Retrieve investment account details",
            "parameters": None,
            "response": {
                "description": "A JSON object that details all of the customer's investments.",
                "content_type": "application/json"
            }
        },
        # "/customer-reviews": {
        #     "method": "GET",
        #     "description": "Retrieve customer reviews for the ice cream store.",
        #     "parameters": None,
        #     "response": {
        #         "description": "A JSON object containing customer reviews, ratings, and comments.",
        #         "content_type": "application/json"
        #     }
        # },
        # "/customizations": {
        #     "method": "GET",
        #     "description": "Retrieve available ice cream customizations.",
        #     "parameters": None,
        #     "response": {
        #         "description": "A JSON object listing available customizations like toppings and sugar-free options.",
        #         "content_type": "application/json"
        #     }
        # }
    }
}

scoopsie_api_docs = json.dumps(scoopsie_api_docs)
