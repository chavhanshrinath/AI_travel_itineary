from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itineary_chains import generate_itineary
from src.utils.lpgger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""

        logger.info("TravelPlanner initialized")

    def set_city(self, city:str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content= city))
            logger.info(f"City set to {city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException("Error setting city",e)
        
    def set_interests(self, interests_str:str):
        try:
            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content= interests_str))
            logger.info(f"Interests set to {interests_str}")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException("Error setting interests",e)
        
    def generate_itineary(self):
        try:
            logger.info(f"Generating itineary for {self.city} with interests {self.interests}")
            self.itineary = generate_itineary(self.city, self.interests)
            self.messages.append(AIMessage(content= self.itineary))
            logger.info(f"Itineary generated for {self.city} with interests {self.interests}")
            return self.itineary
        except Exception as e:
            logger.error(f"Error generating itineary: {e}")
            raise CustomException("Error generating itineary",e)
        
    def get_itineary(self):
        return self.itineary
        