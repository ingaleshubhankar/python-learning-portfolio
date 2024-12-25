import base64
message="Hello, World!"
encoded=base64.b64encode(message.encode())
decoded=base64.b64decode(encoded).decode()

print(f"Encoded:{encoded}, Decoded:{decoded}")


