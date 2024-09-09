# Example menu, special offers, customer reviews, and customizations

search_customer = {
    # "flavors": [
    #     {"flavorName": "Strawberry", "count": 50},
    #     {"flavorName": "Chocolate", "count": 75}
    # ],
    # "toppings": [
    #     {"toppingName": "Hot Fudge", "count": 50},
    #     {"toppingName": "Sprinkles", "count": 2000},
    #     {"toppingName": "Whipped Cream", "count": 50}
    # ]
    "result": [
      {
        "name": "Alba Veiga Vasconcellos",
        "accountId": "000617091",
        "document": "54624695275"
      },
      {
        "name": "Cassio Estevam Valansuela",
        "accountId": "000456785",
        "document": "53199483283"
      },
      {
        "name": "Ariel Darmont dos Anjos",
        "accountId": "00083726",
        "document": "74195277760"
      },
      {
        "name": "Ariel dos Anjos",
        "accountId": "000464631",
        "document": "37695991368"
      }
    ]
}

detail_customer = {
    "result": {
        "name": "Ariel Darmont dos Anjos",
        "accountId": "00083726",
        "document": "74195277760",
        "summary": {
            "investmentFund": {
                "grossValue": 2600,
                "netValue": 2440
            },
            "fixedIncome": {
                "grossValue": 1300,
                "netValue": 1000
            },
            "equity": {
                "grossValue": 10130,
                "netValue": 10130
            }
        },
        "products": {
            "fixedIncome": [
                {
                    "name": "CDB Banco Agora - 14,7% PRÉ",
                    "issuer": "BANCO MASTER",
                    "grossValue": 1300,
                    "netValue": 1000,
                    "dueDate": "2027/09/09",
                    "profitabilityPercent": 43.20
                }
            ],
            "investmentFund": [
                {
                    "name": "MOLLITIAM PREVIDÊNCIA ICATU QUALIFICADO FIM CP",
                    "cnpj": "41082931000163",
                    "grossValue": 2600,
                    "netValue": 2440,
                    "classification": {
                        "class": "pension",
                        "subclass": "Free Multimarket"
                    }
                }
            ],
            "equity": [
                {
                    "name": "Petrobrás",
                    "ticker": "PETR4",
                    "grossValue": 10130,
                    "netValue": 10130
                }
            ]
        }
    }
}

# customer_reviews = {
#     "reviews": [
#         {"userName": "andrew_1", "rating": 5, "comment": "Loved the chocolate flavor!"},
#         {"userName": "john", "rating": 4, "comment": "Great place, but always crowded."},
#         {"userName": "allison", "rating": 5, "comment": "Love the ice-creams and Scoopsie is super helpful!"}
#     ]
# }
#
# customizations = {
#     "options": [
#         {"customizationName": "Sugar-Free", "details": "Available for most flavors."},
#         {"customizationName": "Extra Toppings", "details": "Choose as many toppings as you want for an extra $5!"}
#     ]
# }
