from math import pi, sqrt

import numpy as np
from scipy.special import fresnel

from pyx import canvas, color, deco, graph, style, text, unit
from pyx.graph import graphxy, data, axis
from pyx.graph.axis import painter, tick

xrange = 12
lineproperties = [graph.style.line([style.linestyle.solid,
                                    style.linewidth.thick,
                                    style.linejoin.round,
                                    color.rgb(0.2, 0, 0.8)])]

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,lining,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)

c = canvas.canvas()

painter_x = painter.regular(basepathattrs=[deco.earrow],
                            titlepos=1, titledist=-0.35,
                            titleattrs=[text.halign.right])

painter_y = painter.regular(basepathattrs=[deco.earrow],
                            titlepos=1.03, titledist=0.15,
                            titleattrs=[text.valign.top], titledirection=None)

g1 = c.insert(
         graphxy(width=5, height=2, xaxisat=0, yaxisat=0,
                 x=axis.linear(title="$x$", min=0, max=xrange,
                               painter=painter_x, parter=None),
                 y=axis.linear(title=r"$I(x)$", max=1.2,
                               painter=painter_y, parter=None)
                 )
     )

x2 = np.linspace(0, (0.93*xrange)**2, 800)
factor = sqrt(0.5*pi)
_, integral = fresnel(np.sqrt(x2)/factor)
integral = factor*integral
g1.plot(data.points(list(zip(np.sqrt(x2), integral)), x=1, y=2),
        lineproperties)

g2 = c.insert(
         graphxy(xpos=g1.xpos-g1.width, ypos=g1.ypos+g1.height+0.5,
                 width=10, height=2, xaxisat=0, yaxisat=0,
                 x=axis.linear(title="$x$", min=-xrange, max=xrange,
                               painter=painter_x, parter=None),
                 y=axis.linear(title=r"$f(x)$", min=-1.1, max=2,
                               painter=painter_y, parter=None)
                 )
     )

phase = np.cos(x2)
for sign in (-1, 1):
    g2.plot(data.points(list(zip(sign*np.sqrt(x2), phase)), x=1, y=2),
            lineproperties)

g3 = c.insert(
         graphxy(xpos=g2.xpos, ypos=g2.ypos+g2.height+0.5,
                 width=10, height=2, xaxisat=0, yaxisat=0,
                 x=axis.linear(title="$x$", min=-xrange, max=xrange,
                               painter=painter_x, parter=None),
                 y=axis.linear(title=r"$S(x)$", painter=painter_y, parter=None)
                 )
     )

x = np.linspace(-0.95*xrange, 0.95*xrange, 200)
action = x**2
g3.plot(data.points(list(zip(x, action)), x=1, y=2), lineproperties)

c.writePDFfile()
