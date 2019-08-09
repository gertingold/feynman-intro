from pyx import canvas, color, deco, path, style, text, unit

boxwidth = 3
height = 4
qi = 0.2*boxwidth
qf = 0.7*boxwidth
linecolor1 = color.rgb(0.8, 0, 0)
linecolor2 = color.rgb(0, 0, 0.8)

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.5)
c = canvas.canvas()
c.fill(path.rect(0, 0, boxwidth, height), [color.rgb(0.92, 1, 0.92)])
for n in range(-1, 4):
    c.stroke(path.line(n*boxwidth, 0, n*boxwidth, height),
             [style.linewidth.THick, color.grey(0.4)])
poslinestyle = (style.linestyle.dashed, style.linewidth.Thick)
for n in range(-1, 2):
    q = qf + 2*n*boxwidth
    c.stroke(path.line(q, 0, q, height), [*poslinestyle, linecolor1])
    c.stroke(path.line(q, height+1.1, q, height+1.5), [style.linewidth.thick])
for n in range(-1, 2):
    q = -qf + (2*n+2)*boxwidth
    c.stroke(path.line(q, 0, q, height), [*poslinestyle, linecolor2])
    c.stroke(path.line(q, height+0.1, q, height+0.5), [style.linewidth.thick])
for n in range(0, 2):
    c.stroke(path.line(-qf+2*n*boxwidth, height+0.3,
                       -qf+2*(n+1)*boxwidth, height+0.3),
             [style.linewidth.thick, deco.barrow, deco.earrow])
    c.text(-qf+(1+2*n)*boxwidth, height+0.4, '$2L$',
           [text.halign.center])
    c.stroke(path.line(qf-2*(n-1)*boxwidth, height+1.3,
                       qf-2*n*boxwidth, height+1.3),
             [style.linewidth.thick, deco.barrow, deco.earrow])
    c.text(qf-(2*n-1)*boxwidth, height+1.4, '$2L$',
           [text.halign.center])
c.text(qf, -0.5, r'$q_\text{f}$', [text.halign.center])
c.text(2*boxwidth-qf, -0.5, r'$2L-q_\text{f}$', [text.halign.center])
c.writePDFfile()
