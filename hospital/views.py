from django.shortcuts import render,redirect,get_object_or_404
from hospital.models import Hospital,Department,Bed
from hospital.forms import HospitalForm,DepartmentForm,BedForm
from hospital.forms import BedForm,DepartmentForm,HospitalForm

# Create your views here.

# hospital list
def hospital_list(request):
    hospital = Hospital.objects.all()
    return render(request,'hospital/hospital_list.html',{'hospital':hospital})


# hospital details
def hospital_details(request,id):
    hospital = get_object_or_404(Hospital, id=id)
    department = hospital.department.all()
    beds = hospital.bed.all()
    return render(request,'hospital/hospital_detail.html',{'hospital': hospital,'department':department,'beds':beds})


#add hospital
def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request,'hospital/hospital_form.html',{'form':form})

#show thw hospital
def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request,'hospital/hospital_list.html',{'hospitals':hospitals})

# update hospital 
def update_hospital(request,id):
    hospital = get_object_or_404(Hospital,id=id)
    if request.method =='POST':
        form = HospitalForm(request.POST,request.FILES,instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_detail',id=hospital.id)
    else:
        form = HospitalForm(instance=hospital)
    return render(request,'hospital/hospital_form.html',{'form':form,'hospital':hospital})

# delete hospital
def delete_hospital(request,id):
    hospital = get_object_or_404(Hospital,id=id)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')

    return render(request,'hospital/hospital_delete.html',{'hospital':hospital})

# add department
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
            department = form.save()
            return redirect('hospital_detail',id=department.hospital.id)
    else:
        form = DepartmentForm()
    return render(request,'hospital/department_form.html',{'form':form})


# add bed
def add_bed(request):
    if request.method == 'POST':
        form = BedForm(request.POST,request.FILES)
        if form.is_valid():
            bed = form.save()
            return redirect('hospital_detail',id=bed.hospital.id)
    else:
        form = BedForm()
    return render(request,'hospital/bed_form.html',{'form':form})


#update bed and department

# def update_department(request,id):
#     department = get_object_or_404(Department,id= id)
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST,request.FILES,instance=department)
#         if form.is_valid():
#             form.save()
#             return redirect('hospital_detail',id= department.hospital.id)
#     else:
#         form = DepartmentForm(instance=department)
#     return render(request,'hospital/department_form.html',{'form':form,'department':department})



# def update_bed(request,id):
#     bed = get_object_or_404(Bed,id= id)
#     if request.method == 'POST':
#         form =BedForm(request.POST,request.FILES,instance=bed)
#         if form.is_valid():
#             form.save()
#             return redirect('hospital_detail',id=bed.hospital.id)
#     else:
#         form = BedForm(instance=bed)
#     return render(request,'hospital/bed_form.html',{'form':form,'bed':bed})


def delete_department(request, id):
    department = get_object_or_404(Department, id=id)

    hospital_id = department.hospital.id

    if request.method == 'POST':
        department.delete()
        return redirect('hospital_detail', id=hospital_id)

    return render(
        request,
        'hospital/delete_department.html',
        {'department': department}
    )