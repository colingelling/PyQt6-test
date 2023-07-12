"""

Created by Colin Gelling on 03/05/2023
Using Pycharm Professional

"""


class Bootstrapper:

    """
        This class provides important background functionality needed by the app in order to function properly
    """

    def __init__(self):
        super().__init__()

        self.setup_environment()
        self.setup_controller()
        self.setup_database()
        self.use_database()

    @staticmethod
    def setup_environment():
        from core.Environment.CollectEnvironmentalValues import CollectEnvironmentalValues
        class_instance = CollectEnvironmentalValues()
        class_method = class_instance.update_environment()
        return class_method

    @staticmethod
    def setup_controller():
        from core.Controllers.ViewController import ViewController
        class_instance = ViewController()
        class_method = class_instance.show_home()
        return class_method

    @staticmethod
    def setup_database():
        from core.Modules.ManageDatabase import ManageDatabase
        class_instance = ManageDatabase()
        class_method = class_instance.initialize_connection()
        return class_method

    @staticmethod
    def use_database():
        from core.Modules.ManageDatabase import ManageDatabase
        class_instance = ManageDatabase()
        class_method = class_instance.use_connection()
        return class_method
