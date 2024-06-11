import Pyfunctions, Pyvars, lib
from get_excel import get_excel
from insert_info import insert_info

def main():
    # ===========================
    #  Valida a pasta de entrada
    # ===========================

    diretorio_download = Pyvars.diretorio_download
    diretorio_json = Pyvars.diretorio_json
    nome_planilha = Pyvars.nome_planilha

    return_clean_folder = clean_folder(path_sheet=diretorio_download, path_json_status=diretorio_json, nome_planilha=nome_planilha)
    
    Pyfunctions.log_message(level=return_clean_folder["level"], message=return_clean_folder["message"])
    
    if return_clean_folder["status"] == 0:
        return
    
    elif return_clean_folder["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[main][clean_folder()] - Retorno não mapeado ao tentar abrir o Chrome: {return_clean_folder}")
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
        return

    elif return_open_chrome["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[Pyfunctions][open_chrome()] - Retorno não mapeado ao tentar abrir o Chrome: {return_open_chrome}")
        return
    
    driver = return_open_chrome["payload"]

    # ===============
    #  Fim do Módulo
    # ===============

    Pyfunctions.log_message(level="info", message="[main] - Módulo finalizado com sucesso.")
   
    # Valida se planilha já foi baixada na máquina antes.
    diretorio_json = Pyvars.diretorio_json

    with open(diretorio_json, 'r') as arquivo_json:
        dados = lib.json.load(arquivo_json)
    
    baixar_nova_planilha = dados["baixar_nova_planilha"]
    
    if baixar_nova_planilha:
        get_excel(driver=driver)
    else:
        insert_info(driver=driver)

# def clean_folder()
def clean_folder(*, path_sheet:str, path_json_status:str, nome_planilha:str) -> dict[int, str, str, None]:
    """
        - Cria a pasta de entrada caso ela não exista ou tenha sido apagada;
        - Limpa os arquivos indesejados da pasta de entrada;
        - Valida se será necessário realizar o Download da planilha ou ela já foi feita antes;

        [Args]
            path_sheet (str): Caminho onde deve ser armazenado a planilha de entrada;
            path_json_status (str): Caminho onde deve ficar o JSON informando se a planilha deve ou não ser extraida;
            nome_planilha (str): Nome padrão que a planilha é entregue (nome_planilha.xlsx);
 
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

    if not isinstance(path_json_status, str):
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
        
    # ----- Limpa arquivos indesejados na pasta de entrada ----- #
    for arquivo in lib.os.listdir(path_sheet):
        caminho_arquivo = lib.os.path.join(path_sheet, arquivo)
        
        if arquivo == nome_planilha:
            continue
        
        lib.os.remove(caminho_arquivo)

    # ----- Valida se a planilha de entrada existe na máquina ----- #
    if lib.os.listdir(path_sheet) == []:
        with open(path_json_status, 'r') as arquivo_json:
            dados = lib.json.load(arquivo_json)
        
        dados['baixar_nova_planilha'] = True
        
        with open(path_json_status, 'w') as arquivo_json:
            lib.json.dump(dados, arquivo_json, indent=4)
    
    else:
        with open(path_json_status, 'r') as arquivo_json:
            dados = lib.json.load(arquivo_json)
        
        dados['baixar_nova_planilha'] = False
        
        with open(path_json_status, 'w') as arquivo_json:
            lib.json.dump(dados, arquivo_json, indent=4)
    
    return {"status": 1,
            "level": "info",
            "message": f"[main][clean_folder()] - Pasta de entrada limpa e configurada com sucesso.", 
            "payload": None}

if __name__ == "__main__":
    main()
