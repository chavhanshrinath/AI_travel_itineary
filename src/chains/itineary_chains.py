from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import OPENAI_API_KEY


llm = ChatOpenAI(
    api_key = OPENAI_API_KEY,
    model_name = "gpt-4o-mini",
    temperature=0.3
)


itnineary_prompt = ChatPromptTemplate([
    ("system" , "You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
    ("human" , "Create a itineary for my day trip")
])

def generate_itineary(city:str , interests:list[str]) -> str:
    response = llm.invoke(
        itnineary_prompt.format_messages(city=city,interests=', '.join(interests))
    )

    return response.content