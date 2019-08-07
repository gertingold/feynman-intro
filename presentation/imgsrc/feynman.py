from pyx import canvas, color, deco, path, style, text, unit

width = 6
height = 3
qi = 0.5
qf = 2
tmax = 0.8*width
lowertick = -0.15
color_cl = color.rgb(0.2, 0, 0.8)
color_fluc = color.rgb(0.2, 0.6, 0)

text.set(text.LatexRunner)
text.preamble(r'''\usepackage[sfdefault,scaled=.85]{FiraSans}
                  \usepackage{newtxsf}
                  \usepackage{nicefrac}''')
unit.set(vscale=1.2, wscale=1.3, xscale=1.3)
c = canvas.canvas()
c.stroke(path.line(0, 0, width, 0), [deco.earrow])
c.text(width+0.1, 0, '$t$', [text.valign.middle])
c.stroke(path.line(0, 0, 0, height), [deco.earrow])
c.text(0.2, height, '$q$', [text.valign.top])
c.stroke(path.curve(0, qi, 0.4*tmax, qi+0.2*(qf-qi),
                    0.5*tmax, 2*qf, tmax, qf), [color_fluc])
c.stroke(path.curve(0, qi, 0.2*tmax, qi+2*(qf-qi),
                    0.7*tmax, 0.5*qf, tmax, qf), [color_fluc])
c.stroke(path.curve(0, qi, 0.2*tmax, qi-0.4*(qf-qi),
                    0.7*tmax, 1.1*qf, tmax, qf), [color_fluc])
c.stroke(path.curve(0, qi, 0.2*tmax, qi+0.8*(qf-qi),
                    0.7*tmax, 1.2*qf, tmax, qf),
         [style.linewidth.thick, color_cl])
for x, y in ((0, qi), (tmax, qf)):
    c.fill(path.circle(x, y, 0.04),
           [color.grey(1), deco.stroked([color.grey(0)])])
c.text(-0.1, qi, r'$q_\text{i}$', [text.halign.right, text.valign.middle])
c.text(tmax+0.1, qf, r'$q_\text{f}$', [text.valign.middle])
c.stroke(path.line(0.73*tmax, 1.03*qf, tmax, 0.6*qf),
         [color_cl, deco.barrow])
c.text(tmax+0.1, 0.6*qf, 'classical trajectory',
       [text.valign.middle, color_cl])
c.writePDFfile()
