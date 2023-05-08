class fmtSQL:

    def __init__(self, cmd=''):
        # crnt cmd
        self.__cmd = str(cmd)
        # define key words
        self.__select = 'SELECT'
        self.__update = 'UPDATE'
        self.__insert_into = 'INSERT INTO'
        self.__values =   'VALUES'
        self.__from =   'FROM'
        self.__where =  'WHERE'
        self.__as =     'AS'
        self.__set =    'SET'
        self.__delete =    'DELETE'

    def append(self, arg):
        self.__cmd =  self.__cmd + ' ' + str(arg)

    def UPDATE(self, table):
        self.append(self.__update)
        self.append(table)
        return self

    def VALUES(self, vals):
        self.append(self.__values)
        self.append(vals)
       #lvals = '('
       #for c in vals:
       #    lvals = lvals + c + ','
       #lvals = lvals[:-1] + ')'
       #self.append(lvals)

        return self

    def INSERT_INTO(self, table, cols):
        self.append(self.__insert_into)
        self.append(table)
        self.append(cols)
       #lcols = '('
       #for c in cols:
       #    lcols = lcols + c + ','
       #lcols = lcols[:-1] + ')'
       #self.append(lcols)

        return self

    def SELECT(self, col='*'):
        self.append(self.__select)
        self.append(col)

        return self

    def FROM(self, table):
        self.append(self.__from)
        self.append(table)
        return self

    def WHERE(self, arg):
        self.append(self.__where)
        self.append(arg)
        return self

    def AS(self, name):
        self.append(self.__as)
        self.append(name)
        return self

    def SET(self, arg):
        self.append(self.__set)
        self.append(arg)
        return self

    def DELETE(self):
        self.append(self.__delete)
        return self

    def set_cmd(self, cmd):
        self.__cmd = cmd

    def get_cmd(self):
        return self.__cmd

    def __str__(self):
        return self.get_cmd()

#### EXEMPLO ####
# fmt = fmtSQL()
# fmt.SELECT().FROM('universos_paralelos').WHERE('eu = bonito')
#
#     cmd = str(fmt)
#     ou 
#     cmd = fmt.get_cmd()
