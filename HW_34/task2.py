
import os

class CustomConfigParser:
    def __init__(self):
        self._config = {}

    def read(self, filepath):
        self._config.clear()
        file=None
        try:
            file = open(filepath, 'r')
            current=''
            for i , s in enumerate (file):
                if s[0]=='[':
                    current = s[1:s.index(']')]
                    self._config[current]={ }
                elif s == '\n':
                    continue
                else:
                    key,value=s.replace('\n','').split(' = ')
                    if any(not c.isalnum()for c in key):
                        #проверка на то , что все сим ключа являются буквами или ц
                        raise ValueError (f"Invalid line in config file: {i+1}")
                    self._config[current][key]=value
            file.close()
            print(self._config)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filepath} not found")
        except ValueError as e:
            file.close()
            raise

    def get(self, section, key):
         if section in self._config and key in self._config[section]:
             print (key)
         else:
             raise KeyError

    def set(self, section, key, value):
      if section in self._config:
          if key in self._config[section]:
              self._config[section][key]=value
          elif key not in self._config[section]:
              self._config[section].setdefault(key,value)
      elif section not in self._config:
          self._config.setdefault(section, {key : value})
      print(self._config)

    def add_section(self, section):
        self._config.setdefault(section, {})

    def remove_section(self, section):
        if section in self._config:
            del self._config[section]
        elif section not in self._config:
            raise KeyError

    def remove_option(self, section, key):
        if section in self._config and key in self._config[section]:
            del self._config[section][key]
        elif section or key in self._config[section] not in self._config:
            raise KeyError

    def write(self, filepath):
            with open(filepath, 'w') as file:
                config_lines = []
                for section, contents in self._config.items():
                    config_lines.append(f"[{section}]")
                    for key, value in contents.items():
                        config_lines.append(f"{key} = {value}")
                    config_lines.append("")  # пустую строку после секции

                config_string = "\n".join(config_lines)
                file.write(config_string)


Alice = CustomConfigParser()
Alice.read('y.configus')
Alice.get('database', 'username')
Alice.set('server', 'host', 'apppp')
Alice.write('y.configus')