class MissingWeDriver(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = args[0]

    def __str__(self):
        return f("{self.message} \n--> Please define a webdriver ")
