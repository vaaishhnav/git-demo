from dotenv import dotenv_values

config = dotenv_values(".env")

print(config["NAME"])
print(config["AGE"])