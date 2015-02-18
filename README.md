
# Coletar informações do site da Cetelem (Submarino)

Este é um protótipo de Web Scraping ("raspagem" da web) para coletar informações do Internet Banking relacionado ao cartão Submarino.

Uma tarefa que sempre toma cerca de 10 minutos, que através desse script é reduzida para 15 segundos.

# Setup

Copie ```.env-sample``` para ```.env```, edite e preencha seu nome de usuário e senha de acesso ao Internet Banking Cetelem.

Execute (dentro do virtualenv, se preferir):

    $ pip install -r requirements.txt
    $ python cetelem.py

Se não quiser salvar usuário e senha no arquivo, use:

    $ CETELEM_USER=<SEU USUÁRIO> CETELEM_PASSWORD=<SUA SENHA> python cetelem.py

# [EN] Collect information from Cetelem site (Submarino)

This is a Web Scraping prototype to collect information from Internet Banking related to Submarino credit card.

A task that always take 10 minutes, that through this script is reduced to 15 seconds.

# [EN] Setup

Copy ```.env-sample``` to ```.env```, edit and fill your user name and password from Cetelem Internet Banking.

Execute (into vrtualenv, if prefer):

    $ pip install -r requirements.txt
    $ python cetelem.py

If you don't want to save user name and password in file, use:

    $ CETELEM_USER=<YOUR USER> CETELEM_PASSWORD=<YOUR PASSWORD> python cetelem.py
