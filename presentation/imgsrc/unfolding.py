from pyx import canvas, color, deco, path, style, text, unit

boxwidth = 3
height = 4
qi = 0.2*boxwidth
qf = 0.7*boxwidth
linecolor = color.rgb(0.2, 0, 0.8)

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.fill(path.rect(0, 0, boxwidth, height), [color.rgb(0.92, 1, 0.92)])
for n in range(-1, 4):
    c.stroke(path.line(n*boxwidth, 0, n*boxwidth, height),
             [style.linewidth.THick, color.grey(0.4)])
poslinestyle = (style.linestyle.dashed, style.linewidth.thick)
c.stroke(path.line(qi, 0, qi, height),
         [*poslinestyle, color.rgb(0.2, 0.6, 0)])
for n in range(-1, 2):
    q = qf + 2*n*boxwidth
    c.stroke(path.line(q, 0, q, height),
             [*poslinestyle, color.rgb(0.6, 0, 0)])
for n in range(-1, 1):
    q = -qf + (2*n+2)*boxwidth
    c.stroke(path.line(q, 0, q, height),
             [*poslinestyle, color.rgb(0.6, 0, 0)])
for delta in (2*(boxwidth-qf), -2*qf):
    c.stroke(path.curve(qf, -0.1,
                        qf+0.3*delta, -0.5,
                        qf+0.7*delta, -0.5,
                        qf+delta, -0.1),
             [deco.earrow])
for delta in (-4*boxwidth+2*qf, 2*qf):
    c.stroke(path.curve(2*boxwidth-qf, height+0.1,
                        2*boxwidth-qf+0.3*delta, height+0.5,
                        2*boxwidth-qf+0.7*delta, height+0.5,
                        2*boxwidth-qf+delta, height+0.1),
             [deco.earrow])
for n, q in enumerate((qf, -qf, 2*boxwidth-qf, -2*boxwidth+qf,
                       2*boxwidth+qf)):
    ypos = (n+0.5)*height/5
    c.stroke(path.line(qi, ypos, q, ypos),
            [style.linewidth.Thick, color.rgb(0.2, 0, 0.8)])
    c.stroke(path.circle(qi, ypos, 0.06),
             [style.linewidth.thick, linecolor, deco.filled([color.grey(1)])])
    c.stroke(path.circle(q, ypos, 0.06),
             [style.linewidth.thick, linecolor, deco.filled([color.grey(1)])])
c.writePDFfile()
