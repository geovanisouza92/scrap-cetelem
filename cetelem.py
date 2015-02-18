#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=F0401


from __future__ import print_function

from re import search
from decouple import config
from selenium.webdriver import Firefox


USER = config('CETELEM_USER')
PASSWORD = config('CETELEM_PASSWORD')

_limite = r'.*compra:\n(?P<limite>R\$[^\n]*)\n'
_super_limite = r'.*Super Limite:\n(?P<super_limite>R\$[^\n]*)\n'


def main():
    driver = Firefox()
    driver.implicitly_wait(30)

    # Abrir portal Cetelem
    driver.get('http://www.cetelem.com.br/portal/Para_Voce/index.shtml')

    # Clicar em Acessar
    driver.find_element_by_link_text('Acessar').click()

    # Digitar usuário e senha
    driver.find_element_by_id('userid').clear()
    driver.find_element_by_id('userid').send_keys(USER)

    for it in list(PASSWORD):
        driver.find_element_by_name(it).click()

    # Clicar em acessar
    driver.find_element_by_id('acessarps').click()

    # Extrair limites
    dados = driver.find_element_by_id('dadosCartaoInternetBanking').text
    limite = search(_limite, dados).group(1)
    super_limite = search(_super_limite, dados).group(1)

    # Extrair fatura
    driver.find_element_by_link_text('Consulte sua fatura').click()
    mes = driver.find_element_by_xpath(
        "//div[@id='abasFatura']/table/tbody/tr/td[2]").text
    subtotal = driver.find_element_by_xpath(
        "//div[@id='boxFatura']/table/tbody/tr[2]/td").text

    # Fechar navegador
    driver.quit()

    # Resultados
    print('Limite:', limite)
    print('Super Limite:', super_limite)
    print('Fatura de', mes, subtotal)


if __name__ == "__main__":
    main()
