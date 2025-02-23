# File Organizer

## Overview
The File Organizer is a Python script designed to help you organize files in a specified directory. It sorts files into folders based on their file types, making it easier to manage and locate your files.

## Features
- Automatically organizes files into folders by type
- Supports a wide range of file types
- Easy to configure and use

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd file-organizer
    ```

## Usage
1. Open a terminal and navigate to the project directory.
2. Run the script with the directory you want to organize:
    ```bash
    python main-file-org.py
    ```

## Configuration
You can customize the file types and their corresponding folders by editing the `config.json` file in the project directory.

## Example
Before running the script:
```
/path/to/your/directory
├── document1.pdf
├── image1.jpg
├── song1.mp3
```

After running the script:
```
/path/to/your/directory
├── Documents
│   └── document1.pdf
├── Images
│   └── image1.jpg
├── Music
│   └── song1.mp3
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.