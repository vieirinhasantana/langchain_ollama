from langchain.prompts import PromptTemplate

ice_cream_assistant_template = """
Você é um assistente especialista em investimentos chamado "FinancePro". Sua especialidade é exclusivamente fornecer informações e orientações relacionadas a investimentos, 
produtos financeiros, retornos e dados de clientes. Isso inclui verificar os produtos financeiros que um cliente possui, 
analisar os retornos de seus investimentos, determinar se possuem múltiplas contas em diferentes instituições financeiras, 
e acessar dados por meio de open finance, se disponível. Se uma pergunta não for relacionada a investimentos ou produtos financeiros, 
responda com: "Minha especialidade é estritamente em consultas relacionadas a investimentos e finanças."
Histórico do Chat: {chat_history}
Pergunta: {question}
Resposta:"""

ice_cream_assistant_prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template=ice_cream_assistant_template
)

api_url_template = """
Dada a seguinte documentação da API oficial da loja de sorvetes Scoopsie: {api_docs}, 
extraia a URL de API mais eficiente para responder à pergunta do usuário. Se a pergunta se referir a uma busca, 
inclua a consulta como um parâmetro na URL. Se a pergunta exigir o acesso a uma conta específica, 
use o número da conta no caminho. Retorne apenas a URL da API com os parâmetros apropriados, 
sem explicações ou texto adicional.
Pergunta: {question} URL da API:
"""
api_url_prompt = PromptTemplate(input_variables=['api_docs', 'question'],
                                template=api_url_template)

api_response_template = """"
Com a Documentação da API oficial da Scoopsie: {api_docs} e a pergunta específica do usuário: {question} em mente, 
e dada esta URL da API: {api_url} para consulta, aqui está a resposta da API da Scoopsie: {api_response}. 
Forneça um resumo que responda diretamente à pergunta do usuário, 
omitindo detalhes técnicos como formato de resposta, e focando em entregar a resposta com clareza e concisão, 
como se a própria Scoopsie estivesse fornecendo essa informação.
Resumo:
"""
api_response_prompt = PromptTemplate(input_variables=['api_docs', 'question', 'api_url',
                                                      'api_response'],
                                     template=api_response_template)
