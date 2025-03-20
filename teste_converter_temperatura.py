import logging

logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')

def celsius_para_fahrenheit(celsius):
    logging.info(f"Convertendo {celsius}°C para Fahrenheit. ")
    fahrenheit = celsius * 9/5 +32
    logging.info(f"Resultado: {fahrenheit}°F")
    return fahrenheit

celsius_para_fahrenheit(25)
celsius_para_fahrenheit(-10)