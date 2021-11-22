import re
import time
def welcome(n="User"):
    print("\n\n\nHello "+n+"! Welcome to Career Guide!\n")
    n1=input("Do you want to login as a new user?[Y/N]: ")
    if((n1=="Y") or n1=="y"):
         details()    
    else:
        mainstuff()      
def details():
    name=input("Enter Name: ")
    flag=1
    while(flag!=0):
        age=int(input("Enter Age: "))
        if((age>0) or (age<100)):
            flag=0
            continue
        else:
            print("Enter a valid age")
    flag=1
    while(flag!=0):
        email=input("Enter Email ID: ")
        import re
        if re.match("^.*[@yahoo.com][@gmail.com][@hotmail.com]$",email):
            flag=0
        else:
            print("Invalid Email !\n")
    flag=1
    while(flag!=0):
        phone=input("Enter Phone Number: ")
        if(len(phone)!=10):
            print("Invalid Phone Number !")
        else:
            flag=0
    changedetails(name,age,email,phone)
def changedetails(name,age,email,phone):
    flag=1
    while(flag!=0):
            e=input("Do you want to make any changes to your information? [Y/N]: ")
            if((e=="Y") or (e=="y")):
                e1=int(input("What do you want to change?\n1.Name\n2.Age\n3.Email\n4.Phone Number\n"))
                if(e1==1):
                    name=input("Enter Name: ")    
                elif(e1==2):
                    age=int(input("Enter Age: "))
                elif(e1==3):
                    flag1=1
                    while(flag1!=0):
                        email=input("Enter Email ID: ")
                        import re
                        if re.match("^.*[@yahoo.com][@gmail.com][@hotmail.com]$",email):
                            flag1=0
                        else:
                            flag1=1
                            print("Invalid Email !\n")
                elif(e1==4):
                    flag1=1
                    while(flag1!=0):
                        phone=input("Enter Phone Number: ")
                        if(len(phone)!=10):
                            print("Invalid Phone Number !")
                            flag1=1
                        else:
                           flag1=0  
                else:
                    print("Enter a Valid Input!")
            elif((e=="N") or (e=="n")):
                flag=0

    print("Hello "+name+"! Welcome to Career Guide!.\n")
    mainstuff();
def mainstuff():
    print("CONTENTS:\n")
    ch=input("1.Choose a profession\n2.Discover your interests\n3.Colleges\n4.Further Studies\n5.Jobs\n")
    if(ch=="1"):
        option1()
        e2=input("\nBack to Contents ?[Y/N]: \n")
        if((e2=="Y") or (e2=="y")):
            mainstuff()
        else:
            e22=input("Alright then! Press Y to go back to Contents anytime ! ")
            if((e22=="Y") or (e22=="y")):
                mainstuff()
    if(ch=="2"):
        option2()
        e2=input("\nBack to Contents ?[Y/N]: \n")
        if((e2=="Y") or (e2=="y")):
            mainstuff()
        else:
            e22=input("Alright then! Press Y to go back to Contents anytime ! ")
            if((e22=="Y") or (e22=="y")):
                mainstuff()
    if(ch=="3"):
        option3()
        e2=input("\nBack to Contents ?[Y/N]: \n")
        if((e2=="Y") or (e2=="y")):
            mainstuff()
        else:
            e22=input("Alright then! Press Y to go back to Contents anytime ! ")
            if((e22=="Y") or (e22=="y")):
                mainstuff()
    if(ch=="4"):
        option4()
        e2=input("\nBack to Contents ?[Y/N]: \n")
        if((e2=="Y") or (e2=="y")):
            mainstuff()
        else:
            e22=input("Alright then! Press Y to go back to Contents anytime ! ")
            if((e22=="Y") or (e22=="y")):
                mainstuff()
    if(ch=="5"):
        option5()
        e2=input("\nBack to Contents ?[Y/N]: \n")
        if((e2=="Y") or (e2=="y")):
            mainstuff()
    if(ch=="escape"):
        print("Thank You! Have a great day!")
def option1():
    print("Pick a professsion!\n")
    w1=int(input("1.Aerospace & Aviation\n2.Agriculture,Horticulture & Allied Services\n3.Animation,Multimedia & Web Desgning\n4.Arts(Fine/Visual/Performing)\n5.Banking & Insuarance\n"))
    if(w1==1):
        print("\nSo, you chose Aerospace & Aviation ! Look at all the careers available: \n")
        s=int(input("1.Airport Manager\n2.Air Force Officer\n3.Air Traffic Controller\n4.Pilot\n5.Airline Ticketing Agent\n6.Flight Instructor\n7.Helicopter Pilot\n8.Airport Operations Manager\n9.Ground Staff\n10.Aviation Consultant\n11.Ferry Pilot\n12.Airline Customer Servie Agent\n13.Air Freight Manager\n14.Air Hostess\n"))
        if(s==1):
            print("Airport Manager manages and oversees the daily operations of an airport. Their job role is to enforce the Federal Aviation Administration (FAA) rules, manage security, negotiate airport contact and leases. They are responsible for supervising the staff, implementing operating procedures, coordination renovation projects, monitoring airport expenditures and others.\nThey have to take care of multiple roles, from ensuring that all the departments of the airport are functioning and are in coordination with one another. They also assign the daily work and projects to the staff or supervising the construction work. Sometimes they are also required to work with airlines and shuttle services if their job demands them to do so.\nAlso, it is very important for airport managers to have good interpersonal and organizing skills as they spend a lot of time interacting with others. Knowledge of different languages is an asset for an Airport Manager as they have to communicate with people from all over the world.")
            print("\n\nEligibility to become Airport Manager\nStep-1: To become an airport manager one should have a bachelor’s degree in the aviation or the related field.Ideally, the programme should be a four-year degree course and must include subjects such as aerodynamics, physics, aviation sciences, economics, finance, and management.\nSome students can also opt for aviation diplomas and courses.\n\nStep-2: However, after completing formal education it is very important for graduates to earn some professional experience in airport administrative before being qualified for work as airport managers.\nThey require hands-on-training to learn about managing and supervising personnel, ensuring airport security, etc.\n\nStep-3: The third and final step in the process of becoming an airport manager is to obtain the certification- Accredited Airport Executive (AAE).Most of the employers prefer candidates with AAE certification.To obtain the same it is mandatory for candidates to have a bachelor’s degree and one year of professional expeence in the respective field.However, candidates who do not have a bachelor's degree must have at least eight years of airport management experience.\n\nAdditional Requirements: Apart from this, candidates are also required to appear in a multiple choice exam and a personal interview to qualify for the position of an airport manager.\n\n")
        if(s==2):
            print("\nIndian Air Force is one of the major air arms across the country and its main job is to guard the country against external aggression in the air.\nFighter planes and aircraft are the major constituents of the Air Force as their job is to defence the sky.\nTherefore the entire services of the Airforce are concerned with the flying of the aircraft and the pilot is the main air force officer.\n")
            print("\n\nCareer Path:1 The first way is to join National Defence Academy, Pune which mainly trains cadets in three services.To get through NDA a competitive examination is held twice a year i.e. in February and September. Only unmarried male candidates till 19 years of age can apply for the same. They should be class 12th pass or equivalent examination with physics and maths as mandatory subjects. National Defence Academy, Pune, trains cadets for the 3 services. A competitive examination is held twice in a year, in February & September, for a 3-year training course commencing in January and July. Only unmarried male candidates age between 16 1/2 and 191/2  years are eligible.\n (XI with Physics & Maths) .\nCareer Path: 2 Both male and female candidates can apply for the same between 20-24 years of age. They are required to pass NCC Air Wing Senior div C Certificate. Candidates must have a bachelor's degree in any field with a minimum of 60% marks from a recognised university.\nCareer Path:3 Short Service Commission is for the candidates who wish to become the technical officers in the Air Force. Candidates must have a bachelor’s degree in any field and must have cleared the AFCAT examination. Both male and female candidates between 20-24 years of age can apply.\n")
        if(s==3):
            print("\nAir traffic controllers coordinate the movement of aircraft to maintain the safe distances between the aircraft. Their primary concern is safety, but they also must direct aircraft efficiently to minimize delays. They manage the flow of aircraft into and out of the airport airspace, guide pilots during takeoff and landing, and monitor aircraft as they travel through the skies for security purposes. Air traffic controllers use radar, computers, or visual references to monitor and direct the movement of the aircraft in the skies and ground traffic at airports.\n\n")
            print("Eligibility to become Air Traffic Controller: \nAspirants who are planning to become air traffic controller must have a bachelor’s degree (B.Sc in Science) with physics and mathematics as mandatory subjects or B.Tech/B.E. degree in any field can apply for the post of Junior Executive Controller (ATC). The minimum pass percentage to apply for ATC is 60 percent.\n UG Courses:\n1. Candidate must have a B.Sc in Science or B.Tech/B.E. degree with a minimum aggregate of 60%. However, the minimum aggregate rules vary from category to category.\n2. Candidates have to appear in the written test, voice test and medical test.\n 3.The age criteria for general category candidates is 27 years whereas for reserved category candidates it is 32 years and for OBC candidates it is 30 years to apply for the ATC.\n\n")
        if(s==4):
            print("The backbone of the aviation industry are the pilots. They are the professionals who are responsible for operating the aircraft and managing and maintaining the internal systems of the aircraft.\nPilots usually fly to carry passengers and goods from one destination to the other. But this is not the only work that a pilot does, he/she is also responsible for checking the management of the cockpit, keeping a keen look on the air regulation, planning flights and checking the air traffic as and when required.\nThere are more distinctive job roles that a pilot performs apart from the ones that have been mentioned.")
            print("Eligibility to become Pilot:\nA basic criterion is to have a 12th pass certificate from a certified and recognized institution. For better insight read the details given below.\nSubject Combination – Science Stream in 10+2 \nExam – IGRUA, ATPL, Institutions Exams, etc.\nEligibility : \n1.Candidates interested in pursuing different pilot courses must have a passing certificate of 10+2 from a recognised institution.\n2.It is important for candidates to be from Science stream with Physics and Mathematics as main subjects.\n3.Candidates must have at least 50 percent in 10+2.\n4.Marksheet of other qualifying examination as required by the institutions must also accompany candidates at the time of admission.\n")
        if(s==5):
            print("An Airline Ticketing Agent is an individual who is responsible for booking flight tickets and handle reservations for customers.\nAirline Ticketing Agents directly interact with customers, answer customer questions about flight timings, seat availability, fares, reservations etc.\nThey also handle key operations such as data collection, data entry, payment collection and verification etc. for airlines.\nAirline Ticketing Agents work as ground staff on airports and should be open for working long hours in shifts while standing on their feet.\n")
            print("Eligibility to become Airline Ticketing Agent Airline Ticketing Agent is an entry-level job that is usually available for candidates after completing High School (or Class 10th).\nCandidates can apply with the High School certificates for the job. Diploma courses are also available catering to a student who wishes to take up a career as an Airline Ticketing Agent.\nSome of the requirements posed by airlines for Airline Ticket Agent jobs include: Candidate must have completed Class 10th Candidate must have completed at least 18 years of age (varies by the recruiting company) Candidates are required to demonstrate a basic knowledge of computers and good typing skills Apart from these, good communication skills and basic mathematical skills are required for the job.\nCandidates interested in joining an airline as an Airline Ticketing Agent can also pursue the following courses.\nDiploma in Airline Ticketing Diploma in Travel and Tourism Management Diploma in International Travel, Tourism and Hospitality Management etc. Candidates must note that these courses are usually available at the 10 +2 / Class 12th level.\n\n")
        if(s==6):
            print("A Flight Instructor trains a student on every aspect of flying an aircraft. Mostly, the aircraft training provided by a flight instructor includes training in aeroplanes and helicopters only.\nThe instructions provided by a flight instructor cover a wide range of subjects related to flying. These include theoretical knowledge about flying such as information on aerodynamics, use and functioning of the equipment in a cockpit etc.\n\n")
            print("Eligibility to become Flight Instructor\nThe post of Flight Instructor is very heavily regulated by the DGCA. Students who are interested in becoming a flight instructor must satisfy the requirements specified by DGCA. DGCA grants two levels of ratings to flight instructors in India —- AFIR and FIR i.e. Assistant Flight Instructor Rating and Flight Instructor Rating. Some of the points are common to both the rating while others are more specific Let’s take a look at the common criteria fist before going further into the specifics of each rating. \n1.Candidate must have a valid and appropriate CPL or professional pilot’s licence, \n2.Candidate must have a Class 1 Medical Certificate. \n3.Candidate must have an ATPL, which can be gained after passing in an oral exam conducted by DGCA. \n4.Candidate must have an FTROL, which is issued to a candidate who has completed a written examination in the specified subjects related to flying.\n \nNow, here are the criteria specific for both posts. \nFor AFIR\n 1.Candidate must be at least 18 years of age. \n2.Candidate must have a satisfactory level of experience in flying. The details can be found below, \n3.For aeroplane: At least 100 hours of flight time as Pilot-in-Command (PIC) with a minimum of 20 hours completed in the last 18 months. \n4.For a helicopter: A minimum of 50 hours of flight time as PIC with at least 20 hours withing the last eighteen months. \nAt least 20 hours of Patter Flying (i.e. Instructor Rating Course) \nFor FIR \n1.Only a person who has worked as an AFI can be granted an FIR by DGCA. For a FIR, a candidate must satisfy the following minimum requirements. \na.At least 20 years old. \nb.Candidate must have sufficient flying experience the details of which can be found given below. \nc.20 hours of flight time as PIC with at least 20 take-offs and 20 landings. \nd.Min. 200 hours of flight time on aeroplanes or 100 hours of flight time on helicopters as an AFI or a Qualified Flight Instructor in the Defence Forces.\n")
            print("OR \nCandidate must have the following levels of flying experience. \nFor aeroplane: 500 hours as PIC \nFor helicopters: 150 hours as PIC \nIn addition, candidates are also required to have completed a Flight Instructor course from a DGCA-approved institution within the last six years. \nAnother important thing to note is that the ratings of AFIR and FIR remain valid for 12 months after which, an AFI or FI will need to get it renewed from the DGCA as per regulations.\n")
        if(s==7):
            print("A Helicopter Pilot is a professional who has trained and holds a license to fly a helicopter in India. Only people who hold a valid license approved by DGCA (Directorate General of Civil Aviation) are eligible to fly helicopters or any other aircraft in India. Becoming a helicopter pilot in India is an interesting choice especially for a person that is passionate about flying. The career is thrilling and presents its own unique challenges. However, it can prove to be a very rewarded career not only in terms of money but also for job satisfaction.\n")
            print("Eligibility to become Helicopter Pilot\nSince DGCA is the only body that issues Pilot Licenses in India, it is the body specifies the conditions for a person to be eligible to be issued a Helicopter Pilot License in India. The detailed eligibility criteria for a PL (H) in India can be found below.\nCommercial Helicopter Pilot License CPL(H) Eligibility Criteria Educational Qualification:\nPassed Class 12th from a recognized with Physics and Mathematics Medical Fitness\nCandidate must have a Class I medical fitness certificate issued by a DGCA approved doctor or medical establishment.\nAge Limit\nCandidate applying for a CPL must be at least 17 years of age at the time of application. Private Helicopter Pilot License PPL(H)\nEligibility Criteria Educational Qualification:\nPassed Class 10th from a recognized board Medical Fitness	Candidates must have obtained a Class II medical fitness certificate issued by a doctor or medical establishment approved by the DGCA. Age Limit\nCandidate must be a minimum of 16 years of age at the time of applying for a PPL.\n")
        if(s==8):
            print("An Airport Operations Manager is a person who oversees the daily operations of an airport. He / she is responsible for ensuring that an airport is functioning as planned and all of the operations are in compliance with the prescribed regulations and policies.\n\n")
            print("In order to be eligible for the role of an Airport Operations Manager in India, the minimum qualification is a bachelor’s degree. Candidates having an academic qualification related to the management stream may be preferred for these roles. Depending on the level of the airport as well as the seniority level of the position, candidates may also be required to have completed a master’s degree and / or have relevant work experience in a related field.\n")
        if(s==9):
            print("Ground Staff are responsible for attending to the passengers before, after and in between the flight. They are also responsible for solving the queries of the passengers, providing flight information and ensuring that they face no difficulties during the flight. Ground Staff is a major part of the aviation industry and they cannot be replaced with machines or computers. Some of the major responsibilities performed by the ground staff are checking passengers for the flight, assisting the passengers who are with children and disabled passengers, handling the unloading and loading of passengers luggage from the aircraft, carrying security check activities as regular interval, updating passengers with timings and change in the flight schedule, preparing the flight plan according to the weather condition and climate of the destination and origin and re-booking the passengers whose flights have been delayed.\n")
            print("Eligibility to become Ground Staff Check the minimum eligibility criteria for a career as a Ground Staff provided below.\nAcademic Qualification: Candidates who are looking for a career in ground staff must have cleared 12th from any recognised institution or university. The job description for this position will vary depending on the type of industry. There is no additional requirement for Ground Staff. However, candidates who are aiming for a successful career in Ground Staff can check some degree essential for this profile provided below. Diploma in Airport Ground Staff Training Post Graduate Diploma in Airport Ground Staff Training Experience: Since most of the companies prefer experienced candidates, it is advisable that candidates gain some experience before applying for any senior-level positions in ground staff. They can complete any training program in ground staff or any other aviation related course to gain some experience. Skills: Candidates should have some experience in customer service while looking for a career in ground staff. There are many other skills which can help the candidates have a successful career in ground staff. Some relevant skills are provided below. Communication skills Planning/ Organizing Responsibility Teamwork Problem-solving skills Interpersonal abilities Flexibility Soft skills Management skills Professional/ Technical technique\n\n")
        if(s==10):
            print("Aviation Consultant is a person who works with the aviation industry and provides solutions to technical and complicated issues. He also helps the company understand the best form of aviation practices in recent times. Some major responsibilities of an Aviation Consultant are implementing safety measures that employees and other staff members of the company have to follow for the smooth operation of the aircraft, establishing new strategies and policies to achieve the goal, analysing the performance and progress of all aircraft activities, presenting reports to the client, providing solutions to the problems of the client and ensuring the maintenance of the aircraft control system.\n")
            print("\nEligibility to become Aviation Consultant Check the minimum eligibility criteria for a career as an Aviation Consultant provided below. Academic Qualification: Candidates must have cleared a bachelor's degree in aviation management or airport management to get a job as an Aviation Consultant. Candidates who have completed a bachelor's with aviation regulations, air traffic control systems, transportation legislation and airport management as the main subject will be preferred. Experience: You should have some experience in the aviation industry while applying for a job as an Aviation Consultant. They can enrol for any training or certification program in the aviation industry to understand the principles of the industry. Skills: Career as an Aviation Consultant requires some additional skills apart from academic knowledge. Some of the required skills for an Aviation Consultant are listed below. Creative thinking Problem-solving Self-awareness Team Work Analytical Skills Good Communication Decision Making Adaptability Skills\n")
        if(s==11):
            print("\nA Ferry Pilot is a person who transports an aircraft from one place to another. He is responsible for the transportation of new or used aircraft from manufactures to the purchaser. He also transports the plane to a location for maintenance or to provide assistance in case of emergency situations. A ferry pilot takes care of the transportation of the aircraft within the time limit. He is mostly hired by cargo companies for the transportation of flights or planes that needs maintenance and to complete the delivery of the buyer. A ferry pilot makes sure that all the safety functions are working properly. Candidates who are looking for this job must have a good knowledge of flight management and working of the airline industry.\n")
            print("A Ferry Pilot is a person who transports an aircraft from one place to another. He is responsible for the transportation of new or used aircraft from manufactures to the purchaser. He also transports the plane to a location for maintenance or to provide assistance in case of emergency situations. A ferry pilot takes care of the transportation of the aircraft within the time limit. He is mostly hired by cargo companies for the transportation of flights or planes that needs maintenance and to complete the delivery of the buyer. A ferry pilot makes sure that all the safety functions are working properly. Candidates who are looking for this job must have a good knowledge of flight management and working of the airline industry.\n")
        if(s==12):
            print("An Airline Customer Service Agent is a person who assists the customers with itinerary changes, flight reservations and questions about customer loyalty programs. Besides this, he also helps passengers with providing flight information, issuing tickets, check-in, solving ticket related problems and checking baggage. An Airline Customer Service Agent also upgrades the seats and reissues seats for them when no seats are available in the flight. Besides this, he also checks the boarding passes of the passengers.\n")
            print("Eligibility to become Airline Customer Service Agent Check the minimum eligibility criteria for a career as an Airline Customer Service Agent provided below. Passed high school diploma or equivalent in relevant field Employers will prefer candidates who have completed a bachelor's degree in related fields Six months to one year of work experience is required Knowledge of some tools such as CRM, online chat software, contact centre software, customer relationship management software and Microsoft Office. Skills Required: Some of the necessary skills required to become an Airline Customer Service Agent are Good listening skills Excellent communication skills Customers service skills Good levels of fitness Team working skills\n")
        if(s==13):
            print("An Air Freight Manager is a person who oversees the goods delivery department of an airline company. He/she is responsible for ensuring that the correct procedures are being followed during operations such as the loading, storing and unloading of goods to and from an aeroplane. Since an Air Freight Manager managers the cargo operations of an airline company, the post is also referred to as Air Cargo Manager. The basic responsibility of an Air Freight Manager is to ensure that all of the goods are delivered in good shape to the correct receiver.\n")
            print("Air Freight Managers are generally expected to have a management-focused formal education. However, this varies widely from company to company and also because of the varied responsibilities that an Air Freight Manager might be expected to fulfil. Some companies consider a bachelor's degree (can be in any discipline) sufficient for Air Freight Managers while you might find others insisting on postgraduate education such as an MBA. Apart from that, work experience is one very essential condition for Air Freight Managers as it is a senior-level position and requires practical knowledge of the field.\n\n")
        if(s==14):
            print("The basic eligibility criteria for becoming an air hostess have been listed below. Aspirants must have passed class 12th or equivalent examination with a minimum aggregate of 45-50%. The minimum pass percentage varies from institute to institute. Only those aspirants who are between the age group of 17-26 years can apply. The candidate must be fluent in spoken English. The candidate's height should be at least 157.5 centimetres and weight should be proportionate to the height. He/ she must be eligible for an Indian Passport")
    if(w1==2):
        print("\nSo, you chose Agriculture,Horticulture & Allied Services! Look at all the careers available: \n")
        s=int(input("1.Horticulturist\n2.Pomologist\n"))
        if(s==1):
            print("Horticulturalists can find jobs as farming specialists in vineyards, agriculture estates and fruit orchards.The major job of a horticulturist is to assess forests and bush for rehabilitation and data gathering, harvest seeds and cultivate young trees and plants, collect field and control samples of roots, green matter and yields for analysis, measure forest and agricultural metrics on an ongoing basis, create and maintain onsite and offsite resources like nurseries, young forest sites, seeding, planting, greenhouse, process horticultural specimens and also work in remote locations in all weather conditions.\n")
            print("Eligibility to become Horticulturist: Many horticulturists major in horticulture, botany or biology. The career path of a horticulturist generally includes botany, plant biology, soil science, pest management, and genetics.\nTo become a horticulturist, one must attain the minimum academic benchmark as well as related experience. The academic qualifications required to become a horticulturist is stated below: Subject Combination – Science Stream (Physics, Chemistry and Maths/Biology/Agriculture) in Class XII. Exam – Horticulture Common Entrance Test (HORTICET), Vellanikara College of Horticulture Entrance Exam, Dr. Yashwant Singh Parmar University of Horticulture and Forestry Entrance Exam, MCAER PGCET. For Undergraduate Courses - To pursue a Bachelor’s course in horticulture sciences, candidates must clear class XII with the combination of physics, chemistry and mathematics/ biology/ agriculture. For Postgraduate Courses - For Master’s degree, candidates must have completed their undergraduation with minimum 60% marks. For Doctoral Courses -\nFor Ph.D. programmes, candidates must have PG/ masters degree in the relevant field.\nFor admissions in Ph.D. programmes, various universities conduct their own entrance examination.\n")
        if(s==2):
            print("A Pomologist studies various stages of fruit development and applies knowledge for effective fruit production.\nThey have a good understanding of the physical and chemical properties of fruits and trees that bear it. Pomologist who works as a scientist is specialised in plant genetics, maturation and pollination. They ensure the best yield of fruits in a specific area and have good knowledge of climatology which is an essential factor for the growth of plants.\n")
            print("Eligibility to become Pomologist: The academic qualification to become a Pomologist is given below: After Class 12th (Science), the candidate must pursue a bachelor’s degree inhorticulture, botany,  agricultural scienceor equivalent.\nThose who want to pursue a career as a scientist or researcher in fruits must pursue M.Sc in Pomology followed by a Ph.D in Pomology. Career Path While a relevant bachelors degree would provide an entry-level job to candidates, a postgraduate and doctorate level degree provides better career opportunities in the field of pomology After acquiring a relevant degree, an individual can apply for job roles in fruit production industries, the agriculture sector or private organisations. Based on skills and acquired knowledge a Pomologist can expect jobs in the field of fruit cultivation and research and development.\n")
    if(w1==3):
        print("\nSo, you chose Animation,Multimedia & Web Desgning ! Look at all the careers available: \n")
        s=int(input("1.Animator\n2.Multimedia Specialists\n3.Graphic Designer\n"))
        if(s==1):
            print("A career in animation is one of the most lucrative and most-sought-after courses these days. With attractive salaries and the personal freedom it offers, a career in animation could be the right choice for you. Both movies, video games, and other forms of media use computer animation.")
            print("Eligibility to become Animator:\nTo establish a career as an Animator, one must meet the eligibility criteria for it. The requirements that you need to fulfil for this career choice are mentioned below.\nFor taking up a Diploma course in Animation, a student must be a Class 12 pass out with at least 45% marks.\nThere is no entrance test for getting admission in animation courses. Most colleges offer direct admission.\n")
        if(s==2):
            print("Multimedia Specialists are the professionals who design and create IT-based multimedia products such as Websites, Computer Games, Graphics, Video Clips and other interactive multimedia formats.\n If you enjoy working with the latest interactive technology, a career as a multimedia specialist may be the ideal choice.\n")
            print("Eligibility to become Multimedia Specialists: In order to become a Multimedia specialist, candidates need to fulfil the following eligibility criteria:- \nCandidates must have a bachelor's degree or postgraduate degree in the same. Multimedia specialists must be equipped with the required technical skills including computer programming and graphics design.\nAs such, employers prefer highly trained candidates possessing a bachelor’s degree in computer science, web design, programming, or a related discipline.\nEntry-level positions often require associate degrees or certificates from focused certification programs.\n") 
        if(s==3):
            print("The job of a Graphic Designer includes designing layouts and select colours, images, and typefaces to use, incorporating changes recommended by clients or art directors into final designs, using digital illustration, photo editing software, and layout software to create designs and reviewing designs for errors (if any) before printing or publishing them.\n")
            print("Eligibility to become Graphic Designer:\n Qualification Required Candidates must have any degree or diploma in Graphic Design Students must have a wide understanding of Graphic Designing tools.\nAny certificate in the HTML, Photoshop, CSS or Web Design can act as an added advantage.\nCreative Skills Sound Communication Skills ,IT Skills, Critical Thinking Problem Solving Ability, knowledge of HTML, CSS, Photoshop etc.\nWork Experience Work experience is not required as long as you are creative, talented and capable.\n")
    if(w1==4):
        print("Artists are people who communicate their ideas or feelings through their art. They create unique works from their imagination.\nDepending on the area of specialization and experience, artists can be self-employed or can work in teams throughout the creative process to complete a project or create a product.\nTo be in this profession, one can choose his/her career as an illustrator, graphic designer, sculptor, or multimedia artist.\n")
        s=int(input("1.Artists(Fine Arts & Commercial Arts\n2.Beautician\n3.Content Writer\n"))
        if(s==1):
            print("Eligibility to become Artist (Fine Arts & Commercial Arts) For Commercial Artist Candidates must have completed class X followed by entry to 5 year degree courses art. Some art schools also offer art courses after class X. Candidates must have completed Class XII with any stream however, Art subject is preferred. Candidates must have a Bachelor’s degree/diploma in Art with specialization in the area of interest. Art schools also conduct entrance tests for school leavers for the degree courses called Bachelor of Fine arts (BFA). For Fine Artist Certificate Courses:\nThere is no specific eligibility criteria for such certificate courses. Candidates who are interested for a certificate course can directly apply for such courses. However, some institutes prefer those candidates who have cleared class 10 before applying for certificate courses in fine arts.\nDiploma and Bachelor Degree Courses:\nCandidates from all fields can apply for fine art courses after class 12. Admissions of the candidates are done on the basis of marks scored in class 12 and as per the merit list prepared by respective university. In order to test the skills of the candidate, some of the institutes may take a creative test in painting, drawing, etc.\nPG Diploma and Master Degree Courses: To be eligible to apply for this programme, candidates must have pursued bachelors in fine arts or B.A degree in the same field with at least 50% marks. Admissions are done either on the basis of marks scored in graduation or on the basis of written test.\nAdditionally, Group Discussions and Personal Interviews are conducted to assess candidates skills.\n") 
        if(s==2):
            print("Beauticians are professionals engaged in improving a client’s appearance through hair care, nail, beauty and skin care. Beauticians can often specialize in certain areas such as nail art, makeup application, hair color etc.\n")
            print("One can get trained to become a beautician after class 12th. There are a number of beauty training schools which offer courses and the duration of such courses is 9-24 months.\nHair care, nail care and a lot of other things are taught as a part of the course. People can also choose to get trained on the job, some spas and salons offer training to the employees and a lot of people can also continue to work and get more experience while others may start their own business after getting good experience and exposure.\n")
        if(s==3):
            print("Content writers can be defined as those who create content for the internet or someone who churns out engaging content for online use. In recent years, the demand for content writers has grown manifold with the expansion of the market.\nThere are various types of content writers in the job market today like the ones who write articles, blogs, scripts etc.\nA content writer is responsible for producing content of the highest quality for the organisation he/she works for.\n")
            print("Eligibility to become Content Writer:\n Here is a list of all the eligibility criteria required to be fulfilled by those who wish to become a successful content writer.\nThe aspirants must - Preferably have a Bachelor’s/Master’s degree in Journalism or Literature but degree holders in other specializations are also eligible possess excellent communication skills and writing skills both Have basic knowledge of things like web analytics, email marketing, SEO among all other digital marketing techniques.\n Be comfortable to meet the tight deadlines on a consistent basis\n")
    if(w1==5):
        print("\nSo, you chose Banking & Insurance ! Look at all the careers available: \n")
        s=int(input("\n1.Clerk\n2.Probationary Officer\n3.Loan Counsellor\n4.Insurance Agent\n5.Insurance Sales Agent\n"))
        if(s==1):
            print("A bank clerk plays a very significant role in the smooth functioning of the bank.\nSome of the daily tasks that a bank clerk has to perform are the following:\nPay Attention to Customer and their Requirements such as withdrawal slips.\nIssuing Cheque Books\nMaintaining and Updating Customer’s Record and Accounts\nHandling Deposits and Cash Withdrawals\nMaintain ledger, balance sheets, data entry")
            print("\nAn aspirant must fulfil the given eligibility criteria to become a Clerk:\nA candidate must have a bachelor’s degree as the minimum qualification criteria before applying for the Bank clerk exam.\nAge Criteria: The candidate must be 20-28 years old\nThey must have a valid bachelor’s degree from a recognised university.\nThey must not hold any criminal record while applying for the exam.\n")
        if(s==2):
            print("A Probationary Officer is the someone who is appointed for handling the overall banking management of a bank or company associated with the banking sector.\nThey are the entry-level employees who are promoted to the posts of Assistant Managers of Scale 1 of the bank after the completion of the probation or training period which is of minimum 2 years duration\n")
            print("Eligibility: Candidates must have a passing certificate of bachelor or master degree from a reputed and recognized institution.\nA valid scorecard of the Probationary Officer entrance examination is compulsory to engage in the selection process conducted by different banks and companies.\nCandidates must not hold any kind of criminal or civil offence record and must not possess any kind of negative track record.\nCandidates awaiting graduation or masters result or any other ongoing exam can also apply for the entrance examination.\n")
        if(s==3):
            print("A Loan Counsellor is a person who helps a potential client or borrower find the best loan and scheme for their needs. Loan counsellors act as the intermediary between the borrower and the bank or financial institution and provide information about the various loan schemes offered by the financial institution while also offering guidance on selecting the best loan schemes.\n")
            print("In order to become a loan counsellor in India, a candidate must have at least completed a bachelor’s degree course in a stream related to finance, accounting, economics, commerce etc.\nBanks and other financial institutions also prefer candidates who might have some work experience in related roles for this position.\n")
        if(s==4):
            print("Insurance Agents will be required to meet certain objectives and carry out certain roles, as mentioned below:\nAnalyse customer and client needs and offer appropriate services and insurance plans.\nProduce leads and follow up on them from time to time. Offer quotes to customers Bring in new customers and close sales between current customers\nNetworking and building relationships that promote their businesses.\n")    
            print("Here are the eligibility criteria for a career as an Insurance Agent \nCandidates must have a valid Bachelor-level degree in the field of management, insurance, banking or sales. A masters degree in these fields can also help the candidate to pursue more lucrative career paths.\nIt should be noted that candidates who cleared their class 12 board examination and have displayed impeccable skills in sales and marketing are also eligible to pursue a career as an Insurance Agent.\n")
        if(s==5):
            print("The job requires a lot of roaming around and Insurance Sales Agents often have to stay alert about any prospective opportunities for making a sale. To excel in this field, an agent must have a good knowledge of the market and scope of insurance and financial services. Having good knowledge of the field helps agents to provide accurate information to their clients and, through that, build trust for making a sale. Since insurance is a long-term investment, Insurance Sales Agents are also required to stay in touch with their clients and keep them updated with any required information.\n")
            print("For most of the cases, a bachelor's degree in any stream is enough to become an Insurance Sales Agent. Some companies may even hire candidates with Class 12th level of education. However, to rise in this field, candidates should ideally have a background in banking, insurance, finance, accounts or other related disciplines. Insurance Agents might also be required to have an MBA to be considered for senior management posts.\n")
    ch=input("Would you like to go back to Contents? [Y/N]")
    if((ch=="y") or (ch=="Y")):
        mainstuff()
    else:
        option1()
def option2():
    ch3=input("\n\nHey! Are you ready to discover what you're made of?[Y/N]\n")
    if((ch3=="Y") or (ch3=="y")):
        print("\nJump In !\n")
        r=0
        i=0
        a=0 
        s=0
        e=0 
        c=0

        print("\n Do you like to...")
        p1=input("...do puzzles?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...work on cars?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...attend concerts, theaters or art exhibits[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...work in teams?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            s+=1
        print("\n Do you like to...")
        p1=input("...organize things like files, offices or activities?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...set goals for myself?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1     
        print("\n Do you like to...")
        p1=input("...build things?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1    
        print("\n Do you like to...")
        p1=input("...read fiction, poetry or plays?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...have clear instructions to follow?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...influence or persuade people?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1
        print("\n Do you like to...")
        p1=input("...do experiments?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...teach or train people?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            s+=1
        print("\n Do you like to...")
        p1=input("...help people solve their problems?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            s+=1
        print("\n Do you like to...")
        p1=input("...take care of animals?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...have my day structured?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...sell things/items?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1
        print("\n Do you like to...")
        p1=input("...do creative writing?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...work on science projects?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...take on new responsibilities?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1
        print("\n Do you like to...")
        p1=input("...figure out how things work?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...put things together or assemble models?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...be creative?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...do filing or typing?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...learn about other cultures?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            s+=1
        print("\n Do you like to...")
        p1=input("...analyze things like problems, situations or trends?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...play instruments or sing?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...dream about starting my own business?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1
        print("\n Do you like to...")
        p1=input("...cook?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...act in plays?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...think things through before making decisions?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...work with numbers or charts?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            i+=1
        print("\n Do you like to...")
        p1=input("...have discussions about issues like politics or current events?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            s+=1
        print("\n Do you like to...")
        p1=input("...keep records of my work?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...be a leader?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1
        print("\n Do you like to...")
        p1=input("...work outdoors?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            r+=1
        print("\n Do you like to...")
        p1=input("...work in an office?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            c+=1
        print("\n Do you like to...")
        p1=input("...draw?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            a+=1
        print("\n Do you like to...")
        p1=input("...give speeches?[Y/N]")
        if((p1=="Y") or (p1=="y")):
            e+=1  
        print("\nYour Interest Assessment Results \n")
        print("R    =   REALISTIC       Total Points: ",r)
        print("I    =   INVESTIGATIVE   Total Points: ",i)
        print("A    =   ARTISTIC        Total Points: ",a)
        print("S    =   SOCIAL          Total Points: ",s)
        print("E    =   ENTERPRISING    Total Points: ",e)
        print("C    =   CONVENTIONAL    Total Points: ",c) 
    flag1=1
    while(flag1!=0):
        ch1=input("\nTake your pick! Which sector are you more inclined towards?\n1.REALISTIC\n2.INVESTIGATIVE\n3.ARTISTIC\n4.SOCIAL\n5.ENTERPRISING\n6.CONVENTIONAL\n")
        if(ch1=="1"):
            print("\nSo, you are more of a REALIST!\nRealistic people are DOERS. They are often good at mechanical or athletic jobs. They like to work with things like machines, tools or plants and they like to work with their hands.\n\nRelated Career Clusters:\nAgriculture,\nFood and Natural Resources Architecture and Construction Arts,\nA/V Technology and Communications Health Science Hospitality and Tourism Information Technology Law,\nPublic Safety,\nCorrections and Security Manufacturing Science,\nTechnology,\nEngineering and Mathematics Transportation,\nDistribution and Logistics\n")
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
            else:
                flag1=0
        if(ch1=="2"):
            print("\nSo, you are more of an INVESTIGATIVE person!\nInvestigative people are THINKERS. They like to analyze and solve problems. They often like to work independently and tend to be good at math and science.\n\nRelated Career Clusters:\nHealth Science Information Technology Law,\nPublic Safety,\nCorrections and Security Science,\nTechnology,\nEngineering and Mathematics\n")
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
            else:
                flag1=0
        if(ch1=="3"):
            print("\nSo, you are more of an ARTISTIC person!\nArtistic people are CREATORS. They like to work in situations where they can use their creativity and come up with new ideas. They enjoy performing (theater or music) and visual arts.\n\nRelated Career Clusters:\nArts,\nA/V Technology and Communications,\nEducation and Training,\nHospitality and Tourism,\nHuman Services Marketing,\nSales and Service\n")
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
            else:
                flag1=0
        if(ch1=="4"):
            print("\nSo, you are more of a SOCIAL person!\nSocial people are HELPERS. They like to work directly with people rather than things. They are often good public speakers and enjoy helping others.\n\nRelated Career Clusters:\nArts,\nA/V Technology and Communications,\nEducation and Training,\nGovernment and Public Administration,\nHealth Science,\nHuman Services Law,\nPublic Safety,\nCorrections and Security Marketing,\nSales and Service\n")   
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
            else:
                flag1=0
        if(ch1=="5"):
            print("\nSo, you are more of a ENTREPRENEUR!\nEnterprising people are PERSUADERS. They like to work with other people and enjoy being a leader. They particularly enjoy influencing, persuading and performing.\n\nRelated Career Clusters:\nArts,\nA/V Technology and Communications Business,\nManagement and Administration,\nFinance,\nGovernment and Public Administration,\nHospitality and Tourism Law,\nPublic Safety,\nCorrections and Security Marketing,\nSales and Service\n")
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
                flag1=0
        if(ch1=="6"):
            print("\nSo, you are more of a CONVENTIONAL person!\nConventional people are ORGANIZERS. They are very detail oriented and like to work with data and numbers.\n\nRelated Career Clusters:\nArchitecture and Construction Business,\nManagement and Administration,\nFinance,\nHealth Science,\nManufacturing Marketing,\nSales and Service Transportation,\nDistribution and Logistics\n")
            ch2=input("\nBack to going deep into your interests?[Y/N]:\n")
            if((ch2=="y") or (ch2=="Y")):
                option2()
            else:
                flag1=0
        else:
            flag1=0
def option3():
    w2=int(input("Pick A Choice!\n1. Bachelor of Technology (BTech)\n2. Bachelor of Architecture(BArch)\n3. Defense\n4. MBBS \n5. Law\n6. Chartered Accountancy\n"))
    if(w2==1):
        print("B.Tech Colleges in India \n 3727 B.Tech colleges in India offering 24608 courses B.Tech is one of the popular and sought after courses after 12th.\n Pursuing B.Tech from a top college is the aim of every student so that he/ she can land in the best job after graduation.\n While there are almost 5,000 B.Tech colleges in India, it is difficult to decide the best.\n Some of the popular states in India such as Tamil Nadu, Maharashtra, Andhra, Karnataka, Telangana, Uttar Pradesh, Delhi and Madhya Pradesh have a maximum number of engineering colleges (300+ in each state). B.Tech admission process in various states is based on state-level entrance exam / national-level entrance exam or direct admission process/management quota.\n\n")
        s=int(input("1. Government Colleges\n2. Private Colleges\n"))
        if(s==1):
            print("IIT Kharagpur \nIIT Mumbai	\nMotilal NIT Allahabad \nIIT Kanpu \nMaulana Azad NIT Bhopal \nIIT Madras	\nNIT Calicut \nIIT Delhi	\nNIT Durgapur \nIIT Guwahati	\nNIT Hamirpur \nIIT Roorkee \nMalaviya NIT Jaipur \nIIT Bhubaneswar	\nDr. B. R. Ambedkar NIT Jalandhar \nIIT Gandhinagar \nNIT Jamshedpur \nIIT Hyderabad	\nNIT Kurukshetra \nIIT Jodhpur	Visvesvaraya \nNIT Nagpur \nIIT Patna	\nNIT Patna \nIIT Ropar	\nNIT Raipur \nIIT Indore	\nNIT Rourkela \nIIT Mandi	\nNIT Silchar \nIIT (BHU) Varanasi	\nNIT Srinagar \nIIT Palakkad S V \nNIT Surat \nIIT Tirupati	\nNIT Karnataka, Surathkal \nIIT Dhanbad	\nNIT Tadepalligudem \nIIT Bhilai	\nNIT Trichy \nIIT Goa	\nNIT Warangal \nIIT Jammu	\nNIT Arunachal Pradesh \nIIT Dharwad	\nNIT Sikkim \nNIT Goa \nNIT Meghalaya \nNIT Nagaland \nNIT Manipur \nNIT Mizoram \nNIT Uttarakhand \nNIT Delhi \nNIT Pondicherry")
        if(s==2):
            print("BITS Pilani  \nVIT Vellore - Vellore Institute of Technology \nSRM University Chennai - SRM Institute of Science and Technology \nMIT Manipal - Manipal Institute of Technology \nLPU Jalandhar - Lovely Professional University \nNirma University, Ahmedabad \nVishwakarma Institute of Technology,Pune \nSIT Pune - Symbiosis Institute of Technology \nBMS College of Engineering, Bangalore")
    if(w2==2):
        print("B.Arch (Bachelor of Architecture) is an undergraduate degree in the field of architecture. \nThis five-year full-time programme is a blend of theorical and practical knowledge for students to learn the art of planning, designing and constructing physical structures of various kinds. \nFrom ideating to mapping and overseeing the construction, a qualified architect is involved at every stage of any construction project.")
        print("\n\n")
        print("Jindal School of Art and Architecture, O.P. Jindal Global University \nParul University, Vadodara \nIIT Kharagpur - Indian Institute of Technology,Kharagpur  \nNIT Trichy - National Institute of Technology,Tiruchirappalli \nCollege of Engineering, Trivandrum \nChandigarh University (CU) \nJawaharlal Nehru Architecture and Fine Arts University (JNAFAU) \n ")
    if(w2==3):
        print("India has a number of defence training institutions to train the youth for military services.\nThere are many academies and colleges to train professional soldiers in strategies and techniques of the military along with warfare command, military sciences, and related technology.\n")
        print("\nGovernment Nagarjuna Post Graduate College of Science, Raipur \nDhandai Mata Education Society's College of Arts, Jalgaon\n Guru Nanak College, Chennai\n Deendayal Upadhyaya Gorakhpur University, Gorakhpur \nBundelkhand University, Kanpur \nDr. Ambedkar Government Arts College, Tamil Nadu\n")
    if(w2==4):
        print("MBBS (Bachelor of Medicine and Bachelor of Surgery) is the most popular and designated degree of doctors. These are the two bachelor degrees in one domain as the Bachelor of Medicine and the Bachelor of Surgery.\n")
        print("\nAIIMS Delhi, Delhi \nCMC Vellore ( CMC VELLORE), Vellore \nMaulana Azad Medical College ( MAMC) , Delhi   \nArmed Forces Medical College ( AFMC) , Pune  \nKasturba Medical College ( KMC), Mangalore \nMadras Medical College ( MMC) , Chennai")
    if(w2==5):
        print("Law is a career stream that candidates pursue at undergraduate (UG), postgraduate (PG) or doctorate (PhD) level to practice legal profession in India. \nLaw as a profession offers a plethora of career avenues for students to explore and conquer. The preferred specialisations in Law are either Criminal or Civil.\nHowever, these days other branches are also gaining popularity such as Cyber Law, Patent Law as well as Corporate Law.\n")
        print("\nNational Law School of India University Vijayanagar, Bangalore \nNLU Delhi (NLUD) \nNalsar University of Law Tilak Road, Hyderabad \nNLU Jodhpur (NLUJ)")       
    if(w2==6): 
        print("Chartered Accountancy (CA) is a three-level course designed by the Institute of Chartered Accountants of India (ICAI).\n ICAI conducts CA exam to certify a candidate as a qualified Chartered Accountant after the successful completion of this course. \nChartered Accountant is a designation given to the accounting professional to manage work related to accounting and taxation of a business, like file tax returns, audit financial statements and so on.\n")
        print("\nCMS , Hyderabad \nICAI - Institute of Cost Accountants of India Indraprastha, Delhi\nIndian Institute of Finance and Accounts, Pune")
    n12=input("\nWould you like to explore more?[Y/N]")
    if((n12=="y") or (n12=="Y")):
        option3()
    else:
        mainstuff()
def option4():
    w1=int(input("Choose any Program !\n\n1. PhD\n2. Masters\n"))
    if(w1==1):
        print("\nA PhD is a doctoral research degree and normally the highest level of academic qualification you can achieve. The degree normally takes between three and four years of full-time work towards a thesis offering an original contribution to your subject.\n")
        q1=int(input(" 1.Computer Science\n 2.Biology\n 3.Physics\n 4.Economic\n 5.Theology\n 6.Chemistry\n 7.Mathematics\n 8.Philosophy\n 9.Engineering\n 10.Management\n"))
        if(q1==1):
            print("Depending on the university, curriculum for a PhD in Computer Science varies. Some programs are only research based and some require coursework. Topics of study for a PhD in Computer Science may include information security, database systems, compilers, software engineering, and computational theory. For a PhD in Computer Science, research is usually conducted closely with faculty while candidates work towards completing their dissertation. PhD in Computer Science programs prepare candidates for work in universities, research institutions, or other private or public agencies.\n94 PhD Programs in Computer Science\n")
        if(q1==2):
            print("PhD in Biology programs usually include gaining a solid foundation in biology knowledge base, as well as such concentrations as ecology, evolutionary biology, molecular, cellular, and developmental biology, and neuroscience. PhD programs in Biology usually consist of challenging coursework, seminars, laboratory work, research, and dissertation, all working closely with faculty. Graduates of PhD Biology programs are prepared to enter careers as educators and researchers at private and public institutions.\n75 PhD Programs in Biology\n")
        if(q1==3):
            print("Practical applications for specific theoretical training and skills practiced in a Physics PhD program can include engineering, product development, consulting, teaching and more. Applied physics is the area of research intended for use, but all Physics PhD topics are considered valuable contributions to our knowledge of the world. In addition to a dissertation, duties and expectations for a Physics PhD candidate may include assisting with other ongoing research projects, publications, and to assist in teaching undergraduate courses.\n67 PhD Programs in Physics\n")
        if(q1==4):
            print("A PhD Economics provides dedicated students the research skills and knowledge in specialized fields to become the future teachers and researchers of global economics. PhD Economics graduates are prepared for positions in government, universities, corporate enterprises, and consulting firms as experts in specialized economic fields. Top universities all over the world offer PhD Economics programs that engage students in small, intimate class settings for the personal attention required to not only attain the essential principals of economic theory, but to apply them to issues pertaining to government and business problems.\n58 PhD Programs in Economics\n")
        if(q1==5):
            print("This degree program provides students with ministerial training, culturally relevant ministry, and professional and spiritual formation. Scholars will continue to develop their leadership, writing, analytical, and communication skills in the context of theological thought. Programs vary, but curriculum may involve religious text interpretation, history, philosophy, culture, systemic theology, and practical application of the insights that they gain.\n73 PhD Programs in Theology\n")
        if(q1==6):
            print("Students pursuing a PhD degree in Chemistry may choose from different specialization areas (depending on the university program), but generally, some examples are analytic, organic and inorganic, nanotechnology and materials, physical, theoretical, polymer, or molecular biophysics. Research is often interdisciplinary, crossing into other sciences. Students can earn their PhD Biochemistry degree through coursework, laboratory, teaching, seminars, research, and dissertation. \n53 PhD Programs in Chemistry\n")
        if(q1==7):
            print("Curriculum for a PhD Mathematics program is challenging and generally includes coursework, seminars, teaching, and research. Research is conducted under the guidance of a supervisor and must be on an original topic resulting in a doctoral dissertation. The PhD Mathematics candidate must defend the dissertation in front of a panel of experts. Generally, PhD Mathematics programs take between 3 and 5 years to complete and although requirements differ depending on the academic institution and specific program, candidates must have the appropriate educational background, training, and experience in mathematics.\n51 PhD Programs in Mathematics\n")
        if(q1==8):
            print("PhD candidates studying Philosophy will have the opportunity to specialize in a historical or contemporary philosophical area and may choose a particular branch, like the philosophy of religion, science, mind, ethics, languages or law. Graduates with PhD degrees in Philosophy often go on to rewarding careers in the public or private sector in academia, publishing, humanities, psychology, sociology, linguistics, economics or science. PhD in Philosophy candidates will be required to conduct extensive research over a three to five year period, working mostly independently with guidance from post-doctoral candidates and professors.\n54 PhD Programs in Philosophy\n")
        if(q1==9):
            print("Engineering PhD candidates are specialists in problem solving, technology and computer use. Engineering PhD programs are challenging and require candidates to make a significant contribution to the field through research and practice. Candidates pursuing an Engineering PhD are usually required to complete a thesis or dissertation based on their research, often supervised by a member of faculty. Candidates seeking an Engineering PhD must be committed, competent, have the ability to conduct research, and have a current knowledge base in the field. Engineering PhD programs prepare candidates for work in academic and research institutions, government, or industry.\n45 PhD Programs in Engineering\n")
        if(q1==10):
            print("The field of management is all about overseeing other employees to ensure they are working effectively. Students learn negotiation, conflict resolution, and communication in order to manage a work force efficiently. Most management programs will also help students to understand basic operational business practices, which include more than just how to manage others\n47 PhD Programs in Management\n")
        
        n12=input("\nWould you like to explore more?[Y/N]")
        if((n12=="y") or (n12=="Y")):
            option4()
        else:
            mainstuff()
    if(w1==2):
        print("\nThere are two main types of master’s degrees: \n1. Course-based (taught): Course-based master’s degrees are based on structured course modules taught through lectures, seminars, laboratory work or distance learning. \n2. Research -based: Research-based master’s degrees require the student to carry out their own research project(s) in a specialized field of study. Research master’s degrees normally take a little longer than taught master’s degrees to complete.\n")
        
        q=int(input("1.Master of Arts (MA)\n2.Master of Science (MS, MSc) \n3.Master of Research (MRes) \n4.Master of Business Administration (MBA)\n5.Master of Public Administration (MPA) \n6.The Master of Laws(LLM) \n7.The Master of Arts in Liberal Studies(MA, MALS, MLA/ALM, MLS)\n"))
        if(q==1):
            print("A Master of Arts (MA) is usually awarded in disciplines categorized as arts or social sciences, such as communications, education, languages, linguistics, literature, geography, history and music.\n")
        if(q==2):
            print("A Master of Science (MS, MSc) is usually awarded in disciplines categorized as the sciences, such as biology, chemistry, engineering, health and statistics. Certain fields such as economics and the social sciences can fall under both arts and sciences, with the individual institution deciding on what to call their master’s degree program.\n")
        if(q==3):
            print("A Master of Research (MRes) degree is designed to provide training in how to become a researcher. Containing a significantly larger research element than MA or MSc programs, an MRes may give candidates an advantage if they wish to pursue a PhD or enter a career in research. \n")
        if(q==4):
            print("The Master of Business Administration (MBA) is designed to give students the skills and knowledge required for career progression in business and management roles. Candidates are given broad training in all aspects of business, allowing them to apply their learning to a variety of careers. Many MBA candidates are mid-career professionals, with most programs requiring at least three years’ professional experience.\n")
        if(q==5):
            print("The Master of Public Administration is a public policy degree similar to an MBA but focusing on the public sector rather than the private sector. Students can specialize in areas such as the environment, international administration and science and technology with an aim to work for the government, non-governmental organizations (NGOs), not-for-profit organizations and in consulting. \n")
        if(q==6):
            print("The Master of Laws degree is usually taken after having graduated from a professional law degree and gives candidates the chance to combine their knowledge of the basic skills needed to become a lawyer with specialist knowledge gained through research in a particular area of law.\n")
        if(q==7):
            print("The Master of Arts in Liberal Studies is an interdisciplinary program designed to provide rigorous teaching in the liberal arts. Candidates graduate with both depth and breadth of postgraduate knowledge, with MALS programs drawing from courses and instructors from across the university’s postgraduate curriculum. \nTypically, liberal arts students choose the course for an opportunity to intellectually challenge themselves, explore ideas and pursue knowledge, rather than to pursue a specific career path.\n")
        n12=input("\nWould you like to explore more?[Y/N]")
        if((n12=="y") or (n12=="Y")):
            option4()
        else:
            mainstuff()
def option5():
    print("Want to take a glimpse of the most go-to professions?")
    print("Top 15 Professions to choose from : \n")
    print("Rank	Occupation      Total Jobs	Median Salary	Unemployment Rate")
    print("1	Dentist	        27,600	    	$142,750	0.70%")
    print("2	Nurse	        7,12,900	$65,790	 	2.00%")
    print("3	Pharmacist      69,740	    	$113,410	3.20%")
    print("4	C.S. Analyst	1,20,440	$78,670	        2.50%")
    print("5	Physician	1,68,330	$183,270	0.70%")
    print("6	Database Admin	33,600	    	$75,390	        1.30%")
    print("7	Software Dev.	1,43,400	$89,530	        4.00%")
    print("8	Phy.Therapist	65,740	 	$77,930	        4.70%")
    print("9	Web Developer	65,740	    	$77,390	        4.70%")
    print("10	DentalHygienist	68,300	    	$69,480	        2.80%")
    print("11	Occ.Therapist	36,420	    	$74,820	        0.40%")
    print("12	Veterinarian	23,000	    	$82,940	        0.60%")
    print("13	C.S.Programmer	43,730	    	$72,230	        3.70%")
    print("14	Sch.Psychologist 31,700	    	$67,830     	1.40%")
    print("15	Therapist Asst.	30,300  	$51,340	        3.40%")
    a=input("\nDo you want to view more options?[Y/N]:  \n")
    if((a=="Y") or (a=="y")):
        print("Rank	Occupation      	Total Jobs	Median Salary	Unemployment Rate")
        print("16	Interpreter 		24,620      	$44,260	        1.70%")   
        print("17	MechanicalEngg.		21,200	    	$79,220	        2.40%")
        print("18	Epidemiologist		37,630	    	$64,320	        3.40%")
        print("19	IT Manager		55,830		$118,310        2.90%")
        print("20	Market Research		1,16,400	$60,350	        5.70%")
        print("21	Sonographer		23,300		$65,410         4.40%")
        print("22	C.S.Administrator 	96,600		$70,970	        3.90%")
        print("23	Respiratory Doc.  	31,300		$55,350     	2.90%")
        print("24	Civil Engineer	  	51,400		$77,940	        4.80%")
        print("25	Medical Secretary 	2,10,240	$31,460	        5.70%\n")
    else:            
        ch=input("Would you like to go back to Contents? [Y/N]")
        if((ch=="y") or (ch=="Y")):
            mainstuff()
        else:
            option5()
welcome()