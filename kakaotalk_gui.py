from tkinter import *
import tkinter.ttk as ttk

# values
global country_list
main_country_list = ['Europe', 'Asia',
                     'Africa', 'North America', 'South America']
europe_list = ['Russia', 'Ukraine', 'Poland', 'England', 'Ireland', 'Serbia', 'Romania', 'Estonia', 'Germany', 'Lithuania', 'Croatia', 'Sweden', 'Netherlands', 'Latvia', 'Austria', 'Belarus', 'Spain', 'Slovenia', 'Czech', 'Cyprus', 'France',
               'Belgium', 'Bulgaria', 'Hungary', 'Moldova', 'Italy', 'Bosnia', 'Portugal', 'Georgia', 'Greece', 'Iceland', 'Slovakia', 'Monaco', 'Albania', 'Finland', 'Luxembourg', 'Montenegro', 'Denmark', 'Switzerland', 'Norway', 'Northmacedonia']
asia_list = ['Kazakhstan', 'China', 'Philippines', 'Myanmar', 'Indonesia', 'Malaysia', 'Vietnam', 'Kyrgyzstan', 'Israel', 'HongKong', 'Macao', 'India', 'Cambodia', 'Laos',
             'Yemen', 'Uzbekistan', 'Iraq', 'Thailand', 'Saudiarabia', 'Taiwan', 'Bangladesh', 'Turkey', 'Srilanka', 'Pakistan', 'Newzealand', 'Mongolia', 'Afghanistan', 'Papua', 'Nepal', 'Timorleste', 'Uae', 'Kuwait', 'Oman', 'Qatar', 'Jordan', 'Brunei', 'Tajikistan', 'Bahrain', 'Armenia', 'Lebanon', 'Bhutan', 'Maldives', 'Turkmenistan', 'Japan', 'Southkorea']
africa_list = ['Kenya', 'Tanzania', 'DCongo', 'Nigeria', 'Egypt', 'Ivory', 'Gambia', 'Southafrica', 'Morocco', 'Ghana', 'Cameroon', 'Chad', 'Algeria', 'Senegal', 'Guinea', 'Mali', 'Ethiopia', 'Uganda', 'Angola', 'Mozambique', 'Tunisia', 'Zimbabwe', 'Togo', 'Libyan', 'Swaziland', 'Mauritania', 'Sierraleone',
               'Burundi', 'Benin', 'Botswana', 'Caf', 'Guineabissau', 'Comoros', 'Liberia', 'Lesotho', 'Malawi', 'Namibia', 'Niger', 'Rwanda', 'Reunion', 'Zambia', 'Somalia', 'Congo', 'Furkinafaso', 'Gabon', 'Mauritius', 'Equatorialguinea', 'Djibouti', 'Eritrea', 'Southsudan', 'Saotomeandprincipe', 'Seychelles', 'Capeverde']
north_america_list = ['USA (virtual)', 'Canada', 'Mexico', 'Honduras', 'Nicaragua', 'Costarica', 'Guatemala', 'Puertorico', 'Salvador', 'Jamaica', 'Panama', 'Barbados',
                      'Bahamas', 'Belize', 'Dominica', 'Grenada', 'Saintkitts', 'Guadeloupe', 'Saintlucia', 'Antiguabarbuda', 'Caymanislands', 'Aruba', 'Montserrat', 'Anguilla', 'USA']
south_america_list = ['Haiti', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Brazil', 'Paraguay', 'Bolivia', 'Trinidad', 'Ecuador', 'Dominican', 'Guyana', 'Suriname', 'Chile', 'Uruguay', 'Frenchguiana',
                      'Saintvincentgrenadines']
device_var_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def set_country_list():

    country_list = []

    if main_country_value.get() == 1:

        country_list = europe_list

    elif main_country_value.get() == 2:

        country_list = asia_list

    elif main_country_value.get() == 3:

        country_list = africa_list

    elif main_country_value.get() == 4:

        country_list = north_america_list

    elif main_country_value.get() == 5:

        country_list = south_america_list

    country_list_combobox['values'] = country_list


# GUI ??????
window = Tk()
window.title("???????????? ???????????????")

# ?????? ?????????
frame_main = Frame(window)
frame_main.pack()

# ?????? ?????????
frame_top = LabelFrame(frame_main, text="??????")
frame_top.pack(fill="x", padx=5, pady=5)

# ?????? ?????? ?????????
frame_top1 = LabelFrame(frame_top, text="??????")
frame_top1.pack(fill="x", padx=5, pady=5)

main_country_value = IntVar()
main_country_list_radiobtn1 = Radiobutton(
    frame_top1, text="Europe", value=1, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn2 = Radiobutton(
    frame_top1, text="Asia", value=2, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn3 = Radiobutton(
    frame_top1, text="Africa", value=3, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn4 = Radiobutton(
    frame_top1, text="North America", value=4, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn5 = Radiobutton(
    frame_top1, text="South America", value=5, variable=main_country_value, command=set_country_list)
main_country_list_radiobtn1.pack(side="left")
main_country_list_radiobtn2.pack(side="left")
main_country_list_radiobtn3.pack(side="left")
main_country_list_radiobtn4.pack(side="left")
main_country_list_radiobtn5.pack(side="left")

# ?????? ?????? ?????????
frame_top2 = LabelFrame(frame_top, text="??????")
frame_top2.pack(fill="x", padx=5, pady=5)

country_list_combobox = ttk.Combobox(
    frame_top2, height=20, state="readonly")  # ????????????
country_list_combobox.pack(fill="x", padx=5, pady=5)

# ?????? ?????? ?????????
frame_top3 = LabelFrame(frame_top, text="?????????")
frame_top3.pack(fill="x", padx=5, pady=5)

device_var_combobox = ttk.Combobox(
    frame_top3, height=20, state="readonly", values=device_var_list)  # ????????????
device_var_combobox.pack(fill="x", padx=5, pady=5)

# ?????? ?????????
frame_bottom = LabelFrame(frame_main, text="??????")
frame_bottom.pack(fill="x", padx=5, pady=5)

btn1 = Button(frame_bottom, text="??????/?????? ??????")
btn1.pack(side="left", padx=5, pady=5)

btn2 = Button(frame_bottom, text="LD?????? 1??????")
btn2.pack(side="left", padx=5, pady=5)

btn3 = Button(frame_bottom, text="LD?????? 2??????")
btn3.pack(side="left", padx=5, pady=5)

# GUI ??????
window.resizable(False, False)
window.mainloop()
