import glob
import re

cursos_snippet = open("e:/Clientes/Happy/happy/cursos_snippet.txt", "r", encoding="utf-8").read()

html_files = glob.glob("e:/Clientes/Happy/happy/*.html")

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update Units
    content = re.sub(r'<span>Endereço a confirmar, Asa Norte, Brasília, DF</span>', r'<span>SHCGN 710/711 loja 27</span>', content)
    content = re.sub(r'<span>Endereço a confirmar, Asa Sul, Brasília, DF</span>', r'<span>910 Sul - Mix Park Sul -  Bloco D</span>', content)
    
    # Remove horario a confirmar and its icon
    content = re.sub(r'<div class="unidade-row">\s*<svg[^>]+><circle[^>]+><polyline[^>]+></svg>\s*<span>Horário a confirmar</span>\s*</div>', '', content)
    # Remove the second "A confirmar"
    content = re.sub(r'<div class="unidade-row">\s*<svg[^>]+><path[^>]+></svg>\s*<span>A confirmar</span>\s*</div>', '', content)
    
    # Add Whatsapp links in Asa Norte & Sul
    content = re.sub(r'(<span>SHCGN 710/711 loja 27</span>\s*</div>)', r'\1\n          <div class="unidade-row">\n            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.72 19.79 19.79 0 01.04 1.1 2 2 0 012 .12h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7a2 2 0 011.72 2.02z"/></svg>\n            <span>(61) 996374604</span>\n          </div>', content)
    
    content = re.sub(r'(<span>910 Sul - Mix Park Sul -  Bloco D</span>\s*</div>)', r'\1\n          <div class="unidade-row">\n            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.72 19.79 19.79 0 01.04 1.1 2 2 0 012 .12h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7a2 2 0 011.72 2.02z"/></svg>\n            <span>(61) 3244-2510</span>\n          </div>', content)
    
    # 2. Update CTA Buttons inside Asa Norte & Sul
    # Asa Sul map img src is unidade-asa-sul.jpeg
    content = re.sub(r'(<img src="img/unidade-asa-sul.jpeg" alt="Happy Brasília Asa Sul" />\s*</div>\s*)<a href="https://wa.me/5561999999999"', r'\1<a href="https://wa.me/556132442510"', content)
    # Asa Norte map img src is unidade-asa-norte.webp
    content = re.sub(r'(<img src="img/unidade-asa-norte.webp" alt="Happy Brasília Asa Norte" />\s*</div>\s*)<a href="https://wa.me/5561999999999"', r'\1<a href="https://wa.me/5561996374604"', content)
    
    # 3. Differentials
    differentials = """      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#128663;</div>
        <div class="diferencial-title">Estacionamento Facilitado</div>
        <p class="diferencial-text">Asa Sul com voucher para garagem e Asa Norte com fácil acesso para parar na porta.</p>
      </div>
      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#127468;&#127463;</div>
        <div class="diferencial-title">Metodologia Centro Britânico</div>
        <p class="diferencial-text">Excelência no ensino da língua inglesa com a qualidade reconhecida do Centro Britânico.</p>
      </div>
      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#129302;</div>
        <div class="diferencial-title">Robôs Dash</div>
        <p class="diferencial-text">Para os pequenos de 5 e 6 anos aprenderem programação na prática e com muita diversão.</p>
      </div>
      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#127941;</div>
        <div class="diferencial-title">Competições Internas</div>
        <p class="diferencial-text">Eventos com premiação, como o Ideathon, para estimular o desenvolvimento e a criatividade.</p>
      </div>
      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#128214;</div>
        <div class="diferencial-title">Empréstimo de Livros</div>
        <p class="diferencial-text">Biblioteca acessível aos alunos para incentivar o hábito da leitura e a imaginação.</p>
      </div>
      <div class="diferencial-card fade-in">
        <div class="diferencial-icon">&#127918;</div>
        <div class="diferencial-title">Espaço Gamer e Coworking</div>
        <p class="diferencial-text">Na Asa Sul, os alunos aproveitam o espaço gamer enquanto os pais têm uma área para teletrabalho.</p>
      </div>
    </div>"""
    content = re.sub(r'(<p class="diferencial-text">ABF, Great Place to Work, Excelência em Franchising: a Happy é referência nacional em educação.</p>\s*</div>\s*)</div>', r'\1' + differentials, content)
    
    # 4. Whatsapp Modal
    wa_modal = """
<!-- MODAL WHATSAPP -->
<div id="wa-modal" class="wa-modal">
  <div class="wa-modal-content">
    <span class="wa-modal-close" onclick="closeWaModal()">&times;</span>
    <h3 style="font-family: var(--title-font); color: var(--blue); margin-bottom: 10px; font-size: 1.4rem;">Escolha uma unidade</h3>
    <p style="color: var(--gray-text); margin-bottom: 20px; font-size: .95rem;">Com qual unidade você deseja falar?</p>
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <a href="https://wa.me/556132442510" target="_blank" class="btn btn-blue btn-full" onclick="closeWaModal()">Asa Sul</a>
      <a href="https://wa.me/5561996374604" target="_blank" class="btn btn-blue btn-full" onclick="closeWaModal()">Asa Norte</a>
    </div>
  </div>
</div>
<script>
  function openWaModal(e) {
    e.preventDefault();
    document.getElementById('wa-modal').classList.add('show');
  }
  function closeWaModal() {
    document.getElementById('wa-modal').classList.remove('show');
  }
  window.addEventListener('click', function(e) {
    var modal = document.getElementById('wa-modal');
    if (e.target === modal) {
      closeWaModal();
    }
  });
</script>
</body>"""
    # Replace whatsapp button with modal trigger
    content = re.sub(r'<a href="https://wa.me/5561999999999" target="_blank" class="whatsapp-float"', r'<a href="#" onclick="openWaModal(event)" class="whatsapp-float"', content)
    # Add wa_modal before </body>
    content = content.replace("</body>", wa_modal)
    
    # Add Modal CSS before </style>
    wa_css = """
    /* Modal Whatsapp */
    .wa-modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.5); align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s; }
    .wa-modal.show { display: flex; opacity: 1; }
    .wa-modal-content { background-color: #fefefe; padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; text-align: center; position: relative; transform: translateY(-20px); transition: transform 0.3s; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }
    .wa-modal.show .wa-modal-content { transform: translateY(0); }
    .wa-modal-close { color: #aaa; position: absolute; top: 15px; right: 20px; font-size: 28px; font-weight: bold; cursor: pointer; transition: color 0.2s; }
    .wa-modal-close:hover { color: var(--blue); }
</style>"""
    content = content.replace("</style>", wa_css)

    # 5. index.html "Todos os Cursos"
    if "index.html" in filepath:
        content = content.replace('<option value="" disabled selected>Curso de interesse *</option>', '<option value="" disabled selected>Curso de interesse *</option>\n            <option value="Todos os Cursos">Todos os Cursos</option>')
        # Form Unidades fix
        content = content.replace('<option value="Asa Sul">Asa Sul</option>', '<option value="910 Sul">910 Sul</option>')
        content = content.replace('<option value="Asa Norte">Asa Norte</option>', '<option value="711 Norte">711 Norte</option>')

    # 6. Cursos section for ALL pages EXCEPT index
    if "index.html" not in filepath:
        # Add CSS if not present
        if ".curso-orb" not in content:
            cursos_css = """
    .cursos-section { padding: 100px 0; background: var(--bg-color); }
    .cursos-sub { text-align: center; max-width: 700px; margin: 0 auto 60px; font-size: 1.1rem; color: var(--gray-text); line-height: 1.6; }
    .cursos-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; margin-bottom: 50px; }
    .curso-card { background: #fff; border-radius: 20px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,.06); position: relative; overflow: hidden; transition: transform .3s, box-shadow .3s; display: flex; flex-direction: column; }
    .curso-card:hover { transform: translateY(-6px); box-shadow: 0 12px 40px rgba(0,0,0,.12); }
    .curso-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; }
    .curso-card.code::before    { background: var(--green);  }
    .curso-card.money::before   { background: var(--yellow); }
    .curso-card.speech::before  { background: var(--red);    }
    .curso-card.english::before { background: var(--orange); }

    .curso-card-header { display: flex; align-items: center; gap: 16px; margin-bottom: 18px; }
    .curso-orb { width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; flex-shrink: 0; }
    .curso-card.code .curso-orb    { background: var(--green);  }
    .curso-card.money .curso-orb   { background: var(--yellow); }
    .curso-card.speech .curso-orb  { background: var(--red);    }
    .curso-card.english .curso-orb { background: var(--orange); }

    .curso-name    { font-family: var(--title-font); font-weight: 900; font-size: 1.5rem; letter-spacing: -0.03em; color: var(--blue); }
    .curso-tagline { font-family: var(--condensed-font); font-size: .82rem; text-transform: uppercase; letter-spacing: .06em; color: #aaa; }
    .curso-desc    { font-size: .95rem; color: var(--gray-text); line-height: 1.65; margin-bottom: 20px; }

    .curso-footer  { display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap; }
    .curso-age     { font-family: var(--condensed-font); font-size: .8rem; color: #aaa; display: flex; align-items: center; gap: 6px; }
    .curso-age::before { content: ''; display: inline-block; width: 8px; height: 8px; border-radius: 50%; }
    .curso-card.code .curso-age::before    { background: var(--green);  }
    .curso-card.money .curso-age::before   { background: var(--yellow); }
    .curso-card.speech .curso-age::before  { background: var(--red);    }
    .curso-card.english .curso-age::before { background: var(--orange); }

    .curso-card.code .btn-curso    { background: var(--green);  color: #fff; }
    .curso-card.money .btn-curso   { background: var(--yellow); color: var(--blue); }
    .curso-card.speech .btn-curso  { background: var(--red);    color: #fff; }
    .curso-card.english .btn-curso { background: var(--orange); color: #fff; }

    .cursos-cta-box { background: var(--blue); color: #fff; border-radius: 20px; padding: 40px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 20px; }
    .cursos-cta-box p { font-size: 1.15rem; max-width: 500px; margin: 0; line-height: 1.5; }
    .cursos-cta-box .btn { margin-top: 10px; }
</style>"""
            content = content.replace("</style>", cursos_css)
            # Add responsive css for grid
            resp_css = """      .cursos-grid        { grid-template-columns: 1fr; }
      .curso-card    { padding: 24px 20px; }
      .curso-age     { width: 100%; }"""
            content = re.sub(r'(@media \(max-width: 768px\) {)', r'\1\n' + resp_css, content)
            
            resp_css2 = """      .curso-card   { padding: 20px 16px; }"""
            content = re.sub(r'(@media \(max-width: 480px\) {)', r'\1\n' + resp_css2, content)

        # Insert before CTA Final (penúltima seção)
        # Search for <section id="cta-final"
        if 'id="cursos"' not in content:
            content = re.sub(r'(<section id="cta-final")', cursos_snippet + r'\n\n\1', content)

    # 7. Centro Britanico for happy-english
    if "happy-english.html" in filepath:
        cb_html = """
<!-- SEÇÃO METODOLOGIA CENTRO BRITÂNICO -->
<section id="metodologia-cb" style="padding: 100px 0; background: #fff;">
  <div class="container">
    <div style="display: flex; flex-wrap: wrap; gap: 50px; align-items: center;">
      <div style="flex: 1; min-width: 300px;">
        <h2 class="section-title fade-in" style="text-align: left;">Metodologia Centro Britânico</h2>
        <p class="section-desc fade-in" style="text-align: left; margin-bottom: 20px; font-size: 1.1rem; line-height: 1.7;">
          Na Happy English, unimos a inovação e o ensino prático à excelência do <strong>Centro Britânico</strong>. Uma parceria que garante um ensino da língua inglesa com padrão internacional de qualidade, reconhecido por sua eficácia no preparo para exames e na fluência para o mundo real.
        </p>
        <p class="section-desc fade-in" style="text-align: left; font-size: 1.1rem; line-height: 1.7;">
          Nossos alunos aprendem em um ambiente dinâmico, absorvendo o idioma de forma natural e engajadora, desenvolvendo desde cedo a confiança para se comunicar globalmente.
        </p>
      </div>
      <div style="flex: 1; min-width: 300px; display: flex; justify-content: center; align-items: center;">
        <img src="logo/centroBritanico.png" alt="Metodologia Centro Britânico" style="max-width: 100%; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.1);" class="fade-in">
      </div>
    </div>
  </div>
</section>
"""
        # Add after #diferenciais
        if 'id="metodologia-cb"' not in content:
            content = re.sub(r'(</section>\s*)(<section id="cursos"|<section id="cta-final")', r'\1' + cb_html + r'\n\2', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Applied all changes successfully.")
