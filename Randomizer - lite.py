import time

import tkinter as tk

from tkinter import messagebox as mb

import random as rd

import re as rex

import time as tm

import os as ost




# Here are marks for my variables, functions and other stuff
# w - for static objects, for example - tkinter widgets, or windows
# v - for variables which contain simple values and data




def clear_overall():
    """This func clears up overall record file, using for it -messagebox- module
    from tkinter module, imported as mb. It checks, do you want or no, using
    -messagebox-, and then opens and closes the file in 'w' mode to erase them."""
    if mb.askyesno(title = "Clearing overall log", message = "Do you really want to clean up overall log?"):
        with open(overall_log_path, "w") as f:
            f.write("")
        mb.showinfo(title = "it's done!", message = "Overall log has been cleaned")
    else:
        pass




def open_logs_directory():
    """This function is given to a button, it will open a directory,
       using Windows cmd, and environment variable USERPROFILE, which leads to
       C:\\Users\\Username + Documents. Why there? Because it is set as default folder for
       record logs of the app. Module used here is -os- imported as ost."""
    ost.system("explorer %USERPROFILE%\\Documents")




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
    root_ex_w.geometry("840x400")
    root_ex_w.title("How to use Randomizer?!")
    root_ex_w.resizable(0, 0)
    how_to_label_w = tk.Label(root_ex_w, bg = "lemon chiffon", justify = tk.LEFT, font = ("Times New Roman", 10),
                              text = """
▶ [Amount of selection] ◀ here you define how many digits to be selected, for example, if you need 3 digits picked up from
given range, put 3 in the amount entry!

▶ [Lower/Upper range] ◀ in these two you define, the range of selection, for example, you want 3 digits selected from 10,
then you set amount of selection 3, and give lower range - 1, upper range - 10. Do not forget, that lower range can't
be bigger than upper range, it will lead to an error!

▶ [Record results in overall file] ◀ you use it, to write your every selection result into record log, for example,
you got 3 results like [1,3,54,0], [23,11,34,3], [10,100,433,55], so all there sets will be recorded into overall
log, additionally with the time they were selected.

▶ [See log directory] ◀ use it to open Windows explorer at where overall log is stored.

▶ [Clean overall log] ◀ use it to empty the record log, if you do not need it anymore. Or you can delete it,
manually trough Windows explorer. Randomizer will create a new empty log when it starts new session.

▶ [Run the wheel] ◀ use it to make your choice of random digits.

▶ [Help] ◀ use it to see this weird disarranged explanation window with a lot of grammar mistakes :)


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


    if int(lower) >= int(upper):
        mb.showinfo(title = "Bad range!", detail = "\nLower range can't be bigger than upper range", icon = mb.INFO, type = mb.OK)

    else:
        try:
            result_text.delete(0.0, 200.0)
            population = [i for i in range(int(lower), int(upper) + 1)]
            final = str(rd.sample(population, int(amount)))[1:-1]
            result_text.insert(0.0, final)
            if overall_record.get():
                with open(overall_log_path, "a") as f:
                    f.write(final + f" ------ [{tm.asctime()}]" + "\n")

        except ValueError:
            mb.showinfo(title = "Low population", detail = "Please, set your amount little bit lower than upper range, or \nset your upper range higher than amount, "
                                                           "because there is \nno enough choices to choose")




# Options section relates to the main window, starts here
root_w = tk.Tk()
root_w.title("Random - IT (Lite)")
root_w.config(bg="lemon chiffon")
root_w.resizable(0, 0)




# Variables section
tr = root_w.register(defined_range)
overall_log_path = ost.path.join(ost.getenv("USERPROFILE"), "Documents\\RANDOMIZER LITE - LOG.txt")




# This frame contains entries for choosing values
upper_entries_frame_w = tk.Frame(root_w, bg="lemon chiffon")
upper_entries_frame_w.pack(side = tk.TOP)




# entry for defining amount of selection
selection_amount_entry_w = tk.Entry(upper_entries_frame_w, width = 15, validate = "key", validatecommand = (tr, "%P", 3))
selection_amount_entry_w.insert(0, "1")
selection_amount_entry_w.grid(row = 0, column = 0)
selection_amount_label_w = tk.Label(upper_entries_frame_w, width = 15, text = "Amount", bg = "lemon chiffon", font = ("Times New Roman", 12), anchor = "w")
selection_amount_label_w.grid(row = 0, column = 1)




# lower range of selection
lower_range_entry_w = tk.Entry(upper_entries_frame_w, width = 15, validate = "key", validatecommand = (tr, "%P", 7))
lower_range_entry_w.insert(0, "1")
lower_range_entry_w.grid(row = 1, column = 0, padx = 5, pady = 5)
lower_range_label_w = tk.Label(upper_entries_frame_w, width = 15, text = "Lower range", bg = "lemon chiffon", font = ("Times New Roman", 12), anchor = "w")
lower_range_label_w.grid(row = 1, column = 1, padx = 5, pady = 5)




# upper range of selection
upper_range_entry_w = tk.Entry(upper_entries_frame_w, width = 15, validate = "key", validatecommand = (tr, "%P", 8))
upper_range_entry_w.insert(0, "10")
upper_range_entry_w.grid(row = 2, column = 0, padx = 5, pady = 5)
upper_range_label_w = tk.Label(upper_entries_frame_w, width = 15, text = "Upper  range", bg = "lemon chiffon", font = ("Times New Roman", 12), anchor = "w")
upper_range_label_w.grid(row = 2, column = 1, padx = 5, pady = 5)




# This checkbutton below defines, if results will be written in an overall record log
overall_record = tk.IntVar()
overall_record.set(1)
overall_file_checkbutton_w = tk.Checkbutton(upper_entries_frame_w, text = "Record results\nin overall file", font = ("Times New Roman", 12), bg = "lemon chiffon", activebackground = "lemon chiffon", variable = overall_record)
overall_file_checkbutton_w.grid(row = 3, column = 0, columnspan = 2, sticky = "we", pady = 10)




# This button below is for erasing the overall record log
clean_overall_file_button_w = tk.Button(upper_entries_frame_w, text = "Clean\noverall log", bg = "lemon chiffon", font = ("Times New Roman", 12), command = clear_overall)
clean_overall_file_button_w.grid(row = 4, column = 0, columnspan = 2, sticky = "we", pady = 2)




# This button for opening a directory where the logs stored
see_logs_button_w = tk.Button(upper_entries_frame_w, text = "Log\ndirectory", bg = "lemon chiffon", font = ("Times New Roman", 12), command = open_logs_directory)
see_logs_button_w.grid(row = 5, column = 0, columnspan = 2, sticky = "we", pady = 2)




# Button for opening a window with instructions
explanation_button_w = tk.Button(upper_entries_frame_w, text = "Help", bg = "lemon chiffon", font = ("Times New Roman", 12), command = explanation)
explanation_button_w.grid(row = 6, column = 0, columnspan = 2, sticky = "we", pady = 2)




# Button for calculation of a random choice
choose_button_w = tk.Button(upper_entries_frame_w, text = "Run\nthe wheel", bg = "lemon chiffon", font = ("Times New Roman", 12), command = the_function)
choose_button_w.grid(row = 7, column = 0, columnspan = 2, sticky = "we", pady = 2)




result_text = tk.Text(root_w, width = 30, height = 10)
result_text.pack(pady = 3)




# Company label at the bottom of the app's window
company_label_w = tk.Label(text = f"FreeWind Interactive © {time.gmtime()[0]}\nAll rights reserved", bg = "lemon chiffon", font = ("Times New Roman", 12)) # Here we get or company copyright label always actual, using time module and slicing -year- part
company_label_w.pack()




root_w.mainloop()
