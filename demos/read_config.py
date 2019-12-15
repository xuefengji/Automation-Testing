import configparser

class ReadConfig(object):
    #初始化读取配置文件
    def __init__(self,filename=None):
        if filename == None:
            filename = '../config/cfg.ini'
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    #获取value值
    def get_value(self,section,key):
        return self.cf.get(section,key)


if __name__=='__main__':
    read_config = ReadConfig()
    print(read_config.get_value('register','register_email'))