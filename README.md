# Compression-Run-Length
Programa de compressão e descompressão de imagens baseado no método Run Length Encoding em PYTHON3(python2 não suportado)

Dependencias:
  PIL
  pickle
  numpy
  
 Como usar:
  Use o compressor.py passando como argumento a imagem que deve ser comprimida. Isso gerará um arquivo data.txt com as informações dos píxeis
  Use o descompressor.py passando como argumento o nome do arquivo da nova imagem gerada pela descompressão do arquivo data.txt
  
 NOTA: ESSE MÉTODO NÃO FUNCIONA
 
**Edit do eu do futuro**: Esse método funciona, só não da forma que eu estava usando. Usar esse método em imagens reais sem qualquer tratamento prévio acaba gerando arquivos maiores (devido ao fato de que é muito improvável que dois ou mais pixels seguidos sejam iguais, mesmo que em preto e branco). 

O certo seria usar isso em arquivos em que é esperado que haja sequências grandes repetidas. Ou ainda, diminuir o espaço de cores possíveis dos pixels, para que áreas que aparentam ter a mesma cor mas tem uma leve variação em cada pixel sejam agrupadas pelo algoritmo. Isso levaria a degradação da qualidade da imagem na descompressão.
