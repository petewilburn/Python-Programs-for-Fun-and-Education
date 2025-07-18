# A Python program to create a new .json file with a title and content.

# Minimum Python version: 3.9

# ---------------------------------------------------------------------------------------------
# File: P4002_Create_Json_File.py
# Description: A Python program to create a new JSON file with a specified title and content.
# Author: Pete W.
# License: MIT License
# Copyright (c) 2025 Pete W.
# ---------------------------------------------------------------------------------------------

import json
import os
import re
from typing import Any, Dict, Union

class Json:
    def __init__(self, title: str, content: Dict[str, Any]):
        """Initialize JSON creator with title and content validation."""
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        self.title = title.strip()
        self.content = content

    def save_to_file(self, file_path: str) -> None:
        """Save JSON data to file with error handling."""
        try:
            # Ensure directory exists
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            
            # Create the JSON structure
            json_data = {
                "title": self.title,
                "content": self.content,
                "metadata": {
                    "created_by": "JSON File Creator Program",
                    "version": "1.0"
                }
            }
            
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, indent=4, ensure_ascii=False)
                
        except PermissionError:
            raise PermissionError(f"Permission denied: Cannot save to '{file_path}'")
        except Exception as e:
            raise RuntimeError(f"Failed to save JSON file: {e}")

    def preview_json(self) -> str:
        """Return a formatted preview of the JSON content."""
        preview_data = {
            "title": self.title,
            "content": self.content,
            "metadata": {
                "created_by": "JSON File Creator Program",
                "version": "1.0"
            }
        }
        return json.dumps(preview_data, indent=2, ensure_ascii=False)

class IO:
    @staticmethod
    def print_welcome_message() -> None:
        """Prints a welcome message to the user."""
        print("\nWelcome to the JSON File Creator Program!")
        print("This program will create a new JSON file with your specified title and content.")
        print("You can enter content as JSON or use our simple key-value mode.")
        print("\nLet's get started!\n")

    @staticmethod
    def prompt_for_title() -> str:
        """Prompts the user for a title with retry logic."""
        count = 0
        while count < 3:
            count += 1
            title = input("Please enter the title for your JSON file: ").strip()
            if title:
                return title
            else:
                print("❌ Title cannot be empty. Please try again.")
        raise ValueError("Too many invalid attempts. Exiting the program.")

    @staticmethod
    def prompt_for_content_mode() -> str:
        """Ask user to choose content input mode."""
        print("\nChoose content input mode:")
        print("1. Simple mode (key-value pairs)")
        print("2. Advanced mode (raw JSON)")
        
        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                return choice
            print("❌ Please enter 1 or 2.")

    @staticmethod
    def prompt_for_simple_content() -> Dict[str, Any]:
        """Prompts user for content using simple key-value input."""
        print("\nSimple mode: Enter each key-value pair as 'key -> value' followed by enter. Type 'done' when finished.")
        print("Example: name -> John Doe")
            
        content = {}
        while True:
            key_value = input("Enter key-value (or 'done'): ").strip()
            
            if key_value.lower() == 'done':
                break
                
            if '->' in key_value:
                try:
                    key, value = key_value.split('->', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Try to parse value as number or boolean
                    if value.lower() in ['true', 'false']:
                        value = value.lower() == 'true'
                    elif value.isdigit():
                        value = int(value)
                    elif value.replace('.', '').isdigit():
                        value = float(value)
                    
                    content[key] = value
                    print(f"✅ Added: {key} = {value}")
                except ValueError:
                    print("❌ Invalid format. Use: key -> value")
            else:
                print("❌ Invalid format. Use: key -> value (or 'done' to finish)")
        
        return content

    @staticmethod
    def prompt_for_advanced_content() -> Dict[str, Any]:
        """Prompts the user for content in JSON format with retry logic."""
        count = 0
        print("\nAdvanced mode: Enter valid JSON object")
        print("Example: {\"name\": \"John\", \"age\": 30, \"active\": true}")
        
        while count < 3:
            count += 1
            content_str = input("Enter JSON content: ").strip()
            
            if not content_str:
                content_str = "{}"  # Default to empty object
            
            try:
                content = json.loads(content_str)
                if not isinstance(content, dict):
                    print("❌ Content must be a JSON object (use curly braces {}).")
                    continue
                return content
            except json.JSONDecodeError as e:
                print(f"❌ Invalid JSON format: {e}")
                print("Please check your syntax and try again.")
        
        raise ValueError("Too many invalid attempts with JSON format.")
        
    @staticmethod
    def prompt_for_file_path() -> str:
        """Prompts the user for the file path with validation."""
        count = 0
        while count < 3:
            count += 1
            file_path = input("Enter file path to save JSON (e.g., 'data/output.json'): ").strip()
            
            if not file_path:
                print("❌ File path cannot be empty.")
                continue
            
            # Add .json extension if missing
            if not file_path.lower().endswith('.json'):
                file_path += '.json'
            
            # Validate filename characters (cross-platform safe)
            filename = os.path.basename(file_path)
            invalid_chars = r'[<>:"/\\|?*]'
            if re.search(invalid_chars, filename):
                print("❌ Invalid characters in filename. Avoid: < > : \" / \\ | ? *")
                continue
                
            return file_path
        
        raise ValueError("Too many invalid attempts with file path.")
    
    @staticmethod
    def print_preview(json_creator) -> None:
        """Show a preview of the JSON content."""
        print("\n📋 Preview of your JSON file:")
        print("=" * 40)
        print(json_creator.preview_json())
        print("=" * 40)
        
        confirm = input("\nDoes this look correct? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            raise ValueError("User cancelled - JSON content not confirmed.")
    
    @staticmethod
    def print_success_message(file_path: str) -> None:
        """Prints a success message after saving the JSON file."""
        abs_path = os.path.abspath(file_path)
        print(f"\n✅ Success! JSON file created successfully:")
        print(f"   📄 {file_path}")
        print(f"   📁 Full path: {abs_path}")

    @staticmethod
    def print_thank_you_message() -> None:
        """Prints a thank you message to the user."""
        print("\nThank you for using the JSON File Creator Program!")
        print("We hope you found it useful.")
        print("\nGoodbye!\n")

def main():
    """Main function to run the program."""
    IO.print_welcome_message()
    
    try:
        # Get title
        title = IO.prompt_for_title()
        
        # Choose content input mode
        mode = IO.prompt_for_content_mode()
        
        # Get content based on chosen mode
        if mode == '1':
            content = IO.prompt_for_simple_content()
        else:
            content = IO.prompt_for_advanced_content()
        
        # Get file path
        file_path = IO.prompt_for_file_path()
        
        # Create JSON object and show preview
        json_creator = Json(title, content)
        IO.print_preview(json_creator)
        
        # Save file
        json_creator.save_to_file(file_path)
        IO.print_success_message(file_path)
        
    except ValueError as e:
        print(f"❌ Input Error: {e}")
    except (PermissionError, RuntimeError) as e:
        print(f"❌ File Error: {e}")
    except KeyboardInterrupt:
        print("\n❌ Program interrupted by user.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    finally:
        IO.print_thank_you_message()

if __name__ == "__main__":
    main()

# This program creates a new JSON file with a specified title and content.
# It offers two input modes: simple key-value pairs or advanced JSON syntax.
# 
# Features:
# - Dual input modes: Simple (key->value) and Advanced (raw JSON)
# - Robust input validation with retry logic
# - Cross-platform filename validation
# - JSON preview before saving
# - Automatic directory creation
# - Enhanced error handling and user feedback
# - UTF-8 encoding support for international characters
# 
# The program demonstrates:
# - JSON handling and validation
# - User experience design with multiple input options
# - File system operations with error handling
# - Clean object-oriented architecture