# Security-hybrid-

# Secure Data Storage System with Hybrid Cryptography

This project demonstrates a secure data storage system that uses a combination of symmetric and asymmetric cryptography to provide strong security against both classical and potential quantum attacks. It employs hybrid encryption, combining the strengths of RSA asymmetric encryption for secure key exchange and AES symmetric encryption for efficient data protection.

## Features

- **Hybrid Cryptography:** Utilizes RSA public-key encryption for secure key exchange and AES symmetric encryption for data confidentiality.
- **Secure Data Storage:** Organizes and securely stores sensitive data within categories and files using a hierarchical structure.
- **Data Integrity:** Implements SHA-256 hashing to ensure the integrity of stored data.
- **Protection Against Quantum Attacks:** While not fully quantum-resistant, the hybrid approach provides a high level of security against potential quantum attacks and classical attacks alike.
- **Encrypted File Storage:** Allows you to save encrypted data to secure binary files, ensuring data security at rest.

## Usage

1. Clone the repository and navigate to the project directory.
2. Run the script and follow the prompts to enter a category name, file name, and data to be stored securely.
3. The data will be encrypted using hybrid cryptography and stored within the designated category.
4. Encrypted data will be saved to a secure binary file.
5. To retrieve the data, provide the category and file name. The system will decrypt the data using the hybrid approach.

## Security Considerations

- **Hybrid Approach:** The project employs a hybrid cryptographic approach, utilizing RSA for secure key exchange and AES for data encryption. While not fully quantum-resistant, this approach provides strong protection against many classical and potential quantum attacks.
- **Review by Experts:** The project has undergone a code audit using Codacy, achieving a grade A for code quality. However, for a comprehensive security assessment, it is recommended to collaborate with experts in the field of cryptography and security.

## Potential Value

- **High-Level Security:** The hybrid approach offers a high level of security without requiring quantum computing. It can be particularly valuable in scenarios where quantum-resistant algorithms are not yet fully developed.
- **Secure Data Storage:** Organizations can use this system to securely store sensitive data, such as passwords, keys, and confidential documents, protecting them against various attack vectors.

## Acknowledgments

This project is a demonstration and should not be considered a fully secure implementation for production use. It serves as a starting point to explore hybrid cryptography and understand its benefits and limitations.

## Collaboration

For those interested in exploring the project further or providing expertise in cryptography and security, please reach out for collaboration and discussions.

---

Feel free to customize the content according to your specific project details, goals, and any other relevant information.
feed back is wanted 

stephen vega helped by chat gpt 3.5
