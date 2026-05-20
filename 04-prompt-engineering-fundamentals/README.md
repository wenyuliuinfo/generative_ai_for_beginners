# Prompt Engineering Fundamentals
This module covers essential concepts and techniques for creating effective prompts in generative AI models. The way you write your prompt to an LLM also matters. A carefully-crafted prompt can achieve a better quality of response.

Generative AI is capable of creating new content (e.g., text, images, audio, code etc.) in response to user requests. It achieves this using Large Language Models like OpenAI's GPT series that are trained for using natural language and code.

Users can now interact with these models using familiar paradigms like chat, without needing any technical expertise or training. The models are prompt-based - users send a text input and get back the AI response. They can then "chat with the AI" iteratively, in multi-turn conversations, refining their prompt until the response matches their expectations.

Prompts now become the primary programming interface for generative AI apps, telling the models what to do and influencing the quality of returned responses. *Prompt Engineering* is a fast-growing field of study that focuses on the design and optimization of prompts to deliver consistent and quality responses at scale.

**Content**

- [What is Prompt Engineering](#what-is-prompt-engineering)
- [Why do we need Prompt Engineering](#why-do-we-need-prompt-engineering)
- [Prompt Construction](#prompt-construction)
- [Prompt Content](#primary-content)
- [Prompting Best Practices](#prompting-best-practices)



### What is Prompt Engineering?
We started this lesson by defining **Prompt Engineering** as the process of designing and optimizing text inputs (prompts) to deliver consistent and quality responses (completions) for a given application objective and model. We can think of this as a 2-step process:
1. *Designing* the initial prompt for a given model and objective
2. *Refining* the prompt iteratively to improve the quality of the response

This is necessarily a trial-and-error process that requires user intuition and effort to get optimal results. So why is it important? To answer this, we first need to understand three concepts:
- *Tokenization*: how the model "sees" the prompt
- *Base LLMs*: how the foundation model "processes" a prompt
- *Instruction-Tuned LLMs*: how the model can now see "tasks"


#### 1. Tokenization
An LLM sees prompts as a sequence of tokens where different models can tokenize the same prompt in different ways. Since LLMs are trained on tokens, the way prompts get tokenized has a direct impact on the quality of the generated response.

To get an intuition for how tokenization works, try tools like the OpenAI Tokenizer.


#### 2. Base LLMs - Foundation Models
Once a prompt is tokenized, the primary function of the Base LLM (Foundation Model) is to predict the token in that sequence. Since LLMs are trained on massive text datasets, they have a good sense of the statistical relationships between tokens and can make that prediction with some confidence. Note that they don't understand the meaning of the words in the prompt or token; they just see a pattern they can complete with their next prediction. They can continue predicting the sequence till terminated by user intervention or some pre-established condition.


#### 3. Instruction Tuned LLMs
An Instruction Tuned LLM starts with the foundation model and fine-tunes it with examples or input/output pairs that can contain clear instructions - and the response from the AI attempt to follow that instruction.

This uses techniques like Reinforcement Learning with Human Feedback (RLHF) that can train the model to follow instructions and learn from feedback so that it produces responses that are better-suited to practical applications and more relevant to user objectives.



### Why do we need Prompt Engineering?
Now that we know how prompts are processed by LLMs, let's talk about why we need prompt engineering. The answer lies in the fact that current LLMs pose a number of challenges that make reliable and consistent completions more challenging to achieve without putting effort into prompt construction and optimization.
1. **Model responses are stochastic**. The same prompt will likely produce different responses with different models or model versions. And it may even produce different results with the same model at different times.
2. **Models can fabricate response**. Models are pre-trained with large but finite datasets, meaning they lack knowledge about concepts outside that training scope. As a result, they can produce completions that are inaccurate, imaginary, or directly contradictory to known facts. Prompt engineering techniques help users identify and mitigate such fabrications, e.g., by asking AI for citations or reasoning.
3. **Models capabilities will vary**. Newer models or model generations will have richer capabilities but also bring unique quirks and tradeoffs in cost & complexity. Prompt engineering can help us develop best practices and workflows that abstract away differences and adapt to model-specific requirements in scalable, seamless ways.



### Prompt Construction
We've seen why prompt engineering is important - now let's understand how prompts are constructed so we can evaluate different techniques for more effective prompt design.

#### 1. Basic Prompt
Let's start with the basic prompt: a text input sent to the model with no other context.


#### 2. Complex Prompt
Now let's add context and instructions to that basic prompt. The Chat Completion API lets us construct a complex prompt as a collection of messages with:
- Input/output pairs reflecting user input and assistant response
- System message setting the context for assistant behavior or personality

The request is now in the form below, where the tokenization effectively captures relevant information from context and conversation. Now, changing the system context can be as impactful on the quality of completions, as the user inputs provided.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

#### 3. Instruction Prompt
In the above examples, the user prompt was a simple text query that can be interpreted as a request for information. With instruction prompts, we can use that text to specify a task in more detail, providing better guidance to the AI.

[!prompt_example](/04-prompt-engineering-fundamentals/images/Screenshot%202026-05-20%20at%2011.31.49 AM.png)



### Primary Content
In the above examples, the prompt was still fairly open-ended, allowing the LLM to decide what part of its pre-trained dataset was relevant. With the primary content design pattern, the input text is divided into two parts:
- An instruction (action)
- Relevant content (that influences action)

The primary content segment can be used in various ways to drive more effective instructions:
- **Examples** - instead of telling the model what to do with an explicit instruction, give it examples of what to do and let it infer the pattern.
- **Cues** - follow the instruction with a "cue" that primes the completion, guiding the model towards more relevant responses.
- **Templates** - these are repeatable recipes for prompts with placeholders that can be customized with data for specific use cases.


#### 1. Using Examples
This is an approach where you use the primary content to feed the model some examples of the desired output for a given instruction, and let it infer the pattern for the desired output. 

The prompt now consists of three components:
- A task description
- A few examples of the desired output
- The start of a new example
  
[!using_examples](/04-prompt-engineering-fundamentals/images/Screenshot%202026-05-20%20at%2011.41.15 AM.png)


#### 2. Prompt Cues
Another technique for using primary content is to provide cues rather than examples. In this case, we are giving the model a nudge in the right direction by starting it off with a snippet that reflects the desired response format. The model then "takes the cue" to continue in the vein.

[!prompt_cues](/04-prompt-engineering-fundamentals/images/Screenshot%202026-05-20%20at%2011.43.45 AM.png)


#### 3. Prompt Templates
A prompt templates is a pre-defined recipe for a prompt that can be stored and reused as needed, to drive more consistent user experiences at scale. In its simplest form, it is simply a collection of prompt examples like the one from OpenAI that provides both the interactive prompt components and the API-driven request format - to support reuse.

In it's more complex form like the example from LangChain, it contains placeholders that can be replaced with data from a variety of sources to generate a prompt dynamically. This allows us to create a library of reusable prompts that can be used to drive consistent user experiences programmatically at scale.

Finally, the real value of templates lies in the ability to create and publish prompt libraries for vertical application domains - where the prompt template is now optimized to reflect application-specific context or examples that make the responses more relevant and accurate for the targeted user audience.



### Prompting Best Practices
Now that we know how prompts can be constructed, we can start thinking about how to design them to reflect best practices. We can think about this in two parts - having the right mindset and applying the right techniques.

#### 1. Prompt Engineering Mindset
Prompt Engineering is a trial-and-error process so keep three broad guiding factors in mind:
1. **Domain Understanding Matters**. Response accuracy and relevance is a function of the domain in which that application or user operates. Apply your intuition and domain expertise to customize techniques further. For instance, define *domain-specific personalities* in your system prompts, or use *domain-specific templates* in your user prompts. Provide secondary content that reflects domain-specific contexts, or use *domain-specific cues and examples* to guide the model towards familiar usage patterns.
2. **Model Understanding Matters**. We know models are stochastic by nature. But model implementations can also vary in terms of the training dataset they use, the capabilities they provide and the type of content they are optimized for. Understand the strengths and limitations of the model you are using, and use that knowledge to prioritize tasks or build customized templates that are optimized for the model's capabilities.
3. **Iteration and Validation Matters**. Models are evolving rapidly, and so are the techniques for prompt engineering. As a domain expert, you may have other context or criteria your specific application, that may not apply to broader community. Use prompt engineering tools and techniques to "jump start" prompt construction, then iterate and validate the results using your own intuition and domain expertise. Record your insights and create a knowledge base that can be used as a new baseline by others, for faster iterations in the future.


#### 2. Prompt Engineering Techniques 
Let's look at common best practices that are recommended by OpenAI practitioners.

[!techniques](/04-prompt-engineering-fundamentals/images/Screenshot%202026-05-20%20at%2012.02.52 PM.png)


