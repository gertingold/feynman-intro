from pyx import canvas, color, deco, path, text, unit

width = 8
height = 2
linecolor = color.rgb(0.2, 0, 0.8)

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(-0.5*width, 0, 0.5*width, 0), [deco.earrow])
c.text(0.5*width+0.1, 0, '$x$', [text.valign.middle])
for n in range(-4, 5, 2):
    c.stroke(path.line(0.1*n*width, 0, 0.1*n*width, height),
             [deco.earrow.small, linecolor])
    if n != 0:
        label = r'${}\pi$'.format(n)
    else:
        label = '$0$'
    c.text(0.1*n*width, -0.2, label, [text.halign.center, text.valign.top])
c.writePDFfile()
