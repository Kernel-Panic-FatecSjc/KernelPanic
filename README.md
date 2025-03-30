# FATEC Profº Jessen Vidal - São José dos Campos - 1º Semestre DSM - 2024

<p>Projeto desenvolvido para a API (Aprendizagem por Projeto Integrado) do 1° Semestre do curso Desenvolvimento de software multiplataforma (DSM) em parceria com a equipe Inove do curso de Manufatura avançada no projeto Smart Farming<p>

> _A API se trata de um projeto submetido à metodologia de ensino em implantação na Fatec São José dos Campos, do qual os alunos formam equipes baseadas na metodologia ágil SCRUM, tendo um aluno como Scrum Master, um sendo o Product Owner e o restante dos integrantes como Dev Team._

###  ⏳ Status do projeto: 1/3 Sprint ✅

## Visão Geral
  Este projeto tem como objetivo desenvolver uma API para análise de dados das exportações e importações do estado de São Paulo. A solução permitirá a extração e visualização de informações estratégicas sobre os produtos exportados, destinos e tendências históricas.
  
## Objetivo do produto
  O sistema será uma ferramenta interativa para auxiliar empresas e órgãos governamentais a entender melhor o panorama das exportações paulistas. Entre os principais recursos, destacam-se:

  - Segmentação de dados por município.

  - Filtros para busca por código de exportação.

  - Visualização da evolução histórica da balança comercial.

  - Normalização e análise de dados entre os anos de 2013 e 2023.
  
## Metodologia utilizada
  Para a confecção do produto foi empregado o framework de metodologia ágil Scrum, que consiste sumariamente dividir o desenvolvimento do projeto em Sprints, um conjunto de tarefas que devem ser executadas e desenvolvidas em um período pré-definido de tempo. Além disso, foi definido o Backlog do Produto, que são todas as funcionalidades que o software deverá ter com base nos requisitos levantados com o cliente. Uma vez aprovado por ele, para selecionar quais seriam as entregas das Sprints do projeto, primeiro foi definido o MVP de cada Sprint, que é uma versão do produto que prioriza as tarefas que trazem maior entrega de valor para o cliente. Então, a partir disso o Backlog do Produto foi dividido em 4 Backlog de Sprint.


## MVP's



# Como rodar
> _Os códigos e processos presentes neste readme possuem versão para WINDOWS_
## O que será necessário

Para o funcionamento do nosso sistema, você precisara das seguintes tecnologias:

1. [Git](https://git-scm.com/downloads): Utilizaremos o Git para clonar o nosso repositório.

2. [Python](https://www.python.org/downloads/): Precisaremos do python para podermos utilizar de maneira adequada o nosso ambiente virtual, incluímos ele no arquivo requirements, porém sinta-se a vontade caso queira ter uma garantia baixando o python por si só.

## 1º Passo: Clonando o repositório

<details>
  <summary><b>Clique aqui</b></summary>

  Para clonar o projeto e utilizá-lo em seu computador, siga os seguintes passos:
  
  1. Crie uma pasta onde deseja armazenar nosso projeto, e então abra-a e clique na url da pasta, ou então utilize o atalho `Ctrl+L` para selecionar a url, e escreva 'cmd' para abrir o prompt de comando.
  
  > _Obs.: Caso você esteja no LINUX, a parte de escrever "cmd" não irá funcionar, então clique com o botão direito na pasta que você criou e selecione a opção "Abrir no terminal"_

  Um prompt de comando irá se abrir, e então execute o comando abaixo:
  
  ```
  git clone https://github.com/CyberScrums/Projeto-Smart-Farming.git
  ``` 

</details>
<br>

## 2º Passo: Iniciando o ambiente virtual

<details>
  <summary><b>Clique aqui</b></summary>

  1. Após a clonagem, clique com o botão direito na pasta e selecione a opção de abrir com o Terminal, e insira os seguintes comandos :

  ```
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt (lembre-se de dar primeiro "cd Projeto-Smart-Farm" e em seguida dar "cd src" para entrar na pasta e dar o comando)
  ```

  > _Caso você esteja em LINUX, digite os comandos desta maneira:_<br>
  `python3 -m venv venv`<br>
  `source venv/bin/activate`<br>
  `pip install -r requirements.txt` (lembre-se de dar "cd src" para entrar na pasta e dar o comando)

</details>
<br>

## 3º Passo: Abrindo a aplicação web

<details>
  <summary><b>Clique aqui</b></summary>

  1. Ainda dentro do ambiente virtual e dentro da pasta src, execute o seguinte comando:
  ```
  flask run
  ```

  2. Por fim, entre no link que aparecerá no cmd copiando e colando ele no seu navegador de preferência, ou então simplesmente clique aqui: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

  3. Após finalizar o uso do nosso site, para sair do ambiente virtual, no terminal, execute o atalho `Ctrl+C` para finalizar o serviço do Flask, e então execute o seguinte comando:
  ```
  deactivate
  ```

</details>
<br>

#Membros do grupo
