Essa é um começo de uma Integração entre git e fabric

Criaremos um projeto no fabric, usaremos lakehouse, notebook spark, dataflow , tambem criaremos dos workspace relatorio e engenharia.

## Introdução
Este projeto foi desenvolvido utilizando o Microsoft Fabric, integrado com Power BI para a criação de um relatório financeiro. Abaixo está uma descrição detalhada de cada etapa e componente envolvido.

## Vantagens de usar o Microsoft Fabric
Integração: Facilita a integração de diferentes fontes de dados.

- Escalabilidade: Capaz de lidar com grandes volumes de dados.

- Flexibilidade: Permite utilizar diferentes ferramentas de ETL e análise.

- Segurança: Oferece segurança robusta para proteção dos dados.

# O que é o OneLake?
- O OneLake é um recurso do Microsoft Fabric que unifica o armazenamento de dados em um único local, simplificando o gerenciamento e acessibilidade dos dados.

# O que é Lakehouse?
- O Lakehouse combina as melhores características de data lakes e data warehouses, permitindo armazenar dados não estruturados e estruturados com capacidades de processamento analítico.

# O que é Tabela Delta?
- A Tabela Delta é um formato de armazenamento otimizado que permite a execução de operações ACID (Atomicidade, Consistência, Isolamento, Durabilidade) em um data lake.

# Estrutura do Projeto
### 1. Criação dos Workspaces

* Dois workspaces foram criados: Engenharia e Relatórios.

* O workspace Engenharia é utilizado para armazenamento e processamento dos dados.

* O workspace Relatórios é utilizado para a criação dos relatórios no Power BI.

### 2. Criação do Lakehouse

* Um Lakehouse foi criado no workspace Engenharia para armazenar as tabelas: dPlanoContas, dCalendario, fPagamentos e fRecebimentos.

* ETL com Notebook Spark

* Utilização de um notebook Spark para o tratamento da tabela fRecebimentos.

Etapas do Tratamento:

## 3. Leitura dos dados brutos.

* Limpeza e transformação dos dados.

* Gravação dos dados tratados na Tabela Delta.

## 4. ETL com Dataflow Gen 2

* Utilização do Dataflow Gen 2 para o tratamento da tabela fPagamentos.

## 5. Etapas do Tratamento:

* Importação dos dados.

* Aplicação de transformações necessárias.

* Carregamento dos dados tratados no Lakehouse.

* Criação do Modelo Semântico

* Conexão do modelo semântico com o Power BI Desktop.

* Criação de relações entre as tabelas e definição de medidas e cálculos necessários para a análise financeira.

# Conclusão

- Este projeto demonstra a utilização integrada do Microsoft Fabric e Power BI para o desenvolvimento de um relatório financeiro completo.
As tecnologias utilizadas proporcionam um fluxo de trabalho eficiente e seguro para o gerenciamento e análise de dados.


### Acesso ao Relatório Financeiro
Você pode acessar o relatório financeiro desenvolvido no Power BI através deste [link](https://app.powerbi.com/reportEmbed?reportId=8bf27f2d-d683-4254-a2a0-5f7054c971fa&autoAuth=true&ctid=dc99190e-570a-495f-95c0-f63a23fc80de).


![Relatório_Financeiro](https://github.com/Robertofsouzas/Git-fabric/blob/main/Relatorio_financeiro.png)

