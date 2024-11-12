# Agente de Resumo (Texto e PDF)

## O quê?

Uma ferramenta alimentada por IA que analisa e destila documentos extensos (tanto texto simples como PDFs) em resumos concisos e informativos. Este agente utiliza técnicas avançadas de processamento de linguagem natural para:

- Identificar e extrair informações-chave
- Gerar resumos que capturam as ideias principais e detalhes críticos
- Destacar pontos essenciais para uma compreensão rápida
- Fornecer uma forma simplificada de aceder e compreender o conteúdo do documento

A ferramenta reduz significativamente o tempo necessário para a análise de documentos, permitindo aos utilizadores captar rapidamente os conceitos principais e tomar decisões informadas com base no conteúdo resumido.

## Porquê?

1. **Eficiência de Tempo**: Reduz drasticamente o tempo necessário para extrair informações valiosas de documentos extensos.
2. **Compreensão Melhorada**: Fornece uma visão geral clara das ideias principais, facilitando uma melhor compreensão de tópicos complexos.
3. **Tomada de Decisões Informada**: Permite decisões mais rápidas e confiantes ao apresentar informações essenciais num formato digerível.
4. **Gestão do Conhecimento**: Facilita a organização e categorização eficiente da informação, apoiando a criação de bases de conhecimento abrangentes.
5. **Acessibilidade**: Torna o conteúdo denso ou técnico mais acessível a um público mais vasto.
6. **Compreensão Multi-língua**: Suporta resumos em múltiplas línguas, quebrando barreiras linguísticas na análise de documentos.

## Como?

O Agente de Resumo utiliza uma poderosa combinação de bibliotecas e modelos:

1. **PyPDF (pypdf)**:

   - Lida com a análise de ficheiros PDF e extração de texto
   - Permite ao agente processar ficheiros de texto e PDFs de forma contínua

2. **Hugging Face Transformers**:

   - Fornece modelos de processamento de linguagem natural de última geração
   - Oferece uma estrutura flexível para implementar e afinar modelos de resumo

3. **Modelo mT5 Multilingual XLSum** ([csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum)):

   - Um modelo transformador multilíngue de texto para texto, afinado para resumos
   - Suporta resumos em 45 línguas, tornando-o versátil para diversos tipos de documentos
   - Destaca-se na geração de resumos coerentes e concisos, preservando informações-chave

4. **Streamlit**:
   - Cria uma interface web intuitiva e interativa para o agente de resumo
   - Permite aos utilizadores carregar facilmente documentos, personalizar parâmetros de resumo e visualizar resultados

## Visão Geral da Implementação

1. **Entrada de Documentos**: Os utilizadores carregam ficheiros de texto ou PDF através da interface Streamlit.
2. **Extração de Texto**: Para PDFs, o PyPDF extrai o conteúdo do texto.
3. **Pré-processamento**: O texto extraído é limpo e preparado para resumo.
4. **Resumo**: O modelo mT5 processa o texto, gerando um resumo conciso.
5. **Saída**: O resumo é apresentado ao utilizador através da interface Streamlit, com opções para ajustar o comprimento ou áreas de foco, se necessário.

Esta poderosa combinação de ferramentas permite ao Agente de Resumo processar e resumir eficientemente uma vasta gama de documentos, fornecendo informações valiosas e poupando tempo aos utilizadores em várias indústrias e aplicações.
