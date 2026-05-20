# Building Text Generation Applications
You've seen so far through this curriculum that there are core concepts like prompts and even a whole discipline called "prompt engineering". Many tools you can interact with like ChatGPT, Office 365 and more, support you using prompts to accomplish something.

For you to add such an experience to an app, you need to understand concepts like prompts, completions and choose a library to work with. 

**Content**

- [What is a Text Generation App](#what-is-a-text-generation-app)
- [How can I get started](#how-can-i-get-started)
- [Libraries/SDKs](#librariessdks)
- [Different types of prompts for different things](#different-types-of-prompts-for-different-things)



## What is a Text Generation App?
Normally when you build an app it has some kind of interface like the following:
- Command-based. Console apps are typical apps where you type a command and it carries out a task. For example, `git` is a command-based app.
- User interface (UI). Some apps have graphical user interfaces (GUIs) where you click buttons, input text, select options and more.


### Console and UI Apps are Limited
Compare it to a command-based app where you type a command:
- **It's limited**. You can't just type any command, only the ones that the app supports.
- **Language Specific**. Some apps support many languages, but by default the app is built for a specific language, even if you can add more language support.


### What Can I Build with a Text Generation App?
There are many things you can build. For example:
- **A chatbot**. A chatbot answering questions about topics, like your company and its products could be a good match.
- **Helper**. LLMs are great at things like summarizing text, getting insights from text, producing text like resumes and more.
- **Code assistant**. Depending on the language model you use, you can build a code assistant that helps you write code.



## How Can I Get Started?
You need to find a way to integrate with an LLM which usually entails the following two approaches:
- Use an API. Here you're constructing web requests with your prompt and get generated text back.
- Use a library. Libraries help encapsulate the API calls and make them easier to use.



## Libraries/SDKs
There are a few well known libraries for working with LLMs like:
- **OpenAI**, this library makes it easy to connect to your model and send in prompts.

Then there are libraries that operate on a higher level like:
- **LangChain**, LangChain is well known as supports Python.
- **Semantic Kernel**, Semantic Kernel is a library by Microsoft supporting the languages C#, Python, and Java.



## Different Types of Prompts, for Different Things
Now you've seen how to generate text using a prompt. You even have a program up and running that you can modify and change to generate different types of text.

Prompts can be used for all sorts of tasks. For example:
- **Generate a type of text**. For example, you can generate a poem, questions for a quiz etc.
- **Lookup information**. You can use prompts to look for information like the following example 'What does CORS mean in web development?'.
- **Generate code**. You can use prompts to generate code, for example developing a regular expression used to validate emails.
