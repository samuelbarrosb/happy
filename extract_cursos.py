import re

with open("e:/Clientes/Happy/happy/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Encontrar a secao "Escolha o caminho do seu filho"
# Ela comeca com algo como <section ...> e tem <h2 class="section-title fade-in">Escolha o caminho do seu filho</h2>
start_idx = content.find('<h2 class="section-title fade-in">Escolha o caminho do seu filho</h2>')
# back up to the <section> tag
start_section = content.rfind('<section', 0, start_idx)
# find the end of this section
end_section = content.find('</section>', start_section) + 10

cursos_html = content[start_section:end_section]

with open("e:/Clientes/Happy/happy/cursos_snippet.txt", "w", encoding="utf-8") as f:
    f.write(cursos_html)

print("Snippet extracted successfully.")
