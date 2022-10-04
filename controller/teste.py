import io, re, string, os
class Teste:
    def __init__(self):
        self.directory_driver = 'C:\\tmp\\Driver\\chromedriver.exe'


    def alter_driver(self):
        self.path = os.path.abspath(self.directory_driver)
        self.replacement = 'akl_roepstdlwoeproslP0weos'.encode()

        with io.open(self.path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                fh.seek(len(line), 1)
                newline = re.sub(b"cdc_.{22}", self.replacement, line)
                fh.write(newline)


teste = Teste()
teste.alter_driver()