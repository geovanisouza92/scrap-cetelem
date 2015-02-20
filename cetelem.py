#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=F0401,C0111


from __future__ import print_function

from re import search
from decouple import config
from selenium.webdriver import Firefox


USER = config('CETELEM_USER')
PASSWORD = config('CETELEM_PASSWORD')

_LIMITE = r'.*compra:\n(?P<limite>R\$[^\n]*)\n'
_SUPER_LIMITE = r'.*Super Limite:\n(?P<super_limite>R\$[^\n]*)\n'


def main():
    """Buscar informações de limites disponíveis e total das faturas"""
    driver = Firefox()
    driver.implicitly_wait(30)

    # Abrir portal Cetelem
    driver.get('http://www.cetelem.com.br/wps/portal/cetelem/normal/NL/login')

    # Digitar usuário e senha
    driver.find_element_by_id('userid').clear()
    driver.find_element_by_id('userid').send_keys(USER)

    for digit in list(PASSWORD):
        driver.find_element_by_name(digit).click()

    # Clicar em acessar
    driver.find_element_by_id('acessarps').click()

    # Extrair limites
    dados = driver.find_element_by_id('dadosCartaoInternetBanking').text
    limite = search(_LIMITE, dados).group(1)
    super_limite = search(_SUPER_LIMITE, dados).group(1)

    # Extrair fatura
    driver.find_element_by_link_text('Consulte sua fatura').click()
    mes = driver.find_element_by_xpath(
        "//div[@id='abasFatura']/table/tbody/tr/td[2]").text
    subtotal = driver.find_element_by_xpath(
        "//div[@id='boxFatura']/table/tbody/tr[2]/td").text

    # Extrair próxima fatura
    driver.find_element_by_xpath(
        "//div[@id='abasFatura']/table/tbody/tr/td[3]/a").click()
    proxima_fatura = driver.find_element_by_xpath(
        "//div[@id='boxFatura']/table/tbody/tr[3]/td").text

    # Fechar navegador
    driver.quit()

    # Resultados
    print('Limite:', limite)
    print('Super Limite:', super_limite)
    print('Fatura de', mes, subtotal)
    print('Próxima fatura:', proxima_fatura)


if __name__ == "__main__":
    main()
