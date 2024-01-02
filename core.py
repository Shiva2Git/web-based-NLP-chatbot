from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO,send,emit,join_room
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import func
from pymongo.mongo_client import MongoClient
import json
import random
import string
import time
from bson import ObjectId
from pprint import pprint
# from chat import get_response

app=Flask(__name__)

# SQLALACHEMY CONNECTION ---------------------------------------------------

app.config['SECRET']="secret!123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socket_io=SocketIO(app,cors_allowed_origins="*")
CORS(app)

# MongoDB connection ---------------------------------------------------------

MONGO_PWD='YElQPFJj0mieK3R2'
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
MONGO_DB=client['AdminDB']
collection = MONGO_DB['Users']
mongo_mgs=MONGO_DB['message']


# ORM FOR SQLALACHEMY --------------------------------------------------------


class Subcriber(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phoneNo = db.Column(db.String(20), nullable=False)
    userName=db.Column(db.String(80), nullable=False)
    plan = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    chatAddress=db.Column(db.String(24),nullable=False)
    


# UPDATE DATE INTO SQLALACHEMY DATABASE ---------------------------------------------


def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.after_request
def after_request(response):
    return add_cors_headers(response)


with app.app_context():
    # db.drop_all()
    # db.session.commit()
    db.create_all()
    # user=Subcriber(id= 2,name= "karthi",email="karthi123@gmail.com" ,phoneNo="9978902657",userName="karthi123",plan=400,category="ecommerce")
    # db.session.add(user)
    # user=Subcriber(id= 3,name= "naveen",email="naveen123@gmail.com" ,phoneNo="9978902757",userName="naveen123",plan=400,category="ecommerce")
    # db.session.add(user)
    # user=Subcriber(id= 4,name= "saw",email="saw123@gmail.com" ,phoneNo="9970902757",userName="saw123",plan=400,category="ecommerce")
    # db.session.add(user)
    # db.session.add(user)
    
    # db.session.add(doctor2)
    #  db.session.commit()
    # db.session.query(Subcriber).delete()
    #  db.session.query(Appointment).delete()
    # db.session.commit()


#  FUNCTION FOR INSERT DATA INTO SQLALACHEMY DATABASE -------------------------------------


def insert_data_SQLALACHEMY(name,email,phoneNo,plan,category):
    id_count=db.session.query(Subcriber).count()
    userName=generate_username(name)
    valid=validUser(userName)
    while True:
        if valid:
            break
        else:
            userName=generate_username(name)
            valid=validUser(userName)
    print(userName)
    chat_address = insert_data_MONGODB(id_count,name)
    chat_address=str(chat_address)
    user=Subcriber(id=id_count,name=name,email=email ,phoneNo=phoneNo,userName=userName,plan=plan,category=category,chatAddress=chat_address)
    db.session.add(user)
    db.session.commit()
    



def validUser(name):
    if Subcriber.query.filter_by(userName=name).all():
        return False
    else:
        return True

@app.route('/formvalid/<string:keyType>/<string:value>')
def formvalid(keyType, value):
    if Subcriber.query.filter_by(**{keyType: value}).first():
        return jsonify("True")
    else:
        return jsonify('False')


def generate_username(name):
    random_ = ''.join(random.choices(string.digits, k=4))
    random_suffix = ''.join(random.choices(string.ascii_lowercase, k=2))
    username = name.lower() +random_ + random_suffix
    return username



def trys():
    # sub=Subcriber.query.get(2)
    # # db.session.delete(sub)

    # for sub in sub:
    #     sub.chatAddress="657d824008e8808e57610438"
    # db.session.commit()
    id_count=db.session.query(Subcriber).count()
    print(id_count)

    # chat_address = insert_data_MONGODB(3,"Chaymae Naim")
    # chat_address=str(chat_address)
    # # # print(chat_address)
    # # user = Subcriber(id=1,name= "admin",email="admin123@gmail.com" ,phoneNo="9978982757",userName="admin123",plan=0,category="admin",chatAddress=chat_address)
    # # user = Subcriber(id= 2,name= "naveen",email="naveen123@gmail.com" ,phoneNo="9878902757",userName="naveen123",plan=400,category="ecommerce",chatAddress=chat_address)
    # # # user=Subcriber(id=2,name= "karthi",email="karthi123@gmail.com" ,phoneNo="9978902657",userName="karthi123",plan=400,category="ecommerce",chatAddress=chat_address)
    # # # user=Subcriber(id= 4,name= "saw",email="saw123@gmail.com" ,phoneNo="9970902757",userName="saw123",plan=400,category="ecommerce",chatAddress=chat_address)
    # user=Subcriber(id= 3,name= "Chaymae Naim",email="Chaymae Naim123@gmail.com" ,phoneNo="9970902707",userName="Chaymae Naim",plan=400,category="ecommerce",chatAddress=chat_address)
    # # # user=Subcriber(id= 3,name= "shiva",email="shiva1123@gmail.com" ,phoneNo="9970902707",userName="shiva123",plan=400,category="ecommerce",chatAddress=chat_address)
    # db.session.add(user)
    # db.session.commit()



def insert_data_MONGODB(id,username):
    data = {
        "SQL_id": id,
        "Username": username,
        "Chat": []
    }
    collection.insert_one(data)
    result=collection.find_one({"Username":username})
    return result['_id']


@app.route("/auto")
def auto():
    return render_template("new.html")



@app.route('/autocomplete/<string:prefix>')
def autocomplete(prefix):
    subscribers = Subcriber.query.filter(Subcriber.userName.like(f'{prefix}%')).all()
    suggestions = [subscriber.userName for subscriber in subscribers]
    return jsonify(suggestions)




@app.route('/chat/<string:person1>/<string:person2>')
def chat(person1,person2):
  try:
    chats=[]
    sub1=Subcriber.query.filter_by(userName=person1).first()
    chat_Address=ObjectId(sub1.chatAddress)
    result=collection.find_one({"_id":chat_Address})
    result=result['Chat']
    res = [next(iter(dictionary.keys())) for dictionary in result if dictionary]
    id=result[res.index(person2)][person2]
    chat=mongo_mgs.find_one({"_id":id})
    chat=chat.get("chats",[])
    for i in chat:
        chats.append(i)
    return jsonify((chats))
  except:
      return jsonify([])


@socket_io.on('message')
def handle_mgs(message):
        try:
          if isinstance(message,dict):
            print(message)
            sub=Subcriber.query.filter_by(userName=message['sender']).first()
            sub1=Subcriber.query.filter_by(userName=message['resiver']).first()
           
            if sub:
                  MongoDB_Insert(sub.chatAddress,message)
                  send(message,broadcast=True)
            elif sub1:
                 unkown_chat_Mongo(sub1.chatAddress,message)
                 send(message,broadcast=True)
        except:
            pass
                         

def chat_address_Create(mgs):
    data = {
        "chats": [mgs]
    }
    result = mongo_mgs.insert_one(data).inserted_id
    return result        


def unkown_chat_Mongo(id,mgs):
    id=ObjectId(id)
    chat_address=chat_address_Create(mgs)
    user=mgs['sender']
    collection.update_one({"_id":id},{'$push': {'Chat': {user:chat_address}}})
    return








def MongoDB_Insert(address,mgs):
    id=ObjectId(address)
    existing_entry = collection.find_one({"_id":id, f'Chat.{mgs["resiver"]}': {'$exists': True}})
    sub=Subcriber.query.filter_by(userName=mgs['resiver']).first()
    try:
         id_2=ObjectId(sub.chatAddress)
         existing_entry_2 = collection.find_one({"_id":id_2, f'Chat.{mgs["sender"]}': {'$exists': True}})
         
         if existing_entry:
             existing_entry=existing_entry['Chat'] 
             string_keys = [next(iter(dictionary.keys())) for dictionary in existing_entry if dictionary]
             id=existing_entry[string_keys.index(f'{mgs["resiver"]}')][f'{mgs["resiver"]}']
             id=ObjectId(id)
             mongo_mgs.update_one({"_id":id},{'$push':{'chats':mgs}})
             return
         elif existing_entry_2:  
            existing_entry_2=existing_entry_2['Chat'] 
            string_keys = [next(iter(dictionary.keys())) for dictionary in existing_entry_2 if dictionary]
            id_2=existing_entry_2[string_keys.index(f'{mgs["sender"]}')][f'{mgs["sender"]}']
            # print(id_2)
            id_2=ObjectId(id_2)
            collection.update_one({"_id":id},{'$push': {'Chat': {mgs["resiver"]:id_2}}})
            result=collection.find_one({"_id":id})
            mongo_mgs.update_one({"_id":id_2},{'$push':{'chats':mgs}})
            return
         else:
                chat_address=chat_address_Create(mgs)
                collection.update_one({"_id":id},{'$push': {'Chat': {mgs["resiver"]:chat_address}}})
                print(id)
                collection.update_one({"_id":id_2},{'$push': {'Chat': {mgs["sender"]:chat_address}}})
                print(id_2)
                return
    except:
        print("error")
     




@app.route("/<string:name>", methods=['GET', 'POST'])
def validUsername(name):
    count = db.session.query(func.count()).filter(Subcriber.userName ==name).scalar()
    if Subcriber.query.filter_by(userName=name).all():
        print(count)
        if count==1:
            return ''
        else:
           return jsonify('you cant use this service contact admin ! UserName Limit error phone number: +91 6374876353 and  email id: shiva35143@gmail.com') 
    else:
        return jsonify('you cant use this service contact admin !phone number: +91 6374876353 and  email id: shiva35143@gmail.com')



# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     contact=[]
#     text = request.get_json().get("message")
#     response = get_response(text)
#     message = {"user":"chatbot","answer": response}
#     return jsonify(message)




@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html') 






@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register.html')
def register():
    return render_template('register.html') 


@app.route('/admin')
def admin():
    return render_template('admin.html') 


@app.route('/subName', methods=['GET'])
def subName():
    # trys()
    subcribers = Subcriber.query.all()
    output=[]
    for user in subcribers:
        output.append({
            "name":user.userName
        })
    return jsonify(output)



@app.route('/subcribers', methods=['GET'])
def subcribers():
    # trys()
    # insert_data_SQLALACHEMY("shiva","shiva35123@gmail.com",6374876353,800,"traval")
    # validUser("shiva123")
    subcribers = Subcriber.query.all()
    output=[]
    for user in subcribers:
        output.append({
            "id":user.id,
            "name":user.name,
             "email":user.email,
             "phoneNo":user.phoneNo,
             "userName":user.userName,
             "plan":user.plan,
             "category":user.category,
             "chat_address":user.chatAddress
        })
    return jsonify(output)


if __name__=='__main__':
    socket_io.run(app,host='192.168.1.24',debug=True)

# host='192.168.1.8'
# host='192.168.1.9'