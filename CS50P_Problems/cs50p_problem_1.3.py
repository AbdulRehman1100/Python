media_types = {
    "gif":  "image/gif",
    "jpg":  "image/jpeg",
    "jpeg": "image/jpeg",
    "png":  "image/png",
    "pdf":  "application/pdf",
    "txt":  "text/plain",
    "zip":  "application/zip"
}

file_name = input("Enter file fullname: ").strip().lower()
extension = file_name.rsplit(".", 1)[-1]

if extension in media_types:
    print(media_types[extension])
else:
    print("application/octet-stream")