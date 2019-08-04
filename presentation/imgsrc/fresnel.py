from math import sqrt
from pyx import canvas, color, deco, path, style, text, unit

axislen = 3

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}
                  \usepackage{nicefrac}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(-0.2*axislen, 0, axislen, 0), [deco.earrow])
c.text(axislen+0.1, 0, 'Re($x$)', [text.valign.middle])
c.stroke(path.line(0, -0.2*axislen, 0, axislen), [deco.earrow])
c.text(0.2, axislen, 'Im($x$)', [text.valign.top])
r = 0.85*axislen
p = path.path(path.moveto(0, 0),
              path.lineto(r, 0),
              path.arc(0, 0, r, 0, 45),
              path.lineto(0, 0),
              path.closepath())
pathcolor = color.rgb(0.2, 0, 0.8)
c.stroke(p, [style.linewidth.thick, style.linejoin.round, pathcolor])
c.stroke(path.line(0, 0, 0.53*axislen, 0), [deco.earrow, pathcolor])
c.stroke(path.path(path.arc(0, 0, r, 0, 23)), [deco.earrow, pathcolor])
c.stroke(path.path(path.moveto(r/sqrt(2), r/sqrt(2)),
                   path.lineto(0.48*r/sqrt(2), 0.48*r/sqrt(2))),
         [deco.earrow, pathcolor])
c.text(0.33, 0.11, r'\footnotesize$\nicefrac{\pi}{4}$', [pathcolor])
c.stroke(path.path(path.arc(0, 0, 0.82, 0, 45)),
         [style.linewidth.thin, pathcolor])

c.writePDFfile()
