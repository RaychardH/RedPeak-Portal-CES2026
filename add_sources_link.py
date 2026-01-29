#!/usr/bin/env python3
import re
import os

# Research Sources link HTML
sources_link = '''                        <div class="border-t border-white/10 my-2"></div>
                        <a href="sources-portal.html" class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors hover:bg-white/5" style="color: var(--text-secondary);">
                            <i data-lucide="database" class="w-4 h-4"></i>
                            <span>Research Sources</span>
                        </a>'''

files_to_update = [
    'keynotes.html', 'electronics.html', 'odm.html', 'innovation-awards.html',
    'sustainability.html', 'automobile.html', 'healthcare.html',
    'robotics.html', 'redpeak-pov.html'
]

os.chdir('/Users/raychard/Documents/RedPeak-Portal-CES2026/public')

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"Skipping {filename} - file not found")
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Research Sources already exists
    if 'Research Sources' in content:
        print(f"Skipping {filename} - already has Research Sources")
        continue

    # Find the Insights dropdown menu closing tag
    # Look for the pattern of menu items followed by closing </div>
    pattern = r'(<span>Insights</span>.*?<div class="absolute.*?>)(.*?)(</div>\s*</div>\s*</div>)'

    def add_sources(match):
        return match.group(1) + match.group(2) + '\n' + sources_link + '\n                    ' + match.group(3)

    new_content = re.sub(pattern, add_sources, content, flags=re.DOTALL)

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ Updated {filename}")
    else:
        print(f"✗ Could not update {filename}")

print("\nDone!")
