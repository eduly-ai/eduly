# TexFontTemplates

Qualified name: `manim.utils.tex\_templates.TexFontTemplates`

### *class* TexFontTemplates

Bases: `object`

A collection of TeX templates for the fonts described at [http://jf.burnol.free.fr/showcase.html](http://jf.burnol.free.fr/showcase.html)

These templates are specifically designed to allow you to typeset formulae and mathematics using
different fonts. They are based on the mathastext LaTeX package.

### Examples

Normal usage as a value for the keyword argument tex_template of Tex() and MathTex() mobjects:

```default
``Tex("My TeX code", tex_template=TexFontTemplates.comic_sans)``
```

### Notes

Many of these templates require that specific fonts
are installed on your local machine.
For example, choosing the template TexFontTemplates.comic_sans will
not compile if the Comic Sans Microsoft font is not installed.

To experiment, try to render the TexFontTemplateLibrary example scene:
: `manim path/to/manim/example_scenes/advanced_tex_fonts.py TexFontTemplateLibrary -p -ql`

### Methods

### Attributes

| [`american_typewriter`](#manim.utils.tex_templates.TexFontTemplates.american_typewriter)             | American Typewriter                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [`antykwa`](#manim.utils.tex_templates.TexFontTemplates.antykwa)                                     | Antykwa Półtawskiego (TX Fonts for Greek and math symbols) |
| [`apple_chancery`](#manim.utils.tex_templates.TexFontTemplates.apple_chancery)                       | Apple Chancery                                             |
| [`auriocus_kalligraphicus`](#manim.utils.tex_templates.TexFontTemplates.auriocus_kalligraphicus)     | Auriocus Kalligraphicus (Symbol Greek)                     |
| [`baskervald_adf_fourier`](#manim.utils.tex_templates.TexFontTemplates.baskervald_adf_fourier)       | Baskervald ADF with Fourier                                |
| [`baskerville_it`](#manim.utils.tex_templates.TexFontTemplates.baskerville_it)                       | Baskerville (Italic)                                       |
| [`biolinum`](#manim.utils.tex_templates.TexFontTemplates.biolinum)                                   | Biolinum                                                   |
| [`brushscriptx`](#manim.utils.tex_templates.TexFontTemplates.brushscriptx)                           | BrushScriptX-Italic (PX math and Greek)                    |
| [`chalkboard_se`](#manim.utils.tex_templates.TexFontTemplates.chalkboard_se)                         | Chalkboard SE                                              |
| [`chalkduster`](#manim.utils.tex_templates.TexFontTemplates.chalkduster)                             | Chalkduster                                                |
| [`comfortaa`](#manim.utils.tex_templates.TexFontTemplates.comfortaa)                                 | Comfortaa                                                  |
| [`comic_sans`](#manim.utils.tex_templates.TexFontTemplates.comic_sans)                               | Comic Sans MS                                              |
| [`droid_sans`](#manim.utils.tex_templates.TexFontTemplates.droid_sans)                               | Droid Sans                                                 |
| [`droid_sans_it`](#manim.utils.tex_templates.TexFontTemplates.droid_sans_it)                         | Droid Sans (Italic)                                        |
| [`droid_serif`](#manim.utils.tex_templates.TexFontTemplates.droid_serif)                             | Droid Serif                                                |
| [`droid_serif_px_it`](#manim.utils.tex_templates.TexFontTemplates.droid_serif_px_it)                 | Droid Serif (PX math symbols) (Italic)                     |
| [`ecf_augie`](#manim.utils.tex_templates.TexFontTemplates.ecf_augie)                                 | ECF Augie (Euler Greek)                                    |
| [`ecf_jd`](#manim.utils.tex_templates.TexFontTemplates.ecf_jd)                                       | ECF JD (with TX fonts)                                     |
| [`ecf_skeetch`](#manim.utils.tex_templates.TexFontTemplates.ecf_skeetch)                             | ECF Skeetch (CM Greek)                                     |
| [`ecf_tall_paul`](#manim.utils.tex_templates.TexFontTemplates.ecf_tall_paul)                         | ECF Tall Paul (with Symbol font)                           |
| [`ecf_webster`](#manim.utils.tex_templates.TexFontTemplates.ecf_webster)                             | ECF Webster (with TX fonts)                                |
| [`electrum_adf`](#manim.utils.tex_templates.TexFontTemplates.electrum_adf)                           | Electrum ADF (CM Greek)                                    |
| [`epigrafica`](#manim.utils.tex_templates.TexFontTemplates.epigrafica)                               | Epigrafica                                                 |
| [`fourier_utopia`](#manim.utils.tex_templates.TexFontTemplates.fourier_utopia)                       | Fourier Utopia (Fourier upright Greek)                     |
| [`french_cursive`](#manim.utils.tex_templates.TexFontTemplates.french_cursive)                       | French Cursive (Euler Greek)                               |
| [`gfs_bodoni`](#manim.utils.tex_templates.TexFontTemplates.gfs_bodoni)                               | GFS Bodoni                                                 |
| [`gfs_didot`](#manim.utils.tex_templates.TexFontTemplates.gfs_didot)                                 | GFS Didot (Italic)                                         |
| [`gfs_neoHellenic`](#manim.utils.tex_templates.TexFontTemplates.gfs_neoHellenic)                     | GFS NeoHellenic                                            |
| [`gnu_freesans_tx`](#manim.utils.tex_templates.TexFontTemplates.gnu_freesans_tx)                     | GNU FreeSerif (and TX fonts symbols)                       |
| [`gnu_freeserif_freesans`](#manim.utils.tex_templates.TexFontTemplates.gnu_freeserif_freesans)       | GNU FreeSerif and FreeSans                                 |
| [`helvetica_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.helvetica_fourier_it)           | Helvetica with Fourier (Italic)                            |
| [`latin_modern_tw`](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw)                     | Latin Modern Typewriter Proportional                       |
| [`latin_modern_tw_it`](#manim.utils.tex_templates.TexFontTemplates.latin_modern_tw_it)               | Latin Modern Typewriter Proportional (CM Greek) (Italic)   |
| [`libertine`](#manim.utils.tex_templates.TexFontTemplates.libertine)                                 | Libertine                                                  |
| [`libris_adf_fourier`](#manim.utils.tex_templates.TexFontTemplates.libris_adf_fourier)               | Libris ADF with Fourier                                    |
| [`minion_pro_myriad_pro`](#manim.utils.tex_templates.TexFontTemplates.minion_pro_myriad_pro)         | Minion Pro and Myriad Pro (and TX fonts symbols)           |
| [`minion_pro_tx`](#manim.utils.tex_templates.TexFontTemplates.minion_pro_tx)                         | Minion Pro (and TX fonts symbols)                          |
| [`new_century_schoolbook`](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook)       | New Century Schoolbook (Symbol Greek)                      |
| [`new_century_schoolbook_px`](#manim.utils.tex_templates.TexFontTemplates.new_century_schoolbook_px) | New Century Schoolbook (Symbol Greek, PX math symbols)     |
| [`noteworthy_light`](#manim.utils.tex_templates.TexFontTemplates.noteworthy_light)                   | Noteworthy Light                                           |
| [`palatino`](#manim.utils.tex_templates.TexFontTemplates.palatino)                                   | Palatino (Symbol Greek)                                    |
| [`papyrus`](#manim.utils.tex_templates.TexFontTemplates.papyrus)                                     | Papyrus                                                    |
| [`romande_adf_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.romande_adf_fourier_it)       | Romande ADF with Fourier (Italic)                          |
| [`slitex`](#manim.utils.tex_templates.TexFontTemplates.slitex)                                       | SliTeX (Euler Greek)                                       |
| [`times_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.times_fourier_it)                   | Times with Fourier (Italic)                                |
| [`urw_avant_garde`](#manim.utils.tex_templates.TexFontTemplates.urw_avant_garde)                     | URW Avant Garde (Symbol Greek)                             |
| [`urw_zapf_chancery`](#manim.utils.tex_templates.TexFontTemplates.urw_zapf_chancery)                 | URW Zapf Chancery (CM Greek)                               |
| [`venturis_adf_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.venturis_adf_fourier_it)     | Venturis ADF with Fourier (Italic)                         |
| [`verdana_it`](#manim.utils.tex_templates.TexFontTemplates.verdana_it)                               | Verdana (Italic)                                           |
| [`vollkorn`](#manim.utils.tex_templates.TexFontTemplates.vollkorn)                                   | Vollkorn (TX fonts for Greek and math symbols)             |
| [`vollkorn_fourier_it`](#manim.utils.tex_templates.TexFontTemplates.vollkorn_fourier_it)             | Vollkorn with Fourier (Italic)                             |
| [`zapf_chancery`](#manim.utils.tex_templates.TexFontTemplates.zapf_chancery)                         | Zapf Chancery                                              |

#### american_typewriter *= TexTemplate(_body='', tex_compiler='xelatex', description='American Typewriter', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{American Typewriter}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

American Typewriter

#### antykwa *= TexTemplate(_body='', tex_compiler='latex', description='Antykwa Półtawskiego (TX Fonts for Greek and math symbols)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[OT4,OT1]{fontenc}\\n\\\\usepackage{txfonts}\\n\\\\usepackage[upright]{txgreeks}\\n\\\\usepackage{antpolt}\\n\\\\usepackage[defaultmathsizes,nolessnomore]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Antykwa Półtawskiego (TX Fonts for Greek and math symbols)

#### apple_chancery *= TexTemplate(_body='', tex_compiler='xelatex', description='Apple Chancery', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Apple Chancery}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Apple Chancery

#### auriocus_kalligraphicus *= TexTemplate(_body='', tex_compiler='latex', description='Auriocus Kalligraphicus (Symbol Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{aurical}\\n\\\\renewcommand{\\\\rmdefault}{AuriocusKalligraphicus}\\n\\\\usepackage[symbolgreek]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Auriocus Kalligraphicus (Symbol Greek)

#### baskervald_adf_fourier *= TexTemplate(_body='', tex_compiler='latex', description='Baskervald ADF with Fourier', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[upright]{fourier}\\n\\\\usepackage{baskervald}\\n\\\\usepackage[defaultmathsizes,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Baskervald ADF with Fourier

#### baskerville_it *= TexTemplate(_body='', tex_compiler='xelatex', description='Baskerville (Italic)', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Baskerville}\\n\\\\usepackage[defaultmathsizes,italic]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Baskerville (Italic)

#### biolinum *= TexTemplate(_body='', tex_compiler='latex', description='Biolinum', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{libertine}\\n\\\\renewcommand{\\\\familydefault}{\\\\sfdefault}\\n\\\\usepackage[greek=n,biolinum]{libgreek}\\n\\\\usepackage[noasterisk,defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Biolinum

#### brushscriptx *= TexTemplate(_body='', tex_compiler='xelatex', description='BrushScriptX-Italic (PX math and Greek)', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{pxfonts}\\n%\\\\usepackage{pbsi}\\n\\\\renewcommand{\\\\rmdefault}{pbsi}\\n\\\\renewcommand{\\\\mddefault}{xl}\\n\\\\renewcommand{\\\\bfdefault}{xl}\\n\\\\usepackage[defaultmathsizes,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='\\\\boldmath\\n')*

BrushScriptX-Italic (PX math and Greek)

#### chalkboard_se *= TexTemplate(_body='', tex_compiler='xelatex', description='Chalkboard SE', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Chalkboard SE}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Chalkboard SE

#### chalkduster *= TexTemplate(_body='', tex_compiler='lualatex', description='Chalkduster', output_format='.pdf', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Chalkduster}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Chalkduster

#### comfortaa *= TexTemplate(_body='', tex_compiler='latex', description='Comfortaa', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[default]{comfortaa}\\n\\\\usepackage[LGRgreek,defaultmathsizes,noasterisk]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n\\\\linespread{1.06}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Comfortaa

#### comic_sans *= TexTemplate(_body='', tex_compiler='xelatex', description='Comic Sans MS', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Comic Sans MS}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Comic Sans MS

#### droid_sans *= TexTemplate(_body='', tex_compiler='latex', description='Droid Sans', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[default]{droidsans}\\n\\\\usepackage[LGRgreek]{mathastext}\\n\\\\let\\\\varepsilon\\\\epsilon\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Droid Sans

#### droid_sans_it *= TexTemplate(_body='', tex_compiler='latex', description='Droid Sans (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[default]{droidsans}\\n\\\\usepackage[LGRgreek,defaultmathsizes,italic]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Droid Sans (Italic)

#### droid_serif *= TexTemplate(_body='', tex_compiler='latex', description='Droid Serif', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[default]{droidserif}\\n\\\\usepackage[LGRgreek]{mathastext}\\n\\\\let\\\\varepsilon\\\\epsilon\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Droid Serif

#### droid_serif_px_it *= TexTemplate(_body='', tex_compiler='latex', description='Droid Serif (PX math symbols) (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{pxfonts}\\n\\\\usepackage[default]{droidserif}\\n\\\\usepackage[LGRgreek,defaultmathsizes,italic,basic]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Droid Serif (PX math symbols) (Italic)

#### ecf_augie *= TexTemplate(_body='', tex_compiler='latex', description='ECF Augie (Euler Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\renewcommand\\\\familydefault{fau} % emerald package\\n\\\\usepackage[defaultmathsizes,eulergreek]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

ECF Augie (Euler Greek)

#### ecf_jd *= TexTemplate(_body='', tex_compiler='latex', description='ECF JD (with TX fonts)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{txfonts}\\n\\\\usepackage[upright]{txgreeks}\\n\\\\renewcommand\\\\familydefault{fjd} % emerald package\\n\\\\usepackage{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='\\\\mathversion{bold}\\n')*

ECF JD (with TX fonts)

#### ecf_skeetch *= TexTemplate(_body='', tex_compiler='latex', description='ECF Skeetch (CM Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[T1]{fontenc}\\n\\\\DeclareFontFamily{T1}{fsk}{}\\n\\\\DeclareFontShape{T1}{fsk}{m}{n}{<->s\*[1.315] fskmw8t}{}\\n\\\\renewcommand\\\\rmdefault{fsk}\\n\\\\usepackage[noendash,defaultmathsizes,nohbar,defaultimath]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

ECF Skeetch (CM Greek)

#### ecf_tall_paul *= TexTemplate(_body='', tex_compiler='latex', description='ECF Tall Paul (with Symbol font)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\DeclareFontFamily{T1}{ftp}{}\\n\\\\DeclareFontShape{T1}{ftp}{m}{n}{\\n    <->s\*[1.4] ftpmw8t\\n}{} % increase size by factor 1.4\\n\\\\renewcommand\\\\familydefault{ftp} % emerald package\\n\\\\usepackage[symbol]{mathastext}\\n\\\\let\\\\infty\\\\inftypsy\\n', placeholder_text='YourTextHere', post_doc_commands='')*

ECF Tall Paul (with Symbol font)

#### ecf_webster *= TexTemplate(_body='', tex_compiler='latex', description='ECF Webster (with TX fonts)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{txfonts}\\n\\\\usepackage[upright]{txgreeks}\\n\\\\renewcommand\\\\familydefault{fwb} % emerald package\\n\\\\usepackage{mathastext}\\n\\\\renewcommand{\\\\int}{\\\\intop\\\\limits}\\n\\\\linespread{1.5}\\n', placeholder_text='YourTextHere', post_doc_commands='\\n\\\\mathversion{bold}\\n')*

ECF Webster (with TX fonts)

#### electrum_adf *= TexTemplate(_body='', tex_compiler='latex', description='Electrum ADF (CM Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[LGRgreek,basic,defaultmathsizes]{mathastext}\\n\\\\usepackage[lf]{electrum}\\n\\\\Mathastext\\n\\\\let\\\\varphi\\\\phi\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Electrum ADF (CM Greek)

#### epigrafica *= TexTemplate(_body='', tex_compiler='latex', description='Epigrafica', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[LGR,OT1]{fontenc}\\n\\\\usepackage{epigrafica}\\n\\\\usepackage[basic,LGRgreek,defaultmathsizes]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n\\\\linespread{1.2}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Epigrafica

#### fourier_utopia *= TexTemplate(_body='', tex_compiler='latex', description='Fourier Utopia (Fourier upright Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[upright]{fourier}\\n\\\\usepackage{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Fourier Utopia (Fourier upright Greek)

#### french_cursive *= TexTemplate(_body='', tex_compiler='latex', description='French Cursive (Euler Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[default]{frcursive}\\n\\\\usepackage[eulergreek,noplusnominus,noequal,nohbar,%\\nnolessnomore,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

French Cursive (Euler Greek)

#### gfs_bodoni *= TexTemplate(_body='', tex_compiler='latex', description='GFS Bodoni', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\renewcommand{\\\\rmdefault}{bodoni}\\n\\\\usepackage[LGRgreek]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n\\\\linespread{1.06}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

GFS Bodoni

#### gfs_didot *= TexTemplate(_body='', tex_compiler='latex', description='GFS Didot (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\renewcommand\\\\rmdefault{udidot}\\n\\\\usepackage[LGRgreek,defaultmathsizes,italic]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n', placeholder_text='YourTextHere', post_doc_commands='')*

GFS Didot (Italic)

#### gfs_neoHellenic *= TexTemplate(_body='', tex_compiler='latex', description='GFS NeoHellenic', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\renewcommand{\\\\rmdefault}{neohellenic}\\n\\\\usepackage[LGRgreek]{mathastext}\\n\\\\let\\\\varphi\\\\phi\\n\\\\linespread{1.06}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

GFS NeoHellenic

#### gnu_freesans_tx *= TexTemplate(_body='', tex_compiler='xelatex', description='GNU FreeSerif (and TX fonts symbols)', output_format='.pdf', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\usepackage{txfonts}  %\\\\let\\\\mathbb=\\\\varmathbb\\n\\\\setmainfont[ExternalLocation,\\n                Mapping=tex-text,\\n                BoldFont=FreeSerifBold,\\n                ItalicFont=FreeSerifItalic,\\n                BoldItalicFont=FreeSerifBoldItalic]{FreeSerif}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

GNU FreeSerif (and TX fonts symbols)

#### gnu_freeserif_freesans *= TexTemplate(_body='', tex_compiler='xelatex', description='GNU FreeSerif and FreeSans', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble="\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[ExternalLocation,\\n                Mapping=tex-text,\\n                BoldFont=FreeSerifBold,\\n                ItalicFont=FreeSerifItalic,\\n                BoldItalicFont=FreeSerifBoldItalic]{FreeSerif}\\n\\\\setsansfont[ExternalLocation,\\n                Mapping=tex-text,\\n                BoldFont=FreeSansBold,\\n                ItalicFont=FreeSansOblique,\\n                BoldItalicFont=FreeSansBoldOblique,\\n                Scale=MatchLowercase]{FreeSans}\\n\\\\renewcommand{\\\\familydefault}{lmss}\\n\\\\usepackage[LGRgreek,defaultmathsizes,noasterisk]{mathastext}\\n\\\\renewcommand{\\\\familydefault}{\\\\sfdefault}\\n\\\\Mathastext\\n\\\\let\\\\varphi\\\\phi % no \`var' phi in LGR encoding\\n\\\\renewcommand{\\\\familydefault}{\\\\rmdefault}\\n", placeholder_text='YourTextHere', post_doc_commands='')*

GNU FreeSerif and FreeSans

#### helvetica_fourier_it *= TexTemplate(_body='', tex_compiler='latex', description='Helvetica with Fourier (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[scaled]{helvet}\\n\\\\usepackage{fourier}\\n\\\\renewcommand{\\\\rmdefault}{phv}\\n\\\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Helvetica with Fourier (Italic)

#### latin_modern_tw *= TexTemplate(_body='', tex_compiler='latex', description='Latin Modern Typewriter Proportional', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[variablett]{lmodern}\\n\\\\renewcommand{\\\\rmdefault}{\\\\ttdefault}\\n\\\\usepackage[LGRgreek]{mathastext}\\n\\\\MTgreekfont{lmtt} % no lgr lmvtt, so use lgr lmtt\\n\\\\Mathastext\\n\\\\let\\\\varepsilon\\\\epsilon % only \\\\varsigma in LGR\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Latin Modern Typewriter Proportional

#### latin_modern_tw_it *= TexTemplate(_body='', tex_compiler='latex', description='Latin Modern Typewriter Proportional (CM Greek) (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[variablett,nomath]{lmodern}\\n\\\\renewcommand{\\\\familydefault}{\\\\ttdefault}\\n\\\\usepackage[frenchmath]{mathastext}\\n\\\\linespread{1.08}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Latin Modern Typewriter Proportional (CM Greek) (Italic)

#### libertine *= TexTemplate(_body='', tex_compiler='latex', description='Libertine', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{libertine}\\n\\\\usepackage[greek=n]{libgreek}\\n\\\\usepackage[noasterisk,defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Libertine

#### libris_adf_fourier *= TexTemplate(_body='', tex_compiler='latex', description='Libris ADF with Fourier', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage[upright]{fourier}\\n\\\\usepackage{libris}\\n\\\\renewcommand{\\\\familydefault}{\\\\sfdefault}\\n\\\\usepackage[noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Libris ADF with Fourier

#### minion_pro_myriad_pro *= TexTemplate(_body='', tex_compiler='xelatex', description='Minion Pro and Myriad Pro (and TX fonts symbols)', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{txfonts}\\n\\\\usepackage[upright]{txgreeks}\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Minion Pro}\\n\\\\setsansfont[Mapping=tex-text,Scale=MatchUppercase]{Myriad Pro}\\n\\\\renewcommand\\\\familydefault\\\\sfdefault\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n\\\\renewcommand\\\\familydefault\\\\rmdefault\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Minion Pro and Myriad Pro (and TX fonts symbols)

#### minion_pro_tx *= TexTemplate(_body='', tex_compiler='xelatex', description='Minion Pro (and TX fonts symbols)', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{txfonts}\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Minion Pro}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Minion Pro (and TX fonts symbols)

#### new_century_schoolbook *= TexTemplate(_body='', tex_compiler='latex', description='New Century Schoolbook (Symbol Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{newcent}\\n\\\\usepackage[symbolgreek]{mathastext}\\n\\\\linespread{1.1}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

New Century Schoolbook (Symbol Greek)

#### new_century_schoolbook_px *= TexTemplate(_body='', tex_compiler='latex', description='New Century Schoolbook (Symbol Greek, PX math symbols)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{pxfonts}\\n\\\\usepackage{newcent}\\n\\\\usepackage[symbolgreek,defaultmathsizes]{mathastext}\\n\\\\linespread{1.06}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

New Century Schoolbook (Symbol Greek, PX math symbols)

#### noteworthy_light *= TexTemplate(_body='', tex_compiler='latex', description='Noteworthy Light', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Noteworthy Light}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Noteworthy Light

#### palatino *= TexTemplate(_body='', tex_compiler='latex', description='Palatino (Symbol Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{palatino}\\n\\\\usepackage[symbolmax,defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Palatino (Symbol Greek)

#### papyrus *= TexTemplate(_body='', tex_compiler='xelatex', description='Papyrus', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Papyrus}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Papyrus

#### romande_adf_fourier_it *= TexTemplate(_body='', tex_compiler='latex', description='Romande ADF with Fourier (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{fourier}\\n\\\\usepackage{romande}\\n\\\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\\n\\\\renewcommand{\\\\itshape}{\\\\swashstyle}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Romande ADF with Fourier (Italic)

#### slitex *= TexTemplate(_body='', tex_compiler='latex', description='SliTeX (Euler Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{tpslifonts}\\n\\\\usepackage[eulergreek,defaultmathsizes]{mathastext}\\n\\\\MTEulerScale{1.06}\\n\\\\linespread{1.2}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

SliTeX (Euler Greek)

#### times_fourier_it *= TexTemplate(_body='', tex_compiler='latex', description='Times with Fourier (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{fourier}\\n\\\\renewcommand{\\\\rmdefault}{ptm}\\n\\\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Times with Fourier (Italic)

#### urw_avant_garde *= TexTemplate(_body='', tex_compiler='latex', description='URW Avant Garde (Symbol Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{avant}\\n\\\\renewcommand{\\\\familydefault}{\\\\sfdefault}\\n\\\\usepackage[symbolgreek,defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

URW Avant Garde (Symbol Greek)

#### urw_zapf_chancery *= TexTemplate(_body='', tex_compiler='latex', description='URW Zapf Chancery (CM Greek)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\DeclareFontFamily{T1}{pzc}{}\\n\\\\DeclareFontShape{T1}{pzc}{mb}{it}{<->s\*[1.2] pzcmi8t}{}\\n\\\\DeclareFontShape{T1}{pzc}{m}{it}{<->ssub \* pzc/mb/it}{}\\n\\\\DeclareFontShape{T1}{pzc}{mb}{sl}{<->ssub \* pzc/mb/it}{}\\n\\\\DeclareFontShape{T1}{pzc}{m}{sl}{<->ssub \* pzc/mb/sl}{}\\n\\\\DeclareFontShape{T1}{pzc}{m}{n}{<->ssub \* pzc/mb/it}{}\\n\\\\usepackage{chancery}\\n\\\\usepackage{mathastext}\\n\\\\linespread{1.05}', placeholder_text='YourTextHere', post_doc_commands='\\n\\\\boldmath\\n')*

URW Zapf Chancery (CM Greek)

#### venturis_adf_fourier_it *= TexTemplate(_body='', tex_compiler='latex', description='Venturis ADF with Fourier (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{fourier}\\n\\\\usepackage[lf]{venturis}\\n\\\\usepackage[italic,defaultmathsizes,noasterisk]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Venturis ADF with Fourier (Italic)

#### verdana_it *= TexTemplate(_body='', tex_compiler='xelatex', description='Verdana (Italic)', output_format='.xdv', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[no-math]{fontspec}\\n\\\\setmainfont[Mapping=tex-text]{Verdana}\\n\\\\usepackage[defaultmathsizes,italic]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Verdana (Italic)

#### vollkorn *= TexTemplate(_body='', tex_compiler='latex', description='Vollkorn (TX fonts for Greek and math symbols)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage[T1]{fontenc}\\n\\\\usepackage{txfonts}\\n\\\\usepackage[upright]{txgreeks}\\n\\\\usepackage{vollkorn}\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Vollkorn (TX fonts for Greek and math symbols)

#### vollkorn_fourier_it *= TexTemplate(_body='', tex_compiler='latex', description='Vollkorn with Fourier (Italic)', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\usepackage{fourier}\\n\\\\usepackage{vollkorn}\\n\\\\usepackage[italic,nohbar]{mathastext}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Vollkorn with Fourier (Italic)

#### zapf_chancery *= TexTemplate(_body='', tex_compiler='latex', description='Zapf Chancery', output_format='.dvi', documentclass='\\\\documentclass[preview]{standalone}', preamble='\\n\\\\usepackage[english]{babel}\\n\\\\usepackage{amsmath}\\n\\\\usepackage{amssymb}\\n\\n\\n\\\\DeclareFontFamily{T1}{pzc}{}\\n\\\\DeclareFontShape{T1}{pzc}{mb}{it}{<->s\*[1.2] pzcmi8t}{}\\n\\\\DeclareFontShape{T1}{pzc}{m}{it}{<->ssub \* pzc/mb/it}{}\\n\\\\usepackage{chancery} % = \\\\renewcommand{\\\\rmdefault}{pzc}\\n\\\\renewcommand\\\\shapedefault\\\\itdefault\\n\\\\renewcommand\\\\bfdefault\\\\mddefault\\n\\\\usepackage[defaultmathsizes]{mathastext}\\n\\\\linespread{1.05}\\n', placeholder_text='YourTextHere', post_doc_commands='')*

Zapf Chancery
