#---------------------------------------- sepecial error handler for model not existed
class ModelNotExist(Exception):
    def __init__(self,error_message):
        super().__init__(error_message)
        self.error_message=error_message
    def __str__(self):
        return f'The Error is : {self.error_message} !'