import importlib


class ViewCreator:
    @staticmethod
    def set_authentication(mapping, authenticated):
        """
            Execute matching functionality based up on the authentication
        """

        if authenticated == "yes":
            mapping.authenticated()
        else:
            mapping.not_authenticated()

    @staticmethod
    def validate_navigation_pattern(mapping):

        """
            Verify view and window information values
        """

        if not mapping.navigation_pattern:
            raise ValueError("Navigation pattern has not been set")

    @staticmethod
    def validate_view_data(view_data, view_name):
        """
            Verify that the information exists and has been set properly
        """

        if not view_data:
            raise ValueError(f"View data not found for view: {view_name}")

    @staticmethod
    def validate_view_class(view_class, view_name):
        """
            Verify that the class definition has value
        """

        if not view_class:
            raise ValueError(f"View class not specified for view: {view_name}")

    @staticmethod
    def get_view_module(view_class, authenticated):
        """
            Set different folder for authenticated views
        """

        if authenticated == "yes":
            return f"views.Auth.{view_class}"
        elif authenticated == "no":
            return f"views.{view_class}"
        else:
            raise ValueError("Authentication value has not been set properly.")

    @staticmethod
    def import_view(view_module, view_class, view_name):

        """
            Import module and return view
        """

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
        """
            Set up window relations: switching between windows and views, provide connections
        """

        if connections:
            for connection in connections:
                switch, connected_view = connection
                switch_attr = getattr(view, switch, None)
                if switch_attr is not None:
                    from core.Actions.Controllers.Navigation.NavigationController import NavigationController
                    switch_attr[str].connect(lambda cv=connected_view: NavigationController.set_view(cv, connection))

                else:
                    print(f"Switch attribute '{switch}' not found in the view")
