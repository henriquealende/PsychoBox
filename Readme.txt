O que falta
---------------------------
Implementar QThred para plotar o gráfico
Mudar gráfico para matiplotlib





Ideia da arquitetura do código
-------------------------------
## MainFiles vai ser uma pasta com os arquivos principais, aqueles que criar janelas na interface.
## Pages possui arquivos que possuem funções "funcionais", aquelas que chamam outras funções ou calculam e retornam valores, está separado por página. (falta a página de welcome/new Project)
## PagesSetup possui arquivos que possuem funções voltas ao layout da página, aquelas que enable/disable algo, redefinem o tamanho dos objetos na interface, está separado por grupos e páginas.
## Resources tem os arquivos de img usados no código.
## Signals  possui os comandos de ações quando apertado algum botão na interface, ou quando algum sinal na interface gera um chamado.
## Utils ainda não alterei nada aqui, mas a principio, o ideal seria colocar essas funções em algum dos arquivos anteriores.



MainFiles
----------
## main possui os comando para gerar a interface principal e chama arquivos essenciais para o funcionamento do código.
## expandGraph possui os comando para gerar a interface secundário (janela do gráfico) e chama arquivos essenciais para o funcionamento do código.



Pages
------
## calibration
## filter
## graph
## login
## welcome



PagesSetup
------------
- Páginas (faz alterações relacionas as páginas que possuem o nome da função)
    ## setCalibration
    ## setEditor
    ## setLogin
    ## setWelcome
    ## setGraph

- Grupos
    ## mainSettings (é o arquivo principal, basicamente chama as outras quando necessário, além de possuir os comandos de close/maximazed/minimazed)
    ## setLeftMenu (responsável pelo layout daquele menu lateral)
    ## setWindow   (responsável pelo layout das janelas principais como nome, icone, definir a barra para arrastar a janel ...)



SupportCodes
------
## buttonSignals
## setWundow
