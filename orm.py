#coding: utf-8

class Field(object):
    def __init__(self,name,clumn_type):
        self.name = name
        self.clumn_type = clumn_type

    def __str__(self):
        return '<%s:%s>'%(self.__class__.__name__,self.name)

class IntegerFileld(Field):
    def __init__(self,name):
        super(IntegerFileld,self).__init__(name,'varcahr(100)')

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'bigint')

class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print 'Find model:%s'% name
        mapping = {}
        for k,v in attrs.items():
            if isinstance(v,Field):
                print 'Found mapping:%s==>%s'%(k,v)
                mapping[k]=v
        for k in mapping.keys():
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'Model object has no attribute %s'%key)
    def __setattr__(self,key,value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mapping__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerFileld('pk')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


u = User(pk=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

