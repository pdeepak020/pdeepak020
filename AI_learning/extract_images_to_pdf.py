import fitz  # PyMuPDF
import img2pdf
import os
import sys

def extract_images_and_convert_to_pdf(input_pdf_path, output_pdf_path):
    print(f"Opening PDF: {input_pdf_path}")
    doc = fitz.open(input_pdf_path)
    images = []
    
    # Create a temporary directory for extracted images
    temp_dir = "temp_images"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    try:
        image_count = 0
        for page_index in range(len(doc)):
            page = doc[page_index]
            image_list = page.get_images(full=True)
            
            if not image_list:
                print(f"No images found on page {page_index + 1}")
                continue
                
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                image_filename = os.path.join(temp_dir, f"page{page_index+1}_img{img_index+1}.{image_ext}")
                with open(image_filename, "wb") as f:
                    f.write(image_bytes)
                
                images.append(image_filename)
                image_count += 1
                print(f"Extracted image {image_count}: {image_filename}")
        
        if not images:
            print("No images found in the PDF.")
            return

        print(f"Converting {len(images)} images to {output_pdf_path}...")
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(images))
        
        print(f"Success! Output saved to {output_pdf_path}")
        
    finally:
        # Clean up temporary images
        for img_path in images:
            try:
                os.remove(img_path)
            except Exception as e:
                print(f"Error removing {img_path}: {e}")
        try:
            os.rmdir(temp_dir)
        except Exception as e:
            print(f"Error removing temp directory: {e}")

if __name__ == "__main__":
    input_pdf = r"a:\python\fileconverter\uploads\PHOTO-2026-01-31-09-47-35 2.pdf"
    output_pdf = r"a:\python\fileconverter\uploads\PHOTO-2026-01-31-09-47-35 2_images_only.pdf"
    
    if not os.path.exists(input_pdf):
        print(f"Input file not found: {input_pdf}")
        sys.exit(1)
        
    extract_images_and_convert_to_pdf(input_pdf, output_pdf)
