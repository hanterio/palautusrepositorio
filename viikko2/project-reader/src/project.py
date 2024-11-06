class Project:
    def __init__(self, name, description, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        print(str(alkio) for alkio in self._stringify_dependencies(self.dependencies))
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            #Mietin että laittaisko luokan default-arvoiksi tuon lisenssin ja authorsit, mutta tein näin. Mitäköhän tässä haettiin? 
            f"\nLicense: MIT"
            f"\n\nAuthors:"
            f"\n- Matti Luukkainen"
            f"\n- Kalle Ilves"
            f"\n\nDependencies: \n- {self._stringify_dependencies(self.dependencies).split(",")[0]}"
            f"\n-{self._stringify_dependencies(self.dependencies).split(",")[1]}"
            f"\n-{self._stringify_dependencies(self.dependencies).split(",")[2]}"
            f"\n\nDevelopment dependencies: "
            f"\n- {self._stringify_dependencies(self.dev_dependencies).split(",")[0]}"
            f"\n-{self._stringify_dependencies(self.dev_dependencies).split(",")[1]}"
            f"\n-{self._stringify_dependencies(self.dev_dependencies).split(",")[2]}"
            f"\n-{self._stringify_dependencies(self.dev_dependencies).split(",")[3]}"
        )
