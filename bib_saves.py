import json


# Variávéis globais ==========
saves = {}


# Retorna o caminho da pasta com o nome dado pelo Load ==========



# Salva o tipo de dados especificos dentro do ficheiro ==============
def save(Tipo_de_dados, dados):
    saves[str(Tipo_de_dados)] = dados
    with open(default_file_path, "w", encoding="utf-8") as file:
        json.dump(saves, file)

# Salva todos os dados caso a sua correspondencia esteja certa ========
def save_all():
    global saves
    with open(default_file_path, "w", encoding="utf-8") as file:
        json.dump(saves, file)


# Carrega o ficheiro anterior, USAR SEMPRE ========
def load(file_path):
    global saves, default_file_path, FirstTime
    default_file_path = file_path
    try:
        with open(default_file_path, "r", encoding="utf-8") as file:
            saves = json.load(file)
        FirstTime = False
    except FileNotFoundError:
        FirstTime = True
        print("Erro, sem save anterior.")
    except json.JSONDecodeError:
        FirstTime = True
        print("Erro, ficheiro corrompido.")
        
# Apaga o save
def saves_delete():
    global saves
    saves = {}
    save_all()

def help():
    print("""\033[0;34;33m
    1. load("file_path")  
    Loads previously saved data from the file, REQUIRED IN EVERY CODE TO RUN RIGHT.

    2. save(data_type, data)  
    Saves or updates a value in the `saves` dictionary.  
    Example: save("Money", 5000) → creates/updates the key "Money" with the value 5000.

    3. Accessing and modifying saved data  
    Use directly: bib_saves.saves["key"]  
    Examples:  
        print(bib_saves.saves["Money"])  
        bib_saves.saves["Money"] += 1000  
        bib_saves.saves["Email"] = "FakeEmail@gmail.com"

    4. saves_delete()  
    Deletes all data from memory (and optionally the file).

    5. save_all()
        Saves the dictionary updates all the keys saved (They must be in the correct interconnection).
        Example:
            bib_saves.saves = {
                "Money": Money,
                "Email": Email
            }
          
    6. help()  
    Shows this help message.

    7- Practice exemple of how to start?:
    
import bib_saves as sv

sv.load("C:/Documents/Games/Saves.json")

if not sv.saves:
    sv.save("Money", 0)
    sv.save("Level", 1)
          


    \033[0;34;33mImportant:
    - Always call load() first to retrieve old data.
    - Changes made to bib_saves.saves stay only in memory until you call save().
    - Use descriptive string keys to make the code easier to read.
    ===========================================================================================================""")
help()
 