from tkinter import *
# the ap helper
root= Tk()
root.geometry("450x200")
root.config(bg="light blue")
root.maxsize(600,600)
root.title("Aritmatic calculater")
# frame to pack the find and sum button
frame1=Frame(root,bg="light blue")
frame1.pack(side=TOP)
frame4=Frame(root,bg="light blue")
frame4.pack(side=TOP)
def sumfunction():
    # general gui stuff
    window = Tk()
    window.geometry("400x400")
    window.config(bg="light blue")
    window.minsize(300,300)
    window.title("sum window")
    ################################
    # the entry related stuff
    the_find_progression = StringVar()
    #this frame is to pack the lable and the entry box
    frame2= Frame(window,bg="light blue")
    frame2.pack(side=TOP)
    the_find_entry = Entry(frame2, textvariable=the_find_progression)
    Label(frame2,text="Entry the AP:",font="bold 15",bg="light blue").pack(side=LEFT,padx=15)
    the_find_entry.pack(side=LEFT)
    frame3= Frame(window,bg="light blue")
    frame3.pack(side=TOP)
    Label(frame3,text="till how many terms ",font="bold 15",fg="black",bg="light blue").pack(side=LEFT,padx=10)
    input_terms_number = StringVar()
    entry_terms_number = Entry(frame3, textvariable=input_terms_number)
    entry_terms_number.pack(side=LEFT)
    #####################################
    
    def submit():
        run = 0
        # main find function
        new_list = []
        ap=the_find_entry.get()
        ap_list = ap.split(",")
        number_of_terms = len(ap_list)
        for value in ap_list:
            try:
                int_or_str = int(value)
                sample1=value
                break
            except ValueError:
                run +=1
                pass
        ap_list_copy = ap.split(",")
        item_to_remove = ap_list_copy[run]
        ap_list_copy.remove(item_to_remove)
        for item in ap_list_copy:
            try:
                int_or_str_ = int(item)
                sample2 = item
                break
            except ValueError:
                pass
        number_of_runs = int(entry_terms_number.get())
        difference_position = int(ap_list.index(sample2)) - int(ap_list.index(sample1))
        print(f"difference between the terms {difference_position}")
        d = (int(sample2) - int(sample1))/int(difference_position)
        print(f"the difference {d}")
        frame3= Frame(window,bg="light blue")
        frame3.pack(side=TOP)
        difference = 0
        display_list=[int(ap_list[0])+0]
        for man in range(number_of_runs):
            difference += d
            term = int(ap_list[0])+difference
            display_list.append(int(term))
        Label(window,text=f"difference : {d}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
        Label(window,text=f"a : {ap_list[0]}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
        Label(window,text=f"the AP : {display_list}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
        Label(window,text=f"the sum : {sum(display_list)}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
    Button(window,text="submit",font="bold 15",bg="red",command=submit,pady=10).pack(side=BOTTOM,fill=X)

def findfunction():
    # general gui stuff
    window = Tk()
    window.geometry("400x400")
    window.config(bg="light blue")
    window.minsize(300,300)
    window.title("find window")
    ################################
    # the entry related stuff
    the_find_progression = StringVar()
    #this frame is to pack the lable and the entry box
    frame2= Frame(window,bg="light blue")
    frame2.pack(side=TOP)
    the_find_entry = Entry(frame2, textvariable=the_find_progression)
    Label(frame2,text="Entry the AP:",font="bold 15",bg="light blue").pack(side=LEFT,padx=15)
    the_find_entry.pack(side=LEFT)
    frame3= Frame(window,bg="light blue")
    frame3.pack(side=TOP)
    Label(frame3,text="till how many terms ",font="bold 15",fg="black",bg="light blue").pack(side=LEFT,padx=10)
    input_terms_number = StringVar()
    entry_terms_number = Entry(frame3, textvariable=input_terms_number)
    entry_terms_number.pack(side=LEFT)
    #####################################
    
    def submit():
        run = 0
        # main find function
        new_list = []
        ap=the_find_entry.get()
        ap_list = ap.split(",")
        number_of_terms = len(ap_list)
        for value in ap_list:
            try:
                int_or_str = int(value)
                sample1=value
                break
            except ValueError:
                run +=1
                pass
        ap_list_copy = ap.split(",")
        item_to_remove = ap_list_copy[run]
        ap_list_copy.remove(item_to_remove)
        for item in ap_list_copy:
            try:
                int_or_str_ = int(item)
                sample2 = item
                break
            except ValueError:
                pass
        number_of_runs = int(entry_terms_number.get())
        difference_position = int(ap_list.index(sample2)) - int(ap_list.index(sample1))
        print(f"difference between the terms {difference_position}")
        d = (int(sample2) - int(sample1))/int(difference_position)
        print(f"the difference {d}")
        frame3= Frame(window,bg="light blue")
        frame3.pack(side=TOP)
        difference = 0
        display_list=[int(ap_list[0])+0]
        for man in range(number_of_runs):
            difference += d
            term = int(ap_list[0])+difference
            display_list.append(int(term))
        Label(window,text=f"difference : {d}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
        Label(window,text=f"a : {ap_list[0]}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
        Label(window,text=f"the AP : {display_list}",bg="light blue",font="bold 14").pack(side=TOP,anchor="w")
    Button(window,text="submit",font="bold 15",bg="red",command=submit,pady=10).pack(side=BOTTOM,fill=X)

    window.mainloop()
def sum_formula_function():
    global screen_sum
    window = Tk()
    window.geometry("400x400")
    window.config(bg="light blue")
    window.minsize(300,300)
    window.title("sum formula window")
    Label(window,text="please use ? at the place of unknown values",bg="light blue",font="bold 10").pack(side=TOP)
    ######################3
    # string var for every entry box
    first_term = StringVar()
    number_of_terms = StringVar()
    difference = StringVar()
    sum_input = StringVar()
    ############################
    # the frame
    frame_1 = Frame(window,bg="light blue")
    frame_1.pack(side=TOP,anchor="w")
    frame_2 = Frame(window,bg="light blue")
    frame_2.pack(side=TOP,anchor="w")
    frame_3 = Frame(window,bg="light blue")
    frame_3.pack(side=TOP,anchor="w")
    frame_4 = Frame(window,bg="light blue")
    frame_4.pack(side=TOP,anchor="w")
    first_term_entry = Entry(frame_1,textvariable=first_term)
    number_of_terms_entry=Entry(frame_2,textvariable=number_of_terms)
    difference_entry=Entry(frame_3,textvariable=difference)
    sum_entry=Entry(frame_4,textvariable=sum_input)
    screen_sum = Label(window,text="",font="bold 18",bg="light blue")
    screen_sum.pack(side=TOP,anchor="w")
    ##########################3
    # to pack all the stupid entries
    Label(frame_1,text="a : ",font="bold 18",bg="light blue").pack(side=LEFT)
    first_term_entry.pack(side=LEFT)
    Label(frame_2,text="n : ",font="bold 18",bg="light blue").pack(side=LEFT)
    number_of_terms_entry.pack(side=LEFT)
    Label(frame_3,text="d : ",font="bold 18",bg="light blue").pack(side=LEFT)
    difference_entry.pack(side=LEFT)
    Label(frame_4,text="sum : ",font="bold 18",bg="light blue").pack(side=LEFT)
    sum_entry.pack(side=LEFT)
    ############################################3
    # formula
    # SUM FORMULA = n/2[2a+(n-1)d]
    def submit():
        a = first_term_entry.get()
        n = number_of_terms_entry.get()
        d = difference_entry.get()
        sum_ = sum_entry.get()
        if a == "" or a=="?":
            a_final = ((int(sum_)*2)-(int(n)-1)*int(d)*int(n))/(int(n)*2)
            screen_sum.config(text=f"a : {a_final}")
        elif n =="" or n =="?":
            the_ap_ = [int(a)]
            print(the_ap_)
            while True:
                index = int(the_ap_[-1])+int(d)
                the_ap_.append(index)
                print(the_ap_)
                if int(the_ap_[-1]) == int(sum_):
                    print(len(the_ap_))
                    screen_sum.config(text=f"n : {len(the_ap_)}")
                    break
        elif d =="" or d=="?":
            sum1 = (int(sum_)*2)/int(n)
            sum2 = 2*(int(a))
            sum3 = int(n)-1
            d_final = (sum1-sum2)/sum3
            screen_sum.config(text=f"d : {d_final}")
            print(d_final)
        elif sum_=="" or sum_=="?":
            sum_final = (int(n)/2)*(2*int(a)+(int(n)-1)*int(d))
            print(sum_final)
            screen_sum.config(text=f"sum : {sum_final}")


    Button(window,text="SUBMIT",bg="red",command=submit,font="bold 18").pack(side=BOTTOM,fill=X)
    window.mainloop()
def find_formula_function():
    global screen
    window = Tk()
    window.geometry("400x400")
    window.config(bg="light blue")
    window.minsize(300,300)
    window.title("find formula window")
    Label(window,text="please use ? at the place of unknown values",bg="light blue",font="bold 10").pack(side=TOP)
    #####################
    # the entries
    difference = StringVar()
    first_entry = StringVar()
    term_number = StringVar()
    the_term = StringVar()
    ####################3
    # the frame to pack the entries
    frame1 = Frame(window,bg="light blue")
    frame1.pack(side=TOP,anchor="w")
    frame2 = Frame(window,bg="light blue")
    frame2.pack(side=TOP,anchor="w")
    frame3 = Frame(window,bg="light blue")
    frame3.pack(side=TOP,anchor="w")
    frame4 = Frame(window,bg="light blue")
    frame4.pack(side=TOP,anchor="w")
    ###################################
    # the entry box
    difference_entry = Entry(frame1,textvariable=difference)
    first_entry_entry = Entry(frame2,textvariable=first_entry)
    term_number_entry = Entry(frame3,textvariable=term_number)
    the_term_entry = Entry(frame4,textvariable=the_term)
    # pack entry
    ###########################
    Label(frame1,text="difference : ",bg="light blue",padx=10,font="bold 18").pack(side=LEFT,pady=5)
    difference_entry.pack(side=LEFT)
    Label(frame2,text="a : ",bg="light blue",padx=10,font="bold 18").pack(side=LEFT,pady=5)
    first_entry_entry.pack(side=LEFT)
    Label(frame3,text="n : ",bg="light blue",padx=10,font="bold 18").pack(side=LEFT,pady=5)
    term_number_entry.pack(side=LEFT)
    Label(frame4,text="an : ",bg="light blue",padx=10,font="bold 18").pack(side=LEFT,pady=5)
    the_term_entry.pack(side=LEFT)
    screen = Label(window,text="",font="bold 18",bg="light blue")
    screen.pack(side=TOP,anchor="w")
    def submit():
        d = difference_entry.get()
        a = first_entry_entry.get()
        n= term_number_entry.get()
        an = the_term_entry.get()
        print(d,a,n,an)
# FIND FORMULA an = a+(n-1)d
        if d=="?" or d=="":
            d_final = (int(an)-int(a))/(int(n)-1)
            print(d_final)
            screen.config(text=f"difference {d_final}")
        elif a == "?"or a=="":
            a_final = int(an)-(int(n)-1)*int(d)
            print(a_final)
            screen.config(text=f"a {a_final}")
        elif n == "?" or n=="":
            n_final = ((int(an)-int(a))/int(d))+1
            print(n_final)
            screen.config(text=f"n {n_final}")
        elif an == "?" or an == "":
            an_final = int(a)+(int(n)-1)*int(d)
            print(an_final)
            screen.config(text=f"an {an_final}")


    Button(window,text="SUBMIT",bg="red",command=submit,font="bold 18").pack(side=BOTTOM,fill=X)





    window.mainloop()



##################################################33
# all the buttons
sum_button = Button(frame1,text="SUM FULL AP",command=sumfunction,bg="light blue",font ="blod 15")
sum_button.pack(side=LEFT,padx=10,pady=30)

find_button=Button(frame1,text="FIND FULL AP",command=findfunction,bg="light blue",font="blod 15")
find_button.pack(side=LEFT,padx=10,pady=30)

sum_formula_button=Button(frame4,text="SUM BY FORMULA",command=sum_formula_function,bg="light blue",font="bold 15")
sum_formula_button.pack(side=LEFT,padx=10)

find_formula_button=Button(frame4,text="FIND BY FORMULA",command=find_formula_function,bg="light blue",font="bold 15")
find_formula_button.pack(side=LEFT,padx=10)
#################################################################################33




root.mainloop()