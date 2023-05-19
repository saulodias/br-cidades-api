# API de Consulta de Municípios por Coordenadas Geográficas

Este projeto é uma API Flask que permite consultar o município brasileiro correspondente a um par de coordenadas geográficas (latitude e longitude). Utiliza a biblioteca Geopandas para carregar dados geográficos dos municípios brasileiros e a biblioteca Shapely para realizar consultas espaciais.

## Instalação

Siga as instruções abaixo para configurar e executar o projeto:

1. Faça o download do arquivo `BR_Municipios_2022.zip` contendo os dados dos municípios brasileiros no site do IBGE através do link: [IBGE - Malhas Territoriais](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html). 
    > [Link direto para municípios (2022)](https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip)

2. Coloque o arquivo `BR_Municipios_2022.zip` no mesmo diretório do arquivo `api.py` do projeto.

3. É recomendado criar um ambiente virtual para isolar as dependências do projeto. Utilize o seguinte comando para criar e ativar o ambiente virtual:

    ```bash
    python -m venv api_env
    .\api_env\Scripts\activate
    ```

4. Instale as dependências do projeto. Execute o seguinte comando:

    ```bash
    python -m pip install flask geopandas
    ```

## Executando o servidor de teste

Após a instalação das dependências, você pode iniciar o servidor de teste para consultar os municípios por coordenadas geográficas. Execute o seguinte comando:

```bash
python api.py
```

O servidor será iniciado e estará pronto para receber consultas. A API estará disponível em http://localhost:5000.

## Utilizando a API

A API possui um único endpoint:

### Consultar município por coordenadas

- URL: /city/<coordinates>
- Método: GET

Para fazer uma consulta, substitua `<coordinates>` pelas coordenadas geográficas desejadas no formato "latitude,longitude". A API retornará um JSON com as informações do município correspondente ou uma mensagem de erro caso não seja encontrado nenhum município para as coordenadas fornecidas.


## Exemplo de consulta de município por coordenadas

### Coordenadas

-22.9029407, -43.1736189

### Rota

GET http://127.0.0.1:5000/city/-22.9029407,-43.1736189

### Resultado

```json
{"city": "Rio de Janeiro", "uf": "RJ"}
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.


