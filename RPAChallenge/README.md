[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)

# Project: RPA Challenge

O projeto tem como objetivo automatizar o preenchimento de fomulário através de um site utilizando o excel como base de dados dos clientes.

## Índice

- [Visão Geral](#visão-geral)
- [Steps](#steps)
- [Ferramentas](#ferramentas)
- [Sistemas](#sistemas)
- [Instalação](#instalação)
- [ChromeDriver](#chromedriver)
- [Usabilidade](#usabilidade)

## Visão Geral

A automação deve acessar via web o site da RPA Challenge, realizar o download da planilha e salvá-lo em pasta local da máquina. Após a coleta da planilha a automação deve realizar sua leitura, com base nas suas infomações preencher os campos correspondentes no formulário. 

## Steps

1. Abrir o site da RPA Challenge;
2. Localizar o download da planilha;
3. Salvar e validar a planilha;
4. Abrir a planilha e extrair as suas informações;
5. Preencher os elementos do fomrulário até o fim do arquivo Excel;

## Ferramentas

* Python3 ou superior;
* IDE de sua preferência;

## Sistemas

* Web (https://rpachallenge.com/);
* Excel (https://www.microsoft.com/pt-br/microsoft-365/excel);

## Instalação

**1.** Clone este repositório em sua máquina local:
```cmd
git clone https://github.com/ThiagoLozano/MyPortfolio.git
```

**1.1** Abra o arquivo **RPAChallenge/**:
   * OBS: Você pode abrir direto no seu IDE.
```cmd
cd RPAChallenge/
```

**2.** Possua Python3 ou superior:
```cmd
pip --version
python --version
```

**3.** Instale as dependências no arquivo **requirements.txt**:
```cmd
pip install -r requirements.txt
```

**4.** Instale o **Chromedriver** mais recente compatível com a versão do seu Google Chrome.

## ChromeDriver

Para a instalação do ChromeDriver você deve:

**1.** Acesse o link **chrome://settings/help** e identificar a versão atual do seu Chrome;

**2.** Acesse o site: https://developer.chrome.com/docs/chromedriver/downloads

**3.** Busque pela sua versão atual e realize o download do seu chromedriver;

**3.1** Caso a sua versão seja muito atual e ainda não estiver disponível na primeira tela, acesse o link: https://googlechromelabs.github.io/chrome-for-testing/ e seleciona a opção **stable**, busque por **chromedriver** (win32/win64/mac-x64/mac-arm64) e acesse o link para download.

**4.** Descompacte o arquivo zip e extrai apenas o **chromediver.exe**.

**4.1** Você pode anexar o **chromediver.exe** na pasta do seu projeto atual ou dentro do seu arquivo de instalação do Python3.

## Usabilidade

**1.** A pasta **src** é a principal pasta onde você localizará todos os códigos python.

**1.1** Dentro da pasta **src** você deve localizar o arquivo **main.py**, ele é o código principal, aquele que realiza o início do processo e importa os outros módulos necessários.

**2.** Antes de iniciar o processo, você deve abrir o arquivo **Pyvars.py** e setar as seguintes informações:
   
   * **Caminho de Download:** Onde o arquivo EXCEL deve ser guardado na máquina após seu download;
      * O caminho de Dowload pode ser igual a "" (vazio), sendo o caminho default o **C:\Users\<seu_user>\Downloads**.
      ```python
         # Onde deve ficar a planilha de entrada.
         diretorio_download = r""
      ``` 
   
   * **Caminho de JSON:** Onde o arquivo JSON de status deve ser guardado na sua máquina;
      ```python
            # Onde deve fica status do JSON.
            diretorio_json = r"C:\pastaABC\pastaXYZ\<nome_pasta_json>"
      ```
   
   * **Caminho de LOG**: Onde o arquivo de LOG deve ser guardado na sua máquina;
      ```python
            # Onde deve ficar as LOGs.
            diretorio_logs = r"C:\pastaABC\pastaXYZ\<nome_pasta_logs>"
      ```
   
   * **Nome do arquivo Json**: Nome pessoal para seu arquivo JSON;
      ```python
         name_json = "nome_arquivo_aqui.json"
      ```

      * Estruruta do JSON:
         - **true**: Deve baixar a planilha do site;
         - **false**: Não é necessário baixar a planilha do site.
         ```json
            {
               "baixar_nova_planilha": true
            }
         ```

**3.** A pasta **docs** é uma pasta que contêm um **fluxograma** do processo e uma **documentação** detalhada do passo a passo do projeto caso necessite de mais informações.

**4.** Com todos os ajustes realizados, você pode executar o arquivo **main.py**

```cmd
cd src/
```
```cmd
python main.py
```
