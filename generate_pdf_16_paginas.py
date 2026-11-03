import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Dimensões 16:9 / 16:10 de Alta Resolução (1920 x 1080)
W = 1920
H = 1080

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

f_mono_xs = get_font(14, bold=True)
f_mono_sm = get_font(18, bold=True)
f_mono_lg = get_font(110, bold=False)
f_logo = get_font(24, bold=True)
f_logo_sub = get_font(14, bold=True)
f_title_hero = get_font(64, bold=True)
f_title_thin = get_font(64, bold=False)
f_h2_bold = get_font(44, bold=True)
f_h2_thin = get_font(44, bold=False)
f_h3 = get_font(28, bold=True)
f_body_lg = get_font(22, bold=False)
f_body_md = get_font(18, bold=False)
f_body_sm = get_font(15, bold=False)
f_body_xs = get_font(13, bold=False)
f_body_bold = get_font(18, bold=True)

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
    cover_img = Image.open('frontend/img/cover.jpg').convert('RGBA').resize((W, H), Image.Resampling.LANCZOS)

def draw_logo(draw, x=70, y=50):
    # 4 squares
    s = 14
    gap = 4
    draw.rounded_rectangle([x, y, x + s, y + s], radius=2, fill=BLUE)
    draw.rounded_rectangle([x + s + gap, y, x + 2*s + gap, y + s], radius=2, fill=GREEN)
    draw.rounded_rectangle([x, y + s + gap, x + s, y + 2*s + gap], radius=2, fill=GRAY)
    draw.rounded_rectangle([x + s + gap, y + s + gap, x + 2*s + gap, y + 2*s + gap], radius=2, fill=WHITE)
    draw.text((x + 2*s + gap + 14, y + 2), "Sistema 0", fill=TEXT_WHITE, font=f_logo)
    draw.text((x + 2*s + gap + 140, y + 8), "· CATÁLOGO DIGITAL", fill=TEXT_SUB, font=f_mono_xs)

def draw_footer(draw, page_num, label=""):
    y = H - 45
    draw.line([(70, y - 10), (W - 70, y - 10)], fill=(255, 255, 255, 18), width=1)
    lbl = f"SISTEMA 0 · {label}" if label else "SISTEMA 0"
    draw.text((70, y), lbl, fill=TEXT_SUB, font=f_mono_xs)
    pg_str = f"{page_num:02d} / 16"
    draw.text((W - 130, y), pg_str, fill=TEXT_SUB, font=f_mono_xs)

# ----------------- PAGE 1: COVER -----------------
def make_page_1():
    img = Image.new('RGBA', (W, H), BG_DARK)
    if cover_img:
        img.paste(cover_img, (0, 0))
    # Gradient overlay da esquerda para a direita
    grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(grad)
    for x in range(W):
        alpha = int(255 * (1.0 - (x / W)**1.2)) if x < 1200 else int(255 * 0.1)
        g_draw.line([(x, 0), (x, H)], fill=(10, 13, 20, max(alpha, 80)))
    img.alpha_composite(grad)

    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 60)

    # Edição técnica
    draw.rounded_rectangle([W - 270, 60, W - 80, 95], radius=4, fill=(0, 0, 0, 160), outline=(255, 255, 255, 30))
    draw.text((W - 255, 68), "EDIÇÃO TÉCNICA 2026", fill=TEXT_MUTED, font=f_mono_xs)

    # Centro
    draw.text((80, 360), "CATÁLOGO DE MÓDULOS", fill=BLUE, font=f_mono_sm)
    draw.text((80, 410), "A gestão do seu negócio", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((80, 480), "em dois cliques.", fill=TEXT_WHITE, font=f_title_hero)

    draw.text((80, 580), "Fichas técnicas dos 6 módulos essenciais — da conciliação financeira", fill=TEXT_MUTED, font=f_body_lg)
    draw.text((80, 615), "ao fluxo completo de atendimentos.", fill=TEXT_MUTED, font=f_body_lg)

    draw_footer(draw, 1)
    return img.convert('RGB')

# ----------------- PAGE 2: MANIFESTO -----------------
def make_page_2():
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 60)
    draw.text((W - 200, 68), "MANIFESTO", fill=TEXT_SUB, font=f_mono_xs)

    # Coluna Esquerda
    draw.text((80, 300), "BEM-VINDO", fill=BLUE, font=f_mono_sm)
    draw.text((80, 340), "Menos telas.", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((80, 405), "Menos planilhas.", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((80, 470), "Mais decisão.", fill=TEXT_WHITE, font=f_title_hero)

    p1 = "O Sistema 0 organiza finanças, rotina e operações"
    p2 = "em um único painel de blocos. Cada informação está"
    p3 = "a um toque — sem menus profundos, sem retrabalho."
    draw.text((80, 580), p1, fill=TEXT_MUTED, font=f_body_md)
    draw.text((80, 610), p2, fill=TEXT_MUTED, font=f_body_md)
    draw.text((80, 640), p3, fill=TEXT_MUTED, font=f_body_md)

    # Coluna Direita: Grid 2x2 de métricas
    bx = 1000
    by = 260
    bw = 380
    bh = 220
    gap = 20

    # 01
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=8, fill=BLUE)
    draw.text((bx + 25, by + 20), "01", fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((bx + 25, by + 90), "06", fill=WHITE, font=f_title_thin)
    draw.text((bx + 25, by + 165), "módulos integrados", fill=WHITE, font=f_body_bold)

    # 02
    draw.rounded_rectangle([bx + bw + gap, by, bx + 2*bw + gap, by + bh], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((bx + bw + gap + 25, by + 20), "02", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((bx + bw + gap + 25, by + 90), "2", fill=WHITE, font=f_title_thin)
    draw.text((bx + bw + gap + 25, by + 165), "cliques por operação", fill=TEXT_MUTED, font=f_body_bold)

    # 03
    draw.rounded_rectangle([bx, by + bh + gap, bx + bw, by + 2*bh + gap], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((bx + 25, by + bh + gap + 20), "03", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((bx + 25, by + bh + gap + 90), "<300ms", fill=WHITE, font=f_title_thin)
    draw.text((bx + 25, by + bh + gap + 165), "tempo de resposta", fill=TEXT_MUTED, font=f_body_bold)

    # 04
    draw.rounded_rectangle([bx + bw + gap, by + bh + gap, bx + 2*bw + gap, by + 2*bh + gap], radius=8, fill=GREEN)
    draw.text((bx + bw + gap + 25, by + bh + gap + 20), "04", fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((bx + bw + gap + 25, by + bh + gap + 90), "AES-256", fill=WHITE, font=f_title_thin)
    draw.text((bx + bw + gap + 25, by + bh + gap + 165), "criptografia de ponta", fill=WHITE, font=f_body_bold)

    draw_footer(draw, 2, "MANIFESTO")
    return img.convert('RGB')

# ----------------- PAGE 3: INDEX -----------------
def make_page_3(modules):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 60)
    draw.text((W - 250, 68), "ÍNDICE DOS MÓDULOS", fill=BLUE, font=f_mono_xs)

    draw.text((80, 160), "Visão Geral", fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 220), "Índice dos módulos e catálogo de fichas técnicas", fill=TEXT_SUB, font=f_body_sm)

    # Grid 3x2
    cols = 3
    cw = 550
    ch = 300
    gx = 80
    gy = 280
    dx = 40
    dy = 30

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
        draw.text((x + cw - 70, y + 25), f"P.{pg_num:02d}", fill=sub_c, font=f_mono_sm)
        draw.text((x + 30, y + 150), m["category"].upper(), fill=sub_c, font=f_mono_xs)
        draw.text((x + 30, y + 185), m["name"][0] + " " + m["name"][1], fill=text_c, font=f_h3)

    draw_footer(draw, 3, "ÍNDICE")
    return img.convert('RGB')

# ----------------- MODULE HERO (ODD PAGES: 4, 6, 8, 10, 12, 14) -----------------
def make_module_hero(mod, idx, page_num):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)

    c_hex = mod["color"]
    c_rgb = BLUE if c_hex == "#0066D6" else GREEN if c_hex == "#70B31C" else GRAY if c_hex == "#5C6470" else WHITE

    # Barra lateral de cor
    draw.rectangle([0, 0, 14, H], fill=c_rgb)

    draw_logo(draw, 80, 60)
    draw.text((W - 320, 68), mod["category"], fill=BLUE, font=f_mono_xs)

    # Watermark número
    draw.text((80, 200), mod["num"], fill=(255, 255, 255, 25), font=f_mono_lg)

    # Título do Módulo
    draw.text((80, 340), mod["category"], fill=BLUE, font=f_mono_xs)
    draw.text((80, 380), mod["name"][0], fill=TEXT_WHITE, font=f_h2_thin)
    draw.text((80, 435), mod["name"][1], fill=TEXT_WHITE, font=f_h2_bold)

    draw.text((80, 520), mod["tagline"], fill=TEXT_WHITE, font=f_body_lg)
    draw.text((80, 560), mod["focus"], fill=TEXT_MUTED, font=f_body_md)

    # Rodapé de specs
    sy = 780
    draw.line([(80, sy - 20), (800, sy - 20)], fill=(255, 255, 255, 25), width=1)
    draw.text((80, sy), "RESPOSTA", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((80, sy + 25), mod["speed"], fill=TEXT_WHITE, font=f_body_bold)

    draw.text((320, sy), "OPERAÇÃO", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((320, sy + 25), mod["clicks"], fill=TEXT_WHITE, font=f_body_bold)

    draw.text((540, sy), "ARQUITETURA", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((540, sy + 25), mod["architecture"], fill=TEXT_WHITE, font=f_body_bold)

    # Mockup à direita
    mx = 950
    my = 220
    mw = 870
    mh = 640
    draw.rounded_rectangle([mx, my, mx + mw, my + mh], radius=14, fill=(11, 14, 20), outline=BORDER_DARK)

    # Header do mockup
    draw.line([(mx, my + 60), (mx + mw, my + 60)], fill=BORDER_DARK, width=1)
    draw.text((mx + 30, my + 20), mod["name"][0].capitalize(), fill=TEXT_WHITE, font=f_body_bold)
    draw.text((mx + mw - 200, my + 24), "Administrador Master", fill=TEXT_SUB, font=f_mono_xs)

    # Grid de blocos dentro do mockup
    gx = mx + 30
    gy = my + 90
    gw = 810

    # Big Block (col-span-2)
    is_light = mod["tone"] == "light"
    draw.rounded_rectangle([gx, gy, gx + 520, gy + 170], radius=8, fill=c_rgb)
    draw.text((gx + 25, gy + 20), "STATUS: ATIVO / ONLINE", fill=(71, 85, 105) if is_light else (255, 255, 255, 180), font=f_mono_xs)
    draw.text((gx + 25, gy + 110), mod["name"][0].capitalize(), fill=(15, 23, 42) if is_light else WHITE, font=f_h3)

    # Velocidade
    draw.rounded_rectangle([gx + 540, gy, gx + gw, gy + 170], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((gx + 565, gy + 25), "VELOCIDADE", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + 565, gy + 90), mod["speed"], fill=WHITE, font=f_h2_bold)

    # Linha 2
    gy2 = gy + 190
    draw.rounded_rectangle([gx, gy2, gx + 250, gy2 + 130], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((gx + 20, gy2 + 20), mod["metrics"][0][0][:20], fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + 20, gy2 + 70), mod["metrics"][0][1], fill=WHITE, font=f_body_bold)

    draw.rounded_rectangle([gx + 270, gy2, gx + 520, gy2 + 130], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((gx + 290, gy2 + 20), mod["metrics"][1][0][:20], fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + 290, gy2 + 70), mod["metrics"][1][1], fill=WHITE, font=f_body_bold)

    draw.rounded_rectangle([gx + 540, gy2, gx + gw, gy2 + 130], radius=8, fill=BLUE)
    draw.text((gx + 640, gy2 + 40), "+", fill=WHITE, font=f_h2_bold)
    draw.text((gx + 630, gy2 + 90), "Novo", fill=WHITE, font=f_body_bold)

    # Linha 3
    gy3 = gy2 + 150
    draw.rounded_rectangle([gx, gy3, gx + 520, gy3 + 140], radius=8, fill=GRAY)
    draw.text((gx + 25, gy3 + 20), mod["badge"], fill=(255, 255, 255, 180), font=f_mono_xs)
    draw.text((gx + 25, gy3 + 60), mod["architecture"], fill=WHITE, font=f_body_bold)
    draw.text((gx + 25, gy3 + 95), "Arquitetura", fill=(255, 255, 255, 180), font=f_mono_xs)

    draw.rounded_rectangle([gx + 540, gy3, gx + gw, gy3 + 140], radius=8, fill=WHITE)
    draw.text((gx + 565, gy3 + 25), "OPERAÇÃO", fill=TEXT_SUB, font=f_mono_xs)
    draw.text((gx + 565, gy3 + 70), mod["clicks"], fill=(15, 23, 42), font=f_h2_bold)

    draw_footer(draw, page_num, mod["name"][0] + " " + mod["name"][1])
    return img.convert('RGB')

# ----------------- MODULE SPEC SHEET (EVEN PAGES: 5, 7, 9, 11, 13, 15) -----------------
def make_module_spec(mod, page_num):
    img = Image.new('RGBA', (W, H), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_logo(draw, 80, 60)
    draw.text((W - 250, 68), "FICHA TÉCNICA", fill=BLUE, font=f_mono_xs)

    draw.text((80, 150), "FICHA TÉCNICA", fill=BLUE, font=f_mono_sm)
    draw.text((80, 190), mod["name"][0] + " " + mod["name"][1], fill=TEXT_WHITE, font=f_h2_bold)

    # 3 Colunas: 80 a 620 | 660 a 1220 | 1260 a 1840
    c_hex = mod["color"]
    c_rgb = BLUE if c_hex == "#0066D6" else GREEN if c_hex == "#70B31C" else GRAY if c_hex == "#5C6470" else WHITE
    is_light = mod["tone"] == "light"

    # Coluna 1: Claims & Recomendacao
    x1 = 80
    y_top = 280
    draw.text((x1, y_top), "DIFERENCIAIS ESTRUTURAIS", fill=TEXT_SUB, font=f_mono_xs)
    cy = y_top + 45
    for ci, c in enumerate(mod["claims"]):
        draw.text((x1, cy), f"0{ci+1}", fill=BLUE, font=f_mono_sm)
        # Quebrar texto do claim
        draw.text((x1 + 45, cy), c[:45], fill=TEXT_WHITE, font=f_body_md)
        if len(c) > 45:
            draw.text((x1 + 45, cy + 25), c[45:], fill=TEXT_WHITE, font=f_body_md)
        cy += 80

    # Box Recomendação
    ry = 640
    draw.rounded_rectangle([x1, ry, x1 + 520, ry + 260], radius=8, fill=c_rgb)
    draw.text((x1 + 25, ry + 25), "RECOMENDAÇÃO DE IMPLANTAÇÃO", fill=(71, 85, 105) if is_light else (255, 255, 255, 180), font=f_mono_xs)
    rec_text = mod["recommendation"]
    draw.text((x1 + 25, ry + 80), rec_text[:40], fill=(15, 23, 42) if is_light else WHITE, font=f_body_bold)
    draw.text((x1 + 25, ry + 115), rec_text[40:85], fill=(15, 23, 42) if is_light else WHITE, font=f_body_bold)
    if len(rec_text) > 85:
        draw.text((x1 + 25, ry + 150), rec_text[85:], fill=(15, 23, 42) if is_light else WHITE, font=f_body_bold)

    # Divisória vertical
    draw.line([(640, 260), (640, 920)], fill=(255, 255, 255, 15), width=1)

    # Coluna 2: Funcionalidades & Specs
    x2 = 680
    draw.text((x2, y_top), "FUNCIONALIDADES CHAVE", fill=TEXT_SUB, font=f_mono_xs)
    fy = y_top + 40
    for f in mod["features"]:
        draw.text((x2, fy), f"•  {f}", fill=TEXT_WHITE, font=f_body_sm)
        draw.line([(x2, fy + 28), (x2 + 520, fy + 28)], fill=(255, 255, 255, 15), width=1)
        fy += 45

    # 4 mini boxes de infraestrutura
    by2 = 620
    specs_list = [
        ("STACK", mod["specs"]["stack"]),
        ("SEGURANÇA", mod["specs"]["security"]),
        ("SINCRONIZAÇÃO", mod["specs"]["sync"]),
        ("EXPORTAÇÃO", mod["specs"]["export"]),
    ]
    for bi, (sk, sv) in enumerate(specs_list):
        bx = x2 + (bi % 2) * 270
        by_s = by2 + (bi // 2) * 135
        draw.rounded_rectangle([bx, by_s, bx + 250, by_s + 115], radius=6, fill=CARD_DARK, outline=BORDER_DARK)
        draw.text((bx + 15, by_s + 15), sk, fill=TEXT_SUB, font=f_mono_xs)
        draw.text((bx + 15, by_s + 55), sv[:25], fill=TEXT_WHITE, font=f_body_sm)
        if len(sv) > 25:
            draw.text((bx + 15, by_s + 78), sv[25:], fill=TEXT_MUTED, font=f_body_xs)

    # Divisória vertical
    draw.line([(1250, 260), (1250, 920)], fill=(255, 255, 255, 15), width=1)

    # Coluna 3: Indicadores de Performance
    x3 = 1290
    draw.text((x3, y_top), "INDICADORES DE PERFORMANCE", fill=TEXT_SUB, font=f_mono_xs)
    my = y_top + 50
    for m in mod["metrics"]:
        draw.text((x3, my), m[0][:32], fill=TEXT_MUTED, font=f_body_sm)
        draw.text((x3 + 450, my), m[1], fill=WHITE, font=f_body_bold)
        # Barra de progresso
        draw.rounded_rectangle([x3, my + 30, x3 + 550, my + 40], radius=4, fill=CARD_DARK)
        pct_val = int(m[2].replace('%', '').strip()) if '%' in m[2] else 85
        fill_w = int(550 * (pct_val / 100.0))
        draw.rounded_rectangle([x3, my + 30, x3 + fill_w, my + 40], radius=4, fill=c_rgb)
        my += 75

    # Box de auditoria
    draw.rounded_rectangle([x3, 760, x3 + 550, 880], radius=8, fill=CARD_DARK, outline=BORDER_DARK)
    draw.text((x3 + 25, 785), "AUDITORIA DE ENGENHARIA", fill=BLUE, font=f_mono_xs)
    draw.text((x3 + 25, 820), "Métricas validadas em produção contínua com", fill=TEXT_MUTED, font=f_body_sm)
    draw.text((x3 + 25, 845), "criptografia de nível militar ponta a ponta.", fill=TEXT_MUTED, font=f_body_sm)

    draw_footer(draw, page_num, mod["name"][0] + " " + mod["name"][1] + " · FICHA TÉCNICA")
    return img.convert('RGB')

# ----------------- PAGE 16: CLOSING -----------------
def make_page_16():
    img = Image.new('RGBA', (W, H), BG_DARK)
    if cover_img:
        # Opacidade 20%
        tint = Image.new('RGBA', (W, H), (10, 13, 20, 210))
        c_layer = cover_img.copy()
        c_layer.alpha_composite(tint)
        img.paste(c_layer, (0, 0))

    draw = ImageDraw.Draw(img)
    draw_logo(draw, W // 2 - 140, 240)

    draw.text((W // 2 - 380, 360), "Seu negócio inteiro,", fill=TEXT_WHITE, font=f_title_thin)
    draw.text((W // 2 - 380, 435), "em um só painel.", fill=TEXT_WHITE, font=f_title_hero)

    draw.text((W // 2 - 380, 560), "Solicite uma demonstração ao vivo e conheça o Sistema 0 em funcionamento.", fill=TEXT_MUTED, font=f_body_lg)

    # Botões
    btn_y = 660
    draw.rounded_rectangle([W // 2 - 260, btn_y, W // 2 - 30, btn_y + 60], radius=6, fill=WHITE)
    draw.text((W // 2 - 180, btn_y + 18), "Entrar", fill=(15, 23, 42), font=f_body_bold)

    draw.rounded_rectangle([W // 2 + 10, btn_y, W // 2 + 280, btn_y + 60], radius=6, fill=(0, 0, 0, 120), outline=WHITE)
    draw.text((W // 2 + 40, btn_y + 18), "Agendar demonstração", fill=WHITE, font=f_body_bold)

    draw.text((W // 2 - 180, 840), "contato@sistema-zero.com.br · WhatsApp Comercial", fill=TEXT_SUB, font=f_body_sm)
    draw.text((W // 2 - 210, 875), "© 2026 SISTEMA ZERO · TODOS OS DIREITOS RESERVADOS", fill=TEXT_SUB, font=f_mono_xs)

    draw_footer(draw, 16, "ENCERRAMENTO")
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
    pages.append(make_module_hero(mod, i, p_hero))
    pages.append(make_module_spec(mod, p_spec))

print("Gerando Pág 16: Encerramento...")
pages.append(make_page_16())

out_pdf = "docs/CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf"
out_pdf_brain = r"C:\Users\Rodrigo\.gemini\antigravity\brain\7de99eeb-9e40-46d6-883f-9a2dce0516dc\CATALOGO_SISTEMA_ZERO_16_PAGINAS.pdf"

print(f"Compilando PDF de 16 páginas em {out_pdf}...")
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
