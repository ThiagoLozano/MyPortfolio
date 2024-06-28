import Pyfunctions, Pyvars, lib
from get_excel import get_excel
from insert_info import insert_info

def main():
    # ======================================
    #  Valida os diretórios de Excel e JSON
    # ======================================

    name_sheet = Pyvars.name_sheet
    name_json = Pyvars.name_json
    diretorio_download = Pyvars.diretorio_download
    diretorio_json = Pyvars.diretorio_json
    
    if diretorio_download == "":
        diretorio_download = str(lib.Path.home()) + "\Downloads"

    return_validate_folders= validate_folders(path_sheet=diretorio_download, path_json=diretorio_json, name_sheet=name_sheet, name_json=name_json)

    Pyfunctions.log_message(level=return_validate_folders["level"], message=return_validate_folders["message"])
    
    if return_validate_folders["status"] == 0:
        return
    
    elif return_validate_folders["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[main][validate_folders()] - Retorno não mapeado ao tentar abrir o Chrome: {return_validate_folders}")
        return

    # =============================
    #  Configura o ambiente Chrome
    # =============================

    return_config_chrome = Pyfunctions.config_chrome(dir_download=diretorio_download)
    
    Pyfunctions.log_message(level=return_config_chrome["level"], message=return_config_chrome["message"])

    if return_config_chrome["status"] == 0:
        return
    
    elif return_config_chrome["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[Pyfunction][config_chrome()] - Retorno não mapeado ao tentar abrir o Chrome: {return_config_chrome}")
        return

    config_chrome = return_config_chrome["payload"]

    # ===============
    #  Abre o Chrome
    # ===============

    url_rpachallenge = Pyvars.url_rpachallenge

    return_open_chrome = Pyfunctions.open_chrome(url=url_rpachallenge, options=config_chrome)
    
    Pyfunctions.log_message(level=return_open_chrome["level"], message=return_open_chrome["message"])
    
    if return_open_chrome["status"] == 0:
        return_open_chrome.quit()
        return

    elif return_open_chrome["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[Pyfunctions][open_chrome()] - Retorno não mapeado ao tentar abrir o Chrome: {return_open_chrome}")
        return_open_chrome.quit()
        return
    
    driver = return_open_chrome["payload"]

    # ===============
    #  Fim do Módulo
    # ===============

    Pyfunctions.log_message(level="info", message="[main] - Módulo finalizado com sucesso.")
   
    full_path_json = lib.os.path.join(diretorio_json, name_json)

    # Verifica se planilha já foi baixada na máquina antes.
    with open(full_path_json, 'r') as arquivo_json:
        dados = lib.json.load(arquivo_json)
    
    baixar_nova_planilha = dados["baixar_nova_planilha"]
    
    if baixar_nova_planilha:
        get_excel(driver=driver)
    else:
        insert_info(driver=driver)
    
# def validate_folders()
def validate_folders(*, path_sheet:str, path_json:str, name_sheet:str, name_json:str) -> dict[int, str, str, None]:
    """
        - Cria a pasta de entrada caso ela não exista ou tenha sido apagada;
        - Limpa os arquivos indesejados da pasta de entrada;
        - Valida se será necessário realizar o Download da planilha ou ela já foi feita antes;

        [Args]
            path_sheet (str): Caminho onde deve ser armazenado a planilha de entrada;
            path_json (str): Caminho onde deve ficar o JSON informando se a planilha deve ou não ser extraida;
            name_sheet (str): Nome padrão que a planilha é entregue (nome_planilha.xlsx);
            name_json (str): Nome padrão do arquivo JSON;
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """
    
    # ----- Valida parâmetro ----- #
    if not isinstance(path_sheet, str):
        return {"status": 0,
                "level": "error",
                "message":"[main][clean_folder()] - O parâmetro de entrada 'path_sheet' está incorreto.", 
                "payload": None}

    if not isinstance(path_json, str):
        return {"status": 0,
                "level": "error",
                "message":"[main][clean_folder()] - O parâmetro de entrada 'path_json_status' está incorreto.", 
                "payload": None}

    # ----- Cria a pasta que deve receber a planilha Excel de entrada ----- #
    try:
        lib.os.makedirs(path_sheet, exist_ok=True)
    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[main][clean_folder()] - Problema ao tentar criar a pasta de entrada: {error}", 
                "payload": None}
    
    # ----- Cria a pasta que deve receber o status de extração da planilha ----- #

    try:
        lib.os.makedirs(path_json, exist_ok=True)
    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[main][clean_folder()] - Problema ao tentar criar a pasta de entrada: {error}", 
                "payload": None}
    
    # ----- Cria o arquivo JSON caso ele não exista ----- #

    full_path_json = lib.os.path.join(path_json, name_json)
    
    if not lib.os.path.exists(full_path_json):
        
        data = {
            "baixar_nova_planilha": ""
        }
    
        with open(full_path_json, 'w') as arquivo:
            lib.json.dump(data, arquivo, indent=4)

    # ----- Valida se a planilha precisa ser baixada ou não ----- #
    try:
    
        with open(full_path_json, 'r') as arquivo_json:
            dados = lib.json.load(arquivo_json)

        dados['baixar_nova_planilha'] = True if not name_sheet in lib.os.listdir(path_sheet) else False
        
        with open(full_path_json, 'w') as arquivo_json:
            lib.json.dump(dados, arquivo_json, indent=4)
    
    except FileNotFoundError as error:
        return {"status": 0,
                "level": "error",
                "message": f"[main][clean_folder()] - Arquivo não localizado na máquina: {error}", 
                "payload": None}
    except lib.json.JSONDecodeError as error:
        return {"status": 0,
                "level": "error",
                "message": f"[main][clean_folder()] - Arquivo JSON inválido: {error}", 
                "payload": None}
    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[main][clean_folder()] - Problema ao validar download da planilha: {error}", 
                "payload": None}
    
    return {"status": 1,
            "level": "info",
            "message": f"[main][clean_folder()] - Pasta de entrada limpa e configurada com sucesso.", 
            "payload": None}

if __name__ == "__main__":
    main()
