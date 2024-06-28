import Pyfunctions, Pyvars, lib

def insert_info(*, driver:object):
    diretorio_download = Pyvars.diretorio_download
    
    if diretorio_download == "":
        diretorio_download = str(lib.Path.home()) + "\Downloads"

    name_sheet = Pyvars.name_sheet

    df = lib.pd.read_excel(f"{diretorio_download}\{name_sheet}")
    
    XPATHS= {
        "xpath_start": "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button",
        "xpath_company" : "//input[@ng-reflect-name='labelCompanyName']",
        "xpath_role" : "//input[@ng-reflect-name='labelRole']",
        "xpath_firstName" : "//input[@ng-reflect-name='labelFirstName']",
        "xpath_lastName" : "//input[@ng-reflect-name='labelLastName']",
        "xpath_email" : "//input[@ng-reflect-name='labelEmail']",
        "xpath_address" : "//input[@ng-reflect-name='labelAddress']",
        "xpath_phone" : "//input[@ng-reflect-name='labelPhone']",
        "xpath_submit" : '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input'   
    }

    # Clica no botão 'Start'.
    return_click_element = Pyfunctions.click_element(driver=driver, xpath_element=XPATHS["xpath_start"])

    Pyfunctions.log_message(level=return_click_element["level"], message=return_click_element["message"])
    
    if return_click_element["status"] == 0:
        driver.quit()
        return
    
    elif return_click_element["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[insert_info][click_element()] - Retorno não mapeado ao tentar clicar no elemento: {XPATHS['xpath_start']} - {return_click_element}")
        driver.quit()
        return

    # Preenche os campos do formulário.
    try:
        for _, row in df.iterrows():
            form_data = {
                XPATHS["xpath_firstName"]: row["First Name"],
                XPATHS["xpath_lastName"]: row["Last Name "],
                XPATHS["xpath_company"]: row["Company Name"],
                XPATHS["xpath_role"]: row["Role in Company"],
                XPATHS["xpath_address"]: row["Address"],
                XPATHS["xpath_email"]: row["Email"],
                XPATHS["xpath_phone"]: str(row["Phone Number"])
            }
            
            for xpath, text in form_data.items():
                
                # Preenche o elemento.
                return_insert_element = Pyfunctions.insert_element(driver=driver, xpath_element=xpath, text=text)
                
                Pyfunctions.log_message(level=return_insert_element["level"], message=return_insert_element["message"])
                
                if return_insert_element["status"] == 0:
                    driver.quit()
                    return
                
                elif return_insert_element["status"] not in [0, 1]:
                    Pyfunctions.log_message(level="error", message=f"[Pyfunctions][insert_element()] - Retorno não mapeado ao tentar preencher elemento texto: {return_insert_element}")
                    driver.quit()
                    return

            # Clica no botão 'Submit'.
            return_click_element = Pyfunctions.click_element(driver=driver, xpath_element=XPATHS["xpath_submit"])
            
            Pyfunctions.log_message(level=return_click_element["level"], message=return_click_element["message"])

            if return_click_element["status"] == 0:
                driver.quit()
                return
            
            elif return_click_element["status"] not in [0, 1]:
                Pyfunctions.log_message(level="error", message=f"[insert_info][click_element()] - Retorno não mapeado ao tentar clicar no elemento: {XPATHS['xpath_submit']} - {return_click_element}")
                driver.quit()
                return

    except Exception as error:
        Pyfunctions.log_message(level="error", message=f"[insert_info] - Problema ao tentar preencher o formulário: {error}")
        driver.quit()
        return
    
    # =====================================
    #  Salva a mensagem de retorno do site
    # =====================================

    xpath_message = "/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]"
    
    get_element_text = Pyfunctions.get_element_text(driver=driver, xpath_element=xpath_message)
    
    Pyfunctions.log_message(level=return_click_element["level"], message=return_click_element["message"])
    
    if return_click_element["status"] == 0:
        driver.quit()
        return
    
    elif return_click_element["status"] not in [0, 1]:
        Pyfunctions.log_message(level="error", message=f"[insert_info][click_element()] - Retorno não mapeado ao tentar clicar no elemento: {XPATHS['xpath_start']} - {return_click_element}")
        driver.quit()
        return
    
    text = f"Mensagem de retorno final: {get_element_text['payload']}"
    Pyfunctions.log_message(level="info", message=text)

    # ===============
    #  Fim do Módulo
    # ===============

    Pyfunctions.log_message(level="info", message="[insert_info] - Módulo finalizado com sucesso.")
    
    driver.quit()

if __name__ == "__main__":
    insert_info(driver="")
