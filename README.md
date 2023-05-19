# API de Consulta de Municípios por Coordenadas Geográficas

Este projeto é uma API Flask que permite consultar o município brasileiro correspondente a um par de coordenadas geográficas (latitude e longitude). Utiliza a biblioteca Geopandas para carregar dados geográficos dos municípios brasileiros e a biblioteca Shapely para realizar consultas espaciais.

## Motivação

A criação da **BR Cidades API** surge como uma solução alternativa diante dos altos custos associados às APIs de geolocalização existentes. Muitas vezes, essas APIs oferecem recursos avançados e abrangentes, mas com preços elevados que podem ser inacessíveis para alguns projetos de menor escala.

A proposta da **BR Cidades API** é oferecer uma solução personalizada e econômica, focada apenas na localização por cidade. A ideia é aproveitar a rápida autorização de localização disponível em navegadores modernos, que permite obter as coordenadas do usuário de forma direta e eficiente. Ao utilizar essa abordagem, é possível dispensar a necessidade de uma API de geolocalização externa, reduzindo os custos associados.

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


## Exemplo de consulta à API usando um navegador moderno

Suponha que um usuário esteja utilizando um navegador moderno com suporte à geolocalização. Nesse caso, ele pode facilmente autorizar o acesso à sua localização atual. Com base nessas coordenadas, podemos fazer uma consulta à **BR Cidades API** para obter a cidade e o estado correspondentes.

Aqui está um exemplo de como seria a consulta à API utilizando JavaScript em um navegador moderno:

```javascript
navigator.geolocation.getCurrentPosition(function(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  
  // Fazendo a requisição à **BR Cidades API**
  fetch(`http://127.0.0.1:5000/city/${latitude},${longitude}`)
    .then(response => response.json())
    .then(data => {
      const city = data.city;
      const uf = data.uf;
      
      console.log(`Cidade: ${city}, UF: ${uf}`);
    })
    .catch(error => {
      console.error('Ocorreu um erro:', error);
    });
});
```

Nesse exemplo, utilizamos a função `getCurrentPosition` do objeto `navigator.geolocation` para obter as coordenadas de localização atual do usuário. Em seguida, fazemos uma requisição à **BR Cidades API** passando as coordenadas na URL. A resposta da API retorna um objeto JSON com a cidade e o estado correspondentes, que são exibidos no console do navegador.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.


