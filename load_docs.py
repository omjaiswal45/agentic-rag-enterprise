from pathlib import Path
DOCS_DIR = Path("RAG-Multi-Corpus/datasets/ZX Bank/md")
def load_documents(folder):
    docs =[]
    for path in sorted (folder.rglob("*")):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding ="utf-8")
        docs.append({"filename": path.name, "text": text})
    return docs        
if __name__ == "__main__":
    docs = load_documents(DOCS_DIR)
    print("Documents loaded:", len(docs))

    # TODO 4: show the first 3 documents
    for doc in docs[:3]:                         # docs[:3] = only the first 3 items
        print("-----")
        print("File:", doc["filename"])
        print("Text:", doc["text"][:200])        # [:200] = only the first 200 characters