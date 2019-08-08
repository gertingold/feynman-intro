from math import cos, sin, radians

from pyx import canvas, color, path, style, text, trafo, unit


def spiral(radius, angle, n, dphi=5):
    phif = angle+n*360
    npts = abs(phif)//dphi
    if abs(phif) >= 360:
        dr = 0.1*abs(phif)/360
    else:
        dr = 0
    p = path.path(path.moveto(radius-0.5*dr, 0))
    for nphi in range(1, npts+1):
        phi = radians(phif*nphi/npts)
        r = radius-0.5*dr+dr*nphi/npts
        p.append(path.lineto(r*cos(phi), r*sin(phi)))
    return p


def winding(n, radius, angle=60, endpointcolor=color.rgb(0.6, 0.2, 0),
            pathcolor=color.rgb(0.4, 0.3, 0.8)):
    c = canvas.canvas()
    ticklen = 0.1
    c.stroke(path.circle(0, 0, radius), [style.linewidth.Thin])
    tick = path.line((1-ticklen)*radius, 0,
                     (1+ticklen)*radius, 0)
    c.stroke(tick, [endpointcolor, style.linewidth.Thick])
    c.stroke(tick, [trafo.rotate(angle), endpointcolor, style.linewidth.Thick])
    tick_outer = (1+ticklen)*radius
    for _angle, label in ((0, r'$\phi_\text{i}$'),
                          (radians(angle), r'$\phi_\text{f}$')):
        c.text((tick_outer+0.3)*cos(_angle),
               (tick_outer+0.3)*sin(_angle), label,
               [text.halign.center, text.valign.middle, endpointcolor])
    c.text(0, -radius-0.3, f'$n={n}$', [text.halign.center, text.valign.top])
    c.stroke(spiral(radius, angle, n), [pathcolor, style.linewidth.Thick])
    return c


radius = 1.5

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,lining,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)

c = canvas.canvas()
dx = 3.5*radius
dy = 3.5*radius
for nr, n in enumerate((0, -1)):
    c.insert(winding(n, radius), [trafo.translate(nr*dx, 0)])
for nr, n in enumerate((1, -2, 2)):
    c.insert(winding(n, radius), [trafo.translate(nr*dx, -dy)])

c.writePDFfile()
