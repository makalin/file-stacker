# File Stacker 📚

A powerful command-line tool for merging multiple files (text, PDFs, or images) into a single file. Perfect for combining logs, creating documentation, or assembling photo albums.

## ✨ Features

- Merge multiple files of the same type into a single output file
- Support for various file formats:
  - Text files (.txt, .log, .md)
  - PDF documents (.pdf)
  - Images (.jpg, .jpeg, .png)
- Preserves original content and formatting
- Robust error handling and validation
- Detailed logging with verbose mode option
- Cross-platform support (Windows, macOS, Linux)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-stacker.git
cd file-stacker
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Command Structure
```bash
python fstack.py [input_files...] -o output_file [-v]
```

### Arguments
- `input_files`: One or more files to merge (must be of the same type)
- `-o, --output`: Path for the output file
- `-v, --verbose`: Enable verbose logging (optional)

### Examples

1. Merge multiple PDF files:
```bash
python fstack.py document1.pdf document2.pdf document3.pdf -o merged.pdf
```

2. Combine text files:
```bash
python fstack.py log1.txt log2.txt log3.txt -o combined.txt
```

3. Create a PDF from multiple images:
```bash
python fstack.py image1.jpg image2.png image3.jpg -o photo_album.pdf
```

4. Enable verbose logging:
```bash
python fstack.py -v file1.pdf file2.pdf -o output.pdf
```

## 📋 Requirements

- Python 3.7 or higher
- PyPDF2
- Pillow (Python Imaging Library)

## 🛠️ Technical Details

### Supported File Types

| Type | Extensions | Output Format |
|------|------------|---------------|
| Text | .txt, .log, .md | Single text file with separators |
| PDF | .pdf | Merged PDF document |
| Images | .jpg, .jpeg, .png | Multi-page PDF document |

### File Processing

- **Text Files**: Merged with clear separators and file source indicators
- **PDFs**: Combined while maintaining original formatting and properties
- **Images**: Converted and combined into a single PDF document

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Add support for additional file formats (e.g., .docx, .epub)
- [ ] Implement drag-and-drop GUI interface
- [ ] Add file compression options
- [ ] Enable custom ordering of pages/content
- [ ] Add batch processing capabilities

## ⚠️ Known Issues

- Large image files might require significant memory
- Some PDF files with complex formatting may need additional processing
- Unicode text files must be properly encoded

## 🙏 Acknowledgments

- PyPDF2 team for the PDF processing capabilities
- Pillow team for image processing functionality
- All contributors and users of File Stacker
