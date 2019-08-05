from pyx import canvas, color, deco, path, style, text, unit

width = 5
height = 4
t1 = 2
t2 = 4.5
qi = 1.5
qf = 2.5
lowertick = -0.15

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}
                  \usepackage{nicefrac}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(0, 0, width, 0), [deco.earrow])
c.text(width+0.1, 0, '$t$', [text.valign.middle])
c.stroke(path.line(0, lowertick, 0, height), [deco.earrow])
c.text(0.2, height, '$q$', [text.valign.top])
for t in (t1, t2):
    c.stroke(path.line(t, 0, t, lowertick))
    c.stroke(path.line(t, 0, t, height-0.26), [style.linestyle.dashed])
c.text(t1/2, -0.1, '$t_1$', [text.halign.center, text.valign.top])
c.text(t1+(t2-t1)/2, -0.1, '$t_2$', [text.halign.center, text.valign.top])
qstraight = qi+t1/t2*(qf-qi)
for q in range(-4, 5):
    c.stroke(path.path(path.moveto(0, qi),
                       path.lineto(t1, qstraight+0.4*q),
                       path.lineto(t2, qf)),
             [style.linejoin.round, color.rgb(0.2, 0, 0.8)])
for x, y in ((0, qi), (t2, qf)):
    c.fill(path.circle(x, y, 0.04),
           [color.grey(1), deco.stroked([color.grey(0)])])
c.text(-0.1, qi, r'$q_\text{i}$', [text.halign.right, text.valign.middle])
c.text(t2+0.1, qf, r'$q_\text{f}$', [text.valign.middle])
c.writePDFfile()
