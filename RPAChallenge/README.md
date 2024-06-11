# Project: RPA Challenge

O projeto tem como objetivo automatizar o proceso de extração de planilha e preenchimento de formulário web.

**STATUS:** Ainda em Desenvolvimento

## Índice

- [Visão Geral](#visão-geral)
- [Steps](#steps)
- [Ferramentas](#ferramentas)
- [Softwares](#softwares)
- [Instalação](#instalação)
- [Observações](#observações)

## Visão Geral

A automação deve acessar via web o site da RPA Challenge, realizar o download da planilha e salvá-lo em pasta local da máquina.

Após a coleta da planilha, a automação deve realizar sua leitura e com base nas suas infomações, preencher os campos correspondentes no formulário. 

## Steps

1. Abrir o site da RPA Challenge;
2. Localizar o download da planilha;
3. Salvar e validar a planilha;
4. Abrir a planilha e extrair as informações;
5. Preencher os elementos do fomrulário até o final da informações;

## Ferramentas

* Python3 ou superior

## Softwares

* WEB (https://rpachallenge.com/)

## Instalação

1. Clonar este repositório em sua máquina local.
2. Possuir Python3 ou maior.
3. Instalar as dependencias no arquivo **requirements.txt**.
4. Localizar o arquivo **Pyvars.py** e inserir os seus diretórios de Download, JSON e LOGs.

## Observações

* O foco desse projeto é a utilização da ferramenta em algumas situações como, leitura de planilhas, acesso a web e webscraping.