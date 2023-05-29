#wapp to make employee_management_system
#==========================================================
import matplotlib.pyplot as plt
from tkinter import  *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *
import pandas as pd
import requests
#===========================================================
try:
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	data=res.json()
	city=data["city"]
except Exception as e:
	print("Issue",e)


try:
	a1="https://api.openweathermap.org/data/2.5/weather?"
	a2="q=" + city
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	a4 = "&units=" + "metric"
	wa=a1+a2+a3+a4
	res=requests.get(wa)
	data=res.json()
	temp=data["main"]["temp"]		
except Exception as e:
	print("issue",e)
#=========================================================
root=Tk()
root.title("E.M.S")
root.geometry("500x500+50+50")
root.configure(bg="pale green")
f=("Arial",20,"bold")

def f1():
	root.withdraw()
	aw.deiconify()
def f2():
	aw.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["my_12jan23"]
		coll=db["employee"]
		data=coll.find()
		info=""
		for d in data:
			info=info + "ID = " + str(d["_id"]) + "  Name = " + str(d["name"]) + "  Salary = " + str(d["salary"]) +"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()
	
def f4():
	vw.withdraw()
	root.deiconify()
def f5():
	root.withdraw()
	uw.deiconify()
def f6():
	uw.withdraw()
	root.deiconify()
def f7():
	root.withdraw()
	dw.deiconify()
def f8():
	dw.withdraw()
	root.deiconify()
def f9():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["my_12jan23"]
		coll=db["employee"]
		id=int(aw_ent_id.get())
		name=(aw_ent_name.get())
		salary=float(aw_ent_salary.get())
		if(id>0) and (id.isnumeric()):
			if((name.isalpha()) and (len(name) >=2)): 
				count=coll.count_documents({"_id":id})
				if(salary>8000) and (salary.isnumeric()):
					if count==1:
						showerror(id,"already exists")
					else:
						info={"_id":id,"name":name,"salary":salary}
						coll.insert_one(info)
						showinfo("success","record created.")
				else:
					showerror("Error","Salary should be more than 8K.")
			else:
				showerror("Error","Enter Valid Name,Name must have 2 or more alphabets.")	
		else:
			showerror("Error","Enter valid ID,ID should be postive.")
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()
def f10():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["my_12jan23"]
		coll=db["employee"]
		id=int(dw_ent_id.get())
		count=coll.count_documents({"_id":id})
		if(id>0) and (id.isnumeric()):
			if count==1:
				coll.delete_one({"_id":id})
				showinfo(id," ID Deleted")
			else:
				showerror(id,"Enter Valid ID.")
		else:
				showerror(id,"ID should be positive and a Number.")
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()
		dw_ent_id.delete(0,END)
		dw_ent_id.focus()
def f11():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["my_12jan23"]
		coll=db["employee"]
		id=int(uw_ent_id.get())
		count=coll.count_documents({"_id":id})
		if count==1:
			info={}
			name=(uw_ent_name.get())
			salary=float(uw_ent_salary.get())
			if((name.isalpha()) and (len(name) >=2)): 
				if(salary>8000) and (salary.isnumeric()):
					info["name"]=name
					info["salary"]=salary
					ndata={"$set":info}
					coll.update_one({"_id":id},ndata)
					showinfo(id,"updated")
				else:
					showerror("Error","Salary should be more than 8K")
			else:
				showerror("Error","Enter Valid Name,Name must have 2 or more alphabets.")	
		else:
			showerror("id"," ID does not exists")
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()
def f12():
	con=None
	try:
		con=MongoClient("mongodb://localhost:27017")
		db=con["my_12jan23"]
		coll=db["employee"]
		graph = list(coll.find().sort("salary",-1).limit(5))
		df_mango = pd.DataFrame(graph)
		df_mango.plot(kind="bar",x="name",y="salary",color="DarkMagenta")
		plt.xlabel("Employee")
		plt.ylabel("Salary")
		plt.show()
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()

#========================================================
btn_add=Button(root,width=15,text="Add",font=f,bd=3,bg="grey",command=f1)
btn_add.pack(pady=10)
btn_view=Button(root,width=15,text="View",font=f,bd=3,bg="grey",command=f3)
btn_view.pack(pady=10)
btn_update=Button(root,width=15,text="Update",font=f,bd=3,bg="grey",command =f5)
btn_update.pack(pady=10)
btn_delete=Button(root,width=15,text="Delete",font=f,bd=3,bg="grey",command=f7)
btn_delete.pack(pady=10)
btn_charts=Button(root,width=15,text="Charts",font=f,bd=3,bg="grey",command=f12)
btn_charts.pack(pady=10)
lab_ct=Label(root,text="Location:"+      city    +"    Temp: " +  str(temp)    ,font=f,bg="grey")
lab_ct.pack(pady=10)

#========================================================
aw=Toplevel(root)
aw.title("Add Emp")
aw.geometry("500x500+50+50")
aw.configure(bg="powder blue")
f=("Arial",20,"bold")

aw_lab_id=Label(aw,text="Enter ID: ",font=f)
aw_ent_id=Entry(aw,font=f)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name=Label(aw,text="Enter Name: ",font=f)
aw_ent_name=Entry(aw,font=f)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary=Label(aw,text="Enter Salary:",font=f)
aw_ent_salary=Entry(aw,font=f)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)

aw_save_btn=Button(aw,text="Save",font=f,command=f9)
aw_save_btn.pack(pady=10)
aw_back_btn=Button(aw,text="Back",font=f,command=f2)
aw_back_btn.pack(pady=10)
aw.withdraw()

#=========================================================
vw=Toplevel(root)
vw.title("View Emp")
vw.geometry("500x500+50+50")
vw.configure(bg="Wheat")
f=("Arial",15,"bold")

vw_st_data=ScrolledText(vw,width=38,height=10,font=f)
vw_back_btn=Button(vw,text="Back",font=f,command=f4)
vw_st_data.pack(pady=10)
vw_back_btn.pack(pady=10)
vw.withdraw()

#============================================================
uw=Toplevel(root)
uw.title("Update Emp")
uw.geometry("500x500+50+50")
uw.configure(bg="papaya whip")
f=("Arial",20,"bold")

uw_lab_id=Label(uw,text="Enter ID: ",font=f)
uw_ent_id=Entry(uw,font=f)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name=Label(uw,text="Enter Name: ",font=f)
uw_ent_name=Entry(uw,font=f)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary=Label(uw,text="Enter Salary:",font=f)
uw_ent_salary=Entry(uw,font=f)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)

uw_save_btn=Button(uw,text="Save",font=f,command=f11)
uw_save_btn.pack(pady=10)
uw_back_btn=Button(uw,text="Back",font=f,command=f6)
uw_back_btn.pack(pady=10)
uw.withdraw()

#===========================================================
dw=Toplevel(root)
dw.title("Delete Emp")
dw.geometry("500x500+50+50")
dw.configure(bg="RoyalBlue1")
f=("Arial",20,"bold")

dw_lab_id=Label(dw,text="Enter ID: ",font=f)
dw_ent_id=Entry(dw,font=f)
dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)

dw_save_btn=Button(dw,text="Save",font=f,command=f10)
dw_save_btn.pack(pady=10)
dw_back_btn=Button(dw,text="Back",font=f,command=f8)
dw_back_btn.pack(pady=10)
dw.withdraw()


root.mainloop()