import os
from cryptography.fernet import Fernet
import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt and decrypt data using a given key
def encrypt_data(key, data):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_data(key, encrypted_data):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

# Generate a random RSA private key
def rsa_generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

# Encrypt data using RSA public key and AES symmetric key
def hybrid_encrypt(public_key, symmetric_key, data):
    symmetric_encrypted_data = encrypt_data(symmetric_key, data)
    encrypted_symmetric_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return encrypted_symmetric_key + symmetric_encrypted_data

# Decrypt data using RSA private key and AES symmetric key
def hybrid_decrypt(private_key, encrypted_data):
    encrypted_symmetric_key = encrypted_data[:private_key.public_key().key_size // 8]
    symmetric_encrypted_data = encrypted_data[private_key.public_key().key_size // 8:]
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return decrypt_data(symmetric_key, symmetric_encrypted_data)

# Simulate creating a hierarchical storage structure
class SecureStorage:
    def __init__(self, public_key, private_key, encryption_key):
        self.public_key = public_key
        self.private_key = private_key
        self.encryption_key = encryption_key
        self.categories = {}

    def create_category(self, category_name):
        self.categories[category_name] = {}

    def add_file(self, category_name, file_name, data):
        encrypted_data = hybrid_encrypt(self.public_key, self.encryption_key, data)
        self.categories[category_name][file_name] = encrypted_data

    def get_file(self, category_name, file_name):
        encrypted_data = self.categories[category_name][file_name]
        decrypted_data = hybrid_decrypt(self.private_key, encrypted_data)
        return decrypted_data

    def hash_data(self, data):
        sha256 = hashlib.sha256()
        sha256.update(data)
        return sha256.hexdigest()

# Example usage
if __name__ == "__main__":
    private_key = rsa_generate_private_key()
    public_key = private_key.public_key()
    
    master_key = generate_key()
    storage = SecureStorage(public_key, private_key, master_key)

    storage.create_category("Passwords")
    
    category_name = input("Enter a category name: ")
    file_name = input("Enter a file name: ")
    data = input("Enter the data to be stored: ").encode()

    encrypted_data = hybrid_encrypt(public_key, master_key, data)
    storage.add_file(category_name, file_name, encrypted_data)
    
    # Save the encrypted data to a secure file
    secure_file_path = f"{category_name}_{file_name}_encrypted.bin"
    with open(secure_file_path, "wb") as f:
        f.write(encrypted_data)
    print("Encrypted data saved to secure file:", secure_file_path)
    
    # Retrieve the encrypted data from the secure file and decrypt it
    with open(secure_file_path, "rb") as f:
        retrieved_encrypted_data = f.read()
        decrypted_data = storage.get_file(category_name, file_name)
        print("Decrypted Data:", decrypted_data)
