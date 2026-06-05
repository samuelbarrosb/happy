import glob
import re

html_content = """        <div class="dep-card">
          <div class="dep-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="dep-text">"Meu filho de 6 anos fez a colônia de férias Dash and Dot e amou!"</p>
          <div class="dep-author">
            <div class="dep-avatar" style="background:var(--green)">AM</div>
            <div class="dep-info">
              <div class="dep-name">Aline Minervino</div>
              <div class="dep-role">Mãe de aluno</div>
            </div>
          </div>
        </div>

        <div class="dep-card">
          <div class="dep-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="dep-text">"Eu amoooo o Happy! A minha filha começou a estudar lá este ano e já aprendeu a criar a sua própria lojinha online."</p>
          <div class="dep-author">
            <div class="dep-avatar" style="background:var(--blue)">FR</div>
            <div class="dep-info">
              <div class="dep-name">Fernanda Ribeiro</div>
              <div class="dep-role">Mãe de aluna</div>
            </div>
          </div>
        </div>

        <div class="dep-card">
          <div class="dep-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="dep-text">"Meu lugar favorito!!! melhor escola de tecnologia para crianças do Brasil."</p>
          <div class="dep-author">
            <div class="dep-avatar" style="background:var(--yellow)">AB</div>
            <div class="dep-info">
              <div class="dep-name">Ana Beatriz</div>
              <div class="dep-role">Aluna</div>
            </div>
          </div>
        </div>

        <div class="dep-card">
          <div class="dep-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="dep-text">"Eles têm uma didática incrível. Meu filho de 8 anos já está criando seus próprios jogos e entendendo lógica de programação de forma super lúdica!"</p>
          <div class="dep-author">
            <div class="dep-avatar" style="background:var(--red)">CS</div>
            <div class="dep-info">
              <div class="dep-name">Carlos Santos</div>
              <div class="dep-role">Pai de aluno</div>
            </div>
          </div>
        </div>

        <div class="dep-card">
          <div class="dep-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="dep-text">"O melhor investimento que fiz na educação da minha filha. O ambiente é acolhedor e os professores são extremamente preparados."</p>
          <div class="dep-author">
            <div class="dep-avatar" style="background:var(--orange)">MO</div>
            <div class="dep-info">
              <div class="dep-name">Marcela Oliveira</div>
              <div class="dep-role">Mãe de aluna</div>
            </div>
          </div>
        </div>"""

for filepath in glob.glob('e:/Clientes/Happy/happy/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Substituir os depoimentos
    # Encontrar o div "depoimentos-grid" e substituir seu conteudo
    # A estrutura original é: <div class="depoimentos-grid fade-in"> ... </div>
    pattern = r'(<div class="depoimentos-grid[^>]*>)(.*?)(</div>\s*</div>\s*</section>)'
    
    # We need a robust regex because the closing tags might be different
    # Let's find <div class="depoimentos-grid fade-in"> and the NEXT </div> that closes the container
    # Since regex for nested divs is hard, we can just replace everything between <div class="depoimentos-grid fade-in"> and </div></div></section>
    
    match = re.search(r'<div class="depoimentos-grid fade-in">.*?</section>', content, flags=re.DOTALL)
    if match:
        new_section = '<div class="depoimentos-grid fade-in">\n' + html_content + '\n      </div>\n    </div>\n  </div>\n</section>'
        content = content[:match.start()] + new_section + content[match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Depoimentos atualizados.")
