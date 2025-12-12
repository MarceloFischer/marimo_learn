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
    ### Query optimization 📈

    A key factor behind Polars' performance lies in its **evaluation strategy**. While Pandas defaults to **eager execution**, executing operations in the exact order they are written, Polars offers both **eager and lazy execution**. With lazy execution, Polars employs a **query optimizer** that analyzes all required operations and determines the most efficient way to execute them. This optimization can involve reordering operations, eliminating redundant calculations, and more.

    For example, consider the following expression to calculate the mean of the `Number1` column for categories "A" and "B" in the `Category` column:

    ```python
    (
        df
        .groupby(by="Category").agg(pl.col("Number1").mean())
        .filter(pl.col("Category").is_in(["A", "B"]))
    )
    ```

    If executed eagerly, the `groupby` operation would first be applied to the entire DataFrame, followed by filtering the results by `Category`. However, with **lazy execution**, Polars can optimize this process by first filtering the DataFrame to include only the relevant categories ("A" and "B") and then performing the `groupby` operation on the reduced dataset. This approach minimizes unnecessary computations and significantly improves efficiency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Scalability — handling large datasets in memory ⬆️

    Pandas is limited by its single-threaded design and reliance on Python, which makes it inefficient for processing large datasets. Polars, on the other hand, is built in Rust and optimized for parallel processing, enabling it to handle datasets that are orders of magnitude larger.

    **Example: Processing a Large Dataset**
    In Pandas, loading a large dataset (e.g., 10GB) often results in memory errors:

    ```python
    # This may fail with large datasets
    df = pd.read_csv("large_dataset.csv")
    ```

    In Polars, the same operation runs quickly, without memory pressure:

    ```python
    df = pl.read_csv("large_dataset.csv")
    ```

    Polars also supports lazy evaluation, which allows you to optimize your workflows by deferring computations until necessary. This is particularly useful for large datasets:

    ```python
    df = pl.scan_csv("large_dataset.csv")  # Lazy DataFrame
    result = df.filter(pl.col("A") > 1).groupby("A").agg(pl.sum("B")).collect()  # Execute
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Compatibility with other machine learning libraries 🤝

    Polars integrates seamlessly with popular machine learning libraries like Scikit-learn, PyTorch, and TensorFlow. Its ability to handle large datasets efficiently makes it an excellent choice for preprocessing data before feeding it into ML models.

    **Example: Preprocessing Data for Scikit-learn**

    ```python
    import polars as pl
    from sklearn.linear_model import LinearRegression

    # Load and preprocess data
    df = pl.read_csv("data.csv")
    X = df.select(["feature1", "feature2"]).to_numpy()
    y = df.select("target").to_numpy()

    # Train a model
    model = LinearRegression()
    model.fit(X, y)
    ```

    Polars also supports conversion to other formats like NumPy arrays and Pandas DataFrames, ensuring compatibility with virtually any ML library:

    ```python
    # Convert to Pandas DataFrame
    pandas_df = df.to_pandas()

    # Convert to NumPy array
    numpy_array = df.to_numpy()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### Easy to use, with room for power users

    Polars supports advanced operations like

    - **date handling**
    - **window functions**
    - **joins**
    - **nested data types**

    which is making it a versatile tool for data manipulation.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Why not PySpark?

    While **PySpark** is versatile tool that has transformed the way big data is handled and processed in Python, its **complex setup process** can be intimidating, especially for beginners. In contrast, **Polars** requires minimal setup and is ready to use right out of the box, making it more accessible for users of all skill levels.

    When deciding between the two, **PySpark** is the preferred choice for processing large datasets distributed across a **multi-node cluster**. However, for computations on a **single-node machine**, **Polars** is an excellent alternative. Remarkably, Polars is capable of handling datasets that exceed the size of the available RAM, making it a powerful tool for efficient data processing even on limited hardware.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🔖 References

    - [Polars official website](https://pola.rs/)
    - [Polars vs. Pandas](https://blog.jetbrains.com/pycharm/2024/07/polars-vs-pandas/)
    """)
    return


if __name__ == "__main__":
    app.run()
