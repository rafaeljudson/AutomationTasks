# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
import pandas as pd


# Using Chrome to access web
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# Open the website
driver.get('http://10.10.127.2:8080/WebGlass/Default.aspx')
#
usuario = driver.find_element_by_id("txtUsuario")
usuario.send_keys("denys")

senha = driver.find_element_by_id("txtSenha")
senha.send_keys("123")

botao = driver.find_element_by_id("btnLogin")
botao.click()

driver.get("http://10.10.127.2:8080/Cadastros/CadPedidoEspelhoGerarMult.aspx")

td = driver.find_elements_by_tag_name('td')

ordens = []
endereço1 = "http://10.10.127.2:8080/Cadastros/CadFotos.aspx?id="
endereço2 = "&tipo=pedido"
for i in td:
    if len(i.text) == 6:
        ordens.append(i.text)
        

str(ordens)

sem_anexo = []

for j in ordens:
    anexo = endereço1 + j + endereço2
    driver.get(anexo)
    tdanexo = driver.find_elements_by_tag_name('td')
    for l in tdanexo:
        if (l.text == "Não há fotos cadastradas para este pedido."):
            sem_anexo.append(j)
            

sem_anexo = list(dict.fromkeys(sem_anexo))
print("Existe(m)", len(sem_anexo), "pedido(s) sem anexo(s) de um total de", len(ordens), "no momento")
print("Esse(s) pedido(s) são:")

f = open("Ordens sem Anexo.txt","w+")

for a in sem_anexo:
    f.write("Ordem %s \r\n" % (a))
    
f.close()
    




	
