import requests

class APIHandler:
    __baseURI = "https://official-joke-api.appspot.com/jokes"
    
    def __getRandomUrl(self,count):
        self.__number=str(count)
        return self.__baseURI + "/random/" + self.__number
    
    def __getUrlByID(self,id):
        jokeId = str(id)
        return self.__baseURI +"/"+ jokeId  
    
    def fetch_random_joke(self):
        try:
            return requests.get(self.__getRandomUrl(1)).json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your network.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
    
    def fetch_multiple_jokes(self,count):
        try:
            return requests.get(self.__getRandomUrl(count)).json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your network.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
            
    def fetch_joke_by_id(self,joke_id):
        try:
            return requests.get(self.__getUrlByID(joke_id)).json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your network.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")     
    
        