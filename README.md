# Hidden File Detector

Hidden File Detector is a Python tool designed to search for hidden files within a specified directory. It calculates file hashes and identifies file types using MIME type detection. The tool utilizes concurrent processing for efficiency and provides error handling to manage any exceptions during the process.

## Usage

1. Clone the repository to your local machine:</br>
```
git clone https://github.com/1cYinfinity/hidden-file-detector.git
```

3. Navigate to the project directory:</br>
  ```
cd hidden-file-detector
```

5. Install the required dependencies:</br>
  ```
pip install -r requirements.txt
```

7. Run the tool by executing the main.py script:</br>
  ```
python main.py
```

9. Follow the on-screen prompts to enter the path of the directory you want to search for hidden files.

10. Once the search is complete, the tool will display the hidden files found along with their file types.

## Example

Suppose you want to search for hidden files within the directory `~/Documents` , here's how you can use the tool:</br>
```
python main.py
Enter the path of the directory to search for hidden files: ~/Documents
Searching for hidden files...
Hidden files found:
File: ~/Documents/hidden_file.txt, Type: text/plain
File: ~/Documents/hidden_image.jpg, Type: image/jpeg
```

## Dependencies

* Python 3.x
* imghdr
* python-magic

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
