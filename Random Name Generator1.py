import random, string, os
from colored import Fore, Back, Style
from colorama import Fore as d
import datetime
# <Human name automatic>
os.system('cls')
class Human:
    Male_in = ['Aadarsh', 'Aadhyatm', 'Aadi', 'Aadrik', 'Aakarsh', 'Aanandit', 'Aanjney', 'Aarav', 'Aarnav', 'Aarush',
            'Aarv',
            'Aayush', 'Abhimanyu', 'Abhinay', 'Abhinivesh',
            'Abhiram', 'Achyut', 'Adamya', 'Aditya', 'Advaith', 'Advik', 'Agastya', 'Agnikumara', 'Agraj', 'Ajinkya',
            'Akalp', 'Akshat', 'Akshay', 'Ambuj', 'Amiya',
            'Amit', 'Amol', 'Anand', 'Angad', 'Anirudh', 'Anmol', 'Ansh', 'Anshuman', 'Anuj', 'Arjun', 'Arpit',
            'Arunava',
            'Arvind', 'Aryan', 'Ashwin', 'Astik',
            'Atharv', 'Atri', 'Atul', 'Avi', 'Ayush', 'Ayushman', 'Ayushya', 'Badrinarayanan', 'Baidyanath', 'Bajrang',
            'Bakhshi', 'Bakhtawar', 'Bala Shankar',
            'Bala Subramani', 'Balaark', 'Balamurugan', 'Batnasiddhikara', 'Bhagat', 'Bhagyanandana', 'Bhargava',
               'Bhavesh',
               'Bhavik', 'Bhavin', 'Bhooteshwara',
               'Bhushan', 'Bindusar', 'Brijesh', 'Chaanakya', 'Chaitanya', 'Chakradev', 'Chakradhar', 'Chanakya',
               'Chandrakant', 'Chandrashekhar', 'Chandresh', 'Charan',
               'Chhatrapati', 'Chinmay', 'Chintan', 'Chintransh', 'Chirayu', 'Chithrakundhala', 'Chithravarma',
               'Chitrasen',
               'Dahak', 'Daityakarya', 'Daivya', 'Daiwik',
               'Daksh', 'Dakshesh', 'Danavendra', 'Darsh', 'Dasarath', 'Dev', 'Deval', 'Devansh', 'Dhanush', 'Dharmesh',
               'Dhaval', 'Dhruv', 'Dignesh', 'Ekalinga', 'Ekansh',
               'Ekaraj', 'Ekavir', 'Gagan', 'Gajanan', 'Gandharv', 'Gaurang', 'Gaurav', 'Gautam', 'Giridhar', 'Girik',
               'Girindra', 'Girish', 'Gopal', 'Govindaram',
               'Guneet', 'Hansaraj', 'Hardik', 'Hareshwar', 'Harikant', 'Harish', 'Harsh', 'Harshal', 'Harshavardhan',
               'Harshil', 'Hemendra', 'Herik', 'Himesh', 'Hitesh',
               'Hritik', 'Indrajit', 'Ishaan', 'Ishanyu', 'Ishwar', 'Jagadisha', 'Jagat', 'Jagdish', 'Jai', 'Jaiprakash',
               'Jairaj', 'Jatin', 'Jayadeva', 'Jayesh', 'Jeet',
               'Jigar', 'Jigisu', 'Jignesh', 'Joshil', 'Kalpit', 'Karan', 'Keshari', 'Kirat', 'Kirti', 'Krishna', 'Kundan',
               'Kunjan', 'Lakhan', 'Laksh', 'Lakshit',
               'Lavnik', 'Lohit', 'Maanas', 'Maanav', 'Madhav', 'Madhusudan', 'Mahadhyuta', 'Mahakaleshwar',
               'Maharshi' 'Mahatva', 'Mahesh', 'Mahendra', 'Mandar', 'Mangal',
               'Mansukh', 'Manthan', 'Mayur', 'Mitesh', 'Mukund', 'Munjal', 'Nachiket', 'Naksh', 'Nakul', 'Nakulesh',
               'Naman',
               'Naresh', 'Navamani',
               'Naveen', 'Navin', 'Navratna', 'Nayanesh', 'Neel', 'Neelesh', 'Neeraj', 'Neerav', 'Nihal', 'Nihant',
               'Nikesh',
               'Nikunj', 'Nilesh', 'Nimish', 'Nirbhay',
               'Nirvighna', 'Nishant', 'Nitesh', 'Nitin', 'Nivant', 'Nitant', 'Ojas', 'Om', 'Omkaar', 'Pankaj', 'Pratap',
               'Paresh', 'Parikshit', 'Parth', 'Prabhas', 'Prajith',
               'Prajnan', 'Pranav', 'Pranay', 'Praruj', 'Pratap', 'Prathamesh', 'Prathit', 'Prathu', 'Pratyush', 'Praveen',
               'Prithvij', 'Pruthviraj', 'Punit', 'Pushkar',
               'Pushpraj', 'Raaghava', 'Rachit', 'Radhatanaya', 'Raghav', 'Rajasekharan', 'Ram', 'Ramesh', 'Ranveer',
               'Reshvind', 'Rishabh', 'Rishi', 'Ritik', 'Rohan',
               'Ronith', 'Rudra', 'Rujul', 'Saksham', 'Samaksh', 'Samar', 'Samarpana', 'Samarth', 'Samesh', 'Saket',
               'Sanatan',
               'Sanatkumar', 'Sankalp', 'Sanket', 'Sarthak',
               'Sarvesh', 'Satvik', 'Saunak', 'Savarkar', 'Shantanu', 'Shashank', 'Shaurya', 'Shivaji', 'Shivam',
               'Shivansh',
               'Siddharth', 'Siddhesh',
               'Sridhara', 'Sriharsha', 'Srivasthav', 'Subhash', 'Sudharma', 'Sudhir', 'Sunil', 'Suraj', 'Sushil',
               'Swapnil',
               'Tanay', 'Tanish', 'Tanuj', 'Tanveer',
               'Tarak', 'Teerth', 'Tejas', 'Tushar', 'Udant', 'Udarsh', 'Umang', 'Upkaar', 'Utkarsh', 'Vasant', 'Vasudev',
               'Vedant', 'Veer', 'Venkatesh', 'Vihaan',
               'Vijay', 'Vijayrathna', 'Viraj', 'Vishal', 'Vishu', 'Vishveshwara', 'Vivaan', 'Vivek', 'Vyas', 'Yagnesh',
               'Yagyavalkya', 'Yash', 'Yatan', 'Yatin', 'Yug',
               'Yuvraj']

    Male_nonin = ['James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Charles',
            'Christopher',
            'Daniel', 'Matthew', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua', 'Kenneth', 'Kevin',
            'Brian', 'George', 'Timothy', 'Ronald', 'Edward', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'Nicholas',
            'Eric',
            'Jonathan', 'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon', 'Benjamin', 'Samuel', 'Gregory', 'Alexander',
            'Frank', 'Patrick', 'Raymond', 'Jack', 'Dennis', 'Jerry', 'Tyler', 'Aaron', 'Jose', 'Adam', 'Nathan',
            'Henry',
            'Douglas', 'Zachary', 'Peter', 'Kyle', 'Ethan', 'Walter', 'Noah', 'Jeremy', 'Christian', 'Keith', 'Roger',
            'Terry',
            'Gerald', 'Harold', 'Sean', 'Austin', 'Carl', 'Arthur', 'Lawrence', 'Dylan', 'Jesse', 'Jordan', 'Bryan',
            'Billy',
            'Joe', 'Bruce', 'Gabriel', 'Logan', 'Albert', 'Willie', 'Alan', 'Juan', 'Wayne', 'Elijah', 'Randy', 'Roy',
            'Vincent', 'Ralph', 'Eugene', 'Russell', 'Bobby', 'Mason', 'Philip', 'Louis']

    Female_in = ['Aadya', 'Aakriti', 'Aanchal', 'Aanya', 'Aaradhya', 'Aarohi', 'Aarushi', 'Aashvi', 'Aastha', 'Aditi',
              'Advika', 'Ahaana', 'Ahilya', 'Aishwarya',
              'Akanksha', 'Akshara', 'Amita', 'Amrita', 'Ananya', 'Anika', 'Ankita', 'Anshika', 'Anupriya', 'Anuradha',
              'Anusha', 'Anushka', 'Anushree', 'Anvi',
              'Anya', 'Aprajita', 'Aradhya', 'Archana', 'Archita', 'Arpita', 'Arti', 'Arunima', 'Arya', 'Asha', 'Ati',
              'Avni', 'Baghyawati', 'Barkha', 'Bhagyashri',
              'Bhanumati', 'Bhavaani', 'Bhavini', 'Bhavna', 'Bhumi', 'Bindu', 'Chaitaly', 'Chakrika', 'Chanchal',
              'Chandani', 'Chandrika', 'Charita', 'Chhaaya',
              'Chhavi', 'Chitrangda', 'Daksha', 'Damini', 'Damyanti', 'Deeksha', 'Deepa', 'Deepika', 'Deepti', 'Dhriti',
              'Disha', 'Divya', 'Divyani', 'Diya',
              'Draksha', 'Ekaja', 'Ekani', 'Ekta', 'Falguni', 'Ganga', 'Gargi', 'Garima', 'Gaurangi', 'Gauri',
                 'Gaurika',
                 'Gautami', 'Gayathri', 'Geet', 'Geetika',
                 'Harinakshi', 'Harini', 'Harita', 'Harsha', 'Harshitha', 'Hema', 'Hemal', 'Hemangini', 'Hemani',
                 'Ikshita',
                 'Indian Baby Girl Names', 'Isha', 'Ishani',
                 'Ishanvi', 'Ishita', 'Jagrati', 'Jahnvi', 'Janaki', 'Jaya', 'Jeevika', 'Jhalak', 'Juhi', 'Jyoti', 'Kajal',
                 'Kamya', 'Kanchan', 'Kangana', 'Kanika',
                 'Karishma', 'Kashish', 'Kaveri', 'Kavya', 'Khushi', 'Krishna', 'Kriti', 'Kritika', 'Ladli', 'Lakshita',
                 'Lakshmi', 'Leena', 'Lekha', 'Lipika', 'Madhuri',
                 'Mallika', 'Manjari', 'Mansi', 'Manu', 'Manya', 'Manyata', 'Maya', 'Megha', 'Meghana', 'Mekhala', 'Mira',
                 'Mitali', 'Mokshita', 'Monika', 'Mugdha',
                 'Naina', 'Nanda', 'Navya', 'Neetu', 'Netra', 'Nidhi', 'Nidra', 'Niharika', 'Nikita', 'Nilima', 'Nirbhaya',
                 'Nirja', 'Nisha', 'Ojasvita', 'Omisha',
                 'Pahal', 'Palak', 'Pallavi', 'Panini', 'Patralekha', 'Pavani', 'Pooja', 'Prabha', 'Pragya', 'Praniti',
                 'Pratyusha', 'Preksha', 'Priya', 'Priyanka',
                 'Priyanshi', 'Pushti', 'Rachana', 'Rachita', 'Radha', 'Radhika', 'Rajata', 'Rajeshri', 'Rajni', 'Raksha',
                 'Rani', 'Rasha', 'Ratna', 'Richa', 'Ridhi',
                 'Ritika', 'Riya', 'Ruchi', 'Sadhna', 'Sadhvi', 'Sakshi', 'Saloni', 'Sameeksha', 'Sanchita', 'Sandhya',
                 'Sarika', 'Saumya', 'Sharmila', 'Shikha', 'Shiva',
                 'Shivangi', 'Shivani', 'Shivika', 'Shivsuta', 'Shraddha', 'Shravasti', 'Shravya', 'Shreya', 'Shreyashi',
                 'Shruti', 'Shweta', 'Siddhi', 'Sneha', 'Snighdha',
                 'Sobhita', 'Sonakshi', 'Srishti', 'Sudiksha', 'Suhani', 'Suman', 'Sumedha', 'Swati', 'Tamanna', 'Tanmayi',
                 'Tanuja', 'Tanvi', 'Tapsee', 'Tripti', 'Trisha',
                 'Triveni', 'Triya', 'Tulsi', 'Turvi', 'Udyati', 'Unnati', 'Unni', 'Upadhriti', 'Upasna', 'Upma', 'Urmi',
                 'Vaani', 'Vaishnavi', 'Vamakshi', 'Vamika',
                 'Vani', 'Vansha', 'Vanya', 'Varsha', 'Vartika', 'Vasana', 'Vasatika', 'Vasudha', 'Vedhika', 'Vidya',
                 'Vimala',
                 'Vina', 'Vinaya', 'Vishakha', 'Vrinda',
                 'Vrishti', 'Vyanjana', 'Yachana', 'Yadavi', 'Yahvi', 'Yamuna', 'Yashaswini', 'Yashika', 'Yashoda',
                 'Yashodhara', 'Yasti', 'Yauvani', 'Yochana', 'Yoshita',
                 'Yukti', 'Yuktika']

    Female_nonin = ['Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
              'Lisa',
              'Nancy', 'Betty', 'Margaret', 'Sandra', 'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle', 'Carol',
              'Amanda',
              'Dorothy', 'Melissa', 'Deborah', 'Stephanie', 'Rebecca', 'Sharon', 'Laura', 'Cynthia', 'Kathleen', 'Amy',
              'Angela',
              'Shirley', 'Anna', 'Brenda', 'Pamela', 'Emma', 'Nicole', 'Helen', 'Samantha', 'Katherine', 'Christine',
              'Debra',
              'Rachel', 'Carolyn', 'Janet', 'Catherine', 'Maria', 'Heather', 'Diane', 'Ruth', 'Julie', 'Olivia',
              'Joyce',
              'Virginia', 'Victoria', 'Kelly', 'Lauren', 'Christina', 'Joan', 'Evelyn', 'Judith', 'Megan', 'Andrea',
              'Cheryl',
              'Hannah', 'Jacqueline', 'Martha', 'Gloria', 'Teresa', 'Ann', 'Sara', 'Madison', 'Frances', 'Kathryn',
              'Janice',
              'Jean', 'Abigail', 'Alice', 'Julia', 'Judy', 'Sophia', 'Grace', 'Denise', 'Amber', 'Doris', 'Marilyn',
              'Danielle',
              'Beverly', 'Isabella', 'Theresa', 'Diana', 'Natalie', 'Brittany', 'Charlotte', 'Marie', 'Kayla', 'Alexis',
              'Lori']

    surName_in = ['Tiwari', 'Tripathi', 'Trivedi', 'Sharma', 'Pandey', 'Pathak', 'Shukla', 'Mishra', 'Dubey', 'Dwivedi',
               'Chaturvedi', 'Chaubey', 'Arora',
               'Kapoor', 'Singh', 'Yadav', 'Goel', 'Malhotra', 'Rana', 'Chaudhary', 'Nigam', 'Sehgal', 'Chauhan',
               'Verma',
               'Saxena', 'Mahajan', 'Srivastava',
               'Tyagi', 'Shrivastav', 'Rastogi', 'Aggarwal', 'Jaiswal', 'Meena', 'Pawar', 'Joshi', 'Agrahari', 'Pal',
               'Patil', 'Acharya', 'Kashyap', 'Rao',
               'Deshai', 'Shastri', 'Upadhyay', 'Chandel', 'Chakraborty', 'Deshpande', 'Vyas', 'Ojha', 'Shandilya',
               'Agnihotri', 'Vajpayee', 'Dixit', 'Purohit',
               'Mohapatra', 'Nath', 'Vedi', 'Ahuja', 'Bose', 'Khurana', 'Ganguly', 'Malik', 'Sachdev', 'Khattar',
               'Mohan',
                  'Kaundinya', 'Jha', 'Vashishtha',
                  'Parashar', 'Kaushik', 'Govind']

    surName_nonin = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
               'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson',
               'Martin', 'Lee',
               'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker',
               'Young',
               'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson',
               'Baker',
               'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner',
               'Diaz',
               'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook',
               'Rogers',
               'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson', 'Bailey', 'Reed', 'Kelly', 'Howard', 'Ramos',
               'Kim', 'Cox',
               'Ward', 'Richardson', 'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennet', 'Gray', 'Mendoza',
               'Ruiz', 'Hughes',
               'Price', 'Alvarez', 'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez']



    gender_list = ["MALE", "FEMALE"]
    gender = random.choice(gender_list)

    country = random.choice([0,1])
    def getFirstName(self):
        global firstName
        if self.gender.lower() == "male":
            if self.country == 1:
                firstName = random.choice(Human.Male_in)
            else:
                firstName = random.choice(Human.Male_nonin)
        elif self.gender.lower() == "female":
            if self.country == 1:
                firstName = random.choice(Human.Female_in)
            else:
                firstName = random.choice(Human.Female_nonin)
        return firstName

    def getLastName(self):
        if self.country == 1:
            lastname = random.choice(Human.surName_in)
        else:
            lastname = random.choice(Human.surName_nonin)
        return lastname

    def get_phone_number(self):
        digits = random.choices(string.digits, k=7)
        number = ''.join(digits)
        return "897"+number

    def getdob(self):
        # <random dob>
        curr_time = datetime.datetime.now()
        list_currtime = str(curr_time).split()
        curr_date = list_currtime[0]
        list_curr_date = curr_date.split("-")
        yyyy = int(list_curr_date[0])
        mm = int(list_curr_date[1])
        dd = int(list_curr_date[2])
        monthr = '{:02}'.format(random.randint(1, mm - 1))
        dater = '{:02}'.format(random.randint(1, 28))
        dob = f'{random.randint(1900, yyyy)}-{monthr}-{dater}'
        return dob
        # </random dob>


# </Human name automatic>