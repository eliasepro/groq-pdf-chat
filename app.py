import streamlit as st
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  # Embeddings gratuitos
from langchain_groq import ChatGroq # A IA da Groq
from langchain.chains import RetrievalQA

# Configuração da Página
st.set_page_config(page_title="Chat PDF", page_icon="🦙")
st.title("Chat PDF com groq")

# Sidebar
with st.sidebar:
    st.header("Configurações")
    # Link para ajudar o usuário a achar a chave
    st.markdown("[Obtenha sua API Key grátis aqui](https://console.groq.com/keys)")
    groq_api_key = st.text_input("Groq API Key", type="password")
    
    if not groq_api_key:
        st.warning("Insira a chave da Groq para começar.")
        st.stop()
    
    uploaded_file = st.file_uploader("Carregue seu PDF", type="pdf")

def main():
    if uploaded_file is not None:
        # Salvar arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        st.info("Lendo documento... Aguarde.")
        
        try:
            # 1. Carregar PDF
            loader = PyPDFLoader(tmp_path)
            documents = loader.load()

            # 2. Dividir Texto
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            splits = text_splitter.split_documents(documents)

            # 3. Embeddings (A parte que roda local, mas é leve)
            # Usamos um modelo "MiniLM" que é muito rápido e não pesa na CPU
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            
            vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

            st.success("Tudo pronto!")

            # 4. Configurar o Modelo Llama 3 na Groq
            # O modelo 'llama-3.3-70b-versatile' é muito inteligente e rápido
            llm = ChatGroq(
                groq_api_key=groq_api_key, 
                model_name="llama-3.3-70b-versatile",
                temperature=0
            )
            
            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vectorstore.as_retriever()
            )

            # 5. Chat
            query = st.text_input("Pergunte algo sobre o PDF:")
            
            if query:
                with st.spinner("Consultando a nuvem..."):
                    resposta = qa_chain.invoke({"query": query})
                    st.write("### Resposta:")
                    st.write(resposta['result'])

        except Exception as e:
            st.error(f"Erro: {e}")
        
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == "__main__":
    main()