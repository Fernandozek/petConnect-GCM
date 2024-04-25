# PetConnect - Conexões que Salvam

A preocupação crescente com o número cada vez maior de animais desabrigados e em situação de vulnerabilidade em conjunto com a busca pelo bem estar destes animais, fez com que surgisse a PetConnect, que visa se tornar uma alternativa positiva e solidária para auxiliar as instituições na divulgação de animais que estão em busca de um lar, visando facilitar o processo de  adoção.

O PetConnect trata-se de um sistema que possui como objetivo criar uma conexão afetiva e duradoura entre animais resgatados ou abandonados a potenciais adotantes que possuem interesse em compartilhar um lar amoroso com esses animais. O sistema visa facilitar a comunicação durante o processo de adoção, tornando mais acessível e seguro, atuando como intermediador entre as organizações filantrópicas que resgatam e cuidam dos animais, com a população que busca realizar uma adoção responsável. Para que essa relação se torne o mais simples possível o sistema oferece uma interface amigável e intuitiva disponibilizando que os usuários que possuem interesse em realizar a adoção possam explorar as informações dos animais disponíveis, conhecendo suas características, histórias, personalidades e necessidades especiais, caso tenham alguma.

Promovendo como ponto principal uma cultura de adoção responsável, ajudando a dar aos animais resgatados uma segunda chance de terem uma vida cheia de amor e cuidado, ao mesmo tempo que fortalece a rede de apoio a ações filantrópicas em benefício desses animais.

## Como rodar o projeto

## Pré-requisitos

- Python 3.8+
* Recomendado: Python 3.10.9
## Configuração do Ambiente

1. Clone o repositório:
    
    git clone https://github.com/Fernandozek/petConnect-GCM.git
    cd petConnect-GCM
    

2. Crie um ambiente virtual e ative-o:
    
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    

3. Instale as dependências:
    
    pip install -r requirements-dev.txt
    
    ou
    
    pip install -r requirements.txt
    

## Executando o Projeto

1. Aplique as migrações:
    
    python manage.py migrate
    

2. Execute o servidor de desenvolvimento:
    
    python manage.py runserver
    

Agora você pode acessar o site em http://localhost:8000/api.

## Executando os Testes

Para executar os testes, use o seguinte comando:


python manage.py test api


### Utilizando o coverage:
Executando

coverage run manage.py test api


### Criando o report

coverage report


### Criando a documentação em html

coverage html