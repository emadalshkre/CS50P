text = input("File Name: ")
if ".gif" in text:
    print("image/gif")
elif ".jpeg" in text or ".jpg" in text:
    print("image/jpeg")
elif ".png" in text:
    print("image/png")
elif ".pdf" in text:
    print("application/pdf")
elif ".txt" in text:
    print("text/plain")
elif ".zip" in text:
    print("application/zip")
else:
    print("application/octet-stream")