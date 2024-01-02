var head=document.querySelector("head")
var body=document.querySelector("body")

var script_1=document.createElement("script")
script_1.src='C:\Users\codossal\Desktop\website chatbot\static\js\script.js'
head.appendChild(script_1)

var script_2=document.createElement("script")
script_2.src='https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.js'
head.appendChild(script_2)

var script_3=document.createElement("script")
script_3.src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js'
head.appendChild(script_3)


var link_1=document.createElement("link")
link_1.href='C:\Users\codossal\Desktop\website chatbot\static\css\style.css'
link_1.rel="stylesheet"
head.append(link_1)

const chatboxContainer = document.createElement('div');
chatboxContainer.id = 'chatboxid';
chatboxContainer.className = 'chatbox';
chatboxContainer.style.display = 'none';

// Create chatbox support section
const chatboxSupport = document.createElement('div');
chatboxSupport.className = 'chatbox__support';

// Create chatbox header
const chatboxHeader = document.createElement('div');
chatboxHeader.className = 'chatbox__header';

// Create chatbox image in the header
const chatboxImageHeader = document.createElement('div');
chatboxImageHeader.className = 'chatbox__image--header';
const img = document.createElement('img');
img.src = 'https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png';
img.alt = 'image';
chatboxImageHeader.appendChild(img);

// Create chatbox content in the header
const chatboxContentHeader = document.createElement('div');
chatboxContentHeader.className = 'chatbox__content--header';
const heading = document.createElement('h3');
heading.className = 'chatbox__heading--header';
heading.textContent = 'Chatbot';
chatboxContentHeader.appendChild(heading);

// Create close button in the header
const closeButton = document.createElement('button');
closeButton.className = 'chatbox_close-btn';
const closeImg = document.createElement('img');
closeImg.id = 'close-btn';
closeImg.src = '../static/img/close-line-icon.svg';
closeButton.appendChild(closeImg);

// Append header components
chatboxHeader.appendChild(chatboxImageHeader);
chatboxHeader.appendChild(chatboxContentHeader);
chatboxHeader.appendChild(closeButton);

// Create chatbox messages section
const chatboxMessages = document.createElement('div');
chatboxMessages.className = 'chatbox__messages';
const messagesContainer = document.createElement('div');
messagesContainer.id = 'chatbox__messages';
chatboxMessages.appendChild(messagesContainer);

// Create chatbox footer
const chatboxFooter = document.createElement('div');
chatboxFooter.className = 'chatbox__footer';

// Create input field in the footer
const inputField = document.createElement('input');
inputField.type = 'text';
inputField.id = 'chat';
inputField.placeholder = 'Write a message...';

// Create send button in the footer
const sendButton = document.createElement('button');
sendButton.className = 'chatbox_send--footer send_button';
sendButton.id = 'sendbtn';
sendButton.textContent = 'Send';

// Append footer components
chatboxFooter.appendChild(inputField);
chatboxFooter.appendChild(sendButton);

// Append support components
chatboxSupport.appendChild(chatboxHeader);
chatboxSupport.appendChild(chatboxMessages);
chatboxSupport.appendChild(chatboxFooter);

// Append chatbox support to container
chatboxContainer.appendChild(chatboxSupport);

// Create chatbox button
const chatboxButton = document.createElement('div');
chatboxButton.className = 'chatbox__button';
chatboxButton.id = 'showChatbot';
const button = document.createElement('button');
button.id = 'showbtn';
const buttonImg = document.createElement('img');
buttonImg.src = '/static/img/chatbox-icon.svg';
button.appendChild(buttonImg);
chatboxButton.appendChild(button);

// Append everything to the body
body.appendChild(chatboxContainer);
body.appendChild(chatboxButton);

