# instalação para usar banco de dados
# instalação da biblioteca sqlalchemy e pymysql

# IMPORTANDO A BIBLIOTECA
## INICIALIZANDO AS VARIÁVEIS DE CONEXÃO
from sqlalchemy import create_engine, text

#Variáveis de conexão com o banco
host = "localhost"
user =  "root"
password = "root"
database = "bd_produtos"

# Função pra conectar ao banco:
def conecta_banco():
    try:
        engine= create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}") # URL DE CONEXÃO COM O BANCO, USANDO SQLAlchemy e PyMySQL
        with engine.connect () as conexao:  # estabelece a conexão
            query = "SELECT * FROM vendas"  # Query: "Linguagem SQL p selecionar todos os registros da tab. de produtos"
            resultados = conexao.execute(text(query)) # conexao.execute - executa a consulta no banco de dados  text(query) - transforma a string da qery em um objeto comp. com SQLAlchemy
            for item in resultados:
                print (f"Produto: {item[0]}, DataVenda: {item[1]}, Categoria: {item[2]}, Valor: {item[3]}")

    except ImportError as e:
        print (f"Erro: {e}")    
    
# Chama função que conecta ao banco de dados
conecta_banco()    