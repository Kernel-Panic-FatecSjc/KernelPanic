# FATEC Profº Jessen Vidal - São José dos Campos - 1º Semestre DSM - 2024

<p>Projeto desenvolvido para a API (Aprendizagem por Projeto Integrado) do 1° Semestre do curso Desenvolvimento de software multiplataforma (DSM) em parceria com a equipe Inove do curso de Manufatura avançada no projeto Smart Farming<p>

> _A API se trata de um projeto submetido à metodologia de ensino em implantação na Fatec São José dos Campos, do qual os alunos formam equipes baseadas na metodologia ágil SCRUM, tendo um aluno como Scrum Master, um sendo o Product Owner e o restante dos integrantes como Dev Team._

###  ⏳ Status do projeto: 2/3 Sprint ✅

## Visão Geral
  Este projeto tem como objetivo desenvolver uma API para análise de dados das exportações e importações do estado de São Paulo. A solução permitirá a extração e visualização de informações estratégicas sobre os produtos exportados, destinos e tendências históricas.
  
## Objetivo do produto
  O sistema será uma ferramenta interativa para auxiliar empresas e órgãos governamentais a entender melhor o panorama das exportações paulistas. Entre os principais recursos, destacam-se:

  - Segmentação de dados por município.

  - Filtros para busca por código de exportação.

  - Visualização da evolução histórica da balança comercial.

  - Normalização e análise de dados entre os anos de 2013 e 2023.

<span id="backlog">

## 📋 Backlog / User Stories

| Rank | Prioridade | User Story | Estimativa | Sprint | Requisitos do Parceiro |
|:----:|:----------:|:----------:|:----------:|:------:|:-----------------------|
| 1 | 🔴 Alta | Eu como cliente, quero ter acesso aos códigos de normalização e formatação das planilhas de exportações internacionais dos municípios Paulistas dos anos de 2013 até 2023 | 20 | 1 | Planilhas dos anos de 2013 até 2023 normalizadas |
| 2 | 🔴 Alta | Eu como cliente, quero poder visualizar o site com os gráficos para visualizar a interface do site e o desenvolvimento do projeto | 20 | 1 | Visualização dos site com os gráficos ainda sem dados / dados fictícios  |
| 3 | 🔴 Alta | Eu como usuário, quero um gráfico de linha para visualização da evolução da balança comercial das exportações dos municipios Paulistas do ano de 2013 até 2023 | 20 | 2 | Visualização da balança comercial de apenas um município por vez |
| 4 | 🔴 Alta | Eu como usuário, no gráfico de linha, quero filtro de cidade origem. | 8 | 2 | Filtro pela cidade de origem |
| 5 | 🔴 Alta | Eu como usuário, no gráfico de linha, quero filtro por pais destino | 8 | 2 | Filtro pelo pais destino |
| 6 | 🔴 Alta | Eu como usuário, no gráfico de linha, quero filtro por código NCM | 8 | 2 | Filtro por código NCM |
| 7 | 🔴 Alta | Eu como usuário, no gráfico de linha, quero filtro de valor agregado | 8 | 2 | Filtro por valor agregado |
| 8 | 🔴 Alta | Eu como usuário, quero um gráfico de funil para visualização das 5 cargas com maior valor agregado por municipio Paulista. | 20 | 3 | Visualização da carga com maior valor agregado |
| 9 | 🔴 Alta | Eu como usuário, no gráfico dos top 5 cargas, quero filtro por código NCM | 8 | 3 | Filtro por código NCM |
| 10 | 🔴 Alta | Eu como usuário, no gráfico dos top 5 cargas, quero filtro de país destino | 8 | 3 | Filtro pelo país destino |
| 11 | 🟠 Média | Eu como usuário, no gráfico dos top 5 cargas, quero filtro de cidade origem. | 8 | 3 | Filtro pela cidade de origem |
| 12 | 🟠 Média | Eu como usuário, no gráfico dos top 5 cargas, quero filtro de valor agregado | 8 | 3 | Filtro por valor agregado |
| 13 | 🟡 Baixa | Eu como usuário, no gráfico dos top 5 cargas, quero filtro por ano da exportação. | 3 | 3 | Filtro pelo ano de exportação |


## Tecnlogias utilizadas
<div align="center">
<img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Microsoft_Teams-6264A7?style=for-the-badge&logo=microsoft-teams&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Python-00000?style=for-the-badge&logo=Python&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/Pandas-00000?style=for-the-badge&logo=Pandas&logoColor=white&color=043873">
<img src="https://img.shields.io/badge/MySQL-0000?style=for-the-badge&logo=MySQL&logoColor=white&color=043873">
</div>

## Metodologia utilizada
  Para a confecção do produto foi empregado o framework de metodologia ágil Scrum, que consiste sumariamente dividir o desenvolvimento do projeto em Sprints, um conjunto de tarefas que devem ser executadas e desenvolvidas em um período pré-definido de tempo. Além disso, foi definido o Backlog do Produto, que são todas as funcionalidades que o software deverá ter com base nos requisitos levantados com o cliente. Uma vez aprovado por ele, para selecionar quais seriam as entregas das Sprints do projeto, primeiro foi definido o MVP de cada Sprint, que é uma versão do produto que prioriza as tarefas que trazem maior entrega de valor para o cliente. Então, a partir disso o Backlog do Produto foi dividido em 4 Backlog de Sprint.


## MVP's



# Google Colab: 
https://colab.research.google.com/drive/1O28wrwHK5T3kbF00_QEZJqcLTJb21rAI?usp=sharing




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

## 3º Passo: criarBanco de Dados

<details>
  <summary><b>Clique aqui</b></summary>

  1. No Terminal Exectue e insira a senha:
  ```
  mysql -u root -p
  ```
  2. Dentro do MySQL execute:
  ```
  source ~/KernelPanic/Database/criarBanco.sql
  ```
</details>
<br>

## 4° Passo : Inserir Dados no Banco
<details>
  <summary><b>Clique aqui</b></summary>

  1.Procure o Arquivo dbDataManipulation.py e coloque suas credencias Root:
  ```
  /KernelPanic/src/dataManipulation-API/dbDataManipulation.py
  ```

  2. No Terminal da pasta Raiz do projeto, execute:
  ```
  python3 /src/dataManipulation-API/dbDataManipulation.py
  ```

</details>
<br>

## 5º Passo: Abrindo a aplicação web

<details>
  <summary><b>Clique aqui</b></summary>

  1. Ainda dentro do ambiente virtual e dentro da pasta src, execute o seguinte comando:
  ```
  flask run
  ```
   
  2. Por fim, entre no link que aparecerá no cmd copiando e colando ele no seu navegador de preferência, ou então simplesmente clique aqui:
    <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

  4. Após finalizar o uso do nosso site, para sair do ambiente virtual, no terminal, execute o atalho `Ctrl+C` para finalizar o serviço do Flask, e então execute o seguinte comando:
  ```
  deactivate
  ```
</details>
<br>

## Equipe <a name="equipe"><a>
|  Foto        |     Função    |           Nome            |                            LinkedIn                            |                      GitHub                       |
| :----: | :-----------: | :-----------------------: | :------------------------------------------------------------: | :-----------------------------------------------: |
| <img src="https://avatars.githubusercontent.com/u/162122368?v=4" width="75px"> | Scrum Master  | Daniel Porto Renó Sás Piloto | [Linkedin](https://www.linkedin.com/in/daniel-piloto-98b717226/)  | [GitHub](https://github.com/danprsp)           |
| <img src="https://avatars.githubusercontent.com/u/106409918?v=4" width="75px"> | Product Owner | Vitor Serpa da Silva |  [Linkedin](https://www.linkedin.com/in/vitor-serpa-925b46322/)  | [GitHub](https://github.com/VitorSerpa) |
| <img src="https://avatars.githubusercontent.com/u/140865436?v=4" width="75px">|Dev Team| Henry Vilela Silva Tito |  [Linkedin](https://www.linkedin.com/in/henry-tito-989b4b354/)  | [GitHub](https://github.com/HenryTito)  |
| <img src="https://avatars.githubusercontent.com/u/202815299?v=4" width="75px"> | Dev Team      | Lucas Daniel Vasconcellos do Prado |  [Linkedin](https://www.linkedin.com/in/lucas-do-prado-30843b33a/)  | [GitHub](https://github.com/orgs/Kernel-Panic-FatecSjc/people/lucasdaniel0122)    |
| <img src="https://avatars.githubusercontent.com/u/144951743?v=4" width="75px"> | Dev Team      | Miguel Tomio Toledo Nonaka |  [Linkedin](www.linkedin.com/in/miguel-nonaka)  | [GitHub](https://github.com/miguelnonaka)    |
| <img src="https://avatars.githubusercontent.com/u/102493225?v=4" width="75px"> | Dev Team      | Paula Emy Tamay |  [Linkedin](https://www.linkedin.com/in/paula-tamay-7a168228a/)  | [GitHub](https://github.com/PaulaEmy)    |
| <img src="https://avatars.githubusercontent.com/u/163305926?v=4" width="75px"> | Dev Team      | Vinícius da Silva Leite |  [Linkedin](https://www.linkedin.com/in/vinícius-leite-4792b02ba/)  | [GitHub](https://github.com/vinislvleite)    |
| <img src="https://avatars.githubusercontent.com/u/119637682?v=4" width="75px"> | Dev Team | Heloisa Cardillo | [Linkedin](https://www.linkedin.com/in/heloisa-cardillo-lima/) | [GitHub](https://github.com/heloisa-cardillo) |
