"""

Created by Colin Gelling on 03/05/2023
Using Pycharm Professional

"""


class Bootstrapper:
    def __init__(self):
        super().__init__()

        self.setup_environment()
        self.setup_database()
        self.use_database()

    @staticmethod
    def setup_environment():
        from core.Configurators.EnvironmentConfigurator import EnvironmentConfigurator
        class_instance = EnvironmentConfigurator()
        class_method = class_instance.environment()
        return class_method

    @staticmethod
    def setup_controller():
        from core.Actions.Controllers.Navigation.ViewController import ViewController
        class_instance = ViewController()
        class_method = class_instance.show_home()
        return class_method

    @staticmethod
    def setup_database():
        from core.Actions.Management.DatabaseManager import DatabaseManager
        class_instance = DatabaseManager()
        class_method = class_instance.initialize_connection()
        return class_method

    @staticmethod
    def use_database():
        from core.Actions.Management.DatabaseManager import DatabaseManager
        class_instance = DatabaseManager()
        class_method = class_instance.use_connection()
        return class_method
