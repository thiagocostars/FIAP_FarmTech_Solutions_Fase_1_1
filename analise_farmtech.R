#THIAGO SALES - FIAP - FARM TECH SOLUTION - FASE 1
# Script R para Análise de Dados da FarmTech Solutions
# Instala e carrega o pacote 'dplyr' para manipulação de dados.
# O 'dplyr' fornece funções para filtrar, selecionar e resumir dados.
# Se os pacotes já estiverem instalados, a linha 'install.packages' pode ser comentada.
if (!require(dplyr)) {
  install.packages("dplyr")
  library(dplyr)
}

# Instala e carrega pacotes para conexão com API e tratamento de JSON.
if (!require(httr) | !require(jsonlite)) {
  install.packages("httr")
  install.packages("jsonlite")
  library(httr)
  library(jsonlite)
}

# 1. Leitura dos dados do arquivo CSV
# O arquivo CSV deve estar na mesma pasta que este script.
dados_culturas <- read.csv("dados_culturas.csv")

# 2. Exibição dos dados lidos para verificação.
print("Dados lidos do arquivo CSV:")
print(dados_culturas)

# 3. Cálculo de estatísticas básicas (média e desvio padrão).
# O operador '%>%', do pacote 'dplyr', passa o resultado de uma função para a próxima.
estatisticas_gerais <- dados_culturas %>%
  summarise(
    media_areas = mean(area),
    desvio_padrao_areas = sd(area),
    media_insumos = mean(insumos_necessarios),
    desvio_padrao_insumos = sd(insumos_necessarios)
  )

print("\nEstatísticas Gerais dos Dados:")
print(estatisticas_gerais)

# API

# Configurações da API - OpenWeatherMap (https://openweathermap.org/).
api_key <- "INSERIR SUA API KEY AQUI"
cidade <- "Sao Paulo" # Escolhida
url_base <- "http://api.openweathermap.org/data/2.5/weather"

# 4. Fazer a requisição à API.
# O pacote 'httr' é usado para fazer requisições HTTP.
resposta <- GET(url_base, query = list(q = cidade, appid = api_key, units = "metric", lang = "pt_br"))

# 5. Processar a resposta da API (JSON).
# O 'jsonlite' converte a resposta da web para um formato que o R pode usar.
dados_tempo <- fromJSON(content(resposta, "text", encoding = "UTF-8"))

# 6. Exibir informações relevantes.
# O 'if' verifica se a requisição foi bem-sucedida (código 200 OK).
if (resposta$status_code == 200) {
  temperatura <- dados_tempo$main$temp
  descricao_tempo <- dados_tempo$weather$description
  umidade <- dados_tempo$main$humidity
  
  print(paste("\nDados meteorológicos para", cidade, ":"))
  print(paste("Temperatura:", temperatura, "°C"))
  print(paste("Condição:", descricao_tempo))
  print(paste("Umidade:", umidade, "%"))
} else {
  print("\nErro ao buscar dados da API. Verifique a chave ou a cidade.")
  print(content(resposta, "text", encoding = "UTF-8"))
}