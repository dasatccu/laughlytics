class Joke:
    def __init__(self,id,type,setup,punchline):
        self.__id = id
        self.__type = type
        self.__setup = setup
        self.__punchline = punchline
        self.__length = len(setup)+len(punchline)
        
    def to_dict(self):
        return {
            "id" : self.__id,
            "type" : self.__type,
            "setup" : self.__setup,
            "punchline" : self.__punchline,
        }    
    
    def __str__(self):
        return "ID :: "+str(self.__id)+" Type :: "+str(self.__type)+" Setup :: "+str(self.__setup)    