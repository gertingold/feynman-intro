from random import random, seed
from pyx import canvas, color, deco, path, style, text, unit

width = 6
height = 3
qi = 0.5
qf = 2
tmax = 0.8*width
lowertick = -0.15

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(0, 0, width, 0), [deco.earrow])
c.text(width+0.1, 0, '$t$', [text.valign.middle])
c.stroke(path.line(0, lowertick, 0, height), [deco.earrow])
c.text(0.2, height, '$q$', [text.valign.top])
n = 6
for nt in range(n+1):
    t = nt*tmax/n
    c.stroke(path.line(t, 0, t, lowertick))
    c.stroke(path.line(t, 0, t, height-0.26), [style.linestyle.dashed])
seed(424242)
positions = [(height-0.3)*random() for _ in range(n-1)]
positions.append(qf)
p = path.path(path.moveto(0, qi))
for nt, q in enumerate(positions):
    p.append(path.lineto((nt+1)*tmax/n, q))
c.stroke(p, [style.linejoin.round, color.rgb(0.2, 0, 0.8)])
c.text(0, -0.55, '$0$', [text.halign.center])
c.text(3*tmax/n, -0.55, '$n{-}1$', [text.halign.center])
c.text(4*tmax/n, -0.55, '$n$', [text.halign.center])
c.text(tmax, -0.55, '$N$', [text.halign.center])
for x, y in ((0, qi), (tmax, qf)):
    c.fill(path.circle(x, y, 0.04),
           [color.grey(1), deco.stroked([color.grey(0)])])
c.text(-0.1, qi, r'$q_\text{i}$', [text.halign.right, text.valign.middle])
c.text(tmax+0.1, qf, r'$q_\text{f}$', [text.valign.middle])
c.text(width-0.2, height-0.26, '$N={}$'.format(n), [text.valign.top])
c.writePDFfile()
