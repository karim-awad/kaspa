class ModuleException(Exception):

    def __init__(self, module_name, message, errors):

        # Call the base class constructor with the parameters it needs
        super(ModuleException, self).__init__(module_name + ": " + message)

        self.errors = errors