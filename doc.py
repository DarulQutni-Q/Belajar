# Creating a PDF file with the transcribed table of 20 sifat wajib & mustahil␍
import os␍
from reportlab.lib import colors␍
from reportlab.lib.enums import TA_CENTER, TA_LEFT␍
from reportlab.lib.pagesizes import A4, landscape␍
from reportlab.lib.styles import ParagraphStyle␍
from reportlab.pdfbase import pdfmetrics␍
from reportlab.pdfbase.ttfonts import TTFont␍
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer␍, Table,
                                TableStyle)

␍
# Register a font that supports Arabic and Latin (try DejaVu Sans)␍
font_paths = [␍
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",␍
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",␍
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"␍
]␍
␍
font_registered = False␍
for p in font_paths:␍
    if os.path.exists(p):␍
        try:␍
            pdfmetrics.registerFont(TTFont("CustomSans", p))␍
            font_registered = True␍
            break␍
        except Exception as e:␍
            # try next␍
            pass␍
␍
if not font_registered:␍
    # fallback: use default font␍
    pass␍
␍
# File path␍
out_pdf = "/mnt/data/sifat_wajib_mustahil_table.pdf"␍
␍
# Content (transcription) - same as created in canvas document␍
rows = [␍
    ["No", "Sifat Wajib (Arab / ID)", "Sifat Mustahil (Arab / ID)", "Dalil 'Aqli (ringkas)", "Dalil Naqli (kutipan / rujukan)"],␍
    ["1", "وُجُود — Wujud / Ada", "عَدَم — ‘Adam / Tiada", "Wujud segala makhluk, karena mustahil wujud makhluk dengan sendirinya", "اللَّهُ الَّذِي خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ وَمَا بَيْنَهُمَا  [السجدة : 4]"],␍
    ["2", "قِدَم — Qidam (Terdahulu)", "حُدُوث — Hudūth (Baharu)", "Jikalau Allah baharu maka Allah akan membutuhkan kepada yang membaharukan-Nya, dan yang demikian itu mustahil", "هُوَ الْأَوَّلُ وَالْآخِرُ  [الحديد : 3]"],␍
    ["3", "بَقَاء — Baqā’ (Kekal)", "فَنَاء — Fanā’ (Binasa)", "Jikalau Allah fana maka Allah baharu, dan yang demikian itu mustahil", "وَيَبْقَىٰ وَجْهُ رَبِّكَ ذُو الْجَلَالِ وَالْإِكْرَامِ  [الرحمن : 27]"],␍
    ["4", "مُخَالَفَةُ لِلْحَوَادِث — Berbeda dengan segala yang baharu", "مُمَاثَلَة/مُشَابَهَة — Menyerupai makhluk", "Jikalau Allah menyerupai sesuatu yang baharu maka Allah juga baharu, dan yang demikian itu mustahil", "لَيْسَ كَمِثْلِهِ شَيْءٌ  [الشورى : 11]"],␍
    ["5", "قِيَامُهُ بِـنَفْسِهِ — Qiyāmu-hu bi-nafsihī (Mandiri)", "اِحْتِيَاج — Berhajat kepada yang lain", "Jikalau Allah membutuhkan kepada tempat (zat) maka Allah adalah sifat, dan yang demikian itu mustahil. Dan jikalau Allah membutuhkan kepada yang menciptakan maka Allah itu baharu, dan yang demikian itu juga mustahil", "— (disarankan: QS. Al-Baqarah 2:255 Āyat al-Kursīh)"],␍
    ["6", "وَحْدَانِيَّة — Wahdāniyyah (Esa/Tauhid)", "تَعَدُّد — Ta‘addud (Berbilang)", "Jikalau Allah tidak esa maka tidak akan diperdapati sesuatupun daripada alam ini, dan yang demikian itu mustahil (batil)", "قُلْ هُوَ اللَّهُ أَحَدٌ  [الإخلاص : 1]"],␍
    ["7", "قُدْرَة — Qudrah (Kuasa)", "عَجْز — ‘Ajz (Lemah)", "Jikalau Allah tidak kuasa maka tidak akan diperdapati sesuatu pun daripada makhluk ini, dan yang demikian itu mustahil (batil)", "إِنَّ اللَّهَ عَلَىٰ كُلِّ شَيْءٍ قَدِيرٌ  [umum di Al-Qur'an]"],␍
    ["8", "إِرَادَة — Irādah (Berkehendak)", "كَرْهٌ/إِكْرَاه — Terpaksa", "Jikalau Allah tidak berkehendak maka Allah lemah, dan yang demikian itu mustahil", "إِنَّ رَبَّكَ لَهُ مَا فِي السَّمَاوَاتِ وَالْأَرْضِ  [هود : 107]"],␍
    ["9", "عِلْم — ‘Ilm (Mengetahui)", "جَهْل — Jahl (Bodoh)", "Jikalau Allah tidak mengetahui maka Allah tidak berkehendak, dan yang demikian itu mustahil", "وَاللَّهُ بِكُلِّ شَيْءٍ عَلِيمٌ  [المدثر : 48]"],␍
    ["10", "حَيَاة — Hayāt (Hidup)", "مَوْت — Mawt (Mati)", "Jikalau Allah tidak hidup maka Allah tidak kuasa, tidak berkehendak dan tidak mengetahui, dan yang demikian itu mustahil", "وَمَنْ يَقْتُلِ الْمَلَكُ الَّذِي لَا يَمُوتُ  [الفرقان : 58]"],␍
    ["11", "سَمْع — Samā‘ (Mendengar)", "صَمَم/صَمْت — Ṣamt (Tuli)", "Jikalau Allah tidak mendengar maka Allah akan bersifat dengan tuli yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَاللَّهُ سَمِيعٌ عَلِيمٌ  [المدثر : 24]"],␍
    ["12", "بَصَر — Baṣar (Melihat)", "عَمًى — ‘Amā (Buta)", "Jikalau Allah tidak melihat maka Allah akan bersifat dengan buta yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَاللَّهُ يُبْصِرُ بِمَا تَعْمَلُونَ  [الحجرات : 18]"],␍
    ["13", "كَلَام — Kalām (Berfirman)", "صَمْت تَامّ — Ṣamt Tām (Bisu)", "Jikalau Allah tidak berkalam maka Allah akan bersifat dengan bisu yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا  [النساء : 164]"],␍
    ["14", "مَلِك — Malik (Penguasa)", "عَاجِز — Yang lemah", "Jikalau Allah tidak kuasa maka tidak akan diperdapati sesautupun daripada makhluk ini, dan yang demikian itu mustahil (batil)", "إِنَّ اللَّهَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ  [umum]"],␍
    ["15", "مُرِيد — Murīd (Yang berkehendak)", "مَكْرُوه/مُكْرَه — Yang terpaksa", "Jikalau Allah tidak berkehendak maka Allah lemah, dan yang demikian itu mustahil", "إِنَّ رَبَّكَ سَيَفْعَلُ إِنْ شَاءَ  [هود : 107]"],␍
    ["16", "عَالِم — ‘Ālim (Yang mengetahui)", "جَاهِل — Jahil (Yang bodoh)", "Jikalau Allah tidak mengetahui maka Allah tidak berkehendak, dan yang demikian itu mustahil", "وَاللَّهُ بِكُلِّ شَيْءٍ عَلِيمٌ  [المدثر : 48]"],␍
    ["17", "حَيّ — Ḥayy (Yang hidup)", "مَيِّت — Mayyit (Yang mati)", "Jikalau Allah tidak hidup maka Allah tidak kuasa, tidak berkehendak dan tidak mengetahui, dan yang demikian itu mustahil", "وَمَنْ يَقْتُلِ الْمَلَكُ الَّذِي لَا يَمُوتُ  [الفرقان : 58]"],␍
    ["18", "سَمِيع — Samī‘ (Yang mendengar)", "أَصَمّ — Aṣamm (Yang tuli)", "Jikalau Allah tidak mendengar maka Allah akan bersifat dengan tuli yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَاللَّهُ سَمِيعٌ عَلِيمٌ  [المدثر : 24]"],␍
    ["19", "بَصِير — Baṣīr (Yang melihat)", "أَعْمَى — A‘mā (Yang buta)", "Jikalau Allah tidak melihat maka Allah akan bersifat dengan buta yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَاللَّهُ يُبْصِرُ بِمَا تَعْمَلُونَ  [الحجرات : 18]"],␍
    ["20", "مُتَكَلِّم — Mutakallim (Yang berkata-kata)", "أَكْمَه — Akmah (Yang bisu)", "Jikalau Allah tidak berkalam maka Allah akan bersifat dengan bisu yang merupakan sebuah kekurangan, dan yang demikian itu mustahil", "وَكَلَّمَ اللَّهُ مُوسَى تَكْلِيمًا  [النساء : 164]"]␍
]␍
␍
# Build document␍
doc = SimpleDocTemplate(out_pdf, pagesize=landscape(A4), rightMargin=18, leftMargin=18, topMargin=18, bottomMargin=18)␍
elements = []␍
␍
# Title␍
title_style = ParagraphStyle(name='Title', fontName='CustomSans' if font_registered else 'Helvetica-Bold', fontSize=16, alignment=TA_CENTER)␍
elements.append(Paragraph("Tabel: 20 Sifat Wajib Allah dan Sifat Mustahil — Transkripsi", title_style))␍
elements.append(Spacer(1, 12))␍
␍
# Prepare table data with Paragraph for wrapping␍
body_style = ParagraphStyle(name='Body', fontName='CustomSans' if font_registered else 'Helvetica', fontSize=9, alignment=TA_LEFT, leading=11)␍
table_data = []␍
for r in rows:␍
    table_row = []␍
    for i, cell in enumerate(r):␍
        # Use Paragraph to wrap text␍
        p = Paragraph(cell.replace("\n", "<br/>"), body_style)␍
        table_row.append(p)␍
    table_data.append(table_row)␍
␍
# Create table␍
tbl = Table(table_data, colWidths=[30, 200, 200, 240, 180])␍
tbl_style = TableStyle([␍
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),␍
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),␍
    ('VALIGN', (0,0), (-1,-1), 'TOP'),␍
    ('ALIGN', (0,0), (0,-1), 'CENTER'),␍
    ('ALIGN', (1,0), (-1,0), 'CENTER'),␍
    ('LEFTPADDING', (0,0), (-1,-1), 6),␍
    ('RIGHTPADDING', (0,0), (-1,-1), 6),␍
])␍
tbl.setStyle(tbl_style)␍
␍
elements.append(tbl)␍
␍
# Build PDF␍
doc.build(elements)␍
␍
# Provide download link to user␍
print(f"[Download the PDF](/mnt/data/sifat_wajib_mustahil_table.pdf)")

