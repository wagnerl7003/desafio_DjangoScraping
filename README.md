WEBSCRAPING
Utilizando BeautifulSoup e Selenium, o script consegue coletar todas as informações da pagina, indentificando sozinho o que é propaganda e ignorando.
Primeiro ele verifica qual é a ultima pagina do site, armazena esse resultado, e depois começa a coletar as informações pagina por pagina.
As informações nas barras foram convertidas em um valor float baseado na porcentagem contida na tag Style.
As informações são armazenadas no banco de dados a cada linha extraída.
O ChromeDriver esta com as configurações para que ele rode de forma invisível.
Basta apenas rodar o script que ele coleta sozinho todas informações

DJANGO
Foi criado um sistema simples de CRUD, aonde as informações já coletadas no Script 'webscraping.py' aparecem, já com a opção de poder editar ou excluir. Para a exclusão existe um confirmação pra saber se o usuário deseja realmente apagar o item.
É possível também adicionar novos itens na tabela.

Algumas coisas que gostaria de fazer se tivesse mais tempo será fazer um botão que rodasse a função de webscraping de forma mais direta, e colocaria uma barra de pesquisa e um sistema de filtragem para facilitar a consulta
