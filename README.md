<h1>StatusMetroSP</h1>
<p>Esse é o script que será usado no meu trabalho - TCC da faculdade. Ele basicamente pega as informações contidas no site do <a href="http://www.metro.sp.gov.br/">Metro SP</a> sobre o status da operação do metro. Uma vez que ele puxa as informações, ele envia ao usuário por e-mail o status de como está as linhas do metro. Nesse caso, ele está pegando o usuário de um arquivo txt externo que está salvo na pasta "data" </p>

<h3>Link da API do Metro SP de onde é tirado as informações</h3>

`url = "http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanas"`
 

<h3> Bibliotecas para importar: </h3>

`import requests
import smtplib
import json
import ast`
