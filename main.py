from src.api_handler import APIHandler

api = APIHandler()
print(api.fetch_random_joke())
print(api.fetch_multiple_jokes(5))
print(api.fetch_joke_by_id(144))
#print(api.getUrlByID(144))