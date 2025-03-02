Version in [🇺🇸 English](#english) and [🇧🇷 Português](#português)

## 🇺🇸 English
# ENGLISH VERSION: Python Banking System aBank:

This is a simple banking system developed in Python using Object-Oriented Programming (OOP). The project simulates a basic banking system with functionalities like account creation, deposit, withdrawal, and transfers between accounts.

## Functionalities
* Creation of bank accounts

* Deposit of values

* Withdrawal of values with balance verification

* Transfer of values between accounts

* Terminal-based interaction interface

## Project Structure
The project is divided into the following files:

* `main.py` - The entire bank system is in this file. It contains verification functions and a handcrafted DBMS in Python. This would be the "backend."

* `interface.py` - User interaction interface to perform bank operations. It is interconnected with main.py to access functions. This would be the "frontend" of the application.

* `db.json` The system's database.

  * `cliente = []` customer information.

    * `id` a numeric sequential ID of the account for control.

    * `name`, `cpf`, `email`, `phone`, `password` personal data.

    * `registration_date` creation date and time.

   * `conta = []` the account related to the customer.

     * `id` ID related to the created account.

     * `client_id` identifies which customer this account is linked to. It receives the customer's id in cliente = [].
  
     * `account_number` account number, used for control and transactions like transfers.
  
     * `account_type` checks the type of account, whether it's a checking account, savings, investments, etc.
  
     * `balance`
  
     * `opening_date` creation date and time.
     
     * `status` checks the account status—whether it's active, valid, invalid, etc.
     
     * `password` account password.
   
   * `transacoes = []` transaction history related to each customer.

## Objective and Motivation:
Python was the first language I learned and studied. I took a break from developing projects with it but was always fascinated by systems. So, I decided to create a banking system. I researched a bit about how it works, especially the database, and decided to apply that knowledge. It was good to see that my logic and knowledge hadn’t faded. This is the second attempt because I created a more comprehensive system earlier (a day before creating this one). I would develop the system, analyze it, and see where improvements could be made, where to implement features, and gradually increase the system's level and complexity. Then, I decided to rewrite it, this time thinking of it as a portfolio to publish. I incorporated a lot of the logic from the first version into this one, but this time the system was written in English. However, I decided to keep the database in Portuguese. It took me one day to create this system, though not continuously, as I would take breaks, do other things, and then return to it. I estimate it took around six hours without breaks. I intend to release a version using an SQL database and a hosted API—a system with better and more advanced validation (at a senior developer level), and I might create such a system in React. I won’t be publishing the first version of my system.

## How to Run
* Make sure you have Python installed (version 3.6 or higher).

* Clone this repository or download the files.

* In the terminal, navigate to the project folder and run the file `interface.py`

Follow the instructions displayed in the terminal interface.

## Requirements
Python 3.6+

## Contribution
If you would like to contribute improvements to the project, you can fork the repository and submit your changes.

## License
Feel free to use and modify it as needed.

# Sistema Bancário em Python aBank (PT-BR)
Este é um sistema bancário simples desenvolvido em Python, utilizando Programação Orientada a Objetos (POO). O projeto simula um sistema bancário básico com funcionalidades como criação de conta, depósito, saque e transferências entre contas.

## Funcionalidades

* Criação de contas bancárias

* Depósito de valores

* Saque de valores com verificação de saldo

* Transferência de valores entre contas

* Interface de interação via terminal

## Estrutura do Projeto

O projeto está dividido nos seguintes arquivos:

* `main.py` - Todo o sistema do banco está nesse arquivo. Ele tem as funções de verificações e um SGBD feito "a mão" em Python. Seria o "backend"

* `interface.py` - Interface de interação com o usuário para executar as operações do banco. Interligado com o main.py acessando as funções. Esse serio o "frontend" da aplicação.

* `db.json` O Banco de dados do sistema.

  * `cliente = []` as informações do cliente.
    * `id` um ID numérico ordenado da conta para controle.
    * `name`, `cpf`, `email`, `phone`, `password` dodos pessoais
    * `registration_date` data e hora de criação

  * `conta = []` a conta relacionada ao cliente
      * `id` ID relacionado a conta criada.
      * `client_id` é a forma de identificar a qual cliente esse conta está relacionada. Recebe o `id` do cliente no `cliente = []`
      * `account_number` número da conta, para controle e transações como transferência
      * `account_type` verifica qual o tipo da conta, se é corrente ou poupança, investimentos etc.
      * `balance` saldo.
      * `opening_date` data e  hora de criação
      * `status` verifica status da conta. Se é ativa, valido, inválido etc.
      * `password` senha da conta
  
  * `transacoes = []` histórico de transações relacionado a cada cliente.

 ## Objetivo e motivação:
Python foi a primeira linguagem que aprendi e estudei. Parei um tempo de desenvolver projetos com ele mas sempre foi fascinado por sistemas. Então decidi criar um sistema de um banco. Pesquisei um pouco como é e como funciona, principalmente o banco de dados e então decidi aplicar. Foi bom ver que minha lógica e conhecimentos não se perderam. Esse é a segunda tentativa pq fiz um sistema bem completo antes (1 dia antes de criar este), eu ia fazendo o sistema, analisava e via onde poderia melhorar, onde poderia implementar e então aos poucos aumentava o nível e complexidade do sistema. Depois decidi reescrever e dessa vez pensando como portifólio para publicar. Então fui fazendo e muito das lógicas que fiz no primeiro, coloquei nesse mas dessa vez em inglês o sistema. Porém no banco de dados decidi deixar em português mesmo. Demorei 1 dia para criar esse sistema mas não foi "percapta" pois eu fazia um pouco, descançava e fazia outras coisas e depois voltava, acho que sem intervalos demorei umas 6 horas. Pretendo lançar uma versão usando banco de dados SQL e API hospedada. Um sistema com validação melhor e mais avançada (nível de um dev sênior) e talvez faço um sistema desse em React. A primeira versão desse meu sistema não vou publicar. 

## Como Executar

* Certifique-se de ter o Python instalado (versão 3.6 ou superior).

* Clone este repositório ou baixe os arquivos.

* No terminal, navegue até a pasta do projeto e execute:

o arquivo `interface.py`
``` python interface.py ```

Siga as instruções exibidas na interface do terminal.

## Requisitos

Python 3.6+

Contribuição

Se desejar contribuir com melhorias para o projeto, pode fazer um fork do repositório e envie.

## Licença

Sinta-se livre para usá-lo e modificá-lo conforme necessário.
