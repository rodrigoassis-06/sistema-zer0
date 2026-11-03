import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Resolução A4 Vertical de Alta Definição (1276 x 1790)
W = 1276
H = 1790

def get_font(size, bold=False):
    names = [
        "C:\\Windows\\Fonts\\segoeui.ttf" if not bold else "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\arial.ttf" if not bold else "C:\\Windows\\Fonts\\arialbd.ttf"
    ]
    for n in names:
        if os.path.exists(n):
            try:
                return ImageFont.truetype(n, size)
            except:
                pass
    return ImageFont.load_default()

f_mono_xs = get_font(15, bold=True)
f_mono_sm = get_font(19, bold=True)
f_mono_lg = get_font(120, bold=False)
f_logo = get_font(26, bold=True)
f_title_hero = get_font(60, bold=True)
f_title_thin = get_font(60, bold=False)
f_h2_bold = get_font(42, bold=True)
f_h2_thin = get_font(42, bold=False)
f_h3 = get_font(28, bold=True)
f_body_lg = get_font(22, bold=False)
f_body_md = get_font(19, bold=False)
f_body_sm = get_font(16, bold=False)
f_body_xs = get_font(14, bold=False)
f_body_bold = get_font(19, bold=True)

# Cores
BG_DARK = (10, 13, 20)
CARD_DARK = (22, 27, 34)
BORDER_DARK = (33, 38, 45)
TEXT_WHITE = (241, 245, 249)
TEXT_MUTED = (148, 163, 184)
TEXT_SUB = (100, 116, 139)
BLUE = (0, 102, 214)
GREEN = (112, 179, 28)
GRAY = (92, 100, 112)
WHITE = (255, 255, 255)

cover_img = None
if os.path.exists('frontend/img/cover.jpg'):
    raw_c = Image.open('frontend/img/cover.jpg').convert('RGBA')
    # Scale to cover W x H
    scale = max(W / raw_c.width, H / raw_c.height)
    sw, sh = int(raw_c.width * scale), int(raw_c.height * scale)
    scaled_c = raw_c.resize((sw, sh), Image.Resampling.LANCZOS)
    # Center crop
    left = (sw - W) // 2
    top = (sh - H) // 2
    cover_img = scaled_c.crop((left, top, left + W, top + H))

def draw_logo(draw, x=80, y=70):
    s = 14
    gap = 4
    draw.rounded_rectangle([x, y, x + s, y + s], radius=2, fill=BLUE)
    draw.rounded_rectangle([x + s + gap, y, x + 2*s + gap, y + s], radius=2, fill=GREEN)
    draw.rounded_rectangle([x, y + s + gap, x + s, y + 2*s + gap], radius=2, fill=GRAY)
    draw.rounded_rectangle([x + s + gap, y + s + gap, x + 2*s + gap, y + 2*s + gap], radius=2, fill=WHITE)
    draw.text((x + 2*s + gap + 14, y + 1), "Sistema 0", fill=TEXT_WHITE, font=f_logo)
    draw.text((x + 2*s + gap + 155, y + 8), "· CATÁLOGO DIGITAL", fill=TEXT_SUB, font=f_mono_xs)

def draw_footer_v(draw, page_num, is_left, label=""):
    y = H - 65
    draw.line([(80, y - 15), (W - 80, y - 15)], fill=(255, 255, 255, 18), width=1)
    lbl = f"SISTEMA 0 · {label}" if label else "SISTEMA 0"
    pg_str = f"{page_num:02d} / 16"
    if is_left:
        draw.text((80, y), pg_str, fill=TEXT_SUB, font=f_mono_xs)
        draw.text((W - 380, y), lbl, fill=TEXT_SUB, font=f_mono_xs)
    else:
        draw.text((80, y), lbl, fill=TEXT_SUB, font=f_mono_xs)
        draw.text((W - 140, y), pg_str, fill=TEXT_SUB, font=f_mono_xs)

# ----------------- PAGE 1: COVER (PORTRAIT) -----------------
def make_page_1():
    img = Image.new('RGBA', (W, H), BG_DARK)
    if cover_img:
        img.paste(cover_img, (0, 0))
    # Gradient overlay vertical
    grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(grad)
    for y in range(H):
        alpha = int(255 * min(1.0, 0.4 + (y / H) * 0.6))
        g_draw.line([(0, y), (W, y)], fill=(10, 13, 20, alpha))
    img.alpha_composite(grad)

    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 80)

    draw.rounded_rectangle([W - 270, 80, W - 80, 120], radius=4, fill=(0, 0, 0, 180), outline=(255, 255, 255, 30))
    draw.text((W - 255, 90), "EDIÇÃO TÉCNICA 2026", fill=TEXT_MUTED, font=f_mono_xs)

    draw.text((80, 850), "CATÁLOGO DE MÓDULOS", fill=BLUE, font=f_mono_sm)
    draw.text((80, 910), "A gestão do seu negócio", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((80, 985), "em dois cliques.", fill=TEXT_WHITE, font=f_title_hero)

    draw.text((80, 1130), "Fichas técnicas dos 6 módulos essenciais — da conciliação financeira", fill=TEXT_MUTED, font=f_body_lg)
    draw.text((80, 1170), "ao fluxo completo de atendimentos e rotina operacional.", fill=TEXT_MUTED, font=f_body_lg)

    # Box inferior
    draw.rounded_rectangle([80, 1550, W - 80, 1630], radius=8, fill=(0, 0, 0, 150), outline=BORDER_DARK)
    draw.text((110, 1580), "ARQUITETURA DE ALTA PERFORMANCE · MULTI-NICHO", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((W - 280, 1580), "16 PÁGINAS", fill=BLUE, font=f_mono_sm)

    draw_footer_v(draw, 1, False)
    return img.convert('RGB')

# ----------------- PAGE 2: MANIFESTO (PORTRAIT) -----------------
def make_page_2():
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 80)
    draw.text((W - 220, 90), "MANIFESTO", fill=TEXT_SUB, font=f_mono_xs)

    draw.text((80, 240), "BEM-VINDO", fill=BLUE, font=f_mono_sm)
    draw.text((80, 290), "Menos telas.", fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 350), "Menos planilhas.", fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 410), "Mais decisão.", fill=TEXT_WHITE, font=f_h2_bold)

    p_lines = [
        "O Sistema 0 organiza finanças, rotina e operações",
        "em um único painel de blocos inteligentes.",
        "",
        "Cada informação está a um toque — sem menus profundos,",
        "sem planilhas paralelas e com zero retrabalho operacional.",
        "Projetado para empresários que exigem controle e clareza."
    ]
    y_text = 520
    for line in p_lines:
        if line:
            draw.text((80, y_text), line, fill=TEXT_MUTED, font=f_body_lg)
        y_text += 38

    # 4 Cards de Métricas em Grid 2x2
    bx = 80
    by = 820
    bw = 530
    bh = 220
    gap = 25

    # 01
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=8, fill=BLUE)
    draw.text((bx + 30, by + 25), "01", fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((bx + 30, by + 85), "06", fill=WHITE, font=f_title_thin)
    draw.text((bx + 30, by + 160), "módulos integrados", fill=WHITE, font=f_body_bold)

    # 02
    draw.rounded_rectangle([bx + bw + gap, by, bx + 2*bw + gap, by + bh], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((bx + bw + gap + 30, by + 25), "02", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((bx + bw + gap + 30, by + 85), "2", fill=WHITE, font=f_title_thin)
    draw.text((bx + bw + gap + 30, by + 160), "cliques por operação", fill=TEXT_MUTED, font=f_body_bold)

    # 03
    draw.rounded_rectangle([bx, by + bh + gap, bx + bw, by + 2*bh + gap], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((bx + 30, by + bh + gap + 25), "03", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((bx + 30, by + bh + gap + 85), "<300ms", fill=WHITE, font=f_title_thin)
    draw.text((bx + 30, by + bh + gap + 160), "tempo de resposta", fill=TEXT_MUTED, font=f_body_bold)

    # 04
    draw.rounded_rectangle([bx + bw + gap, by + bh + gap, bx + 2*bw + gap, by + 2*bh + gap], radius=8, fill=GREEN)
    draw.text((bx + bw + gap + 30, by + bh + gap + 25), "04", fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((bx + bw + gap + 30, by + bh + gap + 85), "AES-256", fill=WHITE, font=f_title_thin)
    draw.text((bx + bw + gap + 30, by + bh + gap + 160), "criptografia de ponta", fill=WHITE, font=f_body_bold)

    draw_footer_v(draw, 2, True, "MANIFESTO")
    return img.convert('RGB')

# ----------------- PAGE 3: INDEX (PORTRAIT) -----------------
def make_page_3(modules):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 80)
    draw.text((W - 260, 90), "ÍNDICE DOS MÓDULOS", fill=BLUE, font=f_mono_xs)

    draw.text((80, 200), "Visão Geral", fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 260), "Índice completo das 6 fichas técnicas oficiais", fill=TEXT_SUB, font=f_body_md)

    # Grid 2 colunas x 3 linhas
    cols = 2
    cw = 535
    ch = 320
    gx = 80
    gy = 340
    dx = 25
    dy = 25

    for i, m in enumerate(modules):
        col = i % cols
        row = i // cols
        x = gx + col * (cw + dx)
        y = gy + row * (ch + dy)

        c_hex = m["color"]
        c_rgb = BLUE if c_hex == "#0066D6" else GREEN if c_hex == "#70B31C" else GRAY if c_hex == "#5C6470" else WHITE
        is_light = m["tone"] == "light"
        text_c = (15, 23, 42) if is_light else WHITE
        sub_c = (71, 85, 105) if is_light else (255, 255, 255, 190)

        draw.rounded_rectangle([x, y, x + cw, y + ch], radius=8, fill=c_rgb)
        pg_num = 4 + i * 2
        draw.text((x + cw - 80, y + 25), f"P.{pg_num:02d}", fill=sub_c, font=f_mono_sm)
        draw.text((x + 30, y + 180), m["category"].upper(), fill=sub_c, font=f_mono_xs)
        draw.text((x + 30, y + 215), m["name"][0] + " " + m["name"][1], fill=text_c, font=f_h3)

    draw_footer_v(draw, 3, False, "ÍNDICE")
    return img.convert('RGB')

# ----------------- MODULE HERO (PORTRAIT, PÁG ÍMPAR) -----------------
def make_module_hero_v(mod, idx, page_num):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    c_hex = mod["color"]
    c_rgb = BLUE if c_hex == "#0066D6" else GREEN if c_hex == "#70B31C" else GRAY if c_hex == "#5C6470" else WHITE
    is_light = mod["tone"] == "light"

    # Barra lateral
    draw.rectangle([0, 0, 14, H], fill=c_rgb)

    draw_logo(draw, 80, 80)
    draw.text((W - 320, 90), mod["category"], fill=BLUE, font=f_mono_xs)

    # Numeral Watermark
    draw.text((80, 180), mod["num"], fill=(255, 255, 255, 25), font=f_mono_lg)

    # Título & Subtítulos
    draw.text((80, 310), mod["category"], fill=BLUE, font=f_mono_xs)
    draw.text((80, 350), mod["name"][0], fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 405), mod["name"][1], fill=TEXT_WHITE, font=f_h2_bold)

    draw.text((80, 490), mod["tagline"], fill=TEXT_WHITE, font=f_body_lg)
    draw.text((80, 530), mod["focus"], fill=TEXT_MUTED, font=f_body_md)

    # Mockup Central Vertical
    mx = 80
    my = 630
    mw = W - 160
    mh = 620
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=14, fill=(11, 14, 20), outline=BORDER_DARK)

    # Topbar do mockup
    draw.line([(mx, my + 60), (mx + mw, my + 60)], fill=BORDER_DARK, width=1)
    draw.text((mx + 30, my + 20), mod["name"][0].capitalize(), fill=TEXT_WHITE, font=f_body_bold)
    draw.text((mx + mw - 220, my + 24), "Administrador Master", fill=TEXT_SUB, font=f_mono_xs)

    # Blocos internos
    gx = mx + 30
    gy = my + 90
    gw = mw - 60

    # Big Block
    draw.rounded_rectangle([gx, gy, gx + int(gw * 0.65), gy + 160], radius=8, fill=c_rgb)
    draw.text((gx + 25, gy + 20), "STATUS: ATIVO / ONLINE", fill=(71, 85, 105) if is_light else (255, 255, 255, 180), font=f_mono_xs)
    draw.text((gx + 25, gy + 100), mod["name"][0].capitalize(), fill=(15, 23, 42) if is_light else WHITE, font=f_h3)

    # Velocidade
    vx = gx + int(gw * 0.65) + 20
    draw.rounded_rectangle([vx, gy, gx + gw, gy + 160], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((vx + 25, gy + 25), "VELOCIDADE", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((vx + 25, gy + 90), mod["speed"], fill=WHITE, font=f_h2_bold)

    # Linha 2
    gy2 = gy + 180
    draw.rounded_rectangle([gx, gy2, gx + int(gw * 0.32), gy2 + 130], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((gx + 20, gy2 + 20), mod["metrics"][0][0][:20], fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + 20, gy2 + 70), mod["metrics"][0][1], fill=WHITE, font=f_body_bold)

    draw.rounded_rectangle([gx + int(gw * 0.34), gy2, gx + int(gw * 0.65), gy2 + 130], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((gx + int(gw * 0.34) + 20, gy2 + 20), mod["metrics"][1][0][:20], fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + int(gw * 0.34) + 20, gy2 + 70), mod["metrics"][1][1], fill=WHITE, font=f_body_bold)

    draw.rounded_rectangle([vx, gy2, gx + gw, gy2 + 130], radius=8, fill=BLUE)
    draw.text((vx + 140, gy2 + 35), "+", fill=WHITE, font=f_h2_bold)
    draw.text((vx + 130, gy2 + 85), "Novo", fill=WHITE, font=f_body_bold)

    # Linha 3
    gy3 = gy2 + 150
    draw.rounded_rectangle([gx, gy3, gx + int(gw * 0.65), gy3 + 120], radius=8, fill=GRAY)
    draw.text((gx + 25, gy3 + 20), mod["badge"], fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((gx + 25, gy3 + 60), mod["architecture"], fill=WHITE, font=f_body_bold)

    draw.rounded_rectangle([vx, gy3, gx + gw, gy3 + 120], radius=8, fill=WHITE)
    draw.text((vx + 25, gy3 + 20), "OPERAÇÃO", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((vx + 25, gy3 + 60), mod["clicks"], fill=(15, 23, 42), font=f_h3)

    # Specs Bar inferior
    sy = 1340
    draw.line([(80, sy - 20), (W - 80, sy - 20)], fill=(255, 255, 255, 25), width=1)
    draw.text((80, sy), "RESPOSTA", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((80, sy + 30), mod["speed"], fill=TEXT_WHITE, font=f_body_bold)

    draw.text((450, sy), "OPERAÇÃO", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((450, sy + 30), mod["clicks"], fill=TEXT_WHITE, font=f_body_bold)

    draw.text((800, sy), "ARQUITETURA", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((800, sy + 30), mod["architecture"], fill=TEXT_WHITE, font=f_body_bold)

    draw_footer_v(draw, page_num, True, mod["name"][0] + " " + mod["name"][1])
    return img.convert('RGB')

# ----------------- MODULE SPEC SHEET (PORTRAIT, PÁG PAR) -----------------
def make_module_spec_v(mod, page_num):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 80)
    draw.text((W - 250, 90), "FICHA TÉCNICA", fill=BLUE, font=f_mono_xs)

    draw.text((80, 190), "FICHA TÉCNICA", fill=BLUE, font=f_mono_sm)
    draw.text((80, 230), mod["name"][0] + " " + mod["name"][1], fill=TEXT_WHITE, font=f_h2_bold)

    c_hex = mod["color"]
    c_rgb = BLUE if c_hex == "#0066D6" else GREEN if c_hex == "#70B31C" else GRAY if c_hex == "#5C6470" else WHITE
    is_light = mod["tone"] == "light"

    # Seção 1: Diferenciais Estruturais
    y = 330
    draw.text((80, y), "DIFERENCIAIS ESTRUTURAIS", fill=TEXT_SUB, font=f_mono_xs)
    y += 35
    for ci, c in enumerate(mod["claims"]):
        draw.text((80, y), f"0{ci+1}", fill=BLUE, font=f_mono_sm)
        draw.text((125, y), c, fill=TEXT_WHITE, font=f_body_md)
        y += 45

    # Seção 2: Funcionalidades & Arquitetura (2 colunas)
    y += 25
    draw.line([(80, y), (W - 80, y)], fill=(255, 255, 255, 15), width=1)
    y += 30

    col_w = (W - 160 - 40) // 2
    # Funcionalidades
    draw.text((80, y), "FUNCIONALIDADES CHAVE", fill=TEXT_SUB, font=f_mono_xs)
    fy = y + 35
    for f in mod["features"][:5]:
        draw.text((80, fy), f"•  {f}", fill=TEXT_WHITE, font=f_body_sm)
        fy += 40

    # Arquitetura Specs
    ax = 80 + col_w + 40
    draw.text((ax, y), "ARQUITETURA & SEGURANÇA", fill=TEXT_SUB, font=f_mono_xs)
    ay = y + 35
    specs_list = [
        ("STACK", mod["specs"]["stack"]),
        ("SEGURANÇA", mod["specs"]["security"]),
        ("SINCRONIZAÇÃO", mod["specs"]["sync"]),
        ("EXPORTAÇÃO", mod["specs"]["export"]),
    ]
    for sk, sv in specs_list:
        draw.text((ax, ay), sk, fill=TEXT_SUB, font=f_mono_xs)
        draw.text((ax + 160, ay), sv, fill=TEXT_WHITE, font=f_body_sm)
        ay += 45

    # Seção 3: Indicadores Operacionais
    y = 920
    draw.line([(80, y), (W - 80, y)], fill=(255, 255, 255, 15), width=1)
    y += 30
    draw.text((80, y), "INDICADORES OPERACIONAIS", fill=TEXT_SUB, font=f_mono_xs)
    y += 45
    for m in mod["metrics"]:
        draw.text((80, y), m[0], fill=TEXT_MUTED, font=f_body_sm)
        draw.text((W - 240, y), m[1], fill=WHITE, font=f_body_bold)
        draw.rounded_rectangle([80, y + 25, W - 80, y + 33], radius=4, fill=CARD_DARK)
        pct_val = int(m[2].replace('%', '').strip()) if '%' in m[2] else 85
        fill_w = int((W - 160) * (pct_val / 100.0))
        draw.rounded_rectangle([80, y + 25, 80 + fill_w, y + 33], radius=4, fill=c_rgb)
        y += 65

    # Seção 4: Box de Recomendação
    ry = 1420
    draw.rounded_rectangle([80, ry, W - 80, ry + 160], radius=8, fill=c_rgb)
    draw.text((110, ry + 25), "RECOMENDAÇÃO DE IMPLANTAÇÃO", fill=(71, 85, 105) if is_light else (255, 255, 255, 180), font=f_mono_xs)
    rec_text = mod["recommendation"]
    draw.text((110, ry + 75), rec_text[:65], fill=(15, 23, 42) if is_light else WHITE, font=f_body_bold)
    if len(rec_text) > 65:
        draw.text((110, ry + 110), rec_text[65:], fill=(15, 23, 42) if is_light else WHITE, font=f_body_bold)

    draw_footer_v(draw, page_num, False, mod["name"][0] + " " + mod["name"][1] + " · FICHA TÉCNICA")
    return img.convert('RGB')

# ----------------- PAGE 16: CLOSING (PORTRAIT) -----------------
def make_page_16():
    img = Image.new('RGBA', (W, H), BG_DARK)
    if cover_img:
        tint = Image.new('RGBA', (W, H), (10, 13, 20, 210))
        c_layer = cover_img.copy()
        c_layer.alpha_composite(tint)
        img.paste(c_layer, (0, 0))

    draw = ImageDraw.Draw(img)
    draw_logo(draw, W // 2 - 140, 300)

    draw.text((W // 2 - 320, 460), "Seu negócio inteiro,", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((W // 2 - 320, 535), "em um só painel.", fill=TEXT_WHITE, font=f_title_hero)

    draw.text((W // 2 - 400, 680), "Solicite uma demonstração ao vivo e conheça o Sistema 0 em funcionamento.", fill=TEXT_MUTED, font=f_body_lg)

    btn_y = 820
    draw.rounded_rectangle([W // 2 - 260, btn_y, W // 2 - 30, btn_y + 70], radius=8, fill=WHITE)
    draw.text((W // 2 - 180, btn_y + 22), "Entrar", fill=(15, 23, 42), font=f_body_bold)

    draw.rounded_rectangle([W // 2 + 10, btn_y, W // 2 + 280, btn_y + 70], radius=8, fill=(0, 0, 0, 120), outline=WHITE)
    draw.text((W // 2 + 40, btn_y + 22), "Agendar demonstração", fill=WHITE, font=f_body_bold)

    draw.text((W // 2 - 220, 1150), "contato@sistema-zero.com.br · WhatsApp Comercial", fill=TEXT_SUB, font=f_body_md)
    draw.text((W // 2 - 230, 1200), "© 2026 SISTEMA ZERO · TODOS OS DIREITOS RESERVADOS", fill=TEXT_SUB, font=f_mono_xs)

    draw_footer_v(draw, 16, True, "ENCERRAMENTO")
    return img.convert('RGB')

# ----------------- MAIN PIPELINE -----------------
import build_black_edition_catalog
modules = build_black_edition_catalog.modules

pages = []
print("Gerando Pág 01: Capa...")
pages.append(make_page_1())

print("Gerando Pág 02: Manifesto...")
pages.append(make_page_2())

print("Gerando Pág 03: Índice...")
pages.append(make_page_3(modules))

for i, mod in enumerate(modules):
    p_hero = 4 + i * 2
    p_spec = 5 + i * 2
    print(f"Gerando Págs {p_hero:02d} e {p_spec:02d}: {mod['name'][0]} {mod['name'][1]}...")
    pages.append(make_module_hero_v(mod, i, p_hero))
    pages.append(make_module_spec_v(mod, p_spec))

print("Gerando Pág 16: Encerramento...")
pages.append(make_page_16())

out_pdf = "docs/CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf"
out_pdf_brain = r"C:\Users\Rodrigo\.gemini\antigravity\brain\7de99eeb-9e40-46d6-883f-9a2dce0516dc\CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf"

print(f"Compilando PDF A4 de 16 páginas em {out_pdf}...")
pages[0].save(
    out_pdf,
    save_all=True,
    append_images=pages[1:],
    resolution=150.0
)
print("Salvo em docs com sucesso!")

pages[0].save(
    out_pdf_brain,
    save_all=True,
    append_images=pages[1:],
    resolution=150.0
)
print("Salvo no diretório de artefatos com sucesso!")
