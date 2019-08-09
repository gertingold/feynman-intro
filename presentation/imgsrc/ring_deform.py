from pyx import canvas, color, deco, path, style, text, unit

width = 5
height = 4
linecolor1 = color.rgb(0.2, 0.5, 0)
linecolor2 = color.rgb(0.2, 0, 0.8)

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(0, 0, width, 0), [deco.earrow])
c.text(width+0.1, 0, '$t$', [text.valign.middle])
c.stroke(path.line(0, -0.45*height, 0, 0.55*height), [deco.earrow])
c.text(0.2, 0.55*height, '$q$', [text.valign.top])
c.stroke(path.path(path.moveto(0, 0),
                   path.curveto(0.1*width, 0.2*height,
                                0.3*width, -0.4*height,
                                0.4*width, -0.4*height),
                   path.curveto(0.5*width, -0.4*height,
                                0.7*width, 0.7*height,
                                0.9*width, 0.3*height)),
         [linecolor1, style.linewidth.thick, style.linestyle.dashed])
for x, y, label in ((0.9*width, 0.3*height, r'$q_\text{f}$'),
                    (0.9*width, -0.4*height, r'$q_\text{f}-2\pi$'),
                    (0, 0, r'$q_\text{i}$')):
        if x == 0:
            c.text(x-0.15, y, label, [text.halign.right, text.valign.middle])
        else:
            if y > 0:
                linecolor = linecolor1
            else:
                linecolor = linecolor2
            c.text(x+0.15, y, label, [text.valign.middle])
            c.stroke(path.line(0, 0, x, y),
                     [style.linewidth.thick, linecolor])
        c.fill(path.circle(x, y, 0.04),
               [color.grey(1), deco.stroked([color.grey(0)])])
c.writePDFfile()
