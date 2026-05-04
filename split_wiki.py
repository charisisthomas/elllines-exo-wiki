import os
import re

content = open("wiki-elllines-exoterikou.md", "r", encoding="utf-8").read()

sections = [
    ("01-forologiki-katoikia.md", "1. Φορολογική Κατοικία & Φορολογικός Εκπρόσωπος", "Φορολογία"),
    ("02-forologikes-diloseis.md", "2. Φορολογικές Δηλώσεις & Τεκμήρια", "Φορολογία"),
    ("03-akinita-airbnb.md", "3. Ακίνητη Περιουσία & Βραχυχρόνια Μίσθωση", "Ακίνητα"),
    ("04-klironomies.md", "4. Κληρονομιές, Δωρεές & Μεταβιβάσεις", "Φορολογία"),
    ("05-kinitira-epanapatrismou.md", "5. Κίνητρα Επαναπατρισμού", "Επενδύσεις"),
    ("06-psifiakes-ypiresies.md", "6. Ψηφιακές Υπηρεσίες από το Εξωτερικό", "Γραφειοκρατία"),
    ("07-amka-asfali.md", "7. ΑΜΚΑ & Κοινωνική Ασφάλιση", "Ασφάλιση"),
    ("08-syntaxi.md", "8. Σύνταξη από Ελλάδα & Εξωτερικό", "Συντάξεις"),
    ("09-agora-akinitou.md", "9. Αγορά Ακινήτου στην Ελλάδα (Μη Κάτοικοι)", "Ακίνητα"),
    ("10-golden-visa.md", "10. Golden Visa", "Επενδύσεις")
]

# Find the start of each section
pattern = r"## \d+\. .*?(?=\n## \d+\. |\n## 11\. )"
matches = list(re.finditer(pattern, content, re.DOTALL))

os.makedirs("src/content/wiki", exist_ok=True)
os.makedirs("src/content/wiki-en", exist_ok=True)

for i, match in enumerate(matches):
    if i >= 10: break
    
    filename, title, category = sections[i]
    section_content = match.group(0).strip()
    
    # Strip the "## X. Title" from the content itself since we'll render it via frontmatter
    # or keep it as h1? Actually Astro will use frontmatter title. Let's keep it but change ## to #
    # Or just remove the first line
    lines = section_content.split("\n")
    if lines[0].startswith("## "):
        lines = lines[1:]
    section_content = "\n".join(lines).strip()
    
    # Construct frontmatter
    frontmatter = f"""---
title: "{title[title.find('.')+2:]}"
description: "Οδηγός και πληροφορίες για: {title[title.find('.')+2:]}."
category: "{category}"
lastUpdated: "2026-05-01"
lang: "el"
---

{section_content}
"""
    
    with open(f"src/content/wiki/{filename}", "w", encoding="utf-8") as f:
        f.write(frontmatter)
        
    en_frontmatter = f"""---
title: "{title[title.find('.')+2:]} (English)"
description: "Guide and information for: {title[title.find('.')+2:]}."
category: "{category}"
lastUpdated: "2026-05-01"
lang: "en"
---

> 🇬🇧 **English translation coming soon.** View the Greek version for now.

{section_content}
"""
    with open(f"src/content/wiki-en/{filename}", "w", encoding="utf-8") as f:
        f.write(en_frontmatter)

print("Created 10 Greek and 10 English markdown files.")
