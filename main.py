from pathlib import Path

import streamlit as st
from pypdf import PdfReader

from summarizer import summarization


def extract_text(path: Path) -> str:
    reader = PdfReader(path)
    pages = reader.pages
    text = ""
    for index, page in enumerate(pages):
        text += (
            page.extract_text(
                extraction_mode="plain", layout_mode_space_vertically=True
            )
            .replace("\n", " ")
            .replace(" ", " ")
        )
        st.write(f"Página processada [{index+1}/{len(pages)}]")
    return text


def save_file(uploaded_file, file_path):
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


def chunk_text(text: str) -> list[str]:
    sentences = text.replace(".", "<eos>")
    sentences = sentences.replace("!", "<eos>")
    sentences = sentences.replace("?", "<eos>")
    sentences = sentences.split("<eos>")
    max_chunk = 500
    current_chunk = 0
    chunks = []

    for sentence in sentences:
        if len(sentences) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(" ")) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(" "))
            else:
                current_chunk += 1
                chunks.append(sentence.split(" "))
        else:
            print(current_chunk)
            chunks.append(sentence.split(" "))

    for index in range(len(chunks)):
        chunks[index] = " ".join(chunks[index])

    return chunks


def main():
    st.title("Processador de Arquivos PDF e TXT")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo PDF ou TXT", type=["pdf", "txt"]
    )

    if uploaded_file is not None:
        file_extension = Path(uploaded_file.name).suffix.lower()
        file_id = uploaded_file.file_id
        new_filename = f"{file_id}{file_extension}"

        # Cria a pasta public se ela não existir
        public_folder = Path("public")
        public_folder.mkdir(exist_ok=True)

        file_path = public_folder / new_filename
        save_file(uploaded_file, file_path)

        st.success(f"Arquivo salvo como {new_filename} na pasta public.")

        if file_extension == ".pdf":
            st.info("Processando arquivo PDF...")
            text = extract_text(file_path)
            txt_filename = f"{file_id}.txt"
            txt_path = public_folder / txt_filename
            txt_path.write_text(text, encoding="UTF-8")
            st.success(f"Texto extraído salvo como {txt_filename} na pasta public.")
        elif file_extension == ".txt":
            st.success("Arquivo TXT carregado com sucesso.")

        txt_path = public_folder / f"{file_id}.txt"
        chunks = chunk_text(txt_path.read_text())
        print(chunks)
        print("\n\n\n\n")

        with st.spinner("Sumarização em progresso..."):
            text = summarization(txt_path.read_text())
            st.code(text, language="markdown", wrap_lines=True)
            print(text)


if __name__ == "__main__":
    main()
