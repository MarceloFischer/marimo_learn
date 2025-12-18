# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "openai==2.9.0",
#     "pandas==2.2.3",
#     "polars==1.22.0",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Uma introdução ao Polars

    _original por [Koushik Khan](https://github.com/koushikkhan)._

    _traduzido por [Marcelo Fischer](https://github.com/MarceloFischer) e [Gemini](https://gemini.google.com/app)_

    Este notebook fornece uma visão geral do [Polars](https://pola.rs/), uma biblioteca de manipulação de dados rápida e fácil de usar para Python, e a compara com alternativas como Pandas e PySpark.

    Assim como no Pandas e no PySpark, a estrutura de dados central no Polars é o **DataFrame**, uma estrutura de dados tabular composta por colunas nomeadas. Por exemplo, a próxima célula constrói um DataFrame que registra o gênero, a idade e a altura, em centímetros, para uma série de indivíduos.
    """)
    return


@app.cell
def _():
    import polars as pl

    df_pl = pl.DataFrame(
        { 
            "gênero": ["Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", 
                       "Masculino", "Feminino", "Masculino", "Feminino"],
            "idade": [13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
            "altura_cm": [150.0, 170.0, 146.5, 142.0, 155.0, 165.0, 170.8, 130.0, 132.5, 162.0]
        }
    )
    df_pl
    return (pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Ao contrário da Pandas, a biblioteca pioneira de DataFrame do Python, o Polars foi projetado com desempenho e usabilidade em mente — o Polars pode escalar para grandes conjuntos de dados com facilidade, mantendo uma API simples e intuitiva.

    O desempenho do Polars deve-se a vários fatores, incluindo sua implementação em Rust e sua capacidade de realizar operações de maneira paralelizada e vetorizada. Ele suporta uma ampla gama de tipos de dados, otimizações avançadas de consulta e integração perfeita com outras bibliotecas Python, tornando-o uma ferramenta versátil para cientistas de dados, engenheiros e analistas. Além disso, o Polars fornece uma API preguiçosa (lazy API) para execução atrasada, permitindo que os usuários otimizem seus fluxos de trabalho encadeando operações e executando-as em uma única chamada.

    Com seu foco em velocidade, escalabilidade e facilidade de uso, o Polars está rapidamente se tornando uma escolha preferencial para profissionais de dados que buscam agilizar seus pipelines de processamento de dados e enfrentar desafios de dados em larga escala.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Escolhendo Polars ao invés de Pandas

    Nesta seção, iremos apresentar algumas razões que fazem o Polars ser superior ao Pandas, seguido de exemplos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Sintaxe Intuitiva

    A sintaxe do Polars é semelhante à do PySpark e intuitiva como o SQL, fazendo uso intenso de **encadeamento de métodos**. Isso facilita a transição de profissionais de dados para o Polars e resulta em uma API mais concisa e legível que a do Pandas.

    **Exemplo:** abaixo, realizamos uma filtragem e agregação básica de dados com Pandas e comparamos ao código necessário para realizar a mesma tarefa com Polars.
    """)
    return


@app.cell
def _():
    import pandas as pd

    df_pd = pd.DataFrame(
        { 
            "gênero": ["Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", 
                       "Masculino", "Feminino", "Masculino", "Feminino"],
            "idade": [13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
            "altura_cm": [150.0, 170.0, 146.5, 142.0, 155.0, 165.0, 170.8, 130.0, 132.5, 162.0]
        }
    )

    # consulta: altura média de homens e mulheres acima dos 15 anos de idade

    # passo-1: filtro
    filtrado_df_pd = df_pd[df_pd["idade"] > 15]

    # passo-2: agrupamento e agregação
    resultado_pd = filtrado_df_pd.groupby("gênero")["altura_cm"].mean()
    resultado_pd
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O mesmo pode ser feito em Polars de forma mais concisa, utilizando encadeamento de métodos. Observe como o código em Polars é mais natural de ser lido como um texto em inglês.
    """)
    return


@app.cell
def _(pl):
    data_pl = pl.DataFrame(
        { 
            "gênero": ["Masculino", "Feminino", "Masculino", "Feminino", "Masculino", "Feminino", 
                       "Masculino", "Feminino", "Masculino", "Feminino"],
            "idade": [13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
            "altura_cm": [150.0, 170.0, 146.5, 142.0, 155.0, 165.0, 170.8, 130.0, 132.5, 162.0]
        }
    )

    # consulta: altura média de homens e mulheres acima dos 15 anos de idade

    # filtro, agrupamento e agregação utilizando encadeamento de métodos
    resultado_pl = data_pl.filter(pl.col("idade") > 15).group_by("gênero").agg(pl.mean("altura_cm"))
    resultado_pl
    return (data_pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Observe como o Polars usa uma abordagem de encadeamento de métodos, semelhante ao PySpark, o que torna o código mais legível e expressivo, ao mesmo tempo em que usa uma *única linha* para realizar a consulta.

    Além disso, o Polars suporta operações do tipo SQL *nativamente*, o que permite escrever consultas SQL diretamente em um dataframe do Polars:
    """)
    return


@app.cell
def _(data_pl):
    resultado = data_pl.sql("SELECT gênero, AVG(altura_cm) FROM self WHERE idade > 15 GROUP BY gênero")
    resultado
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Uma Extensa Coleção de APIs Nativas

    O Polars possui uma API abrangente que permite realizar praticamente qualquer operação usando métodos nativos. Em contraste, o Pandas frequentemente exige que operações mais complexas sejam tratadas usando o método `apply` com uma função lambda. O problema com o `apply` é que ele processa as linhas sequencialmente, percorrendo o DataFrame uma linha por vez (como se fosse um `for` loop), o que pode ser ineficiente. Ao aproveitar os métodos nativos do Polars, você pode operar em colunas inteiras de uma vez, liberando o poder do paralelismo **SIMD (Single Instruction, Multiple Data)**. Essa abordagem não apenas simplifica seu código, mas também melhora significativamente o desempenho.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Otimização de Consultas 📈

    Um fator chave por trás do desempenho do Polars reside em sua **estratégia de avaliação**. Enquanto o Pandas adota a **execução eager (imediata)** por padrão, executando operações na ordem exata em que são escritas, o Polars oferece tanto a **execução eager quanto a lazy (preguiçosa)**. Com a execução lazy, o Polars emprega um **otimizador de consultas** que analisa todas as operações necessárias e determina a forma mais eficiente de executá-las. Essa otimização pode envolver a reordenação de operações, a eliminação de cálculos redundantes e muito mais.

    Por exemplo, considere a seguinte expressão para calcular a média da coluna `Número1` para as categorias "A" e "B" na coluna `Categoria`:

    ```python
    (
        df
        .groupby(by="Categoria").agg(pl.col("Número1").mean())
        .filter(pl.col("Categoria").is_in(["A", "B"]))
    )
    ```

    Se executada de forma eager (imediata), a operação `groupby` seria primeiro aplicada a todo o DataFrame, seguida pela filtragem dos resultados por `Categoria`. No entanto, com a **execução lazy (preguiçosa)**, o Polars pode otimizar esse processo filtrando primeiro o DataFrame para incluir apenas as categorias relevantes ("A" e "B") e, em seguida, realizando a operação `groupby` no conjunto de dados reduzido. Essa abordagem minimiza cálculos desnecessários e melhora significativamente a eficiência.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Escalabilidade — lidando com grandes conjuntos de dados em memória ⬆️

    O Pandas é limitado por seu design de thread única e pela dependência do Python, o que o torna ineficiente para processar grandes conjuntos de dados. O Polars, por outro lado, é construído em Rust e otimizado para processamento paralelo, permitindo que ele lide com conjuntos de dados que são ordens de magnitude maiores.

    **Exemplo: Processando um Conjunto de Dados Grande**
    No Pandas, carregar um conjunto de dados grande (ex: 10GB) frequentemente resulta em erros de memória:

    ```python
    # Isto pode falhar com datasets muito grandes
    df = pd.read_csv("dataset_grande.csv")
    ```

    No Polars, a mesma operação é executada rapidamente, sem pressão de memória:

    ```python
    df = pl.read_csv("dataset_grande.csv")
    ```

    O Polars também suporta avaliação lazy (preguiçosa), que permite otimizar seus fluxos de trabalho adiando os cálculos até que sejam necessários. Isso é particularmente útil para grandes conjuntos de dados:

    ```python
    df = pl.scan_csv("dataset_grande.csv")  # Lazy DataFrame (Datarame preguiçoso)
    result = df.filter(pl.col("A") > 1).groupby("A").agg(pl.sum("B")).collect()  # Executa a operação
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Compatibilidade com Outras Bibliotecas de Aprendizado de Máquina 🤝

    O Polars se integra perfeitamente com bibliotecas populares de aprendizado de máquina, como Scikit-learn, PyTorch e TensorFlow. Sua capacidade de lidar com grandes conjuntos de dados de forma eficiente o torna uma excelente escolha para o pré-processamento de dados antes de alimentá-los em modelos de ML (machine learning [aprendizado de máquina]).

    **Exemplo: Pré-processamento de dados para Scikit-learn**

    ```python
    import polars as pl
    from sklearn.linear_model import LinearRegression

    # Carregar e pré-processar dados
    df = pl.read_csv("dados.csv")
    X = df.select(["variável1", "variável2"]).to_numpy()
    y = df.select("alvo").to_numpy()

    # Treina o modelo de ML (machine learning [aprendizado de máquina])
    modelo = LinearRegression()
    modelo.fit(X, y)
    ```

    O Polars também suporta a conversão para outros formatos, como NumPy arrays e Pandas Dataframes, garantindo compatibilidade com praticamente qualquer biblioteca de ML:

    ```python
    # Convete para Pandas Dataframe
    pandas_df = df.to_pandas()

    # Converte para NumPy array
    numpy_array = df.to_numpy()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Fácil de usar, com oportunidades para usuários avançados

    O Polars suporta operações avançadas como:

    - **manipulação de datas (date handling)**
    - **Funções de janela (window functions)**
    - **junções (joins)**
    - **tipos de dados aninhados (nested data types)**

    o que o torna uma ferramenta versátil para manipulação de dados.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Por que não o PySpark?

    Embora o **PySpark** seja uma ferramenta versátil que transformou a maneira como o big data é gerenciado e processado em Python, seu **processo de configuração complexo** pode ser intimidante, especialmente para iniciantes. Em contraste, o **Polars** exige uma configuração mínima e está pronto para uso imediato, tornando-o mais acessível para usuários de todos os níveis de habilidade.f

    Ao decidir entre os dois, o **PySpark** é a escolha preferida para processar grandes conjuntos de dados distribuídos em um **cluster de múltiplos nós**. No entanto, para computações em **uma máquina de nó único**, o Polars é uma excelente alternativa. Surpreendentemente, o Polars é capaz de lidar com conjuntos de dados que excedem o tamanho da memória RAM disponível, tornando-o uma ferramenta poderosa para o processamento eficiente de dados, mesmo em hardware limitado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🔖 Referências

    - [Polars official website](https://pola.rs/)
    - [Polars vs. Pandas](https://blog.jetbrains.com/pycharm/2024/07/polars-vs-pandas/)
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
