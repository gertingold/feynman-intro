from pyx import canvas, color, deco, path, style, text, trafo, unit

width = 8
height = 4
linecolor1 = color.rgb(0.2, 0, 0.8)
linecolor2 = color.rgb(0.8, 0.3, 0)
qi = 1.2
qf = 3.2
t = 3.5

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.fill(path.rect(0, 0, -0.3, height-0.3), [color.grey(0.5)])
c.stroke(path.line(-0.5*width, 0, 0.5*width, 0), [deco.earrow])
c.text(0.5*width+0.1, 0, '$q$', [text.valign.middle])
c.stroke(path.line(0, 0, 0, height), [deco.earrow])
c.text(0.2, height, '$t$', [text.valign.top])
c.stroke(path.path(path.moveto(qi, 0),
                   path.curveto(qi, 0.5, qi+0.2, 1.3, qi+0.8, 1.6),
                   path.curveto(qi+1.4, 1.9, qf+0.7, 3, qf, t)),
         [style.linewidth.thick, linecolor1])
c.stroke(path.path(path.moveto(qi, 0),
                   path.curveto(0.5*qi, 0.5, -2.5, 1.3, 0, 1.6)),
         [style.linewidth.thick, linecolor2])
p = path.path(path.moveto(0, 1.6),
              path.curveto(2.5, 1.9, 3, 3, qf, t))
c.stroke(p, [style.linewidth.thick, linecolor2])
c.stroke(p, [style.linewidth.thick, style.linestyle.dashed,
             linecolor2, trafo.mirror(90)])
ypos = 0
for q, label in ((qi, r'$q_\text{i}$'),
                 (qf, r'$q_\text{f}$'),
                 (-qf, r'$-q_\text{f}$')):
    c.stroke(path.line(q, 0.1, q, -0.1))
    c.text(q, -0.5, label, [text.halign.center])
    c.stroke(path.circle(q, ypos, 0.06),
             [deco.filled([color.grey(1)])])
    ypos = t
c.writePDFfile()
