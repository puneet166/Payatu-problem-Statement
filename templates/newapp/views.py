

# Create your views here.
import pandas as pd
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
import docx
from pdf2docx import Converter
from docx2pdf import convert 
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
def home (request):
    return render(request,'index.html')

def registration(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect("registration")
        
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email id taken')
                return redirect("registration")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save();
                messages.info(request,'Done')
                return redirect("login")
                
        else:
            messages.info(request,'Password not match')
            return redirect("registration")
        return redirect('/')

    else:
        return render(request,'registration.html')
def login(request):
    if request.method== 'POST':
         username=request.POST['username']
         password=request.POST['psw']
         user=auth.authenticate(username=username,password=password)
         

         if user is not None:
             auth.login(request,user)
             return redirect("/")
         else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
         return render(request,'login.html')
        
def processing(request):
    if  request.user.is_authenticated:
        if request.method== 'POST':
            
                data_file=request.POST['datafile']
                tem_file=request.POST['datafile1']
                data=pd.read_csv(data_file+'.csv')
                answer = request.POST['dropdown'] 
                
                
                for ii in range(len(data)):
                    doc = docx.Document(tem_file+'.docx')
                    for paragraph in doc.paragraphs:
                                        if "{{client_name}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{client_name}}",data.iloc[ii]['client_name'] )
                                            paragraph.text = new_text
                                        if "{{year_count}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{year_count}}",str(data.iloc[ii]['year_count']))
                                            paragraph.text = new_text
                                        if "{{spoc_name}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{spoc_name}}", data.iloc[ii]['spoc_name'])
                                            paragraph.text = new_text
                                        if "{{initial_price}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{initial_price}}",str(data.iloc[ii]['initial_price']))
                                            paragraph.text = new_text
                                        if "{{discount_rate}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{discount_rate}}", str(data.iloc[ii]['discount_rate']))
                                            paragraph.text = new_text
                                        if "{{final_pricing}}" in paragraph.text:
                                            orig_text = paragraph.text
                                            new_text = str.replace(orig_text, "{{final_pricing}}", str(data.iloc[ii]['final_pricing']))
                                            paragraph.text = new_text
                     
                    doc.save(tem_file+"_"+data.iloc[ii]['client_name']+".docx")
                   
                    some_var = request.POST.getlist('Executive_Summary')
                    if(len(some_var)!=4):
                        convert(tem_file+"_"+data.iloc[ii]['client_name']+".docx") 
                        
                        os.remove(tem_file+"_"+data.iloc[ii]['client_name']+".docx")

                        pages=[]
                    
                        pages_con={'ES':[3],'CO':[4],'MA':[7],'APP':[15,16,17,18]}
                        
                    

                        if('ES' not in some_var):
                                pages=pages+pages_con['ES']
                                print("ES")
                        if('CO' not in some_var):
                                print("CO")
                                pages=pages+pages_con['CO']
                        if('MA' not in some_var):
                                print("MA")
                                pages=pages+pages_con['MA']
                        if('A' not in some_var):
                                print("A")
                                pages=pages+pages_con['APP']
                    
                        
                        
                        infile = PdfFileReader(tem_file+"_"+data.iloc[ii]['client_name']+".pdf", 'rb')
                        
                        output = PdfFileWriter()

                        for i in range(infile.getNumPages()):
                            if i not in pages:
                                p = infile.getPage(i)
                                output.addPage(p)
                            with open(tem_file+"_"+data.iloc[ii]['client_name']+".pdf", 'wb') as f:
                                output.write(f)

                        
                        if(answer=='20'):
                            

                            pdf_file = tem_file+"_"+data.iloc[ii]['client_name']+".pdf"
                            docx_file = tem_file+"_"+data.iloc[ii]['client_name']+".docx"

    # convert pdf to docx
                            cv = Converter(pdf_file)
                            cv.convert(docx_file, start=0, end=None)
                            cv.close()
                            os.remove(tem_file+"_"+data.iloc[ii]['client_name']+".pdf")
                            

            
                return render(request,'final.html')
        else:
            return render(request,'GUI.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')