# Document Library Ingestion & Metadata Handling

> **Module 08: SharePoint Operations | Topic 03**

## 1. Learning Outcomes
- **File Upload / Download:** Stream document binaries to and from SharePoint libraries safely.
- **Folder Navigation:** Traverse and create folder structures dynamically.
- **Metadata Tagging:** Attach structured properties (author, department, report date) to uploaded documents.
- **Preventing Corruption:** Use chunked uploads for large documents (> 250 MB).

## 2. Key Syntax & Concepts

### Document Upload Pattern
```python
def upload_file_to_library(session, site_url: str, library_name: str, file_path: Path):
    file_bytes = file_path.read_bytes()
    filename = file_path.name
    
    upload_url = (
        f"{site_url}/_api/web/GetFolderByServerRelativeUrl('{library_name}')"
        f"/Files/add(url='{filename}',overwrite=true)"
    )
    
    headers = {"Content-Type": "application/octet-stream"}
    response = session.post(upload_url, data=file_bytes, headers=headers)
    response.raise_for_status()
    print(f"Uploaded: {filename}")
    return response.json()
```

## 3. Common Mistakes & Gotchas
- **Invalid Characters in Filenames:** Characters like `" * : < > ? / \ |` are forbidden in SharePoint filenames. Sanitize filenames before upload.
- **Overwriting Unintentionally:** Setting `overwrite=true` without versioning enabled permanently destroys prior copies.

## 4. Practice Tasks
- **Task 1:** Build a Python function that reads an Excel report, sanitizes its filename, and uploads it to an executive library.

## 5. Self-Check Questions
- **Q1:** What content type header is used when streaming binary files to SharePoint?
- **Q2:** Why should filenames be sanitized prior to attempting upload?
