"""

Created by Colin Gelling on 09/05/2023
Using Pycharm Professional

"""

from dotenv import load_dotenv, dotenv_values


class CollectEnvironmentalValues:

    """
        This Class is all about doing tasks with the environment based on a single file (.env).
        In order to use the functionality, simply import the file in the document of choice and reach the class
        by using multiple inheritance. The @classmethod is the main functionality, this would set the next two class
        attributes.
    """

    app_credentials = {}
    db_credentials = {}

    def __init__(self):
        super().__init__()
        load_dotenv()

    @classmethod
    def update_environment(cls):

        """
            This function is for updating class Attributes and providing them with keys and values from the .env
        """

        # retrieve keys and values
        env_dict = CollectEnvironmentalValues.read_env()

        # loop through them in order to declare and separate values into groups
        for key, value in env_dict.items():
            if 'APP' in key:
                attribute = CollectEnvironmentalValues.app_credentials
                attribute.update({key: value})
            if 'DB' in key:
                attribute = CollectEnvironmentalValues.db_credentials
                attribute.update({key: value})

    @staticmethod
    def read_env():
        """
            Read the .env file and return its keys and values
        """

        env_file = '.env'
        env_dict = dotenv_values(env_file)
        return env_dict
