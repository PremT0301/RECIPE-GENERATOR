# import openai

# openai.api_key="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"

# def chat_with_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user","content":prompt}]
#     )

#     return response.choices[0].message.content.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("you:")
#         if user_input.lower() in ["quit","exit","bye"]:
#             break

#         response=chat_with_gpt(user_input)
#         print("chatbot: ",response)
import openai 
openai.api_key = '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'
messages = [ {"role": "system", "content": 
			"You are a intelligent assistant."} ] 
while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		) 
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply}) 
