import time

import tkinter as tk

from tkinter import filedialog as fd

from tkinter import messagebox as mb

import random as rd

import re as rex

import time as tm

import os as ost


# Here are marks for my variables, functions and other stuff
# w - for static objects, for example - tkinter widgets, or windows
# v - for variables which contain simple values and data





def clear_user():
    """This func clears up user's record file, using for it -messagebox- module
    from tkinter module, imported as mb. It checks, do you want or no, using
    -messagebox-, and then opens and closes the file in 'w' mode to erase them."""
    if mb.askyesno(title = "Clearing user's log", message = "Do you really want to clean up user's log?"):
        with open(user_log_path, "w") as f:
            pass
        mb.showinfo(title = "It's done!", message = "User's log has been cleaned")
    else:
        pass


def clear_overall():
    """This func clears up overall record file, using for it -messagebox- module
    from tkinter module, imported as mb. It checks, do you want or no, using
    -messagebox-, and then opens and closes the file in 'w' mode to erase them."""
    if mb.askyesno(title = "Clearing overall log", message = "Do you really want to clean up overall log?"):
        with open(overall_log_path, "w") as f:
            pass
        mb.showinfo(title = "it's done!", message = "Overall log has been cleaned")
    else:
        pass


def select_file():
    """Stores filename for openings,into
    -separated_file_log- variable"""
    global separated_file_log
    separated_file_log = fd.askopenfilename()


def open_logs_directory():
    """This function is given to a button, it will open a directory,
       using Windows cmd, and environment variable USERPROFILE, which leads to
       C:\\Users\\Username + Documents. Why there? Because it is set as default folder for
       record logs of the app. Module used here is -os- imported as ost."""
    ost.system("explorer %USERPROFILE%\\Documents")


def one_digit(x):
    """This func validates value entered into an entry,
    for being digit, length only 1 symbol or being an empty string.
    This func is registered to the main root_w of the app.
    %P is already given at registration below"""
    if x.isdigit() and len(x) == 1 or x == "":
        return True
    else:
        return False


def defined_range(x, r):
    """This func checks entered value to be digits and only
    given value -r- long. Func is registered to root_w for
    validation of values entered into entries. Pt is %P, it has
    to be given when the func is called. Regular expression module is
    used here"""
    pt = f"[0-9]{{0,{r}}}"
    if rex.fullmatch(pt, x):
        return True
    else:
        return False


def explanation():
    root_ex_w = tk.Tk()
    root_ex_w.config()
    root_ex_w.geometry("850x700")
    root_ex_w.title("How to use Randomizer?!")
    root_ex_w.resizable(0, 0)
    how_to_label_w = tk.Label(root_ex_w, bg = "lemon chiffon", justify = tk.LEFT, font = ("Times New Roman", 10),
                              text = """
▶ [Amount of selection] ◀ here you define how many digits to be selected, for example, if you need 3 digits picked up from 
given range, put 3 in the amount entry!
    
▶ [Lower/Upper range] ◀ in these two you define, the range of selection, for example, you want 3 digits selected from 10, 
then you set amount of selection 3, and give lower range - 1, upper range - 10. Do not forget, that lower range can't 
be bigger than upper range, it will lead to an error!

▶ [Only with digit] ◀ you use it and results including only this digit will be shown, for example, you picked -1- so, 
results may include [1,11,41,71,14] 

▶ [Exclude with digit(s)] ◀ you use it and results will be filtered from entered digits, for example you entered 3 and 7, so 
there won't be any result including them, like [33,31,71,7,73,27,3,77].

▶ [Warning!!!] ◀ using include and exclude option, you may shorten the result list, and it will lead to an error. 
For example, you have range from 1-10, and selection amount 8, but you excluded 3,1,4, so - 2 - - 5 6 7 8 9 10 left, 
so it is only 7 digits, and not enough for selection amount of 8, so you have to increase you range, or reduce selection
amount, to have enough choices.

▶ [Record results in overall/user's file] ◀ you use it, to write your every selection result into record log, for example,
you got 3 results like [1,3,54,0], [23,11,34,3], [10,100,433,55], so all there sets will be recorded into overall/user's
logs, additionally with the time they were selected.

▶ [Create a separate log for the session] ◀ use it if you need to create additional log for ongoing session, it will open
dialog menu, where you will select an existing file, or will create a file in a directory you need. After this, records
will being recorded into log

▶ [See logs directory] ◀ use it to open Windows explorer at where Overall/User logs stored.

▶ [Clean overall/user log] ◀ use it to empty the record logs, if you do not need them anymore. Or you can delete them, 
manually trough Windows explorer. Randomizer will create new empty logs when it starts new session.

▶ [Twist the wheel] ◀ use it to make your choice of random digits.

▶ [?] ◀ use it to see this weird disarranged explanation window with a lot of grammar mistakes :)


""")
    how_to_label_w.pack()


def the_function():
    """Main function, uses -random- imported as rd
    for random choices, stores it into variables, and
    picks up samples using same random module. Uses
    -time module- imported as tm, to get time and add it
    at the end of every result, which to be recorded into logs"""
    lower = lower_range_entry_w.get()
    upper = upper_range_entry_w.get()
    amount = selection_amount_entry_w.get()
    include = only_number_entry_w.get()
    exclude = remove_numbers_entry_w.get()

    if int(lower) >= int(upper):
        result_label_w["text"] = "Please, set upper range higher than lower range"
    else:

        population = [i for i in range(int(lower), int(upper) + 1)]

        if include:
            for i in include:
                population = [x for x in population if i in str(x)]

        if exclude:
            for i in set(exclude):
                population = [x for x in population if i not in str(x)]

        try:
            if int(amount) > 12:
                sub_window_w = tk.Tk()
                sub_window_w.geometry("1000x800")
                sub_window_w.config(bg ="lemon chiffon")
                sub_text_w = tk.Text(sub_window_w, bg ="lemon chiffon")
                sub_text_w.pack(side = tk.TOP, fill ="both", expand ="True")
                final = str(rd.sample(population, int(amount)))[1:-1] + " "
                sub_text_w.insert(0.0, final)
                if overall_record.get():
                    with open(overall_log_path, "a") as f:
                        f.write(final + f" ------ [{tm.asctime()}]" + "\n")
                if user_file.get():
                    with open(user_log_path, "a") as f:
                        f.write(final + f" ------ [{tm.asctime()}]" + "\n")
                if separated_file_log:
                    with open(separated_file_log, "a") as f:
                        f.write(final + f" ------ [{tm.asctime()}]" + "\n")


            else:
                result = str(rd.sample(population, int(amount)))[1:-1]
                result_label_w.configure(text= result, font = ("Helvetica", 12))
                if overall_record.get():
                    with open(overall_log_path, "a") as f:
                        f.write(result + f" ------ [{tm.asctime()}]" + "\n")
                if user_file.get():
                    with open(user_log_path, "a") as f:
                        f.write(result + f" ------ [{tm.asctime()}]" + "\n")
                if separated_file_log:
                    with open(separated_file_log, "a") as f:
                        f.write(result + f" ------ [{tm.asctime()}]" + "\n")



        except ValueError:
            result_label_w.configure(text="Probably there is a confrontation in "
                                          "exclude/include,\nplease check the values, "
                                          "or there is nothing left to\n select, in this case, "
                                          "lower the amount or get the range higher",
                                     font=("Helvetica", 12))




# Options section relates to the main window, starts here
root_w = tk.Tk()
root_w.geometry("800x500")
root_w.title(" " * 82 + "Random - IT")
root_w.config(bg="lemon chiffon")
root_w.resizable(0, 0)



# Variables section
odv = (root_w.register(one_digit), "%P")  # one digit validation
tr = root_w.register(defined_range)  # defined range validation
overall_log_path = ost.path.join(ost.getenv("USERPROFILE"), "Documents\\RANDOMIZER'S LOG.txt")
user_log_path = ost.path.join(ost.getenv("USERPROFILE"), "Documents\\RANDOMIZER'S USER LOG.txt")
separated_file_log = 0



# This frame contains entries for choosing values
upper_entries_frame_w = tk.Frame(root_w, bg="lemon chiffon")
upper_entries_frame_w.place(x=65, y=25)




# lower range of selection
lower_range_entry_w = tk.Entry(upper_entries_frame_w, width = 8, validate = "key", validatecommand = (tr, "%P", 7))
lower_range_entry_w.insert(0, "1")
lower_range_entry_w.grid(row = 0, column = 2)
lower_range_label_w = tk.Label(upper_entries_frame_w, text = "Lower range", bg = "lemon chiffon", font = ("Times New Roman", 10))
lower_range_label_w.grid(row = 0, column = 3, sticky = "w")




# upper range of selection
upper_range_entry_w = tk.Entry(upper_entries_frame_w, width = 8, validate = "key", validatecommand = (tr, "%P", 8))
upper_range_entry_w.insert(0, "10")
upper_range_entry_w.grid(row = 1, column = 2)
upper_range_label_w = tk.Label(upper_entries_frame_w, text = "Upper range", bg = "lemon chiffon", font = ("Times New Roman", 10))
upper_range_label_w.grid(row = 1, column = 3, sticky = "w")




# entry for including defined number(s) into selection
only_number_entry_w = tk.Entry(upper_entries_frame_w, width = 10, validate = "key", validatecommand = (tr, "%P", 1))
only_number_entry_w.grid(row = 0, column = 4, sticky = "e")
include_number_label_w = tk.Label(upper_entries_frame_w, text = "Only with digit", bg = "lemon chiffon", font = ("Times New Roman", 10))
include_number_label_w.grid(row = 0, column = 5, sticky = "w")




# entry for excluding defined number(s) from selection
remove_numbers_entry_w = tk.Entry(upper_entries_frame_w, width = 10, validate = "key", validatecommand = (tr, "%P", 10))
remove_numbers_entry_w.grid(row = 1, column = 4)
exclude_number_label_w = tk.Label(upper_entries_frame_w, text = "Remove with digit(s) [0-9]", bg = "lemon chiffon", font = ("Times New Roman", 10))
exclude_number_label_w.grid(row = 1, column = 5, sticky = "w")




# entry for defining amount of selection
selection_amount_entry_w = tk.Entry(upper_entries_frame_w, width = 8, validate = "key", validatecommand = (tr, "%P", 3)) # change 3rd argument of validatecommand to any to set selection amount
selection_amount_entry_w.insert(0, "1")
selection_amount_entry_w.grid(row = 0, column = 0)
selection_amount_label_w = tk.Label(upper_entries_frame_w, text = "Amount of selections", bg = "lemon chiffon", font = ("Times New Roman", 10))
selection_amount_label_w.grid(row = 0, column = 1, sticky = "w")




# This checkbutton below defines, if results will be written in an overall record log
overall_record = tk.IntVar()
overall_record.set(1)
overall_file_checkbutton_w = tk.Checkbutton(root_w, text = "Record results\nin overall file", font = ("Times New Roman", 10), bg = "lemon chiffon", activebackground = "lemon chiffon", justify = tk.LEFT, variable = overall_record)
overall_file_checkbutton_w.place(x = 60, y = 100)




# This checkbutton below defines, if results will be written in a file chosen by user
user_file = tk.IntVar()
user_file_checkbutton_w = tk.Checkbutton(root_w, text = "Record results\nin user's file", font = ("Times New Roman", 10), bg = "lemon chiffon", activebackground = "lemon chiffon", justify = tk.LEFT, variable = user_file)
user_file_checkbutton_w.place(x = 195, y = 100)




# This button below creates or chooses, a file for user's own results log
separated_log_button_w = tk.Button(root_w, text = "Create a separate log\nfor the session", width = 18, bg = "lemon chiffon", command = select_file)
separated_log_button_w.place(x = 330, y = 100, height = 52)




# This button below is for erasing the overall record log
clean_overall_file_button_w = tk.Button(root_w, text = "Clean overall log", bg = "lemon chiffon", width = 15, command = clear_overall)
clean_overall_file_button_w.place(x = 585, y = 100, height = 25)




# This button below is for erasing user's record log
clean_user_file_button_w = tk.Button(root_w, text = "Clean user's log", bg = "lemon chiffon", width = 15, command = clear_user)
clean_user_file_button_w.place(x = 585, y = 126, height = 25)




# This button for opening a directory where the logs stored
see_logs_button_w = tk.Button(root_w, text = "See logs\ndirectory", bg = "lemon chiffon", width = 10, command = open_logs_directory)
see_logs_button_w.place(x = 490, y = 100, height = 52)




# Label for showing the result(s)
result_label_w = tk.Label(root_w, text = "-" * 12, font = ("Helvetica", 20), bg = "lemon chiffon")
result_label_w.place(x = 50, y = 200, width = 700, height = 70)




# Button for calculation of a random choice
choose_button_w = tk.Button(root_w, text = "Twist the wheel", bg = "lemon chiffon", command = the_function)
choose_button_w.place(x = 315, y = 310, width = 170, height = 50)




# Button for opening a window with instructions
explanation_button_w = tk.Button(root_w, text = "?", bg = "lemon chiffon", font = ("Times New Roman", 18), command = explanation)
explanation_button_w.place(x = 385, y = 390, width = 30, height = 30)




# Company label at the bottom of the app's window
company_label_w = tk.Label(text = f"FreeWind Interactive © {time.gmtime()[0]}\nAll rights reserved", bg = "lemon chiffon") # Here we get or company copyright label always actual, using time module and slicing -year- part
company_label_w.place(x = 300, y = 450, width = 200, height = 45)




root_w.mainloop()
