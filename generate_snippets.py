#!/usr/bin/env python3

import os
import json
import sys
import fnmatch
from pathlib import Path

def escape_json_string(s):
    """
    Escape a string for JSON format, handling backslashes and quotes
    """
    s = s.replace("\\", "\\\\")  # Escape backslashes first
    s = s.replace('"', '\"')   # Escape quotes
    return s

def parse_template_file(file_path):
    """
    Parse a template file and extract name, shortcut, description, and code
    Returns a tuple: (name, shortcut, description, code_lines)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if len(lines) < 4:
            print(f"Warning: {file_path} has fewer than 4 lines, skipping...")
            return None
        
        # Extract the first 3 lines for name, shortcut, description
        name = lines[0].strip()
        shortcut = lines[1].strip()
        description = lines[2].strip()
        
        # Everything from line 4 onwards is code
        # Preserve indentation by only removing line endings, not leading whitespace
        code_lines = [line.rstrip('\n\r') for line in lines[3:]]
        
        return (name, shortcut, description, code_lines)
    
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def process_code_lines(code_lines):
    """
    Process code lines to escape them for JSON format
    """
    processed_lines = []
    for line in code_lines:
        escaped_line = escape_json_string(line)
        processed_lines.append(escaped_line)
    
    return processed_lines

def load_ignore_patterns(directory):
    """
    Load ignore patterns from ignore.md file (gitignore style)
    """
    ignore_file = Path(directory) / 'ignore.md'
    ignore_patterns = set()
    
    # Default ignore patterns (in case ignore.md doesn't exist)
    default_ignores = {
        'format.md', 'ignore.md', 'generate_snippets.py', 'cpp.json',
        '*.py', '*.json', '*.cpp', '*.exe', '*.o', '.git*', '*.tmp', '*.bak'
    }
    
    if ignore_file.exists():
        try:
            with open(ignore_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    ignore_patterns.add(line)
                        
        except Exception as e:
            print(f"Warning: Could not read ignore.md: {e}")
            ignore_patterns.update(default_ignores)
    else:
        ignore_patterns.update(default_ignores)
    
    return ignore_patterns

def should_ignore_file(file_path, ignore_patterns):
    """
    Check if a file should be ignored based on ignore patterns
    """
    filename = file_path.name
    
    # Check exact filename matches
    if filename in ignore_patterns:
        return True
    
    # Check pattern matches
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    
    return False

def find_template_files(directory):
    """
    Recursively find all potential template files in the directory and subdirectories
    Uses ignore.md to exclude files
    """
    ignore_patterns = load_ignore_patterns(directory)
    template_files = []
    
    # Use rglob to recursively search all subdirectories
    for file_path in Path(directory).rglob('*'):
        if file_path.is_file():
            # Check if file should be ignored
            if should_ignore_file(file_path, ignore_patterns):
                continue
            
            # Include .md files and other text-like files
            if file_path.suffix.lower() in ['.md', '.txt'] or file_path.suffix == '':
                template_files.append(file_path)
    
    return template_files

def generate_cpp_json(template_directory, output_path='cpp.json'):
    """
    Main function to generate cpp.json from template files
    """
    template_files = find_template_files(template_directory)
    base_path = Path(template_directory)
    
    if not template_files:
        print("No template files found!")
        return
    
    # Sort files by directory for better organization in logs
    template_files.sort(key=lambda x: (x.parent, x.name))
    
    snippets = {}
    name_conflicts = {}  # Track which files use the same name
    shortcut_conflicts = {}  # Track which files use the same shortcut
    current_directory = None
    
    for file_path in template_files:
        # Show relative path for better readability
        relative_path = file_path.relative_to(base_path)
        file_directory = relative_path.parent
        
        # Print delimiter when entering a new directory
        if current_directory != file_directory:
            current_directory = file_directory
            if str(file_directory) != '.':
                print(f"\n📁 Processing folder: {file_directory}")
                print("=" * (len(str(file_directory)) + 20))
            else:
                print(f"\n📁 Processing root folder:")
                print("=" * 25)
        
        print(f"Processing: {relative_path}")
        
        parsed_data = parse_template_file(file_path)
        if parsed_data is None:
            continue
        
        name, shortcut, description, code_lines = parsed_data
        
        # Check for name conflicts
        if name in snippets:
            print(f"  ⚠️  WARNING: Name conflict detected!")
            print(f"      Name '{name}' already exists (previous file: {name_conflicts.get(name, 'unknown')})")
            print(f"      Current file: {relative_path}")
            print(f"      The previous snippet will be overwritten!")
        
        # Check for shortcut conflicts
        existing_shortcut = None
        for existing_name, existing_snippet in snippets.items():
            if existing_snippet['prefix'] == shortcut:
                existing_shortcut = existing_name
                break
        
        if existing_shortcut:
            print(f"  ⚠️  WARNING: Shortcut conflict detected!")
            print(f"      Shortcut '{shortcut}' already used by snippet '{existing_shortcut}' (file: {shortcut_conflicts.get(shortcut, 'unknown')})")
            print(f"      Current file: {relative_path}")
            print(f"      Both snippets will have the same trigger, which may cause confusion!")
        
        # Process code lines
        processed_code = process_code_lines(code_lines)
        
        # Create snippet entry
        snippet_entry = {
            "prefix": shortcut,
            "body": processed_code,
            "description": description
        }
        
        snippets[name] = snippet_entry
        name_conflicts[name] = str(relative_path)
        shortcut_conflicts[shortcut] = str(relative_path)
        
        print(f"  ✓ Added snippet: {name} (trigger: {shortcut})")
    
    # Final conflict summary
    duplicate_names = {name: files for name, files in name_conflicts.items() 
                      if list(name_conflicts.values()).count(files) > 1}
    duplicate_shortcuts = {}
    
    # Count shortcut duplicates
    shortcut_counts = {}
    for shortcut in shortcut_conflicts.keys():
        count = sum(1 for snippet in snippets.values() if snippet['prefix'] == shortcut)
        if count > 1:
            duplicate_shortcuts[shortcut] = count
    
    if duplicate_names or duplicate_shortcuts:
        print(f"\n🚨 CONFLICT SUMMARY:")
        if duplicate_shortcuts:
            print(f"   Duplicate shortcuts detected:")
            for shortcut, count in duplicate_shortcuts.items():
                print(f"     - '{shortcut}' used by {count} snippets")
        print(f"   Please review and fix conflicts before using the snippets!")
    
    # Write to cpp.json
    try:
        print(f"\n📝 Writing snippets to file...")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(snippets, f, indent=2, ensure_ascii=False)
        
        # Get file size for additional info
        file_size = os.path.getsize(output_path)
        file_size_kb = file_size / 1024
        
        print(f"✅ SUCCESS: Snippets file written successfully!")
        print(f"   📄 File: {output_path}")
        print(f"   📊 Size: {file_size_kb:.1f} KB ({file_size} bytes)")
        print(f"   🎯 Total snippets: {len(snippets)}")
        
        # Check if it's VS Code directory
        if '.config/Code/User/snippets' in str(output_path):
            print(f"   🔧 VS Code snippets updated! Restart VS Code to see changes.")
        
        # Show a preview of the generated JSON
        print(f"\n📋 Preview of generated snippets:")
        for name, snippet in snippets.items():
            print(f"  - {name}: '{snippet['prefix']}' -> {len(snippet['body'])} lines")
    
    except Exception as e:
        print(f"❌ ERROR: Failed to write to {output_path}")
        print(f"   💥 Error details: {e}")
        print(f"   💡 Check file permissions and directory existence")

def get_vscode_snippets_path():
    """
    Get the VS Code User snippets directory path
    """
    home = Path.home()
    vscode_snippets_path = home / '.config' / 'Code' / 'User' / 'snippets' / 'cpp.json'
    return vscode_snippets_path

def main():
    """
    Main entry point
    """
    # Get the directory to process
    if len(sys.argv) > 1:
        template_directory = sys.argv[1]
    else:
        template_directory = '.'
    
    # Determine output file path
    if len(sys.argv) > 2:
        # If custom output file is specified, use it
        output_file = sys.argv[2]
        output_path = os.path.join(template_directory, output_file)
    else:
        # Default: use VS Code User snippets directory
        output_path = get_vscode_snippets_path()
        output_file = 'VS Code cpp.json'
    
    if not os.path.isdir(template_directory):
        print(f"Error: {template_directory} is not a valid directory")
        sys.exit(1)
    
    print(f"Generating C++ snippets from templates in: {template_directory}")
    print(f"Output file: {output_path}")
    print("-" * 50)
    
    # Create VS Code snippets directory if it doesn't exist
    if len(sys.argv) <= 2:  # Using default VS Code path
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    generate_cpp_json(template_directory, str(output_path))

if __name__ == "__main__":
    main()
