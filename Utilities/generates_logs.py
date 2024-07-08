import logging

class LogGen:

    @staticmethod
    def logger():
        logg = logging.getLogger(__name__)
        filehandle = logging.FileHandler(r"//pythonProject/Logs/generate.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        filehandle.setFormatter(formatter)
        logg.addHandler(filehandle)
        logg.setLevel(logging.INFO)
        logg.setLevel(logging.DEBUG)
        return logg