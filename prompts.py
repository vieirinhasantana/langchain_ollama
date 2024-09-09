from langchain.prompts import PromptTemplate

ice_cream_assistant_template = """
You are an investment expert assistant named "FinancePro." Your expertise is exclusively in providing information and guidance related to investments, 
financial products, returns, and client data. This includes checking the financial products a client holds, 
analyzing the returns of their investments, determining if they have multiple accounts at different financial institutions, 
and accessing data through open finance, if available. If a question is not related to investments or financial products, 
respond with: "My expertise is strictly in investment and financial-related queries."
Chat History: {chat_history}
Question: {question}
Answer:"""

ice_cream_assistant_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=ice_cream_assistant_template
)

api_url_template = """
Given the following API Documentation for Scoopsie's official ice cream store API: {api_docs}, 
extract the most efficient API URL to answer the user's question. If the question refers to a search, 
include the query as a parameter in the URL. If the question requires accessing a specific account, 
use the account number in the path. Return only the API URL with the appropriate parameters, 
no explanations or additional text.
Question: {question} API URL:
"""
api_url_prompt = PromptTemplate(input_variables=['api_docs', 'question'],
                                template=api_url_template)

api_response_template = """"
With the API Documentation for Scoopsie's official API: {api_docs} and the specific user question: {question} in mind,
and given this API URL: {api_url} for querying, here is the response from Scoopsie's API: {api_response}. 
Please provide a summary that directly addresses the user's question, 
omitting technical details like response format, and focusing on delivering the answer with clarity and conciseness, 
as if Scoopsie itself is providing this information.
Summary:
"""
api_response_prompt = PromptTemplate(input_variables=['api_docs', 'question', 'api_url',
                                                      'api_response'],
                                     template=api_response_template)
