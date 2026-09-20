from app.services.ingestion import load_file, Chunk_documents
from pathlib import Path
docs = load_file(Path("data/sample_kb/company_hr_handbook.md"))
chunked_docs = Chunk_documents(docs)

print(chunked_docs)