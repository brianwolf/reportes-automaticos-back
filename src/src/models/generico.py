class AppModel():
    def to_dict(self):
        self_dict = self.__dict__
        for attrname in dir(self.__class__):
            if isinstance(getattr(self.__class__, attrname), property):
                self_dict[attrname] = getattr(self, attrname)

        return self_dict
