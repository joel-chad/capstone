from flask import Flask, jsonify, request, render_template, url_for, redirect, session
from experta import *
import re
from flask.templating import render_template

app = Flask(__name__) # Flask Instance
app.secret_key = 'Jsctania'


diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}
# global results
# results = dict()

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		#symptoms=os.path.dirname("symptoms/"+ disease + ".txt")
		disease_s_file = open("Dsymptoms/"+ disease + ".txt") 
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		disease_s_file = open("Ddescriptions/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_desc_map[disease] = disease_s_data
		disease_s_file.close()
		disease_s_file = open("Dtreatments/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		d_treatment_map[disease] = disease_s_data
		disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" %(id_disease))
    print("A short description of the disease is given below :\n")
    print(disease_details+"\n")
    print("The common treatments recommended by experts are: \n")
    print(treatments+"\n")

    # results.append('guinea')

    result["2"] = f"The most probable disease that you have is {id_disease}"
    result["3"] = f"A short description of the disease is given  : {disease_details}"
    result["4"] = f"The common treatments recommended by experts are:  {treatments}"
    


# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(bloated_stomach, thin_limbs,reddish hair, swollen face):
class Greetings(KnowledgeEngine):

    global result
    result = dict()
    # self.run()

    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Jephtah, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")

        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(slight_hair=W())),salience = 1)
    def symptom_0(self):
	    self.declare(Fact(slight_hair=slight_hair))

    @Rule(Fact(action='find_disease'), NOT(Fact(reddish_hair=W())),salience = 1)
    def symptom_1(self):
        self.declare(Fact(reddish_hair=reddish_hair))

    @Rule(Fact(action='find_disease'), NOT(Fact(hair_falling=W())),salience = 1)
    def symptom_2(self):
        self.declare(Fact(hair_falling=hair_falling))

    @Rule(Fact(action='find_disease'), NOT(Fact(abnormal_skin=W())),salience = 1)
    def symptom_3(self):
        self.declare(Fact(abnormal_skin=abnormal_skin))

    @Rule(Fact(action='find_disease'), NOT(Fact(swollen_face=W())),salience = 1)
    def symptom_4(self):
        self.declare(Fact(swollen_face=swollen_face))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(glazed_eyes=W())),salience = 1)
    def symptom_5(self):
        self.declare(Fact(glazed_eyes=glazed_eyes))

    @Rule(Fact(action='find_disease'), NOT(Fact(apathetic=W())),salience = 1)
    def symptom_6(self):
        self.declare(Fact(apathetic=apathetic))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(smaller_muscles=W())),salience = 1)
    def symptom_7(self):
        self.declare(Fact(smaller_muscles=smaller_muscles))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(anaemic=W())),salience = 1)
    def symptom_8(self):
        self.declare(Fact(anaemic=anaemic))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(diarrhoea=W())),salience = 1)
    def symptom_9(self):
        self.declare(Fact(diarrhoea=diarrhoea))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(bloated_stomach=W())),salience = 19)
    def symptom_10(self):
        self.declare(Fact(bloated_stomach=bloated_stomach))
    
    @Rule(Fact(action='find_disease'), NOT(Fact(thin_body=W())),salience = 1)
    def symptom_11(self):
        self.declare(Fact(thin_body=thin_body))

    @Rule(Fact(action='find_disease'), NOT(Fact(older_face=W())),salience = 1)
    def symptom_12(self):
        self.declare(Fact(older_face=older_face))

    @Rule(Fact(action='find_disease'), NOT(Fact(cranky_child=W())),salience = 1)
    def symptom_13(self):
        self.declare(Fact(cranky_child=cranky_child))

    @Rule(Fact(action='find_disease'), NOT(Fact(wrinkled_skin=W())),salience = 1)
    def symptom_14(self):
        self.declare(Fact(wrinkled_skin=wrinkled_skin))

    @Rule(Fact(action='find_disease'), NOT(Fact(little_fattie_tissue=W())),salience = 1)
    def symptom_15(self):
        self.declare(Fact(little_fattie_tissue=little_fattie_tissue))

    @Rule(Fact(action='find_disease'), NOT(Fact(converse_stomach_rib_prominent=W())),salience = 19)
    def symptom_16(self):
        self.declare(Fact(converse_stomach_rib_prominent=converse_stomach_rib_prominent))

    @Rule(Fact(action='find_disease'), NOT(Fact(chronic_infections=W())),salience = 1)
    def symptom_17(self):
        self.declare(Fact(chronic_infections=chronic_infections))

    @Rule(Fact(action='find_disease'), NOT(Fact(skin_reddish_purging=W())),salience = 1)
    def symptom_18(self):
        self.declare(Fact(skin_reddish_purging=skin_reddish_purging))

    @Rule(Fact(action='find_disease'), NOT(Fact(age=W())),salience = 20)
    def symptom_19(self):
        self.declare(Fact(age=age))		   


    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="no"),Fact(bloated_stomach="yes"),Fact(thin_body="no"),Fact(older_face="no"),Fact(child_cranky="no"),Fact(wrinkled_skin="no"),Fact(little_fattie_tissue="no"),Fact(converse_stomach_rib_prominent="no"),Fact(chronic_infections="no"),Fact(skin_reddish_purging="no"),Fact(age="no"))
    def disease_0(self):
        self.declare(Fact(disease="Kwashiorkor"))

    @Rule(Fact(action='find_disease'),Fact(slight_hair="no"),Fact(reddish_hair="no"),Fact(hair_falling="no"),Fact(abnormal_skin="yes"),Fact(swollen_face="no"),Fact(glazed_eyes="no"),Fact(apathetic="no"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="no"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="no"))
    def disease_1(self):
        self.declare(Fact(disease="Marasmus"))

    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="yes"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="no"))
    def disease_2(self):
        self.declare(Fact(disease="Marasmus-Kwashiorkor"))	

    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="no"),Fact(bloated_stomach="yes"),Fact(thin_body="no"),Fact(older_face="no"),Fact(child_cranky="no"),Fact(wrinkled_skin="no"),Fact(little_fattie_tissue="no"),Fact(converse_stomach_rib_prominent="no"),Fact(chronic_infections="no"),Fact(skin_reddish_purging="no"),Fact(age="yes"))
    def disease_3(self):
        self.declare(Fact(disease="Kwashiorkor_"))	

    
    @Rule(Fact(action='find_disease'),Fact(slight_hair="no"),Fact(reddish_hair="no"),Fact(hair_falling="no"),Fact(abnormal_skin="yes"),Fact(swollen_face="no"),Fact(glazed_eyes="no"),Fact(apathetic="no"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="no"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="yes"))
    def disease_4(self):
        self.declare(Fact(disease="Marasmus_"))	


    @Rule(Fact(action='find_disease'),Fact(slight_hair="yes"),Fact(reddish_hair="yes"),Fact(hair_falling="yes"),Fact(abnormal_skin="yes"),Fact(swollen_face="yes"),Fact(glazed_eyes="yes"),Fact(apathetic="yes"),Fact(smaller_muscles="yes"),Fact(anaemic="yes"),Fact(diarrhoea="yes"),Fact(bloated_stomach="yes"),Fact(thin_body="yes"),Fact(older_face="yes"),Fact(child_cranky="yes"),Fact(wrinkled_skin="yes"),Fact(little_fattie_tissue="yes"),Fact(converse_stomach_rib_prominent="yes"),Fact(chronic_infections="yes"),Fact(skin_reddish_purging="yes"),Fact(age="yes"))
    def disease_5(self):
        self.declare(Fact(disease="Marasmus-Kwashiorkor_"))	
        

    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def disease(self, disease):
        # global res
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common treatments recommended by experts are: \n")
        print(treatments+"\n")


        result["2"] = f"The most probable disease that you have is {id_disease}"
        result["3"] = f"A short description of the disease is given below : {disease_details}"
        result["4"] = f"The common treatments recommended by experts are:  {treatments}"


    @Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
    def if_not_matched(disease):
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" %(id_disease))
        print("A short description of the disease is given below :\n")
        print(disease_details+"\n")
        print("The common treatments recommended by experts are: \n")
        print(treatments+"\n")

    # results.append('guinea')

        result["2"] = f"The most probable disease that you have is {id_disease}"
        result["3"] = f"A short description of the disease is given : {disease_details}"
        result["4"] = f"The common treatments recommended by experts are: \n {treatments}"


    @Rule(Fact(action='find_disease'),
        Fact(slight_hair=MATCH.slight_hair),
        Fact(reddish_hair=MATCH.reddish_hair),
        Fact(hair_falling=MATCH.hair_falling),
        Fact(abnormal_skin=MATCH.abnormal_skin),
        Fact(swollen_face=MATCH.swollen_face),
        Fact(glazed_eyes=MATCH.glazed_eyes),
        Fact(apathetic=MATCH.apathetic),
        Fact(smaller_muscles=MATCH.smaller_muscles),
        Fact(anaemic=MATCH.anaemic),
        Fact(diarrhoea=MATCH.diarrhoea),
        Fact(bloated_stomach=MATCH.bloated_stomach),
        Fact(thin_body=MATCH.thin_body),
        Fact(older_face=MATCH.older_face),
        Fact(cranky_child=MATCH.cranky_child),
        Fact(wrinkled_skin=MATCH.wrinkled_skin),
        Fact(little_fattie_tissue=MATCH.little_fattie_tissue),
        Fact(converse_stomach_rib_prominent=MATCH.converse_stomach_rib_prominent),
        Fact(chronic_infections=MATCH.chronic_infections),
        Fact(skin_reddish_purging=MATCH.skin_reddish_purging),
        Fact(age=MATCH.age),NOT(Fact(disease=MATCH.disease)),salience = -999)


    def not_matched(self,slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles, anaemic, diarrhoea, bloated_stomach,thin_body,older_face, cranky_child,wrinkled_skin ,little_fattie_tissue ,converse_stomach_rib_prominent ,chronic_infections, skin_reddish_purging, age):
        global max_disease
        print("\nDid not find any disease that matches your exact symptoms")
        result['1']='Did not find any disease that matches your exact symptoms'
        lis = [slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles,anaemic ,diarrhoea ,bloated_stomach ,thin_body ,older_face, wrinkled_skin, cranky_child, little_fattie_tissue, converse_stomach_rib_prominent, chronic_infections, skin_reddish_purging, age]
        max_count = 0
        max_disease = ""
        for key,val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0,len(lis)):
                if(temp_list[j] == lis[j] and lis[j] == "yes"):
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)
        #    self.diziz = max_disease





engine = Greetings() # Knowledge Engine Instance

@app.route("/", methods=(("GET", "POST")))
def index():
    preprocess()
    global slight_hair, reddish_hair, hair_falling, abnormal_skin, swollen_face, glazed_eyes, apathetic, smaller_muscles, anaemic, diarrhoea, bloated_stomach, thin_body,older_face, cranky_child,wrinkled_skin ,little_fattie_tissue ,converse_stomach_rib_prominent ,chronic_infections, skin_reddish_purging, age
    if request.method == "POST":
        # engine.reset()
        slight_hair = request.form.get("slight_hair")
        reddish_hair = request.form.get("reddish_hair")
        hair_falling = request.form.get("hair_falling")
        abnormal_skin = request.form.get("abnormal_skin")
        swollen_face = request.form.get("swollen_face")
        glazed_eyes = request.form.get("glazed_eyes")
        apathetic = request.form.get("apathetic")
        smaller_muscles = request.form.get("small_muscles")
        anaemic =  request.form.get("anaemic")
        diarrhoea = request.form.get("diarrhoea")
        bloated_stomach = request.form.get("bloated_stomach")
        thin_body = request.form.get("thin_body")
        older_face = request.form.get("older_face")
        cranky_child = request.form.get("cranky_child")
        wrinkled_skin = request.form.get("wrinkled_skin")
        little_fattie_tissue = request.form.get("little_fattie_tissue")
        converse_stomach_rib_prominent = request.form.get("converse_stomach_rib_prominent")
        chronic_infections = request.form.get("chronic_infections")
        skin_reddish_purging = request.form.get("skin_reddish_purging")
        age=request.form.get("age")

        engine.reset()  # Instantiate Initial Fact
        engine.run()



        # engine.run()

    # print(engine.facts)

        return redirect(url_for('results'))
    return render_template("index.html")  
    # return next(i)
    # return jsonify(results)
    
	# jsonify({})

@app.route("/learn")
def learn():
	return render_template("learn.html")

@app.route("/results")
def results():
    	
	# result=jsonify(engine.response)
    return render_template('results.html', result=result)	

 

@app.route('/pythonlogin', methods=['GET', 'POST'])
def login():
    # global userID 
    # try:
        # connection = pymysql.connect(host='127.0.0.1', user='root',db='pythonlogin')
    # except:
        # print("You are not connected to server(localhost)!")
    # else:
    #     if request.method == "POST":
    #         details = request.form
    #         username = details['username']
    #         password = details['password']
    #         cur = connection.cursor()
    #         query = "SELECT username,password FROM accounts "
    #         cur.execute(query)


            # for (username,password) in cur:
            #     if username==username and password==password:
            #         login = True

            #     else:
            #         login = False

            # session['username']=username 
            # userID = session['username']                    
                
                  
            # if login==True:
            #     print("Logged in successfully as", userID)
            #     return redirect(url_for('home'))
            #     # newWindow()
            # elif login==False:
            #     print("Email or password is wrong")
            # cur.close()
            # connection.close()
            # # return 'success'



    return render_template('login.html')

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/logout')
def logout():

	session.pop('username', None)
	return redirect(url_for('index'))

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # global userID
    if 'username' in session:
        userID = session['username']
        

        return render_template('home.html',userID=userID)

    return "You are not logged in <br><a href = '/pythonlogin'></b>" + "click here to login</b></a>"  


@app.route('/kwash', methods=['GET','POST'])
def kwash():
    if 'username' in session:
        userID=session['username']

        a1=open("Dtreatments/Kwashiorkor.txt")
        b1 = a1.read()
        input_days = ''
        if request.method == 'POST':
            input_days = request.form['message']
            with open("Dtreatments/Kwashiorkor.txt", 'w') as f:
                    f.write(str(input_days))
                    return redirect(url_for('saved'))
        

        return render_template('kwash.html',b1=b1,userID=userID)

    return "You are not logged in <br><a href = '/pythonlogin'></b>" + "click here to login</b></a>"  

    

@app.route('/marasmus', methods=['GET','POST'])
def marasmus():
    if 'username' in session:
        userID=session['username']

        a1=open("Dtreatments/Marasmus.txt")
        b1 = a1.read()
        input_days = ''
        if request.method == 'POST':
            input_days = request.form['message']
            with open("Dtreatments/Marasmus.txt", 'w') as f:

                    f.write(str(input_days))
                    return redirect(url_for('saved'))   


        return render_template('marasmus.html',b1=b1,userID=userID)  

    return "You are not logged in <br><a href = '/pythonlogin'></b>" + "click here to login</b></a>"  
       


@app.route('/kwashmara', methods=['GET','POST'])
def kwashmara():
    if 'username' in session:
        userID=session['username']    

        a1=open("Dtreatments/Marasmus-Kwashiorkor.txt")
        b1 = a1.read()
        input_days = ''
        if request.method == 'POST':
            input_days = request.form['message']
            with open("Dtreatments/Marasmus-Kwashiorkor.txt", 'w') as f:
                    f.write(str(input_days))
                    return redirect(url_for('saved'))    
        
        return render_template('kwashmara.html',b1=b1,userID=userID)   

    return "You are not logged in <br><a href = '/pythonlogin'></b>" + "click here to login</b></a>"  


@app.route('/saved')
def saved():
    if 'username' in session:
        userID=session['username']     

        return render_template('saved.html',userID=userID) 
    
@app.route('/bot')
def bot():
    return render_template('bot.html')  


qa = {
    "chatbot": "Ini ndinoitwa Chatbot",
    "greeting": "Makadini henyu?",
    "cheering": "Tinotenda muri kufara",
    "help": "Zvakanaka !!, Unogona kundibvunza zvaunoda kuziva nezveaids",

    "hiv": "HIV inozivikanwa zvikuru sehutachiona hweAIDS, hutachiona hunokonzera AIDS",
    "aids": "AIDS inoreva kuti Acquired Immuno Deficiency Syndrome",
    "how does hiv lead to aids": "HIV inoparadza masoja emuviri uye inoita kuti muviri ubatwe nezvimwe zvirwere. "
                                 "inotyisa, inotungamira kuAIDS",
    "infection diagnosed": "AIDS inoedzwa nekuyedza ropa remunhu kuti harina hutachiwana hweHIV uye immune system"
                           "ukatadza kurwisa zvimwe zvirwere nemufungo iwoyo ndipo panobva paongororwa ropa"
                           "Utachiona hweHIV hunobva hwazivikanwa kuti hune AIDS.",
    "transmition": "HIV inopfuudzwa kubva kumunhu kuenda kune mumwe kuburikidza: \n Kusangana pabonde. \n Kusanganisa mvura"
                   "mvura yemumuviri kana maronda nemunhu ane AIDS. \n Pazvinhu zvakapinza. \ nKurega ropa"
                   "utapukirwa neHIV.",
    "symptoms of hiv": "Zviratidzo zveAIDS: \n Kutetepa nekukurumidza. \n Frequent fever"
                       "\n Kuti ndinyanye kuneta ndisingazive kuti sei."
                       "\nDiarrhea kweinenge vhiki."
                       "\n Kunwa kweganda remuromo nekunhengo dzakavandika. \n Zvirwere zveganda zvakaita seTB.",
    "how long does it take for aids symptoms to develop after infection with hiv": "Kazhinji munhu anogona"
                                                                                   "Mukondombera kupfuura"
                                                                                   "Makore gumi nemashanu pasina kuratidza zviratidzo"
                                                                                   "chero ipi yeAIDS asi"
                                                                                   "pane rimwe divi,"
                                                                                   "kune vamwe vanhu vanouya"
                                                                                   "zviratidzo zveAIDS munguva pfupi yapfuura"
                                                                                   "yehutachiona hweHIV,"
                                                                                   "Zvinongotora anenge mwedzi mishoma"
                                                                                   "kuratidza zviratidzo zvechirwere ichi.",
    "preventions or avoiding": "Nzira dzekudzivirira kana kuzvidzivirira kubva kuhutachiona hweHIV / AIDS."
                               "Izvi zvinoreva zvakare kuzvidzivirira kubva kunzira dzine njodzi dzekubatira AIDS. \ Dzivisa bonde risina dziviriro,"
                               "Shandisa magurovhosi, uye zvakanaka kuve nemumwe wako. \n Usabatana"
                               "nyatsoshandisai midziyo yenyu, yakaita setsono, zvipunu, mabhurasho emazino nezvimwewo."
                               "izvo zvichakwanisa kuparadzira HIV.",
    "treatments or cure": "Parizvino hapana mushonga wakakwana weAids. Kunze kwekunge,"
                          "kune mishonga inopihwa yekuvhara immune system."
                          "inokonzerwa neHIV.",
    "can hiv positive people have a baby": 
"Hongu, uye mwana anogona kuzvarwa asina AIDS asi uchafanirwa kurapwa"
                                           "HIV (ART)",
    "life expectancy": "Nehutano hwakanaka hweHIV (ART) hutarisiro hweupenyu hwakaenzana newemunhu asina HIV.",
    "herbs or supplements": "Iwe unorayirwa kuti uchenjere nemishonga yemusikirwo, pamwe nekusimbiswa kubva"
                            "chiremba chiremba.",
    "what is the best food if i am hiv positive": "Kufanana nevamwe vanhu, idya chikafu chine hutano uye zvinovaka muviri."
                                                  "Kutapukirwa neHIV hazvireve kuti pane kudya kwakati, kudya senge"
                                                  "vamwe vanhu vehutano hwako. \n",
    "helpful":"Ndafara kukubatsira. ",
}

@app.route("/ask")
def ask():
    question = request.args.get('msg').lower().replace("?", "").strip(" ")

    if (re.findall("iwe | zita | unoshevedzwa| unoitwa", question)) and (re.findall("ani|ndiani", question)):
        return qa["chatbot"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (re.findall("nguva|yakawanda|inotora", question)) and (re.findall("ngani|sei", question)):
        return qa["how long does it take for aids symptoms to develop after infection with hiv"]

    elif ((re.findall("hiv", question)) or (re.findall("Shuramatongo", question)) or  (re.findall("aids", question)))  and (re.findall("zviratidzo | ratidzo | inooneka | inoonekwa", question)):
        return qa["symptoms of hiv"]

    elif (re.findall("chii | chiinoreva | nezve | zvinoreva", question)) and (re.findall("hiv", question)):
        return qa["hiv"]

    elif (re.findall("chii | zvinoreva | nezve | zvinoreva", question)) and (re.findall("aids", question)):
        return qa["aids"]

    elif (re.findall("zvaita|ndatenda|mwaita", question)) and (re.findall("rubatsiro | nguva | yakandibatsira", question)):
        return qa["helpful"]

    elif (re.findall("hiv", question)) and (re.findall("kukonzera | tumira", question)) and (re.findall("aids", question)):
        return qa["how does hiv lead to aids"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (re.findall("kuoneka | kurapwa| inorapwa | kuwanikwa | tsvaga | kuzivikanwaa | kuziva", question)):
        return qa["infection diagnosed"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question)))  and (
    re.findall("paradzira | pararira | tapukira | fambiswa | inofambiswa", question)):
        return qa["transmition"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question)))  and (
    re.findall("kudzivirira | dzivirira | kudzivirirwa | inodzivirirwa", question)):
        return qa["preventions or avoiding"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (
    re.findall("kurapwa | inorapwa | mushonga", question)):
        return qa["treatments or cure"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (
    re.findall("inokanganisa | muridzi | asina | asina | unokwanisa", question)) and (re.findall("mwana| vana", question)):
        return qa["can hiv positive people have a baby"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (
    re.findall("hupenyu | rarama | kurarama", question)) and (re.findall("nguva", question)):
        return qa["life expectancy"]

    # elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (
    # re.findall("mishonga | yakasikwa | mushonga", question)) :
    #     return qa["herbs or supplements"]

    elif ((re.findall("hiv", question)) or (re.findall("aids", question))) and (re.findall("chikafu| kudya| chokudya", question)):
        return qa["what is the best food if i am hiv positive"]

    elif (re.findall("Mwaita|Maita| Bye", question)):
        return "Muchitendei :) "
    
    elif (re.findall("hello|hey|hi", question)):
        return qa["greeting"]

    elif (re.findall("zvakanaka|okay", question)):
        return qa["cheering"]

    elif (re.findall("hongu", question)):
        return qa["help"]

    else:
        return "Handina mhinduro chaiyo kumubvunzo wako. \n handisi kunyatsonzwisisa mubvunzo wako, ndokumbira ubvunze zvekare nezve hiv / aids nemutauro unonzwisisika (ChiShona)"


if __name__ == "__main__":
	preprocess()
	app.run(debug=True)		
			

