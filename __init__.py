class MyDBRouter(object):
    def db_for_read(self, model, **hints):
        return self.__app_router(model)

    def db_for_write(self, model, **hints):
        return self.__app_router(model)

    def allow_relation(self, obj1, obj2, **hints):
        #return obj1._meta.app_label == obj2._meta.app_label
        return True

    def allow_syncdb(self, db, model):
        return self.__app_router(model) == db

    def __app_router(self, model):
        # Can also be written like this,it also works well
        # if model.__name__ == 'test2':
        
        
        if model._meta.app_label.startswith('wikileaks'):
            return 'wikileaks'  
        if model._meta.app_label.startswith('boundaryservice'):
            return 'boundaryservice'  
               
        return 'default'

