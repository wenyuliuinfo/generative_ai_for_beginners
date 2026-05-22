# Integrating with Function Calling
You've learned a fair bit so far in the previous lessons. However, we can improve further. Some things we can address are how we can get a more consistent response format to make it easier to work with the response downstream. Also, we might want to add data from other sources to further enrich our application.

**Content**
- [Scenario: Improving our chatbot with functions](#scenario-improving-our-chatbot-with-functions)
- [Why Function Calling](#why-function-calling)
- [Illustrating the problem through a scenario](#illustrating-the-problem-through-a-scenario)
- [Use cases for using function calls](#use-cases-for-using-function-calls)


## Scenario: Improving our chatbot with functions
For this lesson, we want to build a feature for our education startup that allows users to use a chatbot to find technical courses. We will recommend courses that fit their skill level, current role and technology of interest.

To complete this scenario, we will use a combination of:
- `Microsoft Learn Catalog API` to help users find courses based on the request of the user.
- `Function Calling` to take the user's query and send it to a function to make the API request.


## Why Function Calling
Before function calling, responses from an LLM were unstructured and inconsistent. Developers were required to write complex validation code to make sure they were able to handle each variation of a response. Users could not get answers like "What is the current weather in Stockholm?". This is because models were limited to the time the data was trained on.

Function calling is a feature of the Azure OpenAI to overcome the following limitations:
- **Consistent response format**. If we can better control the response format we can more easily integrate the response downstream to other systems.
- **External data**. Ability to use data from other sources of an application in a chat context.


## Illustrating the Problem through a Scenario
So how do we solve the formatting problem then? By using functional calling, we can make sure that we receive structured data back. When using function calling, the LLM does not actually call or run any functions. Instead, we create a structure for the LLM to follow for its responses. We then use those structured responses to know what function to run in our applications.

![function_calling_flow](/11-integrating-with-function-calling/images/Screenshot%202026-05-22%20at%207.46.47 AM.png)

We can then take what is returned from the function and send this back to the LLM. The LLM will then respond using natural language to answer the user's query.


## Use Cases for using Function Calls
There are many different use cases where function calls can improve your app like:
- **Calling External Tools**. Chatbots are great at providing answers to questions from users. By using function calling, the chatbots can use messages from users to complete certain tasks. For example, a student can ask the chatbot to "Send an email to my instructor saying I need more assistance with this subject". This can make a function call to `send_email(to: string, body: string)`.
- **Create API or Database Queries**. Users can find information using natural language that gets converted into a formatted query or API request. An example of this could be a teacher who requests "Who are the students that completed the last assignment" which could call a function named `get_completed(student_name: string, assignment: int, current_status: string)`.
- **Creating Structured Data**. Users can take a block of text or CSV and use the LLM to extract important information from it. For example, a student can convert a Wikipedia article about peace agreements to create AI flashcards. This can be done by using a function called `get_important_facts(agreement_name: string, data_signed: string, parties_involved: list)`.


## Creating your First Function Call
The process of creating a function call includes 3 main steps:
1. **Calling** the chat completions API with a list of your functions and a user message.
2. **Reading** the model's response to perform an action, i.e., execute a function or API call.
3. **Making** another call to chat completions API with the response from your function to use that information to create a response to the user.

![creating_function_call](/11-integrating-with-function-calling/images/Screenshot%202026-05-22%20at%207.59.29 AM.png)