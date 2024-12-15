import os
import sys
import argparse
from pathlib import Path
from typing import List, Optional
import PyPDF2
from PIL import Image
import logging

class FileStacker:
    def __init__(self):
        self.supported_types = {
            'text': ['.txt', '.log', '.md'],
            'pdf': ['.pdf'],
            'image': ['.jpg', '.jpeg', '.png']
        }
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def validate_files(self, files: List[str], file_type: Optional[str] = None) -> bool:
        """Validate if all files exist and are of the same type."""
        if not files:
            self.logger.error("No files provided")
            return False

        # Get the type from the first file if not specified
        if not file_type:
            ext = Path(files[0]).suffix.lower()
            file_type = next(
                (k for k, v in self.supported_types.items() if ext in v),
                None
            )

        if not file_type:
            self.logger.error(f"Unsupported file type: {ext}")
            return False

        # Validate all files
        for file in files:
            path = Path(file)
            if not path.exists():
                self.logger.error(f"File not found: {file}")
                return False
            if path.suffix.lower() not in self.supported_types[file_type]:
                self.logger.error(f"Mixed file types not supported: {file}")
                return False

        return True

    def merge_text_files(self, input_files: List[str], output_file: str):
        """Merge multiple text files into one."""
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for file in input_files:
                    self.logger.info(f"Processing {file}")
                    with open(file, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n{'='*50}\n")
                        outfile.write(f"Content from: {file}\n")
                        outfile.write(f"{'='*50}\n\n")
                        outfile.write(infile.read())
                        outfile.write('\n')
            self.logger.info(f"Successfully created {output_file}")
        except Exception as e:
            self.logger.error(f"Error merging text files: {str(e)}")
            raise

    def merge_pdf_files(self, input_files: List[str], output_file: str):
        """Merge multiple PDF files into one."""
        try:
            merger = PyPDF2.PdfMerger()
            for file in input_files:
                self.logger.info(f"Processing {file}")
                merger.append(file)
            
            merger.write(output_file)
            merger.close()
            self.logger.info(f"Successfully created {output_file}")
        except Exception as e:
            self.logger.error(f"Error merging PDF files: {str(e)}")
            raise

    def merge_image_files(self, input_files: List[str], output_file: str):
        """Merge multiple images vertically into one PDF."""
        try:
            images = []
            for file in input_files:
                self.logger.info(f"Processing {file}")
                img = Image.open(file)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                images.append(img)

            # Save all images as pages in a PDF
            if images:
                images[0].save(
                    output_file,
                    save_all=True,
                    append_images=images[1:],
                    format='PDF'
                )
                self.logger.info(f"Successfully created {output_file}")
        except Exception as e:
            self.logger.error(f"Error merging image files: {str(e)}")
            raise

    def merge_files(self, input_files: List[str], output_file: str):
        """Main method to merge files based on their type."""
        try:
            # Determine file type from first file
            file_type = None
            ext = Path(input_files[0]).suffix.lower()
            for type_key, extensions in self.supported_types.items():
                if ext in extensions:
                    file_type = type_key
                    break

            if not self.validate_files(input_files, file_type):
                return

            # Create output directory if it doesn't exist
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Merge based on file type
            if file_type == 'text':
                self.merge_text_files(input_files, output_file)
            elif file_type == 'pdf':
                self.merge_pdf_files(input_files, output_file)
            elif file_type == 'image':
                self.merge_image_files(input_files, output_file)

        except Exception as e:
            self.logger.error(f"Error during file merging: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(
        description='File Stacker - Merge multiple files into one'
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='Input files to merge (must be of same type)'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output file path'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    # Set logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.getLogger().setLevel(log_level)

    try:
        stacker = FileStacker()
        stacker.merge_files(args.files, args.output)
    except Exception as e:
        logging.error(f"Failed to merge files: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()