import hashlib

def hash_file(file_one, file_two):

    hash_one = hashlib.sha1()
    hash_two = hashlib.sha1()

    with open(file_one, 'rb') as file:
        chunk = b''
        while True:
            chunk = file.read(1024)
            if chunk == b'':
                break
            hash_one.update(chunk)

    with open(file_two, 'rb') as file:
        chunk = b''
        while True:
            chunk = file.read(1024)
            if chunk == b'':
                break
            hash_two.update(chunk)

    return hash_one.hexdigest(), hash_two.hexdigest()

msg_one, msg_two = hash_file("tutorial.pdf", "tutorial.pdf")
if msg_one != msg_two:
    print("These files are not identical")
else:
    print("These files are identical")

if __name__ == "__main__":
    pass