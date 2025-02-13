import chardet
from langdetect import detect, LangDetectException  # Import langdetect
import pycountry
def detect_encoding_and_language(filepath):
    """Detects encoding and language of a text file."""

    try:
        with open(filepath, "rb") as f:
            rawdata = f.read()

        encoding_result = chardet.detect(rawdata)
        encoding = encoding_result['encoding']
        confidence = encoding_result['confidence']

        if encoding and confidence > 0.5: # Only try to read if encoding detection is reasonably confident
            try:
                with open(filepath, "r", encoding=encoding) as f:
                    text = f.read()
                try:
                    language = detect(text)
                    return encoding, confidence, language
                except LangDetectException:
                    print("Language detection failed (text too short or ambiguous).")
                    return encoding, confidence, None

            except UnicodeDecodeError:
                print(f"Decoding error using detected encoding ({encoding}).")
                return encoding, confidence, None
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
                return encoding, confidence, None
        else:
            print("Encoding detection failed or low confidence.")
            return None, None, None

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None


# Example usage:
filepath = "SampleCurrencyData.txt"  # Replace with your file's path
encoding, confidence, language = detect_encoding_and_language(filepath)

if encoding:
    print(f"Detected encoding: {encoding} (Confidence: {confidence})")
    if language:
        lang_obj=pycountry.languages.get(alpha_2= language)
        
        language_description=f"{lang_obj}"
        
        print(f"Detected language: {language_description}")
        
    else:
        print("Language detection failed.")
else:
    print("Encoding detection failed.")



    
"""
def detect_encoding(filepath):
    Detects the encoding of a text file.
    Args:
        filepath: The path to the text file.
    Returns:
        The encoding name (e.g., 'utf-8', 'latin-1', 'windows-1252') as a string, or None if the encoding 
        could not be reliably detected.  Also returns the confidence level of the detection.
        If an error occurs (like the file not being found), it returns None, None.
"""
"""    
    try:
        with open(filepath, "rb") as f:  # Open in binary mode for chardet
            rawdata = f.read()

        result = chardet.detect(rawdata)
        encoding = result['encoding']
        confidence = result['confidence']

        return encoding, confidence

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None, None
    except Exception as e: # Catch any other potential errors
        print(f"An error occurred: {e}")
        return None, None



# Example usage:
filepath = "SampleCurrencyData.txt"  # Replace with your file's path
encoding, confidence = detect_encoding(filepath)

if encoding:
    print(f"Detected encoding: {encoding} (Confidence: {confidence})")

    # Now you can open the file with the correct encoding:
    try:
        with open(filepath, "r", encoding=encoding) as f:
            contents = f.read()
            # Process the file contents...
            print("File contents (first 100 characters):", contents[:100]) # Print a snippet to show it worked.

    except UnicodeDecodeError:
      print(f"Error: Could not decode file using {encoding}.  The detected encoding might be incorrect.")
    except Exception as e:
      print(f"An error occurred while reading the file: {e}")

else:
    print("Encoding detection failed.")
    
    
#usock = os.filepath

"""    