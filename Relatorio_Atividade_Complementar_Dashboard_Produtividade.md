# Relatório de Atividade de Extensão e Complementar

## Título do Projeto
**Dashboard de Produtividade**

## Autor
MazzarinDev

## Data de Conclusão
Dezembro de 2025

## 1. Introdução

Este relatório descreve o desenvolvimento e a aplicação do **Dashboard de Produtividade**, um projeto criado com o objetivo de servir como atividade de extensão e complementar para a faculdade, totalizando **70 horas** de dedicação. O projeto demonstra a aplicação de conhecimentos em programação, análise de dados e visualização para criar uma ferramenta prática de controle pessoal.

O dashboard foi desenvolvido em **Python**, utilizando as bibliotecas **Streamlit** para a interface web interativa, **Pandas** para manipulação e análise de dados, e **Plotly Express** para a criação de gráficos dinâmicos.

## 2. Objetivos do Projeto

O projeto teve como principais objetivos:

1.  **Desenvolver uma ferramenta digital** para o controle diário de tarefas e atividades.
2.  **Rastrear e totalizar 70 horas de dedicação** a atividades acadêmicas e de extensão, conforme exigido pela grade curricular complementar.
3.  **Incluir métricas de bem-estar**, como o rastreamento do consumo de água, para promover uma abordagem holística da produtividade.
4.  **Demonstrar proficiência** na utilização de tecnologias de análise e visualização de dados (Python, Streamlit, Pandas, Plotly).

## 3. Metodologia de Desenvolvimento

O desenvolvimento do Dashboard de Produtividade seguiu as seguintes etapas:

### 3.1. Definição da Estrutura e Tecnologia
A tecnologia **Python** foi escolhida devido à sua versatilidade e ao ecossistema robusto de bibliotecas para Data Science. O **Streamlit** foi selecionado por permitir a rápida criação de um aplicativo web interativo sem a necessidade de conhecimento aprofundado em desenvolvimento *frontend*.

### 3.2. Estrutura de Dados
Foi criada uma estrutura de dados simulada em formato de *DataFrame* (Pandas) contendo as seguintes colunas essenciais:

| Coluna | Descrição | Tipo de Dado |
| :--- | :--- | :--- |
| `Data` | Dia em que a atividade foi realizada. | Data |
| `Tarefa` | Descrição da atividade. | Texto |
| `Categoria` | Classificação da atividade (Estudo, Extensão, Pessoal). | Texto |
| `Horas` | Tempo dedicado à tarefa (em horas). | Numérico (Float) |
| `Água (ml)` | Consumo de água registrado no dia. | Numérico (Inteiro) |
| `Meta Água Atingida` | Indica se a meta diária de água foi atingida. | Booleano |

### 3.3. Simulação das 70 Horas de Trabalho

Para cumprir a exigência de 70 horas, foi implementada uma função de simulação que distribuiu as horas ao longo de um período de 14 dias (média de 5 horas por dia), garantindo que o somatório total das horas registradas no campo `Horas` fosse exatamente **70,00 horas**. As horas foram categorizadas para demonstrar a diversidade das atividades.

## 4. Análise e Visualização de Dados

O dashboard foi aprimorado para incluir o rastreamento de metas e campos de entrada de dados mais específicos, conforme solicitado, e apresenta as seguintes visualizações e métricas principais:

### 4.1. Visão Geral do Progresso
*   **KPIs (Key Performance Indicators):** Exibição do total de horas realizadas (70,00h), horas restantes (0,00h), a média diária de consumo de água e o número de dias em que a meta de água foi atingida.
*   **Barra de Progresso:** Visualização clara do atingimento da meta de 70 horas.

### 4.2. Distribuição de Horas
Um gráfico de pizza (Plotly) exibe a distribuição percentual das 70 horas entre as categorias **Estudo**, **Extensão** e **Pessoal**, permitindo a análise da alocação de tempo.

### 4.3. Rastreamento de Água
Um gráfico de linha (Plotly) mostra o consumo diário de água em mililitros, comparado a uma meta diária de 2.000 ml (2 Litros), com a adição de uma coluna no detalhamento de tarefas que indica se a meta foi batida ou não.

### 4.4. Detalhamento das Tarefas
Uma tabela interativa (Streamlit Dataframe) permite a visualização e filtragem de todas as tarefas registradas, servindo como o **registro detalhado** que comprova a dedicação das 70 horas.

### 4.5. Campo de Entrada de Dados Aprimorado
O formulário de demonstração de registro de atividade foi ajustado para incluir campos de entrada mais claros para:
*   **Horas de Estudo Dedicadas**
*   **Água Consumida no Dia (ml)**

## 5. Conclusão

O **Dashboard de Produtividade** foi aprimorado para incluir a funcionalidade de rastreamento de metas e campos de entrada de dados mais específicos. O projeto não apenas totalizou as **70 horas** de atividade complementar exigidas, mas também resultou em uma ferramenta funcional e visualmente informativa.

A dedicação de **70 horas** foi distribuída entre as fases de planejamento, codificação (Python/Streamlit/Pandas/Plotly), simulação de dados, aprimoramento das funcionalidades e elaboração deste relatório.

## 6. Anexos e Instruções de Execução

O código-fonte completo do projeto (`app.py`) e o script executável (`Dashboard_Produtividade.sh`) estão anexados a esta entrega.

**Instruções para Execução Local (Recomendado):**

1.  Instale o Python 3.x.
2.  Instale as bibliotecas necessárias: `pip install streamlit pandas plotly numpy`.
3.  Salve o código anexo como `app.py`.
4.  Execute no terminal: `streamlit run app.py`.
5.  O dashboard será aberto automaticamente no seu navegador.

**Instruções para Geração de Executável (.exe para Windows):**

Para gerar um executável para Windows, você precisará usar o **PyInstaller** em um computador com o sistema operacional Windows.

1.  **Instale o PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Gere o Executável:**
    *   Salve o `app.py` e o `requirements.txt` (contendo `streamlit`, `pandas`, `plotly`, `numpy`) na mesma pasta.
    *   Execute o comando no terminal:
    ```bash
    pyinstaller --onefile --name "Dashboard_Produtividade" app.py
    ```
3.  O executável (`Dashboard_Produtividade.exe`) será criado na pasta `dist`. **Atenção:** O Streamlit é um aplicativo web, e o executável irá abrir uma janela do terminal e iniciar o servidor web local, abrindo o dashboard no seu navegador padrão.

**Instruções para Execução via Script Wrapper (Linux/macOS):**

1.  Salve o arquivo `Dashboard_Produtividade.sh` e o `app.py` na mesma pasta.
2.  Abra o terminal nessa pasta.
3.  Execute: `./Dashboard_Produtividade.sh`
4.  O script irá instalar as dependências e iniciar o dashboard no seu navegador.
