import importlib


class ViewCreator:
    @staticmethod
    def set_authentication(mapping, authenticated):
        # check authentication value and set the correct method
        if authenticated == "yes":
            mapping.authenticated()
        else:
            mapping.not_authenticated()

    @staticmethod
    def validate_navigation_pattern(mapping):
        # check if the mapping attribute has been filled
        if not mapping.navigation_pattern:
            raise ValueError("Navigation pattern has not been set")

    @staticmethod
    def validate_view_data(view_data, view_name):
        # check if the information is there
        if not view_data:
            raise ValueError(f"View data not found for view: {view_name}")

    @staticmethod
    def validate_view_class(view_class, view_name):
        # check if the class definition has value
        if not view_class:
            raise ValueError(f"View class not specified for view: {view_name}")

    @staticmethod
    def get_view_module(view_class, authenticated):
        # set different folder for authenticated views
        if authenticated == "yes":
            return f"views.Auth.{view_class}"
        elif authenticated == "no":
            return f"views.{view_class}"
        else:
            raise ValueError("Authentication value has not been set properly.")

    @staticmethod
    def import_view(view_module, view_class, view_name):
        # attempt to import the view
        try:
            module_import = importlib.import_module(view_module)
            view_class = getattr(module_import, view_class)
            view = view_class()
            return view
        except (ImportError, AttributeError) as e:
            print(f"Error creating view: {view_name}. {str(e)}")
            return None

    @staticmethod
    def setup_connections(view, connections):
        # retrieve connections (switches from views) and bind them to specific views
        if connections:
            for connection in connections:
                switch, connected_view = connection
                switch_attr = getattr(view, switch, None)
                if switch_attr is not None:
                    from core.Actions.Controllers.Navigation.NavigationController import NavigationController
                    switch_attr[str].connect(lambda cv=connected_view: NavigationController.set_view(cv, connection))

                else:
                    print(f"Switch attribute '{switch}' not found in the view")
