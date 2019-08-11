from math import pi
from pyx import canvas, color, deco, graph, path, style, text, unit

trange = 8
linecolor = color.rgb(0.2, 0, 0.8)

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,lining,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}
                  \usepackage{nicefrac}''')
unit.set(vscale=1.1, wscale=1.2, xscale=1.1)

painter_x = graph.axis.painter.regular(basepathattrs=[deco.earrow],
                                       titlepos=1, titledist=-0.4,
                                       titleattrs=[text.halign.right])

painter_y = graph.axis.painter.regular(basepathattrs=[deco.earrow],
                                       titlepos=1.03, titledist=0.15,
                                       titleattrs=[text.valign.top],
                                       titledirection=None)

g = graph.graphxy(width=5, height=2, xaxisat=0, yaxisat=0,
                  x=graph.axis.linear(title="$t$", min=0, max=trange,
                                      painter=painter_x, parter=None),
                  y=graph.axis.linear(title=r"$x$", max=1.2,
                                      painter=painter_y, parter=None)
                  )

for np in range(-3, 4):
    p = 0.2*np
    g.plot(graph.data.function("y(x) = 0.5*cos(x)+{}*sin(x)".format(p),
           max=trange-0.7),
           [graph.style.line([style.linestyle.solid, linecolor])])

textattrs = [text.halign.center]
for ttick, label, ydist in ((pi, r'\pi', 0.2), (2*pi, r'2\pi', -0.2)):
    x, y = g.pos(ttick, 0)
    g.stroke(path.line(x, y-0.1, x, y+0.1))
    g.text(x, y+ydist, r'$\nicefrac{{{}}}{{\omega}}$'.format(label), textattrs)
    textattrs.append(text.valign.top)

g.writePDFfile()
