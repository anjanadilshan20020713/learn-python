# def func(length,width,top):
#     perimeter = 2*(length*width)+2*(width*top)+2*(top*length)
#     area = length*width*top
#     print("perimeter is = ",perimeter)
#     print("area is = ",area)
# func(23,23,23)

# def student(subject,marks,friend)
#     print("subject = ",subject)
#     print("marks = ",marks)
# student("maths",34)

# def student(subject,marks,friend):
#     print("subject = ",subject)
#     print("marks = ",marks)
#     print("friend   = ",friend)
# student("maths",34,"kamak")

# def student(subject,marks,*friend):
#     print("subject = ",subject)
#     print("marks = ",marks)
#     print("friend   = ",friend)
# student("maths",34,"kamak","nimal","sunism")

# def student(subject = "physics",marks = 23,*friend):
#     print("subject = ",subject)
#     print("marks = ",marks)
#     print("friend   = ",friend)
# student("maths")

# def student(subject,marks,**friend):
#     print("subject = ",subject)
#     print("marks = ",marks)
#     print("friend   = ",friend)
# student("maths",34,kmal=34,niml=45)

def student(subject,marks,**friend):
    print("subject is = ",subject)
    print("mark = ",marks)
    for key,value in friend.items():
        print(key,"=",Value)
    student("maths",34,kaml=88,nima=88,djff=788)
    