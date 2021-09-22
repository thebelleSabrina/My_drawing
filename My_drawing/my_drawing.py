"""
File:
Name:Sabrina Wang
----------------------
I like bread and I always write code so I decided to combine two things(?.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    I like bread and I always write code so I decided to combine two things(?.
    """
    window = GWindow(width=500, height=800, title='stanCodeistheBest')

#  background(bubbles and slogan)
    bubble1 = GOval(90, 90, x=100, y=200)
    bubble1.color = 'lightpink'
    bubble1.filled = True
    bubble1.fill_color = 'lightpink'
    window.add(bubble1)

    bubble2 = GOval(90, 90, x=40, y=40)
    bubble2.color = 'violet'
    bubble2.filled = True
    bubble2.fill_color = 'violet'
    window.add(bubble2)

    bubble3 = GOval(90, 90, x=400, y=300)
    bubble3.color = 'lightblue'
    bubble3.filled = True
    bubble3.fill_color = 'lightblue'
    window.add(bubble3)

    bubble4 = GOval(90, 90, x=350, y=70)
    bubble4.color = 'slateblue'
    bubble4.filled = True
    bubble4.fill_color = 'slateblue'
    window.add(bubble4)

    label = GLabel('stanCode Is The Best')
    label.font = 'Time New Roman-40-bold'
    window.add(label, 50, 350)

#  Anpanman's body
    cape = GPolygon()
    cape.add_vertex((250, 500))
    cape.add_vertex((100, 800))
    cape.add_vertex((400, 800))
    window.add(cape)
    cape.color = 'chocolate'
    cape.filled = True
    cape.filled_color = 'chocolate'

    l_hand = GRect(150,50,x=75,y=620)
    l_hand.color = 'red'
    l_hand.filled = True
    l_hand.fill_color = 'red'
    window.add(l_hand)

    r_hand = GRect(150,50,x=275,y=620)
    r_hand.color = 'red'
    r_hand.filled = True
    r_hand.fill_color = 'red'
    window.add(r_hand)

    l_glove = GRect(30,50,x=65,y=620)
    l_glove.color = 'yellow'
    l_glove.filled = True
    l_glove.fill_color = 'yellow'
    window.add(l_glove)

    r_glove = GRect(30,50,x=415,y=620)
    r_glove.color = 'yellow'
    r_glove.filled = True
    r_glove.fill_color = 'yellow'
    window.add(r_glove)

    l_glove2 = GOval(50,70,x=45,y=610)
    l_glove2.color = 'yellow'
    l_glove2.filled = True
    l_glove2.fill_color = 'yellow'
    window.add(l_glove2)

    r_glove2 = GOval(50,70,x=435,y=610)
    r_glove2.color = 'yellow'
    r_glove2.filled = True
    r_glove2.fill_color = 'yellow'
    window.add(r_glove2)

    upper_body = GRect(150,250,x=175,y=550)
    upper_body.color = 'red'
    upper_body.filled = True
    upper_body.fill_color = 'red'
    window.add(upper_body)

    belt = GRect(150,50,x=175,y=700)
    belt.color = 'yellow'
    belt.filled = True
    belt.fill_color = 'yellow'
    window.add(belt)

    face = GOval(250, 250, x=125, y=400)
    face.color = 'navajowhite'
    face.filled = True
    face.fill_color = 'navajowhite'
    window.add(face)

    mouth = GOval(110,110,x=195,y=515)
    mouth.filled = True
    mouth.fill_color = 'salmon'
    window.add(mouth)

    cover = GOval(130,110,x=185,y=479)
    cover.color = 'navajowhite'
    cover.filled = True
    cover.fill_color = 'navajowhite'
    window.add(cover)

    l_eyebrow = GOval(60,95,x=190,y=430)
    l_eyebrow.filled = True
    l_eyebrow.fill_color = 'navajowhite'
    window.add(l_eyebrow)

    cover2 = GOval(80, 95, x=185, y=450)
    cover2.color = 'navajowhite'
    cover2.filled = True
    cover2.fill_color = 'navajowhite'
    window.add(cover2)

    r_eyebrow = GOval(60, 95, x=250, y=430)
    r_eyebrow.filled = True
    r_eyebrow.fill_color = 'navajowhite'
    window.add(r_eyebrow)

    cover3 = GOval(80, 95, x=235, y=450)
    cover3.color = 'navajowhite'
    cover3.filled = True
    cover3.fill_color = 'navajowhite'
    window.add(cover3)

    l_eye = GOval(20, 45, x=210, y=460)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)

    r_eye = GOval(20, 45, x=270, y=460)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)

    nose = GOval(60, 50, x=220, y=510)
    nose.filled = True
    nose.fill_color = 'tomato'
    window.add(nose)

    brush_l = GOval(70, 50, x=150, y=520)
    brush_l.filled = True
    brush_l.fill_color = 'coral'
    window.add(brush_l)

    brush_r = GOval(70, 50, x=280, y=520)
    brush_r.filled = True
    brush_r.fill_color = 'coral'
    window.add(brush_r)

    leg = GPolygon()
    leg.add_vertex((250, 770))
    leg.add_vertex((225, 800))
    leg.add_vertex((270, 800))
    window.add(leg)
    leg.color = 'black'
    leg.filled = True
    leg.filled_color = 'black'

    belt_decor = GRect(70,50,x=215,y=700)
    belt_decor.color = 'white'
    belt_decor.filled = True
    belt_decor.fill_color = 'white'
    window.add(belt_decor)

    belt_decor2 = GRect(50, 30, x=225, y=710)
    belt_decor2.color = 'yellow'
    belt_decor2.filled = True
    belt_decor2.fill_color = 'yellow'
    window.add(belt_decor2)


if __name__ == '__main__':
    main()
