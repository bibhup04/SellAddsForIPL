from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=============VARIABLES=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_faculty_advisor=StringVar()
        self.var_stud_ser=StringVar()
        self.var_ser_stud_rollphone=StringVar()

    
        #first img
        img=Image.open(r"college_images\si2.png")
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second img
        img1=Image.open(r"college_images\skylab.png")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        #third img
        img2=Image.open(r"college_images\si2.png")
        img2=img2.resize((550,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bg img
        img3=Image.open(r"college_images\bg2.jpg")
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title lable
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg='white',fg='darkgreen')
        title_lbl.place(x=0,y=0,width=1530, height= 45)



        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=10,y=55,width=1480,height=600)


        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Details',font=('times new roman',12,'bold'))
        Left_frame.place(x=10,y=10,width=720,height=570)


        #left label frame img
        img_left=Image.open(r"college_images\students.jpg")
        img_left=img_left.resize((720,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=707,height=130)

        #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text='Current coure infor',font=('times new roman',12,'bold'))
        current_course_frame.place(x=5,y=135,width=707,height=115)


        #department
        dep_label= Label(current_course_frame,text="Department",font=('times new roman',12,'bold'),bg='white')
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=('times new roman',12,'bold'),state='readonly')
        dep_combo['values']=('Select Department','Computer','Electrical','Eelectronics','IT')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label= Label(current_course_frame,text="Course",font=('times new roman',12,'bold'),bg='white')
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),state='readonly')
        course_combo['values']=('Select Course','CSE','ECE','EEE','EIE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label= Label(current_course_frame,text="Year",font=('times new roman',12,'bold'),bg='white')
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('times new roman',12,'bold'),state='readonly')
        year_combo['values']=('Select Year','2019-20','2020-21','2021-22','2022-23')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label= Label(current_course_frame,text="Semester",font=('times new roman',12,'bold'),bg='white')
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('times new roman',12,'bold'),state='readonly')
        semester_combo['values']=('Select Semester','1','2','3','4','5','6','7','8')
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg='white',relief=RIDGE,text='Current coure infor',font=('times new roman',12,'bold'))
        class_student_frame.place(x=5,y=250,width=707,height=290)


        #studentID
        studentID_label= Label(class_student_frame,text="StudentID:",font=('times new roman',12,'bold'),bg='white')
        studentID_label.grid(row=0,column=0,padx=10,pady=5)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=('times new roman',12,'bold'))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student_name
        student_name_label= Label(class_student_frame,text="Student Name:",font=('times new roman',12,'bold'),bg='white')
        student_name_label.grid(row=0,column=2,padx=10,pady=5)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=('times new roman',12,'bold'))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class_divisions
        class_divisions_label= Label(class_student_frame,text="Class Divisons:",font=('times new roman',12,'bold'),bg='white')
        class_divisions_label.grid(row=1,column=0,padx=10,pady=5)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=18,font=('times new roman',12,'bold'),state='readonly')
        div_combo['values']=('Select Div','A','B','C','D')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #class_divisions_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=('times new roman',12,'bold'))
        #class_divisions_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #roll_no
        roll_no_label= Label(class_student_frame,text="Roll No:",font=('times new roman',12,'bold'),bg='white')
        roll_no_label.grid(row=1,column=2,padx=10,pady=5)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('times new roman',12,'bold'))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #gender
        gender_label= Label(class_student_frame,text="Gender:",font=('times new roman',12,'bold'),bg='white')
        gender_label.grid(row=2,column=0,padx=10,pady=5)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=18,font=('times new roman',12,'bold'),state='readonly')
        gender_combo['values']=('Select Gender','Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

       # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=('times new roman',12,'bold'))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB
        DOB_label= Label(class_student_frame,text="DOB:",font=('times new roman',12,'bold'),bg='white')
        DOB_label.grid(row=2,column=2,padx=10,pady=5)

        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('times new roman',12,'bold'))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label= Label(class_student_frame,text="Email:",font=('times new roman',12,'bold'),bg='white')
        email_label.grid(row=3,column=0,padx=10,pady=5)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('times new roman',12,'bold'))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone_no
        phone_no_label= Label(class_student_frame,text="Phone No:",font=('times new roman',12,'bold'),bg='white')
        phone_no_label.grid(row=3,column=2,padx=10,pady=5)

        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('times new roman',12,'bold'))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #address
        address_label= Label(class_student_frame,text="Address:",font=('times new roman',12,'bold'),bg='white')
        address_label.grid(row=4,column=0,padx=10,pady=5)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=('times new roman',12,'bold'))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #faculty_advisor
        faculty_advisor_label= Label(class_student_frame,text="FA name:",font=('times new roman',12,'bold'),bg='white')
        faculty_advisor_label.grid(row=4,column=2,padx=10,pady=5)

        faculty_advisor_entry=ttk.Entry(class_student_frame,textvariable=self.var_faculty_advisor,width=20,font=('times new roman',12,'bold'))
        faculty_advisor_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='Take Photo Sample',value='Yes')
        radiobtn1.grid(row=6,column=0,padx=10)

       # self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='No Photo Sample',value='No')
        radiobtn2.grid(row=6,column=1,padx=10)


        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=700,height=65)


        #save button
        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=18,font=('times new roman',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text='Update',command=self.update_data,width=19,font=('times new roman',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text='Delete',command=self.delete_data,width=18,font=('times new roman',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=19,font=('times new roman',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)


        #button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=235,width=700,height=32)

        #take_photo button
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text='Take Photo Sample',width=38,font=('times new roman',12,'bold'),bg='blue',fg='white')
        take_photo_btn.grid(row=0,column=0)

        #update_photo button
        update_photo_btn=Button(btn_frame1,text='Update Photo Sample',width=38,font=('times new roman',12,'bold'),bg='blue',fg='white')
        update_photo_btn.grid(row=0,column=1)





        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Class student info',font=('times new roman',12,'bold'))
        Right_frame.place(x=750,y=10,width=690,height=570)


        #Raght lable frame image
        img_right=Image.open(r"college_images\sd.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)
    

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=707,height=130)


        #==============searching system==============
        search_frame=LabelFrame(Right_frame,bd=2,bg='white',relief=RIDGE,text='Search system',font=('times new roman',12,'bold'))
        search_frame.place(x=5,y=135,width=676,height=70)

        search_label= Label(search_frame,text="Search By:",font=('times new roman',15,'bold'),bg='red',fg='white')
        search_label.grid(row=0,column=0,padx=10,pady=5)

        #search combo box
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_ser_stud_rollphone,font=('times new roman',12,'bold'),state='readonly',width=10)
        search_combo['values']=('Select','Roll no','Phone no')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #search
        search_entry=ttk.Entry(search_frame,textvariable=self.var_stud_ser,width=20,font=('times new roman',12,'bold'))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #search button
        search_btn=Button(search_frame,text='Search',command=self.fetch_data_by_rollPhone,width=12,font=('times new roman',12,'bold'),bg='blue',fg='white')
        search_btn.grid(row=0,column=3,padx=4)

        #show_all button
        show_all_btn=Button(search_frame,text='Show All',command=self.fetch_data,width=12,font=('times new roman',12,'bold'),bg='blue',fg='white')
        show_all_btn.grid(row=0,column=4,padx=4)

        #=================table frame
        table_frame=Frame(Right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=210,width=676,height=330)


        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','address','FA','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('dep',text='Department')
        self.student_table.heading('course',text='course')
        self.student_table.heading('year',text='year')
        self.student_table.heading('sem',text='semester')
        self.student_table.heading('id',text='StudentId')
        self.student_table.heading('name',text='name')
        self.student_table.heading('div',text='Divison')
        self.student_table.heading('roll',text='Roll')
        self.student_table.heading('gender',text='gender')
        self.student_table.heading('dob',text='dob')
        self.student_table.heading('email',text='email')
        self.student_table.heading('phone',text='phone')
        self.student_table.heading('address',text='address')
        self.student_table.heading('FA',text='FA')
        self.student_table.heading('photo',text='PhotoSampleStatus')
        
        self.student_table['show']='headings'

        self.student_table.column('dep',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('div',width=100)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('address',width=100)
        self.student_table.column('FA',width=100)
        self.student_table.column('photo',width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #===================Function declaration=======================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_faculty_advisor.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #========================fetch data============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============get cursor=================
    def get_cursor(self,event=''):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content['values']

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_faculty_advisor.set(data[13]),
        self.var_radio1.set(data[14])


    #================update function=======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detais",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Faculty_Advisor=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),                                                                                                               
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_faculty_advisor.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()
                                                                                                             ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    

    #===================delete function========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Please select a student id.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #================reset function=================
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_faculty_advisor.set("")
        self.var_radio1.set("")


    #====================serach student details by roll no or phone no======================
    def fetch_data_by_rollPhone(self):
        if self.var_ser_stud_rollphone.get()=="Select":
            messagebox.showerror("Error","Please select Roll No or phone No",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                my_cursor=conn.cursor()
                if self.var_ser_stud_rollphone.get()=="Roll no":
                    sql="select * from student where Roll=%s"
                    val=(self.var_stud_ser.get(),)
                    my_cursor.execute(sql,val)
                    data=my_cursor.fetchall()

                    if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,values=i)
                        conn.commit()
                    else:
                        messagebox.showerror("Error","Please select a valid Roll No",parent=self.root)
                
                elif self.var_ser_stud_rollphone.get()=="Phone no":
                    sql="select * from student where Phone=%s"
                    val=(self.var_stud_ser.get(),)
                    my_cursor.execute(sql,val)
                    data=my_cursor.fetchall()

                    if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,values=i)
                        conn.commit()
                    else:
                        messagebox.showerror("Error","Please select a valid Phone No",parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=========================Genereate data set or photo sample==========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='bibhu',password='Bibhu@0408',database='face_recgonizer')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Faculty_Advisor=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),                                                                                                               
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_faculty_advisor.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()==id+1
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #=================== Load predifined data on face frontal from opencv=====================
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)
                    #scaling facetor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!")
            

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()