class Screen:
    def main(self):
        classname = "'" + str(self.__class__).split('.')[1].split('>')[0]
        raise NotImplementedError(f"method 'main' in class {classname} not implemented")

    def __call__(self, *args, **kwargs):
        return self.main()
