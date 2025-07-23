#!/usr/bin/env python3
"""
Script to fix Mermaid charts in Markdown files to be dark mode friendly.
Adds dark theme configuration to all Mermaid code blocks.
"""

import os
import re
import glob

# Dark mode theme configuration
DARK_THEME_CONFIG = """%%{init: {'theme':'dark', 'themeVariables': {'primaryColor':'#4f46e5','primaryTextColor':'#ffffff','primaryBorderColor':'#6366f1','lineColor':'#6b7280','secondaryColor':'#10b981','tertiaryColor':'#f59e0b','background':'#1f2937','mainBkg':'#374151','secondBkg':'#4b5563','tertiaryBkg':'#6b7280'}}}%%"""

def fix_mermaid_charts_in_file(file_path):
    """Fix all Mermaid charts in a single markdown file."""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match mermaid code blocks
        # This will match ```mermaid followed by content until ```
        pattern = r'```mermaid\n(.*?)```'
        
        def replace_mermaid_block(match):
            mermaid_content = match.group(1)
            
            # Check if already has theme configuration
            if '%%{init:' in mermaid_content or 'theme' in mermaid_content:
                print(f"  - Skipping chart (already has theme configuration)")
                return match.group(0)  # Return unchanged
            
            # Add dark theme configuration at the beginning
            new_content = f"```mermaid\n{DARK_THEME_CONFIG}\n{mermaid_content}```"
            print(f"  - Fixed Mermaid chart")
            return new_content
        
        # Replace all mermaid blocks
        new_content = re.sub(pattern, replace_mermaid_block, content, flags=re.DOTALL)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✅ Updated {file_path}")
            return True
        else:
            print(f"  ⏭️  No changes needed in {file_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all markdown files."""
    print("🔍 Fixing Mermaid charts for dark mode compatibility...")
    print("=" * 60)
    
    # Find all markdown files in the repository
    md_files = glob.glob("src/Python_Programs/*.md", recursive=True)
    
    if not md_files:
        print("No markdown files found.")
        return
    
    print(f"Found {len(md_files)} markdown files")
    print("-" * 40)
    
    updated_files = 0
    total_files = len(md_files)
    
    for md_file in md_files:
        if fix_mermaid_charts_in_file(md_file):
            updated_files += 1
        print()
    
    print("=" * 60)
    print(f"🎉 Processing complete!")
    print(f"📊 Summary:")
    print(f"   - Total files processed: {total_files}")
    print(f"   - Files updated: {updated_files}")
    print(f"   - Files unchanged: {total_files - updated_files}")
    
    if updated_files > 0:
        print("\n💡 What was changed:")
        print("   - Added dark theme configuration to Mermaid charts")
        print("   - Charts will now be readable in both light and dark modes")
        print("   - Compatible with VS Code, GitHub, and other platforms")
        
        print("\n🔄 Next steps:")
        print("   - Review the changes in your files")
        print("   - Commit and push to repository if satisfied")
        print("   - Test the charts in VS Code and GitHub dark mode")

if __name__ == "__main__":
    main()
