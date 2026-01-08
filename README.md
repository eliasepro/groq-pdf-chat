# Groq PDF Chat

Um chatbot simples e eficiente que permite fazer perguntas para arquivos PDF.

O projeto utiliza a técnica de **RAG (Retrieval-Augmented Generation)** combinando a velocidade da **Groq Cloud** (usando Llama 3) para geração de texto com processamento local leve para embeddings.

## 💡 Sobre o projeto

A ideia principal é permitir conversar com documentos sem precisar de um computador superpotente e sem gastar com APIs pagas.

- **Processamento de Texto (Nuvem):** Utiliza a API gratuita da Groq, que roda modelos Llama 3 em chips LPU ultra-rápidos.
- **Embeddings (Local):** Utiliza o modelo `all-MiniLM-L6-v2` via Hugging Face, que roda tranquilamente na CPU.
- **Interface:** Construída com Streamlit para ser simples e funcional.

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **LangChain**: Orquestração da IA.
- **Streamlit**: Interface web.
- **Groq Cloud**: LLM (Llama-3-70b).
- **FAISS**: Banco de dados vetorial (para busca semântica).
- **Hugging Face**: Embeddings open-source.

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone [https://github.com/SEU-USUARIO/groq-pdf-chat.git](https://github.com/SEU-USUARIO/groq-pdf-chat.git)
cd groq-pdf-chat
```

### 2. Crie um ambiente virtual (Recomendado)

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

```

### 3. Instale as dependências

Crie um arquivo `requirements.txt` com as bibliotecas necessárias ou instale manualmente:

```bash
pip install langchain langchain-community langchain-groq langchain-huggingface streamlit pypdf faiss-cpu sentence-transformers

```

### 4. Configure a API Key

Você precisará de uma chave de API gratuita da Groq.

1. Acesse [console.groq.com](https://console.groq.com/keys).
2. Crie uma chave.
3. Ao rodar o projeto, insira a chave na barra lateral da aplicação.

### 5. Execute o projeto

```bash
streamlit run app.py

```

O navegador abrirá automaticamente no endereço `http://localhost:8501`.

## 📂 Estrutura do Código

- `app.py`: Código principal contendo a interface e a lógica do RAG.
- A aplicação processa o PDF dividindo-o em "chunks" (pedaços), converte para vetores numéricos e busca as partes relevantes quando você faz uma pergunta.

---

Desenvolvido para fins de estudo sobre IA Generativa e RAG.
