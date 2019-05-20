
class Config():

    configs = {}
    #initializer
    def __init__(self):
        try :
            self.file = open("config.txt","r")
            data = self.file.read()
            self.file.close()
            lines = data.split('\n')
            for line in lines:
                keyByValue = line.split('=')
                if len(keyByValue) == 2:
                    self.configs[keyByValue[0]] = keyByValue[1]
        except:
            print("파일 읽기 에러")
            exit()


    def set(self, key, value):
        try :
            self.file = open("config.txt","w")
            self.configs[key] = value
            for key,value in self.configs.items():
                self.file.write(key+"="+value+"\n")
            self.file.close()
        except:
            print("파일 쓰기 에러")
            exit()


    def get(self, key):
        if key in self.configs.keys():
            return self.configs[key]
        else:
            return False

config = Config()
