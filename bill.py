from tkinter import*
import  pymysql

class Bill_App:
        def __init__(self,root):
                pass
                self.root=root
                self.root.geometry("1350x700+0+0")
                self.root.title("Billing Software")
                bg_color="#074463"
                title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times new Roman",30,"bold"),pady=2).pack(fill=X)
        
                #---------------------variables------------------->
                #================cosmetics=======================
                self.soap=IntVar()
                self.face_cream=IntVar()
                self.face_wash=IntVar()
                self.spray=IntVar()
                self.gell=IntVar()
                self.loshan=IntVar()

                #========================grocery===================
                self.rice=IntVar()
                self.food_oil=IntVar()
                self.daal=IntVar()
                self.wheat=IntVar()
                self.sugar=IntVar()
                self.tea=IntVar()

                #=========================cold Drinks===================

                self.maza=IntVar()
                self.cock=IntVar()
                self.frooti=IntVar()
                self.thumbsup=IntVar()
                self.limca=IntVar()
                self.sprite=IntVar()

                #========================Total product price and Tax Variable========
                self.cosmetic_price=StringVar()
                self.grocery_price=StringVar()
                self.cold_drink_price=StringVar()


                self.cosmetic_tax=StringVar()
                self.grocery_tax=StringVar()
                self.cold_drink_tax=StringVar()

                #==========================customer============================
                self.c_name=StringVar()
                self.c_phon=StringVar()
                self.bill_no=StringVar()
                self.search_bill=StringVar()


                #---------cutomer Detail frame--------->
                F1=LabelFrame(self.root,bd=10,text="Customer Details",font=("Times new Roman",15,"bold"),fg="gold",bg=bg_color)
                F1.place(x=0,y=80,relwidth=1)

                cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times new Roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
                cname_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)


                c_phn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("Times new Roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
                c_phn_txt=Entry(F1,width=15,font="arial 15",textvariable=self.c_phon,bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)


                c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("Times new Roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
                c_bill_txt=Entry(F1,width=15,font="arial 15",textvariable=self.bill_no,bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

                bill_btn=Button(F1,text="Search",width=10,cursor="hand2",bd=7,textvariable=self.search_bill,font="arial 15 bold").grid(row=0,column=6,pady=5,padx=10)

                #----------------------------------------Cosmetic Frame-----------------------------------------------------------#
                
                F2=LabelFrame(self.root,bd=10,text="Cosmetics",font=("Times new Roman",15,"bold"),fg="gold",bg=bg_color)
                F2.place(x=5,y=180,width=325,height=380)
                        #-----------------------Entity------------------------------------------------------------------------#
                bath_lbl=Label(F2,text="Bath Soap",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")#to show in left use property use sticky
                bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                Face_cream_lbl=Label(F2,text="Face Cream",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")#to show in left use property use sticky
                Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

                Face_W_lbl=Label(F2,text="Face Wash",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")#to show in left use property use sticky
                Face_W_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                Hair_s_lbl=Label(F2,text="Hair Spray",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")#to show in left use property use sticky
                Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                Hair_g_lbl=Label(F2,text="Hair Gel",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")#to show in left use property use sticky
                Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                body_l_lbl=Label(F2,text="Body Lotion",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")#to show in left use property use sticky
                Hair_g_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


                #----------------------------------------Grocery Product----------------------------------------------------------#
                
                F3=LabelFrame(self.root,bd=10,text="Grocery",font=("Times new Roman",15,"bold"),fg="gold",bg=bg_color)
                F3.place(x=340,y=180,width=325,height=380)

                        #-----------------------Entity------------------------------------------------------------------------#

                g1_lbl=Label(F3,text="Rice",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                g2_cream_lbl=Label(F3,text="Food oil",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g2_cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

                g3_lbl=Label(F3,text="Daal",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                g4_lbl=Label(F3,text="Wheat",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                g5_lbl=Label(F3,text="Sugar",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                g6_lbl=Label(F3,text="Tea",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")#to show in left use property use sticky
                g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

                #----------------------------------------Cold Drinks----------------------------------------------------------#
                
                F4=LabelFrame(self.root,bd=10,text="Cold Drinks",font=("Times new Roman",15,"bold"),fg="gold",bg=bg_color)
                F4.place(x=675,y=180,width=325,height=380)

                        #-----------------------Entity------------------------------------------------------------------------#

                c1_lbl=Label(F4,text="Coca cola",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c1_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

                c2_cream_lbl=Label(F4,text="Sprite",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c2_cream_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

                c3_lbl=Label(F4,text="Maza",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c3_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

                c4_lbl=Label(F4,text="Frooti",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c4_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

                c5_lbl=Label(F4,text="Thumbs Up",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c5_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
                
                c6_lbl=Label(F4,text="Limca",font=("Time new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,sticky="w")#to show in left use property use sticky
                c6_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new raman",16,"bold" ),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


                #=================================Bill Area=================

                F5=Frame(self.root,bd=10,relief=GROOVE)
                F5.place(x=1010,y=180,width=520,height=380)
                bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
                scrol_y=Scrollbar(F5,orient=VERTICAL)
                self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)


                #================================Button Frame=================================

                F6=LabelFrame(self.root,bd=10,text="Bill Menu",font=("Times new Roman",15,"bold"),fg="gold",bg=bg_color)
                F6.place(x=0,y=560,relwidth=1,height=280)

                #============================Total cost area===============================

                m1=Label(F6,text="costmetic Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
                m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=15)

                m2=Label(F6,text="Grocery Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
                m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=15)

                m3=Label(F6,text="Cold Drinks Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
                m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=15)


                #============================Total Tax  area part==========================================

                c1=Label(F6,text="costmetic Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
                c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=15)

                c2=Label(F6,text="Grocery Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
                c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=15)

                c3=Label(F6,text="Cold Drinks Total",bg=bg_color,fg="White",font=("Times new Roman",12,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
                c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 15 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=15)


                btn_F=Frame(F6,bd=7,relief=GROOVE)
                btn_F.place(x=830,y=60,width=650,height=105)

                total_btn=Button(btn_F,text="Total",bg="cadetblue",fg="white",pady=18,width=11,font="arial 15 bold",bd=5,cursor="hand2",command=self.total).grid(row=0,column=0,padx=5,pady=5)

                GBill_btn=Button(btn_F,text="Generate Bill",bg="cadetblue",fg="white",pady=18,width=11,font="arial 15 bold",bd=5,cursor="hand2").grid(row=0,column=1,padx=5,pady=5)

                Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=18,width=11,font="arial 15 bold",bd=5,cursor="hand2").grid(row=0,column=2,padx=5,pady=5)

                Exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=18,width=11,font="arial 15 bold",bd=5,cursor="hand2").grid(row=0,column=3,padx=5,pady=5)

        def total(self):
                 self.total_cosmetic_price=float(
                                 (self.soap.get()*40)+
                                 (self.face_cream.get()*120)+
                                 (self.face_wash.get()*60)+
                                 (self.spray.get()*180)+
                                 (self.gell.get()*140)+
                                 (self.loshan.get()*180)
        )
                 self.cosmetic_price.set(str(self.total_cosmetic_price))

root=Tk()
obj=Bill_App(root)
root.mainloop()