import random
#set of responses
no_responses = ["I'm sorry, I didn't understand you",
                "Why do you think that?",
                "How long have you felt this way?",
                "Tell me more!"
               ]

responses = {
  "what's your name?": [
      "my name is AI-BOT",
      "they call me AI-BOT",
      "I go by AI-BOT"
   ],
  "what's today's weather?": [
      "the weather is sunny",
      "it's sunny today"
    ]
}

conversation = True
print('AI-BOT: Hello!')
while conversation:
    #read user input, and save it into the variable with the name "message"
    message = input('USER:    ')

    #check if the user input is "bye" and cancel the conversation
    if message == "bye":
        conversation = False

    #check if the message is in the set of responses
    if message in responses:
        #select the correct response and show it to the user
        print('AI-BOT: ',random.choice(responses[message]))
    else:
        if conversation:
            print('AI-BOT: ', random.choice(no_responses)) 

'''
responses = {
  "your name": [
      "my name is AI-BOT",
      "they call me AI-BOT",
      "I go by AI-BOT"
   ],
  "weather": [
      "the weather is sunny",
      "it's sunny today"
    ],
    "hockey": [
      "good winter game!",
      "we have to wait for the lake will be frozen"
    ],
    "football": [
      "millions of people follow their favorite team in every game",
      "this game helps kids stay active",
      "it is also called as “Soccer” in North America",
      "ronaldo is the best",
    ]
} 
'''

'''
responses = {
  "hello": [
      "Hello, how can I help you."
   ],
  "i feel (.*)": [
      "Why do you feel {}?",
      "How long have you been felting {}?"
    ],
    "i am (.*)": [
      "How long have you been {}?",
      "Why do you say you are {}?"
    ],
    "i 'm (.*)": [
      "Why are you {}?",
      "How long have you been {}?"
    ],
    "i (.*) you": [
      "Why do you {} yoourself?",
      "What makes you think you {} yoourself?"
    ],
    "i (.*) myself": [
      "Why do you {} yoourself?",
      "What makes you think you {} yoourself?"
    ],
    "(.*) sorry (.*)": [
      "There is no need to apologize.",
      "What are you apologizing for?"
    ],
    "(.*) friend (.*)": [
      "There is no need to apologize.",
      "What are you apologizing for?"
    ],
    "(.*) mother (.*)": [
      "Tell me more about your family."
    ],
    "(.*) father (.*)": [
      "Tell me more about your family."
    ],
    "yes": [
      "Why seem quite sure.",
      "OK, but can you elaborate."
    ],
    "no": [
      "Why not.",
      "OK, but can you elaborate a bit?"
    ],
    "(.*) your name(.*)": [
      "my name is AI-BOT",
      "they call me AI-BOT",
      "I go by AI-BOT"
   ],
    "(.*) weather(.*)": [
      "the weather is sunny",
      "it's sunny today"
    ],
    "(.*) hockey(.*)": [
      "good winter game!",
      "we have to wait for the lake will be frozen"
    ],
    "(.*) football (.*)": [
      "millions of people follow their favorite team in every game",
      "this game helps kids stay active",
      "it is also called as “Soccer” in North America",
      "ronaldo is the best"
    ],
    " (.*)": [
      "Please tell me more.",
      "Let's change focus a bit... tell me about your family.",
      "Can you elaborate on that?"
    ],
    "":[
      "Why do you think that?.",
      "Please tell me more.",
      "Let's change focus a bit... tell me about your family.",
      "Can you elaborate on that?"
    ]

} 
'''

'''
for pattern, response_list in responses.items():
  print('Pattern: ', pattern)
  print('Response: ', response_list)
  print('--------------')
'''

'''
message = "I feel happy"

for pattern, response_list in responses.items():
        matches = re.match(pattern, message.lower())
        if matches:
          print('Pattern: ', pattern) 
'''

'''
def match_response(message):
    for pattern, response_list in responses.items():
        matches = re.match(pattern, message.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.groups())
    return "I am sorry I do not understand what you are saying." 
'''