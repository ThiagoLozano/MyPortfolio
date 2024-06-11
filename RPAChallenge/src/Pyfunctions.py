import lib
import Pyvars

# def log_message()
def log_message(path_dir_logs:str=Pyvars.diretorio_logs, *, level:str, message:str) -> str:
    """
        - Insere mensagens em arquivo de LOG.

        [Args]
            path_dir_logs (str): Caminho onde o arquivo LOG deve ser registrado e salvo;
            level (str): Informação de nível da mensagem (debug, info, warning, error, critical);
            message (str): Informação que deve ser ergistrada no LOG;
 
        [Returns]
            Sem retorno
    """
    # Valida se o diretório de LOG existe.
    lib.os.makedirs(lib.os.path.dirname(path_dir_logs), exist_ok=True)

    # Define o nome e caminho do arquivo de log.
    data_atual = lib.datetime.now().strftime("%d_%m_%Y")
    log_file_name = f"{data_atual}.log"
    log_file_path = f"{path_dir_logs}\{log_file_name}"

    # Configura o LOG.
    lib.logging.basicConfig(filename=log_file_path, level=lib.logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
    
    logger = lib.logging.getLogger()
    log_levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if level in log_levels:
        log_levels[level](message)
    else:
        raise ValueError(f"Nível de log desconhecido: {level}")

# def config_chrome()
def config_chrome(*, dir_download:str) -> dict[int, str, str, None]:
    """
        - Configura o webdriver com as opções desejadas.

        [Args]
            dir_download (str): Local na máquina onde serão guardados as planilhas de entrada.
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """

    # ----- Valida parâmetro ----- #
    if not isinstance(dir_download, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][config_chrome()] - O parâmetro de entrada 'dir_download' está incorreto.", 
                "payload": None}
    
    # ----- Valida diretório ----- #
    if not lib.os.path.exists(dir_download) or not lib.os.path.isdir(dir_download):
        return {"status":  0,
                "level": "error",
                "message": f"[Pyfunctions][config_chrome()] - O diretório '{dir_download}' não existe ou não foi localizado com sucesso." , 
                "payload": None}

    # ----- Configura o Webdriver ----- #
    chrome_options = lib.Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('prefs', {"download.default_directory": dir_download})

    return {"status": 1,
            "level": "info",
            "message": "[Pyfunctions][config_chrome()] - Webdriver Chrome configurado com sucesso." , 
            "payload": chrome_options}

# def open_chome()
def open_chrome(*, url:str, options:object) -> dict[int, str, str, None]:
    """
        - Abre o site informado e anexa as configurações de uso do Chrome.

        [Args]
            url (str): Endereço do site utilizado na operação;
            options (obj): Configurações de Webdriver que devem ser anexadas no Chrome ao iniciar o navegador;
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """
    
    # ----- Valida parâmetro ----- #
    if not isinstance(url, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][open_chrome()] - O parâmetro de entrada 'url' está incorreto.", 
                "payload": None}
        
    if not isinstance(options, object):
        return {"status": 0,
                "level": "error", 
                "message":"[Pyfunctions][open_chrome()] - O parâmetro de entrada 'options' está incorreto.", 
                "payload": None}
        
    # ----- Abre o Chrome ----- #
    try:
        driver = lib.webdriver.Chrome(options=options)
        driver.get(url)
    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[Pyfunctions][open_chrome()] - Problema ao tentar abrir o Chrome: {error}",
                "payload": None}

    return {"status": 1,
            "level": "info",
            "message": "[Pyfunctions][open_chrome()] - Chrome aberto com sucesso." , 
            "payload": driver}

# def get_element_text()
def get_element_text(timeout:int=30, *, driver:object, xpath_element:str) -> dict[int, str, str, None]:
    """
        - Busca um elemento XPATH na página para validar se está na página correta e se a mesma está carregada.

        [Args]
            timeout (int): Tempo que a função terá para validar ser o elemento existe na tela.
            driver (str): Configurações de conexão do Chrome;
            xpath_element (str): Elemento que deve ser buscado na tela;
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """
    
    # ----- Valida parâmetro ---- #
    if not isinstance(timeout, int):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][get_element_text()] - O parâmetro de entrada 'timeout' está incorreto.", 
                "payload": None}
    
    if not isinstance(driver, object):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][get_element_text()] - O parâmetro de entrada 'driver' está incorreto.", 
                "payload": None}
    
    if not isinstance(xpath_element, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][get_element_text()] - O parâmetro de entrada 'xpath_element' está incorreto.", 
                "payload": None}
    
    # ----- Busca o elemento na tela ----- #
    clock = 0
    
    while clock != timeout:
        try:
            driver.find_element(by=lib.By.XPATH, value=xpath_element)
            return {"status": 1,
                    "level": "info",
                    "message": f"[Pyfunctions][get_element_text()] - Elemento texto '{xpath_element}' localizado com sucesso.", 
                    "payload": None}
        
        except Exception:
            lib.time.sleep(5)
            clock += 1
            continue
    
    return {"status": 0,
            "level": "error",
            "message": f"[Pyfunctions][get_element_text()] - Timeout ao buscar elemento '{xpath_element}' na tela.", 
            "payload": None}

# def click_element()
def click_element(driver:object, xpath_element:str) -> dict[int, str, str, None]:
    """
        - Clica no elemento XPATH.

        [Args]
            driver (int): Configurações de conexão do Chrome;
            xpath_element (str): Elemento que deve ser clicado na tela;
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """

    # ----- Valida parâmetro ---- #
    if not isinstance(driver, object):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][click_element()] - O parâmetro de entrada 'driver' está incorreto.", 
                "payload": None}
    
    if not isinstance(xpath_element, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][click_element()] - O parâmetro de entrada 'xpath_element' está incorreto.", 
                "payload": None}

    # ----- Clica no elemento ----- #
    try:
        button = driver.find_element(by=lib.By.XPATH, value=xpath_element)
        button.click()

        return {"status": 1,
                "level": "info",
                "message": f"[Pyfunctions][click_element()] - Elemento '{xpath_element}' clicado com sucesso.", 
                "payload": None}

    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[Pyfunctions][click_element()] - Problema ao tentar clicar no elemento '{xpath_element}': {error}", 
                "payload": None}

# def insert_element()
def insert_element(*, driver:object, xpath_element:str, text:str) -> dict[int, str, str, None]:
    """
        - Preenche o elemento com texto.

        [Args]
            driver (int): Configurações de conexão do Chrome;
            xpath_element (str): Elemento que deve preenchido;
            text (str): Texto que deve ser inserido no elemento;
 
        [Returns]
            Dict{int, str, str, opcional}:
                - Código de status (0 = ERRO / 1 = SUCESSO);
                - Nível da mensagem (debug, info, warning, error, critical)
                - Mensagem de status (para acompanhar informação de retorno);
                - Objeto de retorno;
    """
    
    # ----- Valida parâmetro ---- #
    if not isinstance(driver, object):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][insert_element()] - O parâmetro de entrada 'driver' está incorreto.", 
                "payload": None}
    
    if not isinstance(xpath_element, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][insert_element()] - O parâmetro de entrada 'xpath_element' está incorreto.", 
                "payload": None}
    
    if not isinstance(text, str):
        return {"status": 0,
                "level": "error",
                "message":"[Pyfunctions][insert_element()] - O parâmetro de entrada 'text' está incorreto.", 
                "payload": None}
    
    # ----- Preenche o elemento da tela com o texto ----- #
    try:
        element = driver.find_element(by=lib.By.XPATH, value=xpath_element)
        element.send_keys(text)
        
        return {"status": 1,
                "level": "info",
                "message": f"[Pyfunctions][insert_element()] - Elemento '{xpath_element}' preenchido com '{text}'.", 
                "payload": None}

    except Exception as error:
        return {"status": 0,
                "level": "error",
                "message": f"[Pyfunctions][insert_element()] - Problema ao tentar preencher o elemento '{xpath_element}': {error}", 
                "payload": None}
