from pyx import canvas, color, deco, path, style, text, trafo, unit

ntraj = 5
radius = 0.1
dy = 0.7
width = 10
height = ntraj*dy + (ntraj//2)**2*2*radius
if ntraj % 2:
    height = height + ntraj//2*2*radius
boxwidth = 0.3
boxcolor = color.grey(0.5)
linecolor = color.rgb(0.2, 0, 0.8)
labelypos = -0.5
qi = 2
qf = 7

text.set(engine=text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.fill(path.rect(0, 0, -boxwidth, height), [boxcolor])
c.stroke(path.line(0, 0, 0, height), [style.linewidth.thick])
c.text(0, labelypos, '$0$', [text.halign.center])
c.fill(path.rect(width, 0, boxwidth, height), [boxcolor])
c.stroke(path.line(width, 0, width, height), [style.linewidth.thick])
c.text(width, labelypos, '$L$', [text.halign.center])
for q, label in ((qi, r'$q_\text{i}$'),
                 (qf, r'$q_\text{f}$')):
    c.stroke(path.line(q, 0, q, height), [style.linestyle.dashed])
    c.text(q, labelypos, label, [text.halign.center])
pathsegments = [path.path(path.moveto(qi, 0),
                          path.lineto(qf, 0)),
                path.path(path.moveto(qf, 0),
                          path.lineto(width-radius, 0),
                          path.arc(width-radius, radius, radius, -90, 90),
                          path.lineto(qf, 2*radius)),
                path.path(path.moveto(qf, 0),
                          path.lineto(qi, 0)),
                path.path(path.moveto(qi, 0),
                          path.lineto(radius, 0),
                          path.arcn(radius, radius, radius, 270, 90),
                          path.lineto(qi, 2*radius))]
anzahl_segmente = (1, 2, 2, 3)
ypos = 0.5*dy
for n in range(1, ntraj+1):
    offset = 0
    if n % 2 == 0:
        offset = -1
    nsegmente = anzahl_segmente[(n-1) % 4] + (n-1)//4*4
    for nsegment in range(1, nsegmente+1):
        yshift = (-offset+nsegment-1)//2*2*radius
        c.stroke(pathsegments[(offset+nsegment-1) % 4],
                 [trafo.translate(0, ypos+yshift),
                  linecolor, style.linewidth.Thick])
    c.stroke(path.circle(qi, ypos, 0.06),
             [style.linewidth.thick, linecolor, deco.filled([color.grey(1)])])
    c.stroke(path.circle(qf, ypos+n//2*2*radius, 0.06),
             [style.linewidth.thick, linecolor, deco.filled([color.grey(1)])])
    ypos = ypos + dy + (n//2)*2*radius
c.writePDFfile()
