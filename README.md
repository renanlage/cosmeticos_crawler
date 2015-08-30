# Época Cosméticos Crawler

Crawler implementado com o framework Scrapy da linguagem Python.
O crawler varre o site http://www.epocacosmeticos.com.br em busca de páginas de produto e extrai o título e url da página e o nome do produto

## Pré-requisitos
Os seguintes softwares precisam estar instalados para que o programa rode (links para instalação ao lado):
* Python 2.7+ (https://www.python.org/downloads/)
* pip (https://pip.pypa.io/en/latest/installing.html)

## Instalação

Para rodar o crawler é necessário instalar o Scrapy com o comando `pip install Scrapy` e clonar este repositório do GitHub com o comando:

`git clone https://github.com/renanlage/cosmeticos_crawler.git`

## Uso
No diretório raiz do programa rode o comando:

`scrapy runspider cosmeticos_crawler/spiders/cosmeticos.py -o cosmeticos.csv`

O comando iniciará o crawler que ao término salvará as informações extraídas no arquivo cosmeticos.csv

Ou um crawler que é mais preciso mas mais lento:

`scrapy runspider cosmeticos_crawler/spiders/cosmeticos_slow.py -o cosmeticos_slow.csv`

Opcionalmente pode-se usar o crawler que utiliza o sitemap para buscar todas as páginas de produto, o comando é:

`scrapy runspider cosmeticos_crawler/spiders/cosmeticos_sitemap.py -o cosmeticos_sitemap.csv`

Existe ainda um script para comparar e imprimir informações de dois arquivos extraídos por cada um dos métodos. Basta rodar o comando `python cosmeticos_comparator.py`