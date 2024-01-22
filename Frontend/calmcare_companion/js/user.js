       // Get references to the chat form, input field, and messages container
       const chatForm = document.getElementById('chat-form');
       const userInputField = document.getElementById('user-input');
       const chatMessagesContainer = document.getElementById('chat-messages');
   
       // Event listener for chat form submission
       chatForm.addEventListener('submit', (event) => {
           event.preventDefault();
   
           // Get the user input from the input field
           const userInput = userInputField.value;
   
           // Clear the input field
           // userInputField.value = '';
   
           // Send the user input to the Flask code using an AJAX request
           const xhr = new XMLHttpRequest();
           xhr.open('POST', '/get_symptoms');
           xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
           xhr.onload = () => {
               if (xhr.status === 200) {
                   // Get the response from the Flask code
                   const response = JSON.parse(xhr.responseText);
   
                   // Display the chatbot's response in the chat interface
                   displayChatbotResponse(response.disease);
                   displayChatbotResponse(response.precautions);
   
                   // Speak the chatbot's response
                   speak(response.disease);
                   speak(response.precautions);
               }
           };
           xhr.send(`symptom=${userInput}`);
       });
   
       // Function to display the chatbot's response in the chat interface
       function displayChatbotResponse(message) {
           // Create a new chat message element
           const chatMessage = document.createElement('div');
           chatMessage.classList.add('chat-message');
           chatMessage.textContent = message;
   
           // Append the chat message to the messages container
           chatMessagesContainer.appendChild(chatMessage);
   
           // Scroll to the bottom of the messages container
           chatMessagesContainer.scrollTop = chatMessagesContainer.scrollHeight;
       }