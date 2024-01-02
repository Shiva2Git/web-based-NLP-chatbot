var head=document.querySelector("head")
var body=document.querySelector("body")
var div=document.createElement("div")


function TY(){
    document.getElementById("showChatbot").addEventListener("click", function(){
        document.getElementById("showbtn").style.display = "none";
        document.getElementById("chatboxid").style.display = "block";
        generateRandomUsername()
        
    })
    

document.getElementById("close-btn").addEventListener("click",function(){
    document.getElementById("chatboxid").style.display="none"
    document.getElementById("showbtn").style.display="block"
})


const input = document.querySelector('input');
input.addEventListener('keyup',function(e){
    if (e.keyCode === 13) {
    document.getElementById("sendbtn").click()
  }  
});
}

var temp_chat
var chatbox=[]
var userName

document.addEventListener("DOMContentLoaded",function(){
    TY()
    $(document).ready(function(){

        $('#sendbtn').on('click', function(){
            var chat = document.getElementById("chat").value;
            if (chat === "") {
                return false;
            }
            else if(chatbox.includes("pleace wait i'll connect to admin")){
                       
                
                var socket = io.connect("http://192.168.1.17:5000");
                socket.on('connect', function () {
                        
                    socket.send("User connected");
                    });
               
                socket.on('message', function (data) {
                    if(userName==data.resiver){
                        var ptag = document.createElement("p");
                        var span = document.createElement("span");
                        span.className = "recive_time";
                        span.innerHTML =data.time
                        ptag.className = "recive_chat";
                        ptag.innerHTML = data.message;
                        document.getElementById("chatbox__messages").appendChild(span);
                        document.getElementById("chatbox__messages").appendChild(ptag);
                    }
                });
                        var sendTime=new Date().getHours()
                        sendTime=sendTime>12?sendTime-12:sendTime
                        var AMPM=sendTime>12?"PM":"AM"
                        var min=new Date().getMinutes()<10?+"0"+new Date().getMinutes():new Date().getMinutes()
                        sendTime+=":"+min+" "
                        var Time=sendTime+AMPM
                        var ptag = document.createElement("p");
                        var span = document.createElement("span");
                        span.className = "send_time";
                        span.innerHTML = Time
                        var chatTime = span.textContent;
                        ptag.className = "send_chat";
                        ptag.innerHTML = chat;
                        document.getElementById("chatbox__messages").appendChild(span);
                        document.getElementById("chatbox__messages").appendChild(ptag);
                        var message={"sender":userName,"resiver":"admin123","message":chat,"time":Time}
                        socket.emit('message',message);
                        $('#chat').val('');
                   
        

            }
            else {
                fetch('http://192.168.1.17:5000/predict', {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json',
                        // Add any additional headers if needed
                    },
                    body: JSON.stringify({ user: "user", message: chat }),
                })
                    .then(response => {
                        return response.json();
                    })
                    .then(data => {
                        console.log(data)
                        var ptag = document.createElement("p");
                        var span = document.createElement("span");
                        span.className = "send_time";
                        span.innerHTML = new Date().getHours() + ":" + new Date().getMinutes();
                        ptag.className = "send_chat";
                        ptag.innerHTML = chat;
                        document.getElementById("chatbox__messages").appendChild(span);
                        document.getElementById("chatbox__messages").appendChild(ptag);
                        document.getElementById("chat").value=''

                        if(data.user="chatbot"){
                              var ptag = document.createElement("p");
                              var span = document.createElement("span");
                              span.className = "recive_time";
                              span.innerHTML = new Date().getHours() + ":" + new Date().getMinutes();
                              ptag.className = "recive_chat";
                              ptag.innerHTML = data.answer;
                              document.getElementById("chatbox__messages").appendChild(span);
                              document.getElementById("chatbox__messages").appendChild(ptag);
                              if(data.answer==="pleace wait i'll connect to admin"){
                                chatbox.push(data.answer)
                                connectionMgs()
                              }

                        }
                        
                    })
                    .catch(error => {
                        // Handle errors
                        // console.error('Fetch error:', error);
                    });

            }
        });
    });

});

function connectionMgs(){
    setTimeout(function(){
        var ptag = document.createElement("p");
        var span = document.createElement("span");
        span.className = "recive_time";
        span.innerHTML = new Date().getHours() + ":" + new Date().getMinutes();
        ptag.className = "recive_chat";
        ptag.innerHTML = "admin connected you can chat with admin now ";
        document.getElementById("chatbox__messages").appendChild(span);
        document.getElementById("chatbox__messages").appendChild(ptag);
    },1000)}



    function generateRandomUsername() {
        const length = 7;
        const charset = "abcdefghijklmnopqrstuvwxyz0123";
        let username = "";
        for (let i = 0; i < length; i++) {
          const randomIndex = Math.floor(Math.random() * charset.length);
          username += charset.charAt(randomIndex);
        }
        userName=username
      }
      