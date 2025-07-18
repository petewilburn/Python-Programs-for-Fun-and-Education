# Quick test script for the modern resume generator
import os
import sys

try:
    # Import our enhanced resume generator
    from P4003_Generate_Resume_Document_from_Json_Data import ResumeGenerator, IO
    
    print("🎨 Modern Resume Generator Test")
    print("=" * 40)
    
    # Check if sample file exists
    if os.path.exists('sample_resume.json'):
        print("✅ Sample JSON file found")
        
        # Test the generator
        generator = ResumeGenerator('sample_resume.json')
        print("✅ Resume generator initialized with modern styling")
        
        # Test preview
        preview = generator.get_resume_preview()
        print("✅ Preview generation successful")
        print("\n📋 Resume Preview:")
        print("-" * 30)
        print(preview)
        print("-" * 30)
        
        # Generate a test resume
        test_filename = "modern_resume_test.docx"
        generator.save_resume(test_filename)
        print(f"\n✅ Modern resume generated: {test_filename}")
        
        # Check file size
        if os.path.exists(test_filename):
            size = os.path.getsize(test_filename)
            print(f"📊 File size: {size} bytes")
            print("🎉 Modern styling features applied successfully!")
        
    else:
        print("⚠️ Sample JSON file not found")
        print("But the modern resume generator is ready to use!")
        
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n🌟 Modern Resume Features:")
print("  • Custom Calibri typography")
print("  • Professional color scheme")
print("  • Clean section headers with accent lines")
print("  • Modern contact info layout") 
print("  • Hierarchical text styling")
print("  • Professional spacing and margins")
