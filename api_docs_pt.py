import json

scoopsie_api_docs = {
    "base_url": "http://localhost:5000/",
    "endpoints": {
        "/client/search": {
            "method": "GET",
            "description": "Recuperar o cliente usando parâmetros.",
            "parameters": "Usando o parâmetro de consulta, você pode realizar buscas.",
            "response": {
                "description": "Um objeto JSON contendo informações resumidas de todos os clientes encontrados com base nos parâmetros enviados.",
                "content_type": "application/json"
            }
        },
        "/client/detail": {
            "method": "GET",
            "description": "Recuperar detalhes da conta de investimento.",
            "parameters": None,
            "response": {
                "description": "Um objeto JSON que detalha todos os investimentos do cliente.",
                "content_type": "application/json"
            }
        },
        # "/customer-reviews": {
        #     "method": "GET",
        #     "description": "Recuperar avaliações de clientes para a loja de sorvetes.",
        #     "parameters": None,
        #     "response": {
        #         "description": "Um objeto JSON contendo avaliações de clientes, classificações e comentários.",
        #         "content_type": "application/json"
        #     }
        # },
        # "/customizations": {
        #     "method": "GET",
        #     "description": "Recuperar personalizações de sorvetes disponíveis.",
        #     "parameters": None,
        #     "response": {
        #         "description": "Um objeto JSON listando personalizações disponíveis, como coberturas e opções sem açúcar.",
        #         "content_type": "application/json"
        #     }
        # }
    }
}

scoopsie_api_docs = json.dumps(scoopsie_api_docs)