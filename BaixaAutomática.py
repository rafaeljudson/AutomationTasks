# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Using Chrome to access web
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# Open the website
driver.get("http://10.10.127.2:8080/WebGlass/Default.aspx")
#
usuario = driver.find_element_by_id("txtUsuario")
usuario.send_keys("Judson")

senha = driver.find_element_by_id("txtSenha")
senha.send_keys("24051989")

botao = driver.find_element_by_id("btnLogin")
botao.click()

lista_pedidos =["180180"]

driver.get("http://10.10.127.2:8080/Cadastros/CadSaidaEstoque.aspx")
	
select = Select(driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_drpLoja_drpLoja"))
select.select_by_value('8')

#aqui entra um loop com os pedidos em txt
for i in lista_pedidos:
    pedido = driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_txtNumPedido")
    pedido.send_keys(i)

    pesquisar = driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_imbPesq")
    pesquisar.click()

    marcar_saida = driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_grdProdutos_ctl01_lnkTodos")
    marcar_saida.click()


    marcar = driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_btnMarcarSaida")
    marcar.click()

#Switch the control to the Alert of confirmation
    obj = driver.switch_to.alert
#use the accept() method to accept the alert
    obj.accept()

#Switch the control to the Alert of done with success
    obj = driver.switch_to.alert
#use the accept() method to accept the alert
    obj.accept()

    pedido = driver.find_element_by_id("ctl00_ctl00_Pagina_Conteudo_txtNumPedido").clear()
#Fim do Loop
