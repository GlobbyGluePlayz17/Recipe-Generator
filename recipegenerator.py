import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Your role is to generate recipes that only use certain ingredients. Based on a list of ingredients (measurements may or may not be given), generate a meal recipe they can make using only the ingredients they mentioned."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(
    fn=CustomChatGPT, 
    inputs=gradio.Text(label="Your Ingredients", lines=3, placeholder="List your ingredients here (i.e. 5 cups rice)"), 
    outputs=gradio.Text(label="Recipe", lines=3),
    title="Recipe Generator",
    description="Instructions:\n\nWhat ingredients do you have on-hand and/or need to use? Please list them below.",
    article="Behind Our Product:\n\nFood waste is a worldwide issue requiring immediate action. In the United States alone, there is 119 billion pounds of food wasted per a year. Furthermore, in the entire world, there is about 1.3 billion tons of food wasted per year. A number that will only increase unless preventative measures are taken.\n\nLook into peoples’ homes. Oftentimes, food is left in the fridge to slowly rot away, leaving leftover incomplete portions of food forgotten and eventually thrown away as waste.\n\nNow, with our Recipe Generator, users can simply input ingredients they currently have and Recipe Generator will output a recipe that consists of the given ingredients. This way, users are able to maximize ingredients in their fridge, minimize food waste, and also end up with a satisfying homemade meal.",
    allow_flagging="never"
)
demo.launch(inbrowser=True,share=True)