import Pyfunctions, Pyvars, lib
from insert_info import insert_info

def get_excel(*, driver:object):
    
    diretorio_download = Pyvars.diretorio_download
    nome_planilha = Pyvars.nome_planilha
    planilha = f"{diretorio_download}\{nome_planilha}"

    # ========================
    #  Baixa a planilha Excel
    # ========================
    
    # Valida se o botão 'Download Excel' se encontra carregado na tela.
    xpath_btn_download = "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a"
    
    return_get_element_text = Pyfunctions.get_element_text(driver=driver, xpath_element=xpath_btn_download)
    
    Pyfunctions.log_message(level=return_get_element_text["level"], message=return_get_element_text["message"])
    
    if return_get_element_text["status"] == 0:
        return
    
    elif return_get_element_text["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[Pyfunctions][get_element_text()] - Retorno não mapeado ao tentar abrir o Chrome: {return_get_element_text}")
        return
    
    # Clica no botão 'Download Excel'.
    return_click_element = Pyfunctions.click_element(driver=driver, xpath_element=xpath_btn_download)
    
    Pyfunctions.log_message(level=return_click_element["level"], message=return_click_element["message"])
    
    if return_click_element["status"] == 0:
        return
    
    elif return_click_element["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[Pyfunctions][get_element_text()] - Retorno não mapeado ao tentar abrir o Chrome: {return_click_element}")
        return
    
    # =========================
    #  Valida a planilha Excel
    # =========================
    
    diretorio_download = Pyvars.diretorio_download
    nome_planilha = Pyvars.nome_planilha
    planilha = f"{diretorio_download}\{nome_planilha}"
    
    return_validate_sheet = validate_sheet(path_sheet=planilha)
    
    Pyfunctions.log_message(level=return_validate_sheet["level"], message=return_validate_sheet["message"])
    
    if return_validate_sheet["status"] == 0:
        return
    
    elif return_validate_sheet["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[get_excel][validate_sheet()] - Retorno não mapeado ao tentar validar a planilha de entrada: {return_validate_sheet}")
        return
    
    # ===============
    #  Fim do Módulo
    # ===============

    # Passa para o módulo de Preencher o formulário.
    Pyfunctions.log_message(level="info", message="[get_excel] - Módulo finalizado com sucesso.")
    
    insert_info(driver=driver)

# def validate_sheet()
def validate_sheet(*, path_sheet:str) -> dict[int, str, str, None]:
    """
        - Valida se a planilha está apta para utilizar na operação.

        [Args]
            path_sheet (str): Caminho onde deve ser armazenado a planilha de entrada;

        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """
    
    # ---- Valida parâmetro ----- #
    if not isinstance(path_sheet, str):
        return {"status": 0,
                "level": "error",
                "message":"[get_excel][validate_sheet()] - O parâmetro de entrada 'path_sheet' está incorreto.", 
                "payload": None}
    
    # ----- Valida permissão de leitura da planilha ----- #
    try:
        df = lib.pd.read_excel(path_sheet)
    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[get_excel][validate_sheet()] - Problema ao abrir a planilha para validação: {error}", 
                "payload": None}
    
    # ----- Valida se planilha está totalmente vazia ----- #
    if df.empty:
        return {"status": 0,
                "level": "error",
                "message":"[get_excel][validate_sheet()] - A planilha de entrada se encontra totalmente vazia.", 
                "payload": None}

    # ----- Valida se todos os campos da planilha são nulos (NaN) ----- #
    if df.isnull().values.all():
        return {"status": 0,
                "level": "error",
                "message":"[get_excel][validate_sheet()] - A planilha de entrada contêm todos os valores nulos NaN.", 
                "payload": None}
    
    return {"status": 1,
            "level": "info",
            "message":"[get_excel][validate_sheet()] - Planilha de entrada validada com sucesso.", 
            "payload": None}

if __name__ == "__main__":
    get_excel(driver="")
