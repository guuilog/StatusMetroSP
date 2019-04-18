from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import smtplib
import json
import ast


class Crawler:
    """Crawler na API do metro de SP

    Essa classe tem como objetivo fazer o 'requests' na API do metrô de SP. No final do processamento, esta classe
    retornará uma string que contém as informações das linhas do metrô de SP.

    Exemplos
    --------
    >>> data_ = Crawler().main()
    :return: 'Linha: 1 AZUL - Operação Normal () ; \n Linha: 2 VERDE - Operação Normal () ; \n Linha: 3 VERMELHA - Operação Normal () ;

    Observações:
    ------------
    Ao chamar a função main(), a mesma já chamará o restante das funções.

    """

    def __init__(self):
        self.url = "http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanas"

    # Used in main
    def get_page_content(self):
        return requests.get(url=self.url)

    # Used in main
    @staticmethod
    def load_json(page_content):
        return json.loads(page_content.text)

    # Used in main
    @staticmethod
    def generating_text(data):
        string_body = ''
        for d in data:
            string_body += "Linha: " + str(d['LinhaId']) + " " + d['Nome'] + " - " + d['Status'] + " (" + d['Descricao'] + ") " + "; \n "

        return string_body

    def main(self):
        resp = self.get_page_content()
        data = self.load_json(page_content=resp)
        return self.generating_text(data=data)


class SendMail:
    def __init__(self, body):
        """'Enviadora de emails

        Essa classe manda o email de um determinado remetente com um conteúdo determinado pelo argumento 'body'. Os
        destinatários são definidos num arquivo .txt.

        Parameters
        ----------
        body: str
            Corpo do email.

        Exemplos
        --------
        >>> SendMail(body='Corpo do email').send_message()

        """

        self.email = 'spviva8@gmail.com'
        self.password = 'iWeekedBR'
        self.server = 'smtp.gmail.com'
        self.port = 587
        self.body = body

        self.recipients = open('data/recipients.txt').read()

        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Situação do Metro SP"
        message["From"] = self.email
        message["To"] = self.recipients

        message.attach(MIMEText(self.body))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, message['To'].split(','), message.as_string())


if __name__ == '__main__':
    data_ = Crawler().main()
    SendMail(body=data_).send_message()
